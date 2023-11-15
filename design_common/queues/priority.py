from dataclasses import dataclass
from typing import Any

from design_common.queues.queue_base import Queue
from design_common.queues.priority_item import Item
from utilities.sorting.merge_sort import MergeSort


class Priority(Queue):
    def __init__(self, max_queue_size: int = None, sort: bool = False):
        super().__init__(max_queue_size)
        self._queue: list[Item] = []
        self.merge_sort = MergeSort()
        self._sorted = False
        self._sort = sort

    @property
    def sort(self) -> bool:
        """Get if the queue should be sorted on enqueue."""
        return self._sort

    @sort.setter
    def sort(self, value: bool) -> None:
        """Set if the queue should be sorted on enqueue."""
        self._sort = value

    def _find_highest_priority(self) -> Item:
        """
        Find the item with the highest priority in the queue and remove it.

        Returns:
            Item: The item with the highest priority.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self._sorted:
            highest_priority_index = 0
            priority_value = self._queue[0].priority
            item: Item
            for i, item in enumerate(self._queue):
                if item.priority > priority_value:
                    highest_priority_index = i
                    priority_value = item.priority

            return self._queue.pop(highest_priority_index)
        else:
            return self._queue.pop()

    def _add_to_queue(self, item: Item):
        """Responsible for adding an item to the queue depending on priority."""
        self._queue.append(item)
        self._queue = self.merge_sort.merge_sort(self._queue) if self._sort else self._queue
        self._sorted = True if self._sort else False

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
