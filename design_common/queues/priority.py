from dataclasses import dataclass
from typing import Any

from design_common.queues.queue_base import Queue


@dataclass
class Item:
    """Higher the number, higher the priority."""

    item: Any
    priority: int


class Priority(Queue):
    def __init__(self, max_queue_size: int = None):
        super().__init__(max_queue_size)
        self._queue: list[Item] = []

    def _merge(self, left: list[Item], right: list[Item]) -> list[Item]:
        if left is None or len(left) == 0:
            return right
        if right is None or len(right) == 0:
            return left
        result = []

        left_index = right_index = 0

        while len(left) != 0 and len(right) != 0:
            if left[left_index] <= right[right_index]:
                result.append(left.pop())
            else:
                result.append(right.pop())

        while len(left) != 0:
            result.append(left.pop())

        while len(right) != 0:
            result.append(right.pop())

        return result

    def _merge_sort(self, items: list[Item]):
        if len(items) < 2:
            return

        mid_point = len(items) // 2
        L = items[:mid_point]
        R = items[mid_point:]

        return self._merge(self._merge_sort(L), self._merge_sort(R))

    def _find_highest_priority(self) -> Item:
        """
        Find the item with the highest priority in the queue and remove it.

        Returns:
            Item: The item with the highest priority.

        Raises:
            IndexError: If the queue is empty.
        """
        highest_priority_index = 0
        priority_value = self._queue[0].priority
        item: Item
        for i, item in enumerate(self._queue):
            if item.priority > priority_value:
                highest_priority_index = i
                priority_value = item.priority

        return self._queue.pop(highest_priority_index)

    def _add_to_queue(self, item: Item):
        """Responsible for adding an item to the queue depending on priority."""
        self._queue.append(item)

    def _remove_from_queue(self, multiple):
        """Responsible for retrieving one or many items from a location depending on priority."""
        if multiple is not None and multiple != 1:
            to_return = []
            for _ in range(multiple):
                if self.is_empty():
                    break
                to_return.append(self._find_highest_priority())
            return to_return
        else:
            return self._find_highest_priority()
