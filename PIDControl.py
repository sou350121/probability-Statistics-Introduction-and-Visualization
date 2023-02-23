# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:17:53 2023

@author: ken3
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