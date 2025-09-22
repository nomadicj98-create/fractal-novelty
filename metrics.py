from sklearn.metrics import mutual_info_score
import numpy as np

def edit_distance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

def mutual_info_diff(P, S):
    return mutual_info_score(P, S)

def compression_ratio(original, compressed):
    return 1 - len(compressed) / len(original)
