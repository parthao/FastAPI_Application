from typing import List
from app.models.item import Item

# Simulate a database with an in-memory list
_items_db = [
    Item(id=1, name="Item 1", description="The first item"),
    Item(id=2, name="Item 2", description="The second item"),
]

class ItemRepository:
    def get_all(self) -> List[Item]:
        return _items_db

    def get_by_id(self, item_id: int) -> Item | None:
        return next((item for item in _items_db if item.id == item_id), None)
