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

    def _find_highest_priority(self) -> Item:
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
