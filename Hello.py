import numpy as np
import matplotlib.pyplot as plt

# Turn on interactive mode
plt.ion()

# Define x values
x_values = np.linspace(-10, 10, 400)

# Define the two linear equations
y1_values = 4 * x_values + 2  # 4x + 2
y2_values = 2 * x_values + 18  # 2x + 18

# Create the plot
plt.figure(figsize=(8, 6))

# Plot both lines
line1, = plt.plot(x_values, y1_values, label="y = 4x + 2", color='b')
line2, = plt.plot(x_values, y2_values, label="y = 2x + 18", color='r')

# Labeling the plot
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title("Graph of 4x + 2 = 2x + 18")
plt.xlabel("x")
plt.ylabel("y")

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)

# Interactive Mode
plt.draw()  # Draw the plot to interact with it

# You can manually edit the plot in this mode
input("Press Enter to exit...")  # Keeps the plot open

# Turn off interactive mode when done
plt.ioff()
plt.show()
