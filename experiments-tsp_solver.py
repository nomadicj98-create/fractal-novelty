import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from meta_f import MetaF

def generate_cities(n=20, seed=42):
    np.random.seed(seed)
    return np.random.rand(n, 2)

def extract_pattern(cities):
    return 2  # divide into 2 clusters recursively

def tsp_distance(route, dist_matrix):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1)) + dist_matrix[route[-1], route[0]]

def recursive_tsp(cities):
    dist_matrix = squareform(pdist(cities))
    mf = MetaF(extract_pattern)
    route = mf.solve(list(range(len(cities))))
    return route, tsp_distance(route, dist_matrix)

def plot_route(cities, route):
    ordered = cities[route + [route[0]]]
    plt.plot(ordered[:, 0], ordered[:, 1], 'o-')
    plt.title("Recursive TSP Route")
    plt.show()

def run():
    cities = generate_cities()
    route, dist = recursive_tsp(cities)
    print("Route:", route)
    print("Total Distance:", round(dist, 2))
    plot_route(cities, route)

if __name__ == "__main__":
    run()
