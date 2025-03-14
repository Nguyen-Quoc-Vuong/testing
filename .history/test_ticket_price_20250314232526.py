import pytest
from test_ticket_price import calculate_ticket_price  # Thay 'your_module' bằng tên file chứa hàm

@pytest.mark.parametrize("age, seat_type, expected", [
    (2, "vip", "invalid"),
    (11, "regular", 50000),
    (30, "vip", 130000),
    (121, "vip", "invalid"),
])
def test_calculate_ticket_price(age, seat_type, expected):
    assert calculate_ticket_price(age, seat_type) == expected
