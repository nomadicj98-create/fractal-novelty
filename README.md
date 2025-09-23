# fractal-novelty

README.md

# Fractal Novelty Information Systems

This repository supports the paper "Introduction to Fractal Novelty Information Systems" by John A. Asher.

## Features
- Recursive abstraction engine (Meta-F)
- Novelty metrics: edit distance, MI difference, compression ratio
- Benchmarks: MNIST compression, TSP optimization, symbolic regression
- Visualizations and interactive notebooks

## Installation
```bash
pip install -r requirements.txt

##Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

##Bash

from meta_f import MetaF
solver = MetaF(pattern_extractor)
solution = solver.solve(problem)

##Bash

python experiments/experiments-mnist_compression.py

##output

Compression ratio: ~0.46

##Bash

python experiments/experiments-tsp_solver.py

##output

Route: [3, 7, 1, 0, ...]
Total Distance: ~5.83

##Bash

python experiments/experiments-symbolic_regression.py

##output

Segment Fit: y ≈ ax³ + bx + c

##Bash

pytest tests/

##output

============================= test session starts =============================
collected 3 items

tests/test_metrics.py ...                                               [100%]

============================== 3 passed in 0.01s ==============================

##Bash

jupyter notebook notebooks/demo_meta_f.ipynb


## `requirements.txt`

```text
numpy
scikit-learn
matplotlib
notebook
scikit-learn
matplotlib
notebook
