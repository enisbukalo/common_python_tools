from utilities.sorting.merge_sort import merge_sort

from random import randint


def test_merge_sort_positives():
    sample_size = 10000
    to_sort = [randint(1, sample_size) for _ in range(sample_size)]
    expected = sorted(to_sort)

    assert merge_sort(to_sort) == expected


def test_merge_sort_negatives():
    sample_size = 10000
    to_sort = [randint(-sample_size, 0) for _ in range(sample_size)]
    expected = sorted(to_sort)

    assert merge_sort(to_sort) == expected


def test_merge_sort_mixed():
    sample_size = 10000
    to_sort = [randint(-(sample_size / 2), sample_size / 2) for _ in range(sample_size)]
    expected = sorted(to_sort)

    assert merge_sort(to_sort) == expected


def test_merge_sort_edge_case():
    sample_size = 100
    to_sort = [randint(0, 0) for _ in range(sample_size)]

    assert merge_sort(to_sort) == to_sort
