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
    def max_size(self) -> int:
        """
        Return the value of the max size property.

        Returns:
            int: The value of the max size property.
        """
        return self._max_queue_size

    @property
    def free_space(self) -> int | None:
        """
        Calculates the amount of free space available in the queue assuming a max size was set.

        Returns:
            int | None: The amount of free space available, or None if the max size is not enabled.
        """
        return self._max_queue_size - self.length if self.has_max_size else None

    @property
    def is_empty(self) -> bool:
        """
        Returns if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return True if self.length == 0 else False

    @property
    def has_max_size(self) -> bool:
        """
        Returns if the queue has a max size.

        Returns:
            bool: True if queue has a max size, False otherwise.
        """
        return self._max_queue_size is not None

    @property
    def first(self) -> Any | None:
        """
        Return the first element in the queue.

        Returns:
            Any | None: The first element in the queue, or None if the queue is empty.
        """
        return self._queue[0] if not self.is_empty else None

    @property
    def last(self) -> Any | None:
        """
        Get the last element in the queue.

        Returns:
            Any | None: The last element in the queue, or None if the queue is empty.
        """
        return self._queue[-1] if not self.is_empty else None

    @property
    def length(self) -> int:
        """
        Return the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self._queue)

    @classmethod
    def enqueue(self, *args) -> None:
        """
        Adds the given arguments to the existing queue.

        Parameters:
            *args (Any): The items to add to the queue.

        Raises:
            NotImplementedError: This method is meant to be overridden by child classes.
        """
        raise NotImplementedError

    @classmethod
    def dequeue(self, multiple: int | None = None) -> Any | None:
        """
        Removed an item from the queue.

        Parameters:
            multiple (int | None): The number of items to remove from the queue.

        Returns:
            Any | None: Return item from queue if queue is not empty, else return None.

        Raises:
            NotImplementedError: This method is meant to be overridden by child classes.
        """
        raise NotImplementedError

    def clear(self) -> None:
        """Clears the queue."""
        self._queue = []

    def _at_limit(self) -> bool:
        """
        Check if the current queue is at the max size limit.

        Returns:
            bool: True if the length of the queue is equal to the max size value set, else False.
        """
        return self.length == self._max_queue_size if self.has_max_size else False

    def _surpasses_max_size(self, *args) -> bool:
        """
        Check if the length of the queue plus the length of the arguments surpasses the max size.

        Parameters:
            *args: *args: The items to add to the queue.

        Returns:
            bool: True if the length of the queue + length of args surpasses the maz size, False otherwise.
        """
        return self.length + len(args) > self._max_queue_size if self.has_max_size else False
