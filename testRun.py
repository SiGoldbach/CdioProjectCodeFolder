import math

coordinates_array = [[2, 4], [6, 3], [8, 8], [8, 3], [10, 10], [20, 20], [1, 9], [16, 14]]
obstacle_coordinates = [[8, 8], [10, 12]]
robot_x = 0
robot_y = 0

def find_nearest_ball(robot_x, robot_y, coordinates_array):
    closest_distance = float('inf')
    closest_coordinates = []

    for coordinates in coordinates_array:
        x = coordinates[0]
        y = coordinates[1]
        distance = math.sqrt((x - robot_x) ** 2 + (y - robot_y) ** 2)

        if distance < closest_distance:
            closest_distance = distance
            closest_coordinates = coordinates

    return closest_coordinates, closest_distance

def calculate_angle(target_x, target_y, robot_x, robot_y):
    angle = math.atan2(target_y - robot_y, target_x - robot_x) * (180 / math.pi)
    return angle

def move_robot(target_x, target_y):
    global robot_x, robot_y
    robot_x = target_x
    robot_y = target_y
    # Implement your code to move the robot to the target coordinates
    print("Moving robot to coordinates:", target_x, target_y)

# Main loop to process each target
while coordinates_array:
    # Find the closest coordinates and distance
    closest_coordinates, closest_distance = find_nearest_ball(robot_x, robot_y, coordinates_array)
    print("Closest coordinates:", closest_coordinates)

    # Calculate the angle between the robot's current location and the target
    angle = calculate_angle(closest_coordinates[0], closest_coordinates[1], robot_x, robot_y)
    print("Angle:", angle)

    # Move the robot to the closest coordinates
    move_robot(closest_coordinates[0], closest_coordinates[1])

    # Print the updated robot's coordinates
    print("Robot's coordinates:", robot_x, robot_y)

    # Remove the processed target from the coordinates_array
    coordinates_array.remove(closest_coordinates)

    # Print the closest distance
    print("Closest distance:", closest_distance)
    print()

# After processing all targets
print("All targets processed.")
