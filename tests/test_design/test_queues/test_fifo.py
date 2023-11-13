import pytest

from design_common.queues.fifo import Fifo


def test_fifo_properties():
    with pytest.raises(TypeError):
        Fifo(max_queue_size="hello")

    fifo = Fifo(max_queue_size=300)

    assert fifo.max_size == 300
    assert fifo.has_max_size() is True

    fifo = Fifo()

    assert fifo.is_full() is False
    assert fifo.is_empty() is True
    assert fifo.free_space() == None
    assert fifo.first() is None
    assert fifo.last() is None
    assert fifo.length() is 0


def test_enqueue_with_no_max_size():
    fifo = Fifo()
    assert fifo.length() == 0

    assert fifo.enqueue(1) is True
    assert fifo.length() == 1
    assert fifo.first() == 1
    assert fifo.last() == 1

    fifo.clear()
    assert fifo.length() == 0
    assert fifo._queue == []

    items_to_add = [0, 1, 2, 3, 4, 5, 6, 7]
    running_length = 0
    for item in items_to_add:
        assert fifo.enqueue(item) is True
        running_length += 1
        assert fifo.length() == running_length
        assert fifo.first() == 0
        assert fifo.last() == item

    assert fifo._queue == [0, 1, 2, 3, 4, 5, 6, 7]


def test_enqueue_with_max_size():
    fifo = Fifo(max_queue_size=3)
    assert fifo.length() == 0

    assert fifo.enqueue(1) is True
    assert fifo.length() == 1
    assert fifo.first() == 1
    assert fifo.last() == 1

    assert fifo.enqueue(2) is True
    assert fifo.length() == 2
    assert fifo.first() == 1
    assert fifo.last() == 2

    assert fifo.enqueue(3) is True
    assert fifo.length() == 3
    assert fifo.first() == 1
    assert fifo.last() == 3

    assert fifo.enqueue(4) is False
    assert fifo.length() == 3
    assert fifo.first() == 1
    assert fifo.last() == 3


def test_dequeue_single():
    fifo = Fifo()
    assert fifo.enqueue(1) is True
    assert fifo.enqueue(2) is True
    assert fifo.enqueue(3) is True

    assert fifo.dequeue() == 1
    assert fifo.is_empty() is False
    assert fifo._queue == [2, 3]

    assert fifo.dequeue() == 2
    assert fifo.is_empty() is False
    assert fifo._queue == [3]

    assert fifo.dequeue() == 3
    assert fifo.is_empty() is True
    assert fifo._queue == []

    assert fifo.dequeue() is None
    assert fifo.is_empty() is True
    assert fifo._queue == []


def test_dequeue_multiple():
    fifo = Fifo()
    items_to_add = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in items_to_add:
        assert fifo.enqueue(item) is True

    assert fifo.length() == 10
    assert fifo._queue == items_to_add

    assert fifo.dequeue(5) == [1, 2, 3, 4, 5]
    assert fifo.length() == 5
    assert fifo._queue == [6, 7, 8, 9, 10]

    assert fifo.dequeue(3) == [6, 7, 8]
    assert fifo.length() == 2
    assert fifo._queue == [9, 10]

    assert fifo.dequeue(5) == [9, 10]
    assert fifo.length() == 0
    assert fifo.is_empty() is True
    assert fifo._queue == []
