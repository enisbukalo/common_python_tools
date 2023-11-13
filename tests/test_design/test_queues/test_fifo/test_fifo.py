import pytest

from design_common.queues.fifo.fifo import Fifo


def test_fifo_properties():
    with pytest.raises(TypeError):
        Fifo(boundary="hello", replace_at_boundary=False, take_partial=False)

    with pytest.raises(TypeError):
        Fifo(boundary=300, replace_at_boundary="hello", take_partial=False)

    with pytest.raises(TypeError):
        Fifo(boundary=300, replace_at_boundary=False, take_partial="hello")

    fifo = Fifo(boundary=300, replace_at_boundary=False, take_partial=True)

    assert fifo.boundary == 300
    assert fifo.boundary_enabled is True
    assert fifo.replace_enabled is False
    assert fifo.partial_enabled is True

    fifo = Fifo()

    assert fifo._at_boundary() is False
    assert fifo._surpasses_boundary() is False
    assert fifo.free_space == None


def test_enqueue_with_no_boundary():
    fifo = Fifo()
    assert fifo.__len__() == 0

    fifo.enqueue(1)
    assert fifo.__len__() == 1

    fifo.clear()
    assert fifo.__len__() == 0

    fifo.enqueue(0, 1, 2, 3, 4, 5, 6, 7)
    assert fifo.__len__() == 8


def test_enqueue_with_boundary_without_replace_without_partial():
    fifo = Fifo(boundary=3, replace_at_boundary=False, take_partial=False)
    assert fifo.__len__() == 0

    fifo.enqueue(1)
    assert fifo.__len__() == 1
    assert fifo.queue == [1]

    fifo.enqueue(2)
    assert fifo.__len__() == 2
    assert fifo.queue == [1, 2]

    fifo.enqueue(3)
    assert fifo.__len__() == 3
    assert fifo.queue == [1, 2, 3]

    # From here on out we are at our boundary without replacement enabled.
    #   We should not see the queue change at all with new additions.
    fifo.enqueue(4)
    assert fifo.__len__() == 3
    assert fifo.queue == [1, 2, 3]

    fifo.enqueue(100, "100", 50)
    assert fifo.__len__() == 3
    assert fifo.queue == [1, 2, 3]


def test_enqueue_with_boundary_with_replace_without_partial():
    fifo = Fifo(boundary=3, replace_at_boundary=True, take_partial=False)
    assert fifo.__len__() == 0

    fifo.enqueue(1)
    assert fifo.__len__() == 1
    assert fifo.queue == [1]

    fifo.enqueue(2)
    assert fifo.__len__() == 2
    assert fifo.queue == [1, 2]

    fifo.enqueue(3)
    assert fifo.__len__() == 3
    assert fifo.queue == [1, 2, 3]

    # From here on out we are at our boundary with replacement enabled.
    #   We should see the queue change by dropping the old items and adding the new ones.
    fifo.enqueue(4)
    assert fifo.__len__() == 3
    assert fifo.queue == [2, 3, 4]

    fifo.enqueue(100, "0909", True)
    assert fifo.__len__() == 3
    assert fifo.queue == [100, "0909", True]


def test_enqueue_with_boundary_without_replace_with_partial():
    fifo = Fifo(boundary=5, replace_at_boundary=False, take_partial=True)
    assert fifo.__len__() == 0

    fifo.enqueue(1)
    assert fifo.__len__() == 1
    assert fifo.queue == [1]

    fifo.enqueue(2)
    assert fifo.__len__() == 2
    assert fifo.queue == [1, 2]

    fifo.enqueue(3)
    assert fifo.__len__() == 3
    assert fifo.queue == [1, 2, 3]

    # From here on out we are at our boundary without replacement enabled.
    #   We should see the queue change by only adding what it can to fill the queue from the
    #   front of the args passed in. If at boundary, we won't be replacing anything.

    fifo.enqueue(100, "100", 50)
    assert fifo.__len__() == 5
    assert fifo.queue == [1, 2, 3, 100, "100"]

    fifo.enqueue(True, True, False)
    assert fifo.__len__() == 5
    assert fifo.queue == [1, 2, 3, 100, "100"]


def test_enqueue_with_boundary_with_replace_with_partial():
    fifo = Fifo(boundary=5, replace_at_boundary=True, take_partial=True)
    assert fifo.__len__() == 0

    fifo.enqueue(1)
    assert fifo.__len__() == 1
    assert fifo.queue == [1]

    fifo.enqueue(2)
    assert fifo.__len__() == 2
    assert fifo.queue == [1, 2]

    fifo.enqueue(3)
    assert fifo.__len__() == 3
    assert fifo.queue == [1, 2, 3]

    # From here on out we are at our boundary with replacement enabled.
    #   We should see the queue change by only adding what it can to fill the queue from the
    #   front of the args passed in. If at boundary, we will be replacing now.

    fifo.enqueue(100, "100", 50)
    assert fifo.__len__() == 5
    assert fifo.queue == [2, 3, 100, "100", 50]

    fifo.enqueue(True, True, False)
    assert fifo.__len__() == 5
    assert fifo.queue == ["100", 50, True, True, False]


def test_dequeue():
    fifo = Fifo()
    fifo.enqueue(1)
    fifo.enqueue(2)
    fifo.enqueue(3)

    assert fifo.dequeue() == 1
    assert fifo.is_empty is False
    assert fifo.queue == [2, 3]

    assert fifo.dequeue() == 2
    assert fifo.is_empty is False
    assert fifo.queue == [3]

    assert fifo.dequeue() == 3
    assert fifo.is_empty is True
    assert fifo.queue == []

    assert fifo.dequeue() is None
    assert fifo.is_empty is True
    assert fifo.queue == []
