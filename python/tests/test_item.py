from src.item_types import ItemTypes
from src.gilded_rose import Item


def test_create_item():
    item = Item(ItemTypes.AGED_BRIE.value, 0, 0)
    assert repr(item) == "Aged Brie, 0, 0"
