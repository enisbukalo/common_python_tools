from design_common.queues.queue_base import Queue


class Fifo(Queue):
    def __init__(self) -> None:
        super().__init__()
