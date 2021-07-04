from src.gilded_rose import GildedRose, Item
import pytest

def test_negative_quality():
    gildedrose = GildedRose([Item(name="Other", sell_in=0, quality=0)])

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 0

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 0

def test_update_quality_decrease():
    gildedrose = GildedRose([Item(name="Other", sell_in=1, quality=10)])

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 9

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 7

@pytest.mark.parametrize("input, expected", [([], 0), ([Item(name="FAKE", sell_in=0, quality=1)], 1)])
def test_create_giled_rose(input, expected):
    gildedrose = GildedRose(input)
    assert len(gildedrose.items) == expected

@pytest.mark.parametrize("item_name, quality, expected_quality", [("Aged Brie", 50, 50), ("Sulfuras, Hand of Ragnaros", 80, 80), ("Backstage passes to a TAFKAL80ETC concert", 50, 0)])
def test_update_quality_maximum_value(item_name, quality, expected_quality):
    gildedrose = GildedRose([Item(name=item_name, sell_in=0, quality=quality)])

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == expected_quality


def test_update_quality_aged_brie():
    initial_quality = 10
    gildedrose = GildedRose([Item(name="Aged Brie", sell_in=2, quality=initial_quality)])
    gildedrose.update_quality()

    item = gildedrose.items[0]
    assert item.quality == initial_quality + 1

    gildedrose.update_quality()

    item = gildedrose.items[0]
    assert item.quality == initial_quality + 2

def test_update_quality_expired_aged_brie():
    initial_quality = 10
    gildedrose = GildedRose([Item(name="Aged Brie", sell_in=0, quality=initial_quality)])
    
    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == initial_quality + 2

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == initial_quality + 4

def test_update_quality_sulfuras():
    initial_quality = 10
    gildedrose = GildedRose([Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=initial_quality)])
    
    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == initial_quality

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == initial_quality
