from design_common.queues.queue_base import Queue


class Fifo(Queue):
    def __init__(self, max_queue_size: int = None) -> None:
        """
        Initializes a First In First Out queue (FIFO).

        Args:
            boundary (int, optional): The boundary value. Defaults to None.

        Returns:
            None
        """
        super().__init__(max_queue_size)

    def enqueue(self, *args, replace: bool = False, add_partial: bool = False):
        # Do we even have a max size of the queue?
        if self.has_max_size:
            # Are we at the end of the queue?
            if self._at_limit():
                # Are we replacing old items with the new items?
                if replace:
                    amount_to_remove = len(args)
                    for _ in range(amount_to_remove):
                        self.dequeue()
                    self._queue.extend(args)
                    return
                else:
                    return

            # Will we be at the end of the queue if we add these items?
            if self._surpasses_max_size(*args):
                # Are we replacing old items with the new items?
                if replace:
                    amount_to_remove = len(args) - (self._max_queue_size - self.length)
                    for _ in range(amount_to_remove):
                        self.dequeue()
                    self._queue.extend(args)
                    return
                else:
                    # Since we are not replacing old items, do we want to take partial new items?
                    if add_partial:
                        partial_amount = len(args) - self.free_space
                        self._queue.extend(args[:-partial_amount])
                        return
                    else:
                        return

            self._queue.extend(args)
        else:
            self._queue.extend(args)

    def dequeue(self, multiple=None):
        if multiple is not None:
            to_return = []
            for _ in range(multiple):
                try:
                    to_return.append(self._queue.pop(0))
                except IndexError:
                    pass
            return to_return
        else:
            return self._queue.pop(0) if not self.is_empty else None
