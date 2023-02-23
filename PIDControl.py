# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:17:53 2023

@author: ken3

Introduction

    u(t) = Kp * e(t) + Ki * ∫e(t)dt + Kd * de(t)/dt
    where u(t) is the control signal, e(t) is the error between the setpoint 
    and the measured variable, Kp, Ki, and Kd are the gains of 
    the P, I, and D components, respectively, and de(t)/dt is the derivative of 
    the error with respect to time.
    
    - Proportional (P) component: This component provides a response proportional to 
    the error between the desired setpoint and the measured process variable. 
    The P component alone can cause overshoot and oscillations in the response.
    - Integral (I) component: This component provides a response proportional to 
    the integral of the error over time. The I component alone can eliminate 
    the steady-state error, but can cause a slow response.
    - Derivative (D) component: This component provides a response proportional to 
    the derivative of the error over time. The D component alone can improve 
    the stability of the system and reduce overshoot and oscillations.
"""

import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.error = 0
        self.integral = 0
        self.derivative = 0
        self.last_error = 0

    def calculate(self, setpoint, measured):
        self.error = setpoint - measured
        self.integral += self.error
        self.derivative = self.error - self.last_error
        self.last_error = self.error

        return self.Kp * self.error + self.Ki * self.integral + self.Kd * self.derivative


pid = PIDController(0.5, 0.1, 0.2)

setpoint = 25
measured = 20
time = [0]
output = [measured]

for i in range(1, 100):
    control_signal = pid.calculate(setpoint, measured)
    measured += control_signal
    time.append(i)
    output.append(measured)

plt.plot(time, output)
plt.axhline(y=setpoint, color='r', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Measured value')
plt.title('PID control response')
plt.show()