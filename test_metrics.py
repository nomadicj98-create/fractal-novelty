import pytest
from metrics import edit_distance, mutual_info_diff, compression_ratio

def test_edit_distance():
    assert edit_distance("abc", "adc") == 1
    assert edit_distance("abc", "abc") == 0
    assert edit_distance("abc", "xyz") == 3

def test_mutual_info_diff():
    a = [0, 1, 1, 0]
    b = [1, 0, 1, 0]
    assert mutual_info_diff(a, b) >= 0

def test_compression_ratio():
    original = list(range(100))
    compressed = list(range(60))
    ratio = compression_ratio(original, compressed)
    assert 0.3 < ratio < 0.5
