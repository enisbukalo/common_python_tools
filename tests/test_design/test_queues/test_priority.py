import pytest

from design_common.queues.priority import Priority, Item


def test_priority_properties():
    with pytest.raises(TypeError):
        Priority(max_queue_size="hello")

    priority = Priority(max_queue_size=300)

    assert priority.max_size == 300
    assert priority.has_max_size() is True

    priority = Priority()

    assert priority.is_full() is False
    assert priority.is_empty() is True
    assert priority.free_space() == None
    assert priority.peek() is None
    assert priority.last() is None
    assert priority.length() is 0


def test_enqueue_without_max():
    priority = Priority()

    item_lowest = Item(item=0, priority=-1)
    item_zero = Item(item=0, priority=0)
    item_one = Item(item=1, priority=1)
    item_two = Item(item=2, priority=2)
    item_three = Item(item=3, priority=3)

    items = [item_lowest, item_three, item_one, item_zero, item_two]
    for item in items:
        priority.enqueue(item)

    assert priority.length() == 5
    assert priority.is_full() is False
    assert priority._queue == items


def test_enqueue_with_max():
    priority = Priority(max_queue_size=5)

    item_lowest = Item(item=0, priority=-1)
    item_zero = Item(item=0, priority=0)
    item_one = Item(item=1, priority=1)
    item_two = Item(item=2, priority=2)
    item_three = Item(item=3, priority=3)
    item_four = Item(item=4, priority=4)

    assert priority.free_space() == 5

    items = [item_lowest, item_four, item_three, item_one, item_zero, item_two]
    for item in items:
        priority.enqueue(item)

    assert priority.length() == 5
    assert priority.is_full() is True
    assert priority._queue == items[:5]
    assert priority.free_space() == 0


def test_dequeue_single():
    priority = Priority()

    item_lowest = Item(item=0, priority=-1)
    item_zero = Item(item=0, priority=0)
    item_one = Item(item=1, priority=1)
    item_two = Item(item=2, priority=2)
    item_three = Item(item=3, priority=3)

    items = [item_lowest, item_three, item_one, item_zero, item_two]
    for item in items:
        priority.enqueue(item)

    assert priority.length() == 5
    assert priority.is_full() is False
    assert priority._queue == items

    assert priority.dequeue() == item_three
    assert priority.length() == 4
    assert priority._queue == [item_lowest, item_one, item_zero, item_two]

    assert priority.dequeue() == item_two
    assert priority.length() == 3
    assert priority._queue == [item_lowest, item_one, item_zero]

    assert priority.dequeue() == item_one
    assert priority.length() == 2
    assert priority._queue == [item_lowest, item_zero]

    assert priority.dequeue() == item_zero
    assert priority.length() == 1
    assert priority._queue == [item_lowest]

    assert priority.dequeue() == item_lowest
    assert priority.length() == 0
    assert priority.is_empty() is True
    assert priority._queue == []


def test_dequeue_multiple():
    priority = Priority()

    item_lowest = Item(item=0, priority=-1)
    item_zero = Item(item=0, priority=0)
    item_one = Item(item=1, priority=1)
    item_two = Item(item=2, priority=2)
    item_three = Item(item=3, priority=3)

    items = [item_lowest, item_three, item_one, item_zero, item_two]
    for item in items:
        priority.enqueue(item)

    assert priority.length() == 5
    assert priority.is_full() is False
    assert priority._queue == items

    assert priority.dequeue(2) == [item_three, item_two]
    assert priority.length() == 3
    assert priority._queue == [item_lowest, item_one, item_zero]

    assert priority.dequeue(1) == item_one
    assert priority.length() == 2
    assert priority._queue == [item_lowest, item_zero]

    assert priority.dequeue(10) == [item_zero, item_lowest]
    assert priority.length() == 0
    assert priority.is_empty() is True
    assert priority._queue == []
