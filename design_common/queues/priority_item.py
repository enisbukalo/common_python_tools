from typing import Any
from dataclasses import dataclass

from utilities.decorators import ensure_instance


@dataclass
class ItemBase:
    item: Any
    priority: int


class Item(ItemBase):
    @ensure_instance(ItemBase)
    def __lt__(self, other: Any):
        return self.priority < other.priority

    @ensure_instance(ItemBase)
    def __le__(self, other: Any):
        return self.priority <= other.priority

    @ensure_instance(ItemBase)
    def __gt__(self, other: Any):
        return self.priority > other.priority

    @ensure_instance(ItemBase)
    def __ge__(self, other: Any):
        return self.priority >= other.priority

    @ensure_instance(ItemBase)
    def __eq__(self, other: Any):
        return self.priority == other.priority
