from typing import Any


class Queue:
    def __init__(self, max_queue_size: int = None) -> None:
        """
        Base Queue class for other specialized queue types to use.

        Parameters:
            max_queue_size (int): The max size of the queue. Default is None.
        """
        if not isinstance(max_queue_size, int) and not isinstance(max_queue_size, type(None)):
            raise TypeError("'max_queue_size' must be an integer")

        self._max_queue_size = max_queue_size
        self._queue = []

    @property
    def max_size(self) -> int | None:
        """
        Return the value of the max size property.

        Returns:
            int | None: The value of the max size property if one exists otherwise None.
        """
        return self._max_queue_size

    def free_space(self) -> int | None:
        """
        Calculates the amount of free space available in the queue assuming a max size was set.

        Returns:
            int | None: The amount of free space available, or None if the max size is not enabled.
        """
        return self._max_queue_size - self.length() if self.has_max_size() else None

    def is_full(self) -> bool:
        """
        Check if the current queue is at the max size limit.

        Returns:
            bool: True if the length of the queue is equal to the max size value set, else False.
        """
        return self.length() == self._max_queue_size if self.has_max_size() else False

    def is_empty(self) -> bool:
        """
        Returns if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return True if self.length() == 0 else False

    def has_max_size(self) -> bool:
        """
        Returns if the queue has a max size.

        Returns:
            bool: True if queue has a max size, False otherwise.
        """
        return self._max_queue_size is not None

    def peek(self) -> Any | None:
        """
        Return the highest priority element in the queue.
        (FIFO) = First Element
        (LIFO) = Last Element
        (Priority) = Highest Priority

        Returns:
            Any | None: The highest priority element in the queue, or None if the queue is empty.
        """
        return self._queue[0] if not self.is_empty() else None

    def last(self) -> Any | None:
        """
        Get the last element in the queue.

        Returns:
            Any | None: The last element in the queue, or None if the queue is empty.
        """
        return self._queue[-1] if not self.is_empty() else None

    def length(self) -> int:
        """
        Return the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self._queue)

    @classmethod
    def _add_to_queue(self, item: Any) -> None:
        """
        Adds an item to the queue.

        Parameters:
            item (Any): The item to be added to the queue.

        Raises:
            NotImplementedError: This function is not implemented and should be overridden by subclasses.
        """
        raise NotImplementedError

    @classmethod
    def _remove_from_queue(self, multiple: int | None = None) -> Any | None:
        """
        Retrieve an item from the queue.

        Parameters:
            multiple (int | None): The number of items to remove from the queue. Defaults to None.

        Returns:
            Any | None: The removed item from the queue, or None if the queue is empty.

        Raises:
            NotImplementedError: This method is not implemented.
        """
        raise NotImplementedError

    def clear(self) -> None:
        """Clears the queue."""
        self._queue.clear()

    def enqueue(self, item: Any) -> bool:
        """
        Adds an item to the queue.

        Parameters:
            item (Any): The item to be added to the queue.

        Returns:
            bool: True if the item was added successfully to the queue, False if the queue is full and the item couldn't be added.
        """
        # Do we even have a max size of the queue?
        if self.has_max_size():
            # Are we at the end of the queue?
            if not self.is_full():
                self._add_to_queue(item)
                return True
            else:
                return False
        else:
            self._add_to_queue(item)
            return True

    def dequeue(self, multiple: int | None = None) -> Any | None:
        """
        Retrieve one or many items from the queue.

        Parameters:
            multiple (int | None): The number of items to remove from the queue.

        Returns:
            Any | None: Return one or many items from queue if queue is not empty, else return None.
        """
        return self._remove_from_queue(multiple) if not self.is_empty() else None
