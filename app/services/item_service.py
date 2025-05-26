from typing import List
from app.models.item import Item
from app.repositories.item_repo import ItemRepository

class ItemService:
    def __init__(self):
        self.repo = ItemRepository()

    def list_items(self) -> List[Item]:
        return self.repo.get_all()

    def get_item(self, item_id: int) -> Item | None:
        return self.repo.get_by_id(item_id)
