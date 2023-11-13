import pytest

from design_common.queues.lifo import Lifo


def test_lifo_properties():
    with pytest.raises(TypeError):
        Lifo(max_queue_size="hello")

    lifo = Lifo(max_queue_size=300)

    assert lifo.max_size == 300
    assert lifo.has_max_size() is True

    lifo = Lifo()

    assert lifo.is_full() is False
    assert lifo.is_empty() is True
    assert lifo.free_space() == None
    assert lifo.first() is None
    assert lifo.last() is None
    assert lifo.length() is 0


def test_enqueue_with_no_max_size():
    lifo = Lifo()
    assert lifo.length() == 0

    assert lifo.enqueue(1) is True
    assert lifo.length() == 1
    assert lifo.first() == 1
    assert lifo.last() == 1

    lifo.clear()
    assert lifo.length() == 0
    assert lifo._queue == []

    items_to_add = [0, 1, 2, 3, 4, 5, 6, 7]
    running_length = 0
    for item in items_to_add:
        assert lifo.enqueue(item) is True
        running_length += 1
        assert lifo.length() == running_length
        assert lifo.first() == 0
        assert lifo.last() == item

    assert lifo._queue == items_to_add


def test_enqueue_with_max_size():
    lifo = Lifo(max_queue_size=3)
    assert lifo.length() == 0

    assert lifo.enqueue(1) is True
    assert lifo.length() == 1
    assert lifo.first() == 1
    assert lifo.last() == 1

    assert lifo.enqueue(2) is True
    assert lifo.length() == 2
    assert lifo.first() == 1
    assert lifo.last() == 2

    assert lifo.enqueue(3) is True
    assert lifo.length() == 3
    assert lifo.first() == 1
    assert lifo.last() == 3

    assert lifo.enqueue(4) is False
    assert lifo.length() == 3
    assert lifo.first() == 1
    assert lifo.last() == 3


def test_dequeue_single():
    lifo = Lifo()
    assert lifo.enqueue(1) is True
    assert lifo.enqueue(2) is True
    assert lifo.enqueue(3) is True

    assert lifo.dequeue() == 3
    assert lifo.is_empty() is False
    assert lifo._queue == [1, 2]

    assert lifo.dequeue() == 2
    assert lifo.is_empty() is False
    assert lifo._queue == [1]

    assert lifo.dequeue() == 1
    assert lifo.is_empty() is True
    assert lifo._queue == []

    assert lifo.dequeue() is None
    assert lifo.is_empty() is True
    assert lifo._queue == []


def test_dequeue_multiple():
    lifo = Lifo()
    items_to_add = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in items_to_add:
        assert lifo.enqueue(item) is True

    assert lifo.length() == 10
    assert lifo._queue == items_to_add

    assert lifo.dequeue(5) == [10, 9, 8, 7, 6]
    assert lifo.length() == 5
    assert lifo._queue == [1, 2, 3, 4, 5]

    assert lifo.dequeue(3) == [5, 4, 3]
    assert lifo.length() == 2
    assert lifo._queue == [1, 2]

    assert lifo.dequeue(5) == [2, 1]
    assert lifo.length() == 0
    assert lifo.is_empty() is True
    assert lifo._queue == []
