import pytest

from design_common.queues.priority import Priority


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
