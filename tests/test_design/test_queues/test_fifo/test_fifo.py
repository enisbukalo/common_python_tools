import pytest

from design_common.queues.fifo.fifo import Fifo


def test_fifo_properties():
    with pytest.raises(TypeError):
        Fifo(max_queue_size="hello")

    fifo = Fifo(max_queue_size=300)

    assert fifo.max_size == 300
    assert fifo.has_max_size is True

    fifo = Fifo()

    assert fifo._at_limit() is False
    assert fifo._surpasses_max_size() is False
    assert fifo.free_space == None
    assert fifo.first is None
    assert fifo.last is None
    assert fifo.length is 0


def test_enqueue_with_no_max_size():
    fifo = Fifo()
    assert fifo.length == 0

    fifo.enqueue(1)
    assert fifo.length == 1
    assert fifo.first == 1
    assert fifo.last == 1

    fifo.clear()
    assert fifo.length == 0
    assert fifo._queue == []

    fifo.enqueue(0, 1, 2, 3, 4, 5, 6, 7)
    assert fifo.length == 8
    assert fifo.first == 0
    assert fifo.last == 7


def test_enqueue_with_max_size_without_replace_without_partial():
    fifo = Fifo(max_queue_size=3)
    assert fifo.length == 0

    fifo.enqueue(1)
    assert fifo.length == 1
    assert fifo._queue == [1]

    fifo.enqueue(2)
    assert fifo.length == 2
    assert fifo._queue == [1, 2]

    fifo.enqueue(3)
    assert fifo.length == 3
    assert fifo._queue == [1, 2, 3]

    # From here on out we are at our max size without replacement enabled.
    #   We should not see the queue change at all with new additions.
    fifo.enqueue(4)
    assert fifo.length == 3
    assert fifo._queue == [1, 2, 3]

    fifo.enqueue(100, "100", 50)
    assert fifo.length == 3
    assert fifo._queue == [1, 2, 3]


def test_enqueue_with_max_size_with_replace_without_partial():
    fifo = Fifo(max_queue_size=3)
    assert fifo.length == 0

    fifo.enqueue(1, replace=True)
    assert fifo.length == 1
    assert fifo._queue == [1]

    fifo.enqueue(2, replace=True)
    assert fifo.length == 2
    assert fifo._queue == [1, 2]

    fifo.enqueue(3, replace=True)
    assert fifo.length == 3
    assert fifo._queue == [1, 2, 3]

    # From here on out we are at our max size with replacement enabled.
    #   We should see the queue change by dropping the old items and adding the new ones.
    fifo.enqueue(4, replace=True)
    assert fifo.length == 3
    assert fifo._queue == [2, 3, 4]

    fifo.enqueue(100, "0909", True, replace=True)
    assert fifo.length == 3
    assert fifo._queue == [100, "0909", True]


def test_enqueue_with_max_size_without_replace_with_partial():
    fifo = Fifo(max_queue_size=5)
    assert fifo.length == 0

    fifo.enqueue(1, add_partial=True)
    assert fifo.length == 1
    assert fifo._queue == [1]

    fifo.enqueue(2, add_partial=True)
    assert fifo.length == 2
    assert fifo._queue == [1, 2]

    fifo.enqueue(3, add_partial=True)
    assert fifo.length == 3
    assert fifo._queue == [1, 2, 3]

    # From here on out we are at our max size without replacement enabled.
    #   We should see the queue change by only adding what it can to fill the queue from the
    #   front of the args passed in. If at max size, we won't be replacing anything.

    fifo.enqueue(100, "100", 50, add_partial=True)
    assert fifo.length == 5
    assert fifo._queue == [1, 2, 3, 100, "100"]

    fifo.enqueue(True, True, False, add_partial=True)
    assert fifo.length == 5
    assert fifo._queue == [1, 2, 3, 100, "100"]


def test_enqueue_with_max_size_with_replace_with_partial():
    fifo = Fifo(max_queue_size=5)
    assert fifo.length == 0

    fifo.enqueue(1, replace=True, add_partial=True)
    assert fifo.length == 1
    assert fifo._queue == [1]

    fifo.enqueue(2, replace=True, add_partial=True)
    assert fifo.length == 2
    assert fifo._queue == [1, 2]

    fifo.enqueue(3, replace=True, add_partial=True)
    assert fifo.length == 3
    assert fifo._queue == [1, 2, 3]

    # From here on out we are at our max size with replacement enabled.
    #   We should see the queue change by only adding what it can to fill the queue from the
    #   front of the args passed in. If at max size, we will be replacing now.

    fifo.enqueue(100, "100", 50, replace=True, add_partial=True)
    assert fifo.length == 5
    assert fifo._queue == [2, 3, 100, "100", 50]

    fifo.enqueue(True, True, False, replace=True, add_partial=True)
    assert fifo.length == 5
    assert fifo._queue == ["100", 50, True, True, False]


def test_dequeue_single():
    fifo = Fifo()
    fifo.enqueue(1)
    fifo.enqueue(2)
    fifo.enqueue(3)

    assert fifo.dequeue() == 1
    assert fifo.is_empty is False
    assert fifo._queue == [2, 3]

    assert fifo.dequeue() == 2
    assert fifo.is_empty is False
    assert fifo._queue == [3]

    assert fifo.dequeue() == 3
    assert fifo.is_empty is True
    assert fifo._queue == []

    assert fifo.dequeue() is None
    assert fifo.is_empty is True
    assert fifo._queue == []


def test_dequeue_multiple():
    fifo = Fifo()
    fifo.enqueue(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    assert fifo.dequeue(2) == [1, 2]
    assert fifo.is_empty is False
    assert fifo._queue == [3, 4, 5, 6, 7, 8, 9, 10]

    assert fifo.dequeue(5) == [3, 4, 5, 6, 7]
    assert fifo.is_empty is False
    assert fifo._queue == [8, 9, 10]

    assert fifo.dequeue(10) == [8, 9, 10]
    assert fifo.is_empty is True
    assert fifo._queue == []
