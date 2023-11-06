"""
This module provides classes and functions for working with statistics.

Functions:
    calc_linear_regression(xs: Iterable, ys: Iterable)

Classes:
    None
"""
from typing import Iterable

def calc_linear_regression(xs: Iterable, ys: Iterable) -> tuple:
    """
    Calculates the linear regression of two Iterables of values.

    Args:
        xs (Iterable): An Iterable of x values.
        ys (Iterable): An Iterable of y values.

    Returns:
        tuple: A tuple containing the r-squared value, slope, and y-intercept of the linear regression.
    """
    # Get The Means.
    if len(xs) == 0 and len(ys) == 0: raise ValueError("Inputs must not be empty.")
    if len(xs) != len(ys): raise ValueError("Inputs must be the same length.")

    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)

    # Get The Distances.
    x_dist = [i - x_mean for i in xs]
    y_dist = [i - y_mean for i in ys]

    # Get The Variances.
    Sxx = [i**2 for i in x_dist]
    Syy = [i**2 for i in y_dist]
    Sxy = [i * j for i, j in zip(x_dist, y_dist)]

    # Get The Slope.
    slope = sum(Sxy) / sum(Sxx)

    # Get The Y-Intercept.
    a = y_mean - slope * x_mean

    # Get The Regression Line.
    y_hat = [a + slope * i for i in xs]

    # Get The Regression Distances.
    y_hat_distances = [i - y_mean for i in y_hat]

    # Y Hate Squared
    y_hate_squared = [i**2 for i in y_hat_distances]

    # R Squared
    r_squared = sum(y_hate_squared) / sum(Syy)

    return r_squared, slope, a
