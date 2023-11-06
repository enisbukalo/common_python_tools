import pytest
from statistics_common import calc_linear_regression

def test_calc_linear_regression_empty_input():
    xs = []
    ys = []
    with pytest.raises(ValueError):
        calc_linear_regression(xs, ys)

def test_calc_linear_regression_unequal_length_input():
    xs = [1, 2, 3, 4, 5]
    ys = [2, 4, 6]
    with pytest.raises(ValueError):
        calc_linear_regression(xs, ys)

def test_calc_linear_regression_zero_variance_input():
    xs = [1, 2, 3, 4, 5]
    ys = [2, 4, 6, 8, 10]
    r_squared, slope, a = calc_linear_regression(xs, ys)
    assert r_squared == pytest.approx(1.0, abs=1e-3)
    assert slope == pytest.approx(2.0, abs=1e-3)
    assert a == pytest.approx(0.0, abs=1e-3)