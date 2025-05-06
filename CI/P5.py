import numpy as np

# Distance matrix between cities (symmetric)
cities = np.array([
    [0, 2, 9, 10, 7, 14, 11],
    [1, 0, 6, 4, 12, 8, 10],
    [15, 7, 0, 8, 6, 9, 13],
    [6, 3, 12, 0, 9, 11, 5],
    [7, 12, 6, 9, 0, 4, 8],
    [14, 8, 9, 11, 4, 0, 6],
    [11, 10, 13, 5, 8, 6, 0]
])

# Ant Colony Optimization parameters
num_ants = 10
num_iterations = 100
decay = 0.1
alpha = 1  # pheromone importance
beta = 2   # distance importance
num_cities = cities.shape[0]

# Initialize pheromone matrix
pheromone = np.ones((num_cities, num_cities)) / num_cities

# Variables to track best solution
best_cost = float('inf')
best_path = None

# Function to calculate route distance
def route_distance(route):
    dist = 0
    for i in range(len(route)):
        dist += cities[route[i - 1], route[i]]
    return dist

# Function to select next city based on probability
def select_next_city(probabilities):
    return np.random.choice(range(len(probabilities)), p=probabilities)

# Main loop for Ant Colony Optimization
for iteration in range(num_iterations):
    all_routes = []
    all_distances = []
    
    # Each ant constructs a route
    for ant in range(num_ants):
        visited = []
        current_city = np.random.randint(num_cities)
        visited.append(current_city)
        
        while len(visited) < num_cities:
            unvisited = list(set(range(num_cities)) - set(visited))
            pheromone_values = np.array([pheromone[current_city][j] for j in unvisited])
            distances = np.array([cities[current_city][j] for j in unvisited])
            heuristic = 1 / distances
            
            # Calculate the probability for each unvisited city
            prob = (pheromone_values ** alpha) * (heuristic ** beta)
            prob /= prob.sum()
            
            # Select the next city based on probability
            next_city = unvisited[select_next_city(prob)]
            visited.append(next_city)
            current_city = next_city
        
        # Calculate the distance for the complete route
        route = visited
        distance = route_distance(route)
        
        # Save the route and distance
        all_routes.append(route)
        all_distances.append(distance)
        
        # Update the best solution if a better one is found
        if distance < best_cost:
            best_cost = distance
            best_path = route
    
    # Pheromone evaporation
    pheromone *= (1 - decay)
    
    # Update pheromone levels based on the routes
    for route, dist in zip(all_routes, all_distances):
        for i in range(num_cities):
            a, b = route[i - 1], route[i]
            pheromone[a][b] += 1 / dist

# Output the best path and cost
print("Best path:", best_path + [best_path[0]])  # The path is cyclic, so return to the starting city
print("Best cost:", best_cost)
