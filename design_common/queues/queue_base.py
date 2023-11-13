from copy import deepcopy
from typing import Any


class Queue:
    def __init__(self, boundary: int = None, replace_at_boundary: bool = False, take_partial: bool = False) -> None:
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
        return self._boundary

    @property
    def queue(self):
        return deepcopy((self._queue))

    @property
    def free_space(self) -> int:
        return self._boundary - self.__len__()

    @property
    def boundary_enabled(self) -> bool:
        return self._boundary is not None

    @property
    def replace_enabled(self) -> bool:
        return self._replace

    @property
    def partial_enabled(self) -> bool:
        return self._takes_partial

    @classmethod
    def enqueue(self, *args) -> None:
        raise NotImplementedError

    @classmethod
    def dequeue(self) -> None:
        raise NotImplementedError

    def clear(self) -> None:
        self._queue = []

    def _at_boundary(self) -> bool:
        return self.__len__() == self._boundary

    def _surpasses_boundary(self, *args) -> bool:
        return self.__len__() + len(args) > self._boundary

    def __first__(self) -> Any | None:
        return self._queue[0] if self.__len__() != 0 else None

    def __last__(self) -> Any | None:
        return self._queue[-1] if self.__len__() != 0 else None

    def __len__(self) -> int:
        return len(self._queue)
