import random
import math
import matplotlib.pyplot as plt
import itertools

class TSP:
    def __init__(self, towns, distance_matrix):
        self.towns = towns
        self.distance_matrix = distance_matrix
        self.town_index = {town: i for i, town in enumerate(towns)}

    def total_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distance_matrix[self.town_index[route[i]]][self.town_index[route[i+1]]]
        # Add distance to return to start
        distance += self.distance_matrix[self.town_index[route[-1]]][self.town_index[route[0]]]
        return distance

class SimulatedAnnealingSolver:
    def __init__(self, tsp, initial_temp=10000, cooling_rate=0.995, iteration_limit=100000):
        self.tsp = tsp
        self.temperature = initial_temp
        self.cooling_rate = cooling_rate
        self.iteration_limit = iteration_limit

    def random_route(self):
        route = self.tsp.towns[1:]  # exclude start town Windhoek
        random.shuffle(route)
        return [self.tsp.towns[0]] + route

    def neighbor(self, route):
        # Swap two towns in the route (excluding the first town which is fixed start)
        new_route = route[:]
        i, j = random.sample(range(1, len(route)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        return new_route

    def acceptance_probability(self, old_cost, new_cost, temperature):
        if new_cost < old_cost:
            return 1.0
        else:
            return math.exp((old_cost - new_cost) / temperature)

    def solve(self):
        current_route = self.random_route()
        current_cost = self.tsp.total_distance(current_route)
        best_route = current_route[:]
        best_cost = current_cost

        iteration = 0
        while self.temperature > 1e-8 and iteration < self.iteration_limit:
            new_route = self.neighbor(current_route)
            new_cost = self.tsp.total_distance(new_route)

            ap = self.acceptance_probability(current_cost, new_cost, self.temperature)
            if ap > random.random():
                current_route = new_route
                current_cost = new_cost
                if current_cost < best_cost:
                    best_route = current_route[:]
                    best_cost = current_cost

            self.temperature *= self.cooling_rate
            iteration += 1

        return best_route, best_cost

def plot_route(tsp, route, title):
    town_coords = {
        # Approximate coordinates for visualization (not to scale)
        'Windhoek': (0, 0),
        'Swakopmund': (-100, 50),
        'Walvis Bay': (-90, 40),
        'Otjiwarongo': (50, 100),
        'Tsumeb': (120, 150),
        'Grootfontein': (130, 170),
        'Mariental': (20, -80),
        'Keetmanshoop': (80, -150),
        'Ondangwa': (180, 200),
        'Oshakati': (190, 210)
    }

    x = [town_coords[town][0] for town in route] + [town_coords[route[0]][0]]
    y = [town_coords[town][1] for town in route] + [town_coords[route[0]][1]]

    plt.figure(figsize=(10,6))
    plt.plot(x, y, 'o-', color='blue')
    for i, town in enumerate(route):
        label = town
        if i == 0:
            label += " (Start)"
        plt.text(town_coords[town][0], town_coords[town][1], label)
    plt.title(title)
    plt.xlabel('X Coordinate (approx)')
    plt.ylabel('Y Coordinate (approx)')
    plt.grid(True)
    plt.show()

def brute_force_tsp(tsp):
    # Only for small sets (e.g., 5 towns) due to factorial complexity
    towns = tsp.towns[1:]  # exclude start town
    start = tsp.towns[0]
    best_route = None
    best_cost = float('inf')
    for perm in itertools.permutations(towns):
        route = [start] + list(perm)
        cost = tsp.total_distance(route)
        if cost < best_cost:
            best_cost = cost
            best_route = route
    return best_route, best_cost

def main():
    towns = ['Windhoek', 'Swakopmund', 'Walvis Bay', 'Otjiwarongo', 'Tsumeb', 'Grootfontein', 'Mariental', 'Keetmanshoop', 'Ondangwa', 'Oshakati']
    distance_matrix = [
        [0, 361, 395, 249, 433, 459, 268, 497, 678, 712],
        [361, 0, 35.5, 379, 562, 589, 541, 859, 808, 779],
        [395, 35.5, 0, 413, 597, 623, 511, 732, 884, 855],
        [249, 379, 413, 0, 260, 183, 519, 768, 514, 485],
        [433, 562, 597, 260, 0, 60, 682, 921, 254, 288],
        [459, 589, 623, 183, 60, 0, 708, 947, 308, 342],
        [268, 541, 511, 519, 682, 708, 0, 231, 909, 981],
        [497, 859, 732, 768, 921, 947, 231, 0, 1175, 1210],
        [678, 808, 884, 514, 254, 308, 909, 1175, 0, 30],
        [712, 779, 855, 485, 288, 342, 981, 1210, 30, 0]
    ]

    tsp = TSP(towns, distance_matrix)
    solver = SimulatedAnnealingSolver(tsp)

    initial_route = solver.random_route()
    initial_distance = tsp.total_distance(initial_route)
    print("Initial route and cumulative distances:")
    cumulative_distance = 0
    for i in range(len(initial_route)):
        if i == 0:
            print(f"{initial_route[i]}: 0 km")
        else:
            prev = initial_route[i-1]
            curr = initial_route[i]
            dist = distance_matrix[towns.index(prev)][towns.index(curr)]
            cumulative_distance += dist
            print(f"{curr}: {cumulative_distance:.2f} km")
    # Add distance to return to start
    cumulative_distance += distance_matrix[towns.index(initial_route[-1])][towns.index(initial_route[0])]
    print(f"Return to {initial_route[0]}: {cumulative_distance:.2f} km total")
    plot_route(tsp, initial_route, "Initial Route")

    best_route, best_distance = solver.solve()
    print("\nOptimized route and cumulative distances:")
    cumulative_distance = 0
    for i in range(len(best_route)):
        if i == 0:
            print(f"{best_route[i]}: 0 km")
        else:
            prev = best_route[i-1]
            curr = best_route[i]
            dist = distance_matrix[towns.index(prev)][towns.index(curr)]
            cumulative_distance += dist
            print(f"{curr}: {cumulative_distance:.2f} km")
    # Add distance to return to start
    cumulative_distance += distance_matrix[towns.index(best_route[-1])][towns.index(best_route[0])]
    print(f"Return to {best_route[0]}: {cumulative_distance:.2f} km total")
    plot_route(tsp, best_route, "Optimized Route")

    # Analysis and evaluation
    print("\nAnalysis and Evaluation:")
    print("The simulated annealing algorithm starts with a random route and iteratively improves it by swapping towns.")
    print("Worse solutions are occasionally accepted to escape local minima, controlled by the cooling schedule.")
    print("Parameters such as initial temperature, cooling rate, and iteration limit affect the quality and speed of convergence.")
    print("For larger town sets, brute-force is infeasible due to factorial complexity, making simulated annealing a practical approach.")
    print("For smaller sets (e.g., 5 towns), brute-force can find the optimal route for comparison.")

    # Optional: Compare with brute-force for smaller subset
    small_towns = towns[:5]
    small_distance_matrix = [row[:5] for row in distance_matrix[:5]]
    small_tsp = TSP(small_towns, small_distance_matrix)
    bf_route, bf_distance = brute_force_tsp(small_tsp)
    print("\nBrute-force optimal route for first 5 towns:", bf_route)
    print(f"Brute-force optimal distance: {bf_distance:.2f} km")


if __name__ == "__main__":
    main()
