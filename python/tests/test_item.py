from src.gilded_rose import Item


def test_create_item():
    item = Item("Aged Brie", 0, 0)
    assert repr(item) == "Aged Brie, 0, 0"
