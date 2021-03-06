from src.gilded_rose import GildedRose
from src.item import Item
from src.item_types import ItemTypes
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


@pytest.mark.parametrize(
    "input, expected", [([], 0), ([Item(name="FAKE", sell_in=0, quality=1)], 1)]
)
def test_create_giled_rose(input, expected):
    gildedrose = GildedRose(input)
    assert len(gildedrose.items) == expected


@pytest.mark.parametrize(
    "item_name, quality, expected_quality",
    [
        (ItemTypes.AGED_BRIE.value, 50, 50),
        (ItemTypes.SULFURAS.value, 80, 80),
        (ItemTypes.BACKSTAGE_PASSES.value, 50, 0),
    ],
)
def test_update_quality_maximum_value(item_name, quality, expected_quality):
    gildedrose = GildedRose([Item(name=item_name, sell_in=0, quality=quality)])

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == expected_quality


def test_update_quality_aged_brie():
    initial_quality = 10
    gildedrose = GildedRose(
        [Item(name=ItemTypes.AGED_BRIE.value, sell_in=2, quality=initial_quality)]
    )
    gildedrose.update_quality()

    item = gildedrose.items[0]
    assert item.quality == initial_quality + 1

    gildedrose.update_quality()

    item = gildedrose.items[0]
    assert item.quality == initial_quality + 2


def test_update_quality_expired_aged_brie():
    initial_quality = 10
    gildedrose = GildedRose(
        [Item(name=ItemTypes.AGED_BRIE.value, sell_in=0, quality=initial_quality)]
    )

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == initial_quality + 2

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == initial_quality + 4


def test_update_quality_sulfuras():
    initial_quality = 10
    gildedrose = GildedRose(
        [Item(name=ItemTypes.SULFURAS.value, sell_in=1, quality=initial_quality)]
    )

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == initial_quality

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == initial_quality


def test_update_quality_backstage_passes_11_days_or_more():
    gildedrose = GildedRose(
        [Item(name=ItemTypes.BACKSTAGE_PASSES.value, sell_in=13, quality=10)]
    )

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 11

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 12


def test_update_quality_backstage_passes_10_days_left():
    gildedrose = GildedRose(
        [Item(name=ItemTypes.BACKSTAGE_PASSES.value, sell_in=10, quality=10)]
    )

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 12

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 14


def test_update_quality_backstage_passes_5_days_left():
    gildedrose = GildedRose(
        [Item(name=ItemTypes.BACKSTAGE_PASSES.value, sell_in=5, quality=10)]
    )

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 13

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 16


def test_update_quality_backstage_passes_0_days_left():
    gildedrose = GildedRose(
        [Item(name=ItemTypes.BACKSTAGE_PASSES.value, sell_in=1, quality=10)]
    )

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 13

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 0


def test_update_quality_magically_conjured():
    gildedrose = GildedRose(
        [Item(name=ItemTypes.MAGICALLY_CONJURED.value, sell_in=5, quality=10)]
    )

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 8

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 6


def test_update_quality_expired_magically_conjured():
    gildedrose = GildedRose(
        [Item(name=ItemTypes.MAGICALLY_CONJURED.value, sell_in=0, quality=10)]
    )

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 6

    gildedrose.update_quality()
    item = gildedrose.items[0]
    assert item.quality == 2
