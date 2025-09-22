from sklearn.datasets import fetch_openml
from meta_f import MetaF
import numpy as np

def extract_pattern(image):
    return 2  # simple 2x2 block pattern

def compress_image(image):
    mf = MetaF(extract_pattern)
    return mf.solve(image.flatten().tolist())

def run():
    mnist = fetch_openml('mnist_784', version=1)
    sample = mnist.data[0].values.reshape(28, 28)
    compressed = compress_image(sample)
    print("Compression ratio:", len(compressed) / sample.size)

if __name__ == "__main__":
    run()
