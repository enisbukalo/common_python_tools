from copy import deepcopy
from typing import Any


class Queue:
    def __init__(self, boundary: int = None, replace_at_boundary: bool = False, take_partial: bool = False) -> None:
        """
        Base Queue class for other specialized queue types to use.

        Parameters:
            boundary (int): The boundary value of the queue. Default is None.
            replace_at_boundary (bool): Whether to replace at the boundary. Default is False.
            take_partial (bool): Whether to take partial new items. Default is False.

        Returns:
            None
        """
        if not isinstance(boundary, int) and not isinstance(boundary, type(None)):
            raise TypeError("'boundary' must be an integer")
        if not isinstance(replace_at_boundary, bool):
            raise TypeError("'replace_at_boundary' must be a boolean")
        if not isinstance(take_partial, bool):
            raise TypeError("'take_partial' must be a boolean")

        self._boundary = boundary
        self._replace = replace_at_boundary
        self._takes_partial = take_partial
        self._queue = []

    @property
    def boundary(self) -> int:
        """
        Return the value of the boundary property.

        Returns:
            int: The value of the boundary property.
        """
        return self._boundary

    @property
    def queue(self):
        """
        Return a deep copy of the `_queue` attribute.

        Returns:
            object: A deep copy of the `_queue` attribute.
        """
        return deepcopy((self._queue))

    @property
    def free_space(self) -> int | None:
        """
        Calculates the amount of free space available in the queue assuming a boundary was set.

        Returns:
            int | None: The amount of free space available, or None if the boundary is not enabled.
        """
        return self._boundary - self.__len__() if self.boundary_enabled else None

    @property
    def is_empty(self) -> bool:
        """
        Returns if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return True if self.__len__() == 0 else False

    @property
    def boundary_enabled(self) -> bool:
        """
        Returns if the boundary is enabled.

        Returns:
            bool: True if boundary was enabled, False otherwise.
        """
        return self._boundary is not None

    @property
    def replace_enabled(self) -> bool:
        """
        Returns if replacing is enabled.

        Returns:
            bool: True if replacing is enabled, False otherwise.
        """
        return self._replace

    @property
    def partial_enabled(self) -> bool:
        """
        Returns if partial enqueuing is enabled.

        Returns:
            bool: True if partial enqueuing is enabled, False otherwise.
        """
        return self._takes_partial

    @classmethod
    def enqueue(self, *args) -> None:
        """
        Adds the given arguments to the existing queue.

        Parameters:
            *args (Any): The items to add to the queue.

        Returns:
            None

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
        """
        Clears the queue.

        Parameters:
            None

        Returns:
            None
        """
        self._queue = []

    def _at_boundary(self) -> bool:
        """
        Check if the current queue is at the boundary.

        Returns:
            bool: True if the length of the queue is equal to the boundary value set, else False.
        """
        return self.__len__() == self._boundary if self.boundary_enabled else False

    def _surpasses_boundary(self, *args) -> bool:
        """
        Check if the length of the object plus the length of the arguments surpasses the boundary.

        Parameters:
            *args: *args: The items to add to the queue.

        Returns:
            bool: True if the length of the queue + length of args surpasses the boundary, False otherwise.
        """
        return self.__len__() + len(args) > self._boundary if self.boundary_enabled else False

    def __first__(self) -> Any | None:
        """
        Return the first element in the queue.

        Returns:
            Any | None: The first element in the queue, or None if the queue is empty.
        """
        return self._queue[0] if not self.is_empty else None

    def __last__(self) -> Any | None:
        """
        Get the last element in the queue.

        Returns:
            Any | None: The last element in the queue, or None if the queue is empty.
        """
        return self._queue[-1] if not self.is_empty else None

    def __len__(self) -> int:
        """
        Return the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self._queue)
