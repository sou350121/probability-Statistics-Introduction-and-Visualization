# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 08:48:38 2023

@author: ken3


"""

import taichi as ti
import math

ti.init()
vec2 = ti.types.vector(2, float)

# Simulation of fundamental solutions of Laplace equation
# Pressing left mouse button with 's/v/d' key will create new 'source/vortex/dipole' on cursor position,
#   and pressing right mouse button will create negative one.
# Pressing left and right mouse buttons will delete element around cursor position.
# Pressing left/right mouse button without other keys will increase/decrease the intensity of element around cursor.

screen = (30, 20)  # density of point generation positions on the boundary, also decide window size
arrowField = [int(it / 2) for it in screen]  # number of arrow in window
meshSpace = 20  # screen * meshSpace = windowSize
maxElements = 20  # the max number of each element(source/sink, vortex, dipole)
refillFrame = 20  # frame interval for each refill points
refillVelThresh = .2  # points will be refilled when the absolute value of the velocity on boundary is greater than this value
V = vec2(1., 0)  # the velocity of uniform stream
dt = .002
fadeMax = 10  # frames of fade in/out
fade = fadeMax  # control arrows' fade in and fade out
maxPoints = screen[0] * screen[1] * 2
gui = ti.GUI('demo', tuple(it * meshSpace for it in screen))
guiHeight = meshSpace * screen[1]

points = ti.Vector.field(2, float, maxPoints)
sources = ti.Struct.field({
    "pos": vec2,
    "q": ti.f32
}, shape=maxElements)
vortexes = ti.Struct.field({
    "pos": vec2,
    "q": ti.f32
}, shape=maxElements)
dipoles = ti.Struct.field({
    "pos": vec2,
    "m": ti.f32
}, shape=maxElements)
arrows = ti.Struct.field({
    "base": vec2,
    "dir": vec2,
    "vel": ti.f32
}, shape=arrowField)
points.fill(-100)


def initPoints():
    for x, y in ti.ndrange(*arrowField):
        arrows[x, y].base = \
            vec2((x + 1) * (1 - 1 / arrowField[0]) / arrowField[0], (y + 1) * (1 - 1 / arrowField[1]) / arrowField[1])
    dipoles[0].pos = vec2(0.5, 0.5)
    dipoles[0].m = 0.01
    vortexes[0].pos = vec2(0.5, 0.5)
    vortexes[0].q = -0.5


@ti.func
def getVel(pos):
    vel = V  # add uniform stream velocity
    for i in range(maxElements):
        # add source/sink velocity
        uv = pos - sources[i].pos
        uv[0] *= screen[1] / screen[0]
        vel += uv * sources[i].q / (2 * ti.math.pi * (uv[0] ** 2 + uv[1] ** 2))
        # add vortex velocity
        uv = pos - vortexes[i].pos
        uv = vec2(-uv[1], uv[0])
        uv[0] *= screen[1] / screen[0]
        vel += uv * vortexes[i].q / (2 * ti.math.pi * (uv[0] ** 2 + uv[1] ** 2))
        # add dipole velocity
        uv = pos - dipoles[i].pos
        uv[0] *= screen[1] / screen[0]
        vel_t = vec2(uv[1] ** 2 - uv[0] ** 2, -2 * uv[0] * uv[1])
        vel += vel_t * dipoles[i].m / (uv[0] ** 2 + uv[1] ** 2) ** 2
    return vel


# @param.boundary: 0: left, 1: bottom, 2: right, 3: top
# @param.index: last access point index
@ti.func
def refillPointsOnOneBoundary(boundary, index):
    pointsNumber = screen[0]
    if boundary == 0 or boundary == 2:
        pointsNumber = screen[1]
    for i in range(pointsNumber):
        found = False
        for _ in range(maxPoints):
            if points[index][0] == -100:
                found = True
                if boundary == 0:
                    points[index] = vec2(-dt * refillVelThresh, (i + .5) / screen[1])
                elif boundary == 1:
                    points[index] = vec2((i + .5) / screen[0], -dt * refillVelThresh)
                elif boundary == 2:
                    points[index] = vec2(1 + dt * refillVelThresh, (i + .5) / screen[1])
                elif boundary == 3:
                    points[index] = vec2((i + .5) / screen[0], 1 + dt * refillVelThresh)
                break
            index += 1
            if index >= maxPoints:
                index = 0
        if not found:
            break
    return index


@ti.kernel
def refillPoints():
    # traverse positions and refill points on the boundary.
    # if the normal velocity is less than thresh, refill point will be deleted when update.
    index = 0
    found = True
    ti.loop_config(serialize=True)
    for i in range(4):
        _index = refillPointsOnOneBoundary(i, index)
        if _index == index:
            break
        else:
            index = _index


@ti.kernel
def updatePoints():
    for i in points:
        if points[i][0] != -100:
            vel = getVel(points[i])
            points[i] += vel * dt
        if not (0 <= points[i][0] <= 1 and 0 <= points[i][1] <= 1):
            points[i] = vec2(-100, -100)
        for j in range(maxElements):
            if sources[j].q < 0 and ti.math.length(points[i] - sources[j].pos) < 0.025:
                points[i] = vec2(-100, -100)
            if dipoles[j].m != 0 and ti.math.length(points[i] - dipoles[j].pos) < 0.05:
                points[i] = vec2(-100, -100)


@ti.kernel
def updateArrows():
    for x, y in ti.ndrange(*arrowField):
        vel = getVel(arrows[x, y].base)
        arrows[x, y].vel = vel.norm()
        arrows[x, y].dir = vel / vel.norm() / meshSpace / 1.5


def drawArrows(gui):
    global fade
    if fade < fadeMax:
        fade += 1
    if fade == 0:
        updateArrows()  # after fade out, update arrow filed
    else:
        arr = arrows.to_numpy()
        vel = arr['vel'].reshape(1, -1)[0]
        vel = (vel / vel.max() * 0xdd + 0x11) * (math.fabs(fade / fadeMax))
        mean = vel.mean()
        if mean > 0x7f:
            vel /= mean / 0x7f  # make uniform stream more beautiful
        vel = vel.astype(int)
        vel *= 2 ** 16 + 2 ** 8 + 1
        gui.arrows(
            arr['base'].reshape(arr['base'].shape[0] * arr['base'].shape[1], 2),
            arr['dir'].reshape(arr['dir'].shape[0] * arr['dir'].shape[1], 2),
            radius=1.5, color=vel
        )


def drawMark(gui, frame):
    triangleTrans = [
        vec2(0, 1) / guiHeight,
        vec2(math.cos(7. / 6. * math.pi), math.sin(7. / 6. * math.pi)) / guiHeight,
        vec2(math.cos(-1. / 6. * math.pi), math.sin(-1. / 6. * math.pi)) / guiHeight
    ]
    rectTrans = [
        vec2(1 * screen[1] / screen[0], 1) / guiHeight,
        vec2(-1 * screen[1] / screen[0], -1) / guiHeight,
    ]
    for i in range(maxElements):
        if dipoles[i].m > 0:
            gui.circle(dipoles[i].pos, 0xFFFDC0, dipoles[i].m * 2000)
        elif dipoles[i].m < 0:
            gui.circle(dipoles[i].pos, 0xD25565, dipoles[i].m * -2000)
        if sources[i].q > 0:
            gui.rect(
                sources[i].pos + rectTrans[0] * 2 * sources[i].q,
                sources[i].pos + rectTrans[1] * 2 * sources[i].q,
                2 * sources[i].q + 1, 0xFFFDC0
            )
        elif sources[i].q < 0:
            gui.rect(
                sources[i].pos + rectTrans[0] * 2 * sources[i].q,
                sources[i].pos + rectTrans[1] * 2 * sources[i].q,
                -2 * sources[i].q + 1, 0xD25565
            )
        if vortexes[i].q != 0:
            rotateMatrix = ti.Matrix([
                [math.cos(vortexes[i].q * dt * 40 * frame), -math.sin(vortexes[i].q * dt * 40 * frame)],
                [math.sin(vortexes[i].q * dt * 40 * frame), math.cos(vortexes[i].q * dt * 40 * frame)]
            ])
            trans = [rotateMatrix @ it for it in triangleTrans]
            for it in trans:
                it[0] *= screen[1] / screen[0]
            gui.triangle(
                vortexes[i].pos + trans[0] * 16,
                vortexes[i].pos + trans[1] * 16,
                vortexes[i].pos + trans[2] * 16,
                0xD25565
            )


def processGuiEvent(gui):
    global fade
    while gui.get_event((ti.GUI.PRESS, ti.GUI.LMB), (ti.GUI.PRESS, ti.GUI.RMB)):
        if gui.is_pressed(ti.GUI.LMB) and gui.is_pressed(ti.GUI.RMB):  # process delete event
            for i in range(maxElements):
                if sources[i].q != 0 and (sources[i].pos - vec2(*gui.get_cursor_pos())).norm() < 5 / guiHeight:
                    sources[i].q = 0
                if vortexes[i].q != 0 and (vortexes[i].pos - vec2(*gui.get_cursor_pos())).norm() < 5 / guiHeight:
                    vortexes[i].q = 0
                if dipoles[i].m != 0 and (dipoles[i].pos - vec2(*gui.get_cursor_pos())).norm() < 5 / guiHeight:
                    dipoles[i].m = 0
        else:
            if gui.is_pressed('s'):  # process add source/sink event
                for i in range(maxElements):
                    if sources[i].q == 0:
                        if gui.is_pressed(ti.GUI.RMB):
                            sources[i].q -= 1
                        else:
                            sources[i].q += 1
                        sources[i].pos = vec2(*gui.get_cursor_pos())
                        break
            elif gui.is_pressed('v'):  # process add vortex event
                for i in range(maxElements):
                    if vortexes[i].q == 0:
                        if gui.is_pressed(ti.GUI.RMB):
                            vortexes[i].q -= 0.5
                        else:
                            vortexes[i].q += 0.5
                        vortexes[i].pos = vec2(*gui.get_cursor_pos())
                        break
            elif gui.is_pressed('d'):  # process add dipole event
                for i in range(maxElements):
                    if dipoles[i].m == 0:
                        if gui.is_pressed(ti.GUI.RMB):
                            dipoles[i].m -= 0.01
                        else:
                            dipoles[i].m += 0.01
                        dipoles[i].pos = vec2(*gui.get_cursor_pos())
                        break
            else:
                for i in range(maxElements):  # process increase/decrease event
                    if sources[i].q != 0 and (sources[i].pos - vec2(*gui.get_cursor_pos())).norm() < 5 / guiHeight:
                        if gui.is_pressed(ti.GUI.RMB):
                            sources[i].q -= 0.5 * int(sources[i].q >= 0.0) - (sources[i].q <= 0.0)
                        else:
                            sources[i].q += 0.5 * int(sources[i].q >= 0.0) - (sources[i].q <= 0.0)
                    if vortexes[i].q != 0 and (vortexes[i].pos - vec2(*gui.get_cursor_pos())).norm() < 5 / guiHeight:
                        if gui.is_pressed(ti.GUI.RMB):
                            vortexes[i].q -= 0.1 * int(vortexes[i].q >= 0.0) - (vortexes[i].q <= 0.0)
                        else:
                            vortexes[i].q += 0.1 * int(vortexes[i].q >= 0.0) - (vortexes[i].q <= 0.0)
                    if dipoles[i].m != 0 and (dipoles[i].pos - vec2(*gui.get_cursor_pos())).norm() < 5 / guiHeight:
                        if gui.is_pressed(ti.GUI.RMB):
                            dipoles[i].m -= 0.001 * int(dipoles[i].m >= 0.0) - (dipoles[i].m <= 0.0)
                        else:
                            dipoles[i].m += 0.001 * int(dipoles[i].m >= 0.0) - (dipoles[i].m <= 0.0)
        fade = -math.fabs(fade)  # fade out arrow filed


if __name__ == '__main__':
    initPoints()
    updateArrows()
    refillPoints()
    refillCount = 0
    frame = 0
    while gui.running:
        processGuiEvent(gui)
        drawArrows(gui)
        updatePoints()
        ps = points.to_numpy()
        gui.circles(ps, 3, color=0x2E94B9)
        if refillCount > refillFrame:
            refillCount = 0
            refillPoints()
        drawMark(gui, frame)
        gui.show()
        refillCount += 1
        frame += 1