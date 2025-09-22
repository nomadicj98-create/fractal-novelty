import numpy as np

class MetaF:
    def __init__(self, pattern_extractor):
        self.extractor = pattern_extractor

    def solve(self, problem):
        pattern = self.extractor(problem)
        return self._recursive_solve(problem, pattern)

    def _recursive_solve(self, P, pattern):
        if self._is_base_case(P):
            return self._base_solution(P)
        subproblems = self._decompose(P, pattern)
        subsolutions = [self._recursive_solve(p, pattern) for p in subproblems]
        return self._stitch(subsolutions)

    def _is_base_case(self, P):
        return len(P) <= 1

    def _base_solution(self, P):
        return P

    def _decompose(self, P, pattern):
        return [P[i::pattern] for i in range(pattern)]

    def _stitch(self, solutions):
        return sum(solutions, [])
