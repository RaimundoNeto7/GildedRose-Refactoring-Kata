from src.item import Item
from src.item_types import ItemTypes


class GildedRose(object):
    def __init__(self, items) -> None:
        self.items = items

    def increase_quality(self, item: Item, value: int) -> None:
        item.quality += value

    def decrease_quality(self, item: Item, value: int) -> None:
        item.quality -= value

    def update_sellin(self, item: Item) -> None:
        if item.name != ItemTypes.SULFURAS.value:
            item.sell_in -= 1

    def is_expired(self, item: Item) -> bool:
        return item.sell_in < 0

    def is_sulfuras(self, item: Item) -> bool:
        return item.name == ItemTypes.SULFURAS.value

    def is_backstage_passes(self, item: Item) -> bool:
        return item.name == ItemTypes.BACKSTAGE_PASSES.value

    def is_aged_brie(self, item: Item) -> bool:
        return item.name == ItemTypes.AGED_BRIE.value

    def is_magically_conjured(self, item: Item) -> bool:
        return item.name == ItemTypes.MAGICALLY_CONJURED.value

    def update_backstage_passes_quality(self, item: Item) -> None:
        if self.is_expired(item):
            item.quality = 0
            return

        if item.sell_in <= 5:
            self.increase_quality(item, 3)
            return

        if item.sell_in <= 10:
            self.increase_quality(item, 2)
            return

        self.increase_quality(item, 1)

    def update_aged_brie_quality(self, item: Item) -> None:
        self.increase_quality(item, 1)
        if self.is_expired(item):
            self.increase_quality(item, 1)

    def update_magically_conjured_quality(self, item: Item) -> None:
        self.decrease_quality(item, 2)
        if self.is_expired(item):
            self.decrease_quality(item, 2)

    def update_general_item_quality(self, item: Item) -> None:
        self.decrease_quality(item, 1)
        if self.is_expired(item):
            self.decrease_quality(item, 1)

    def set_maximum_item_quality(self, item: Item) -> None:
        item.quality = min(50, item.quality)

    def set_minimum_item_quality(self, item: Item) -> None:
        item.quality = max(0, item.quality)

    def update_quality(self) -> None:
        for item in self.items:
            if self.is_sulfuras(item):
                continue

            self.update_sellin(item)

            if self.is_backstage_passes(item):
                self.update_backstage_passes_quality(item)

            elif self.is_aged_brie(item):
                self.update_aged_brie_quality(item)

            elif self.is_magically_conjured(item):
                self.update_magically_conjured_quality(item)

            else:
                self.update_general_item_quality(item)

            self.set_maximum_item_quality(item)
            self.set_minimum_item_quality(item)
