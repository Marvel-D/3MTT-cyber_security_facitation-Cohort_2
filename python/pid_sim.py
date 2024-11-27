import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# PID controller parameters
Kp = 1.2   # Proportional gain
Ki = 1.0   # Integral gain
Kd = 0.01  # Derivative gain

# Setpoint (desired temperature)
setpoint = 50.0  # Desired temperature (°C)

# Simulation time
time = np.linspace(0, 50, 500)  # 50 seconds, 500 points

# Define a simple plant model (system to be controlled)
# In this case, the plant is a simple first-order system
def plant_model(y, t, u):
    tau = 5.0  # Time constant of the system
    dydt = (-y + u) / tau
    return dydt

# PID Controller
def pid_controller(setpoint, y_current, integral_error, previous_error, dt):
    error = setpoint - y_current
    integral_error += error * dt
    derivative_error = (error - previous_error) / dt

    # Control input based on PID formula
    u = Kp * error + Ki * integral_error + Kd * derivative_error

    return u, integral_error, error

# Simulate the system response
def simulate_pid():
    y_current = 0.0  # Initial temperature
    integral_error = 0.0
    previous_error = 0.0
    dt = time[1] - time[0]  # Time step
    
    y_values = []  # Store temperature values for plotting

    for t in time:
        u, integral_error, previous_error = pid_controller(
            setpoint, y_current, integral_error, previous_error, dt)
        
        # Simulate the plant for the next time step
        y_current = odeint(plant_model, y_current, [t, t + dt], args=(u,))[-1]
        
        y_values.append(y_current)

    return y_values

# Run the simulation
y_sim = simulate_pid()

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(time, y_sim, label='Temperature (°C)')
plt.axhline(y=setpoint, color='r', linestyle='--', label='Setpoint (50°C)')
plt.title('PID Controller Simulation for Temperature Control')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
