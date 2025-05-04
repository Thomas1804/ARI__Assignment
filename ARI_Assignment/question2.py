import random
import math
import matplotlib.pyplot as plt

class TSP:
    def __init__(self):
        self.towns = [
            "Windhoek", "Swakopmund", "Walvis Bay", "Otjiwarongo",
            "Tsumeb", "Grootfontein", "Mariental", "Keetmanshoop",
            "Ondangwa", "Oshakati"
        ]

        # Distance matrix based on the assignment
        self.distances = [
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

    def route_distance(self, route):
        distance = 0
        for i in range(len(route)):
            from_idx = route[i]
            to_idx = route[(i + 1) % len(route)]
            distance += self.distances[from_idx][to_idx]
        return distance

    def get_town_names(self, route):
        return [self.towns[i] for i in route]

class SimulatedAnnealingSolver:
    def __init__(self, tsp):
        self.tsp = tsp

    def solve(self, initial_temp=10000, cooling_rate=0.995, iterations=10000):
        current_route = list(range(len(self.tsp.towns)))
        random.shuffle(current_route)

        best_route = list(current_route)
        best_distance = self.tsp.route_distance(best_route)

        temperature = initial_temp

        for i in range(iterations):
            # Swap two cities
            new_route = list(current_route)
            a, b = random.sample(range(len(new_route)), 2)
            new_route[a], new_route[b] = new_route[b], new_route[a]

            current_distance = self.tsp.route_distance(current_route)
            new_distance = self.tsp.route_distance(new_route)

            if new_distance < current_distance:
                current_route = new_route
                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance
            else:
                # Accept worse solution with probability
                prob = math.exp((current_distance - new_distance) / temperature)
                if random.random() < prob:
                    current_route = new_route

            # Cool down
            temperature *= cooling_rate

        return best_route, best_distance

def plot_route(tsp, route, title):
    names = tsp.get_town_names(route)
    x = list(range(len(route) + 1))
    y = names + [names[0]]
    plt.figure(figsize=(10, 5))
    plt.plot(x, list(range(len(route)+1)), 'o-')
    for i, town in enumerate(y):
        plt.text(x[i], i, town)
    plt.title(title)
    plt.yticks([])
    plt.xticks([])
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    tsp = TSP()
    solver = SimulatedAnnealingSolver(tsp)

    best_route, best_distance = solver.solve()

    print("Best route found:")
    print(" → ".join(tsp.get_town_names(best_route)))
    print(f"Total distance: {best_distance:.2f} km")

    plot_route(tsp, best_route, "Optimised TSP Route via Simulated Annealing")

