from typing import Any


def ensure_instance(expected_instance: Any):
    """
    A decorator function that ensures the second argument of the decorated function is an instance of the expected instance.

    Parameters:
    - expected_instance (Any): The expected instance type.

    Returns:
    - wrapper: The decorated function.
    """

    def inner(func):
        def wrapper(*args):
            if isinstance(args[1], expected_instance):
                return func(args[0], args[1])
            else:
                raise ValueError(f"{args[0]} is not an instance of {expected_instance}")

        return wrapper

    return inner
