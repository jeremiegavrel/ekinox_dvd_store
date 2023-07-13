import pytest
import discount

TEST_CASES = [
    (
        [
            "Back to the Future 1",
            "Back to the Future 2",
            "Back to the Future 3",
        ], 36
    ),
    (
        [
            "Back to the Future 1",
            "Back to the Future 3",
        ], 27
    ),
    (
        [
            "Back to the Future 1",
        ], 15
    ),
    (
        [
            "Back to the Future 1",
            "Back to the Future 2",
            "Back to the Future 3",
            "Back to the Future 2",
        ], 48
    ),
    (
        [
            "Back to the Future 1",
            "Back to the Future 2",
            "Back to the Future 3",
            "La chèvre",
        ], 56
    ),
    (
        [
            "La chèvre",
            "Ghostbusters",
            "La Guerre des Étoiles",
        ], 60
    )
]

@pytest.mark.parametrize('dvd_list,expected_total', TEST_CASES)
def test_discount_bttf(dvd_list, expected_total):
    total = discount.compute_price_with_bttf_discount(dvd_list)
    assert total == expected_total
