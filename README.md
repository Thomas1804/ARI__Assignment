# Artificial Intelligence Group Assignment

The following assignment is a compilation of implementations of a few AI algorithms and techniques in the form of four main tasks:

---

## Question 1: Search Algorithms - Informed Search

**Objective:**  
Implement two informed search algorithms, A* Search and Greedy Best-First Search, to find the shortest path in a maze from an initial state (A) to a goal state (B).

**Key Features:
- Maze class to read maze from text file, find start and goal, keep walls, and return neighbors.
- `solve(algorithm="greedy")` function with a priority queue frontier with the correct heuristics.
- Node class to keep state, parent, action, and cost.
- Visual display of the maze with initial state, goal, path, explored states, and walls.

---
## Question 2: CSP - Travel Salesperson Problem: Simulated Annealing

**Objective:**
Solve the Traveling Salesman Problem (TSP) for 10 big towns in Namibia using Simulated Annealing to find the shortest route that visits each town once and returns home.

**Key Features:**
- TSP class to store town names and distances, calculate route distance.
- SimulatedAnnealingSolver class to generate initial routes, produce neighbors, implement cooling schedule, and accept/reject routes with probability.
- Output: initial and optimized routes with distances and visualizations using Matplotlib.
- Analysis: comparison of results with brute-force and discussion of parameter effects.

---
## Question 3: Adversarial Search - Tic-Tac-Toe AI with Minimax

**Objective:**
Implement an unbeatable Tic-Tac-Toe AI using the Minimax algorithm.

**Key Features:**
- Functions to determine player turns, available actions, result of actions, winner check, terminal state check, and utility calculation.
- Minimax function to return the optimal move for the current player.
- A runner program to facilitate human vs AI play with terminal or GUI display.

---
## Question 4: MDPs - Q-learning for Gridworld

**Objective:**
Use Q-learning to calculate the optimal value function and policy for a gridworld MDP with special states and rewards.

**Key Features:**
- Gridworld environment with states, actions, and rewards.
- Q-learning algorithm with hyperparameters γ (discount), ε (exploration), α (learning rate), episodes, steps.
- Printing initialization information, learning curves, and final optimal value function and policy.

---
## General Notes

- Assignment is in Python and default libraries such as `random`, `math`, and `matplotlib`.
- Visualizations are included wherever applicable to show paths, routes, and policies.
- Deliverables and testing directions are mentioned for each task.

---

## How to Run

Each task is implemented in separate Python scripts or modules. Refer to the respective directories or files for detailed instructions on how to run and test each component.

---

## Contact

Questions and contributions are to be addressed to the assignment team.
