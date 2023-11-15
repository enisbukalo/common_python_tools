from design_common.queues.queue_base import Queue


class Fifo(Queue):
    def __init__(self, max_queue_size: int = None):
        """
        Initializes a First In First Out queue (FIFO).

        Args:
            max_queue_size (int, optional): The max size of the queue. Defaults to None.

        Returns:
            None
        """
        super().__init__(max_queue_size)

    def _add_to_queue(self, item):
        """Responsible for adding an item to the back of the queue."""
        self._queue.append(item)

    def _remove_from_queue(self, multiple):
        """Responsible for retrieving an item from the front of the queue."""
        if multiple is not None:
            to_return = []
            for _ in range(multiple):
                if self.is_empty():
                    break
                to_return.append(self._queue.pop(0))
            return to_return
        else:
            return self._queue.pop(0)
