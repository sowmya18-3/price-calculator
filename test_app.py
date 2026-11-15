from app import calculate_final_price


def test_normal_case():
    # 49.99 x 3 = 149.97, minus 10% = 134.973, plus 8.5% tax = 146.4457
    assert calculate_final_price(49.99, 3, 10, 8.5) == 146.45


def test_no_discount_no_tax():
    assert calculate_final_price(100, 2, 0, 0) == 200.0


def test_discount_only():
    assert calculate_final_price(100, 1, 10, 0) == 90.0


def test_tax_only():
    assert calculate_final_price(100, 1, 0, 10) == 110.0


def test_full_discount_gives_zero():
    assert calculate_final_price(100, 1, 100, 10) == 0.0