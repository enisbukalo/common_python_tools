from typing import Any, Iterable

from design_common.queues.queue_base import Queue


class Fifo(Queue):
    def __init__(self, boundary: int = None, replace_at_boundary: bool = False, take_partial: bool = False) -> None:
        super().__init__(boundary, replace_at_boundary, take_partial)

    def enqueue(self, *args) -> None:
        # Do we even have a boundary?
        if self.boundary_enabled:
            at_boundary = self._at_boundary()
            surpasses_boundary = self._surpasses_boundary(*args)

            # Are we at the boundary?
            if at_boundary:
                # Are we replacing old items with the new items?
                if self.replace_enabled:
                    amount_to_remove = len(args)
                    for _ in range(amount_to_remove):
                        self.dequeue()
                    self._queue.extend(args)
                    return
                else:
                    return

            # Will we be at the boundary if we add these items?
            if surpasses_boundary:
                # Are we replacing old items with the new items?
                if self.replace_enabled:
                    amount_to_remove = len(args) - (self._boundary - self.__len__())
                    for _ in range(amount_to_remove):
                        self.dequeue()
                    self._queue.extend(args)
                    return
                else:
                    # Since we are not replacing old items, do we want to take partial new items?
                    if self.partial_enabled:
                        partial_amount = len(args) - self.free_space
                        self._queue.extend(args[:-partial_amount])
                        return
                    else:
                        return

            self._queue.extend(args)
        else:
            self._queue.extend(args)

    def dequeue(self) -> None:
        self._queue.pop(0) if self.__len__() != 0 else None
