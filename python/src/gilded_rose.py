# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GildedRose(object):

    def __init__(self, items) -> None:
        self.items = items

    def increase_quality(self, item: Item, value: int) -> None:
        item.quality += value

    def decrease_quality(self, item: Item, value: int) -> None:
        item.quality -= value

    def update_sellin(self, item: Item) -> None:
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

    def is_expired(self, item: Item) -> bool:
        return item.sell_in < 0

    def is_sulfuras(self, item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"

    def is_backstage_passes(self, item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_aged_brie(self, item: Item) -> bool:
        return item.name == "Aged Brie"

    def update_quality(self) -> None:
        for item in self.items:
            if self.is_sulfuras(item):
                continue

            self.update_sellin(item)

            if self.is_backstage_passes(item):
                if self.is_expired(item):
                    item.quality = 0
                elif item.sell_in <= 5:
                    self.increase_quality(item, 3)
                elif item.sell_in <= 10:
                    self.increase_quality(item, 2)
                else:
                    self.increase_quality(item, 1)

            elif self.is_aged_brie(item):
                self.increase_quality(item, 1)   
                if self.is_expired(item):
                    self.increase_quality(item, 1)
                        
            else:                
                self.decrease_quality(item, 1)

                if self.is_expired(item):
                    self.decrease_quality(item, 1)
            
            item.quality = min(50, item.quality)
            item.quality = max(0, item.quality)
