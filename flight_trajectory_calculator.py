import matplotlib.pyplot as plt
import numpy as np


# Add more features.
# Create like a user options menu to check for various calculations
#


def calculate_trajectory(initial_speed, launch_angle, initial_height, gravity=9.81):
    # Convert angle to radians
    angle_rad = np.degrees(launch_angle)

    # Time of flight calculation
    time_of_flight = (initial_speed * np.sin(angle_rad)
                      + np.sqrt((initial_speed * np.sin(angle_rad))**2
                                + 2 * gravity * initial_height)) / gravity

    # Calculate Range
    range_ = initial_speed * np.cos(angle_rad) * time_of_flight

    # Calculate maximum height
    max_height = initial_height + ((initial_speed * np.sin(angle_rad)) ** 2 / (2 * gravity))
    print(f"maximum height is {max_height}")
    return time_of_flight, range_, max_height


def plot_trajectory(initial_speed, launch_angle, initial_height, time_of_flight, gravity=9.81):
    t = np.linspace(0, time_of_flight, num=100)  # Time intervals
    angle_rad = np.radians(launch_angle)

    # Calculate x and Y coordinates
    x = initial_speed * np.cos(angle_rad) * t
    y = initial_height + initial_speed * np.sin(angle_rad) * t - (0.5 * gravity) * t**2

    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title("Trajectory of projectile")
    plt.xlabel("Horizontal distance(m)")
    plt.ylabel("Height/ Vertical distance (m)")
    plt.grid()
    plt.ylim(0, max(y) * 1.1)  # Adjust y-axis limits
    plt.xlim(0, max(x) * 1.1)  # Adjust x-axis limits
    plt.show()


def main():
    # User inputs
    initial_speed = float(input("Enter initial speed of projectile in m/s: "))
    launch_angle = float(input("Enter the launch angle of projectile in degrees: "))
    initial_height = float(input("Enter the initial height of projectile(m): "))

    # Perform calculations
    time_of_flight, range_, max_height = calculate_trajectory(initial_speed,  launch_angle, initial_height, gravity=9.81)

    # Showing trajectory
    print(f"Time of flight: {time_of_flight} seconds")
    print(f"Horizontal distance covered: {range_} meters")
    print(f"Maximum height of projectile: {max_height} meters")

    # Plotting trajectory
    plot_trajectory(initial_speed, launch_angle, initial_height, time_of_flight, gravity=9.81)


if __name__ == "__main__":
    main()





