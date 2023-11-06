from class_common import Singleton

class SingletonTestClass(Singleton):
    def __init__(self) -> None:
        super().__init__()

class BaseTestClass:
    def __init__(self) -> None:
        pass

def test_singleton():
    obj1 = SingletonTestClass()
    obj2 = SingletonTestClass()
    assert obj1 is obj2

    obj1_memory_location = hex(id(obj1))
    obj2_memory_location = hex(id(obj2))
    assert obj1_memory_location == obj2_memory_location

def test_base():
    obj1 = BaseTestClass()
    obj2 = BaseTestClass()
    assert obj1 is not obj2

    obj1_memory_location = hex(id(obj1))
    obj2_memory_location = hex(id(obj2))
    assert obj1_memory_location != obj2_memory_location