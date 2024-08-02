import matplotlib.pyplot as plt
from shapely.geometry import LineString

# Function for plotting of flight paths
def plot_flight_paths(flight_paths):
    fig, ax = plt.subplots()
    
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    used_colors = 0
    
    all_paths = []
    
    for flight_path in flight_paths:
        x_coords = [coord[0] for coord in flight_path]
        y_coords = [coord[1] for coord in flight_path]
        
        # Plot the flight path
        ax.plot(x_coords, y_coords, color=colors[used_colors % len(colors)], marker='o', label=f'Flight {used_colors + 1}')
        used_colors += 1
        
        # Creating a LineString object for the path
        path_line = LineString(flight_path)
        all_paths.append(path_line)
        
        # Checking for intersections with previous paths
        for previous_path in all_paths[:-1]:
            if path_line.intersects(previous_path):
                print(f"Intersection found between Flight {used_colors} and another flight.")
    
    ax.legend()
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Flight Paths')
    plt.grid(True)
    plt.show()

# Give input
flight_paths = [
    [(1, 1), (2, 2), (3, 3)],
    [(1, 1), (2, 4), (3, 2)],
    [(1, 1), (4, 2), (3, 4)]
]

plot_flight_paths(flight_paths)
