import numpy as np
import matplotlib.pyplot as plt
from meta_f import MetaF

def generate_data(n=100, noise=0.1, seed=0):
    np.random.seed(seed)
    x = np.linspace(-2, 2, n)
    y = x**3 + np.sin(x) + noise * np.random.randn(n)
    return x, y

def extract_pattern(data):
    return 2  # split data into halves recursively

def recursive_fit(x, y):
    mf = MetaF(extract_pattern)
    segments = mf.solve(list(zip(x, y)))
    return segments

def plot_data(x, y, segments):
    plt.scatter(x, y, label="Data", alpha=0.6)
    for seg in segments:
        seg_x, seg_y = zip(*seg)
        coeffs = np.polyfit(seg_x, seg_y, deg=3)
        fit_y = np.polyval(coeffs, seg_x)
        plt.plot(seg_x, fit_y, label="Segment Fit")
    plt.title("Recursive Symbolic Regression")
    plt.legend()
    plt.show()

def run():
    x, y = generate_data()
    segments = recursive_fit(x, y)
    plot_data(x, y, segments)

if __name__ == "__main__":
    run()
