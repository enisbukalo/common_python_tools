from class_common import Singleton

class TestClass(Singleton):
    def __init__(self) -> None:
        super().__init__()

def test_singleton():
    obj1 = TestClass()
    obj2 = TestClass()
    assert obj1 is obj2

    obj1_memory_location = hex(id(obj1))
    obj2_memory_location = hex(id(obj2))
    assert obj1_memory_location == obj2_memory_location