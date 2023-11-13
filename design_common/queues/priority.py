from design_common.queues.queue_base import Queue


class Priority(Queue):
    def __init__(self, max_queue_size: int = None) -> None:
        super().__init__(max_queue_size)

    def _add_to_queue(self, item):
        """Responsible for adding an item to the queue depending on priority."""
        pass

    def _remove_from_queue(self, multiple):
        """Responsible for retrieving an item from a location depending on priority."""
        pass
