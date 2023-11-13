from design_common.queues.fifo.fifo import Fifo


def test_fifo():
    fifo = Fifo()
    assert fifo.x == 10
