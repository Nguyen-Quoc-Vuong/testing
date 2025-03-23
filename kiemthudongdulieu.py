import pytest
from ticket_price import calculate_ticket_price

#Kiểm thử dòng dữ liệu
@pytest.mark.parametrize("age, seat_type, expected", [
    (2, "regular", "invalid"),
    (121, "regular", "invalid"),
    (121, "regular", "invalid"),
    (8, "regular", 50000),
    (8, "regular", 50000),
    (50, "regular", 100000),
    (8, "regular", 50000),
    
])

def test_calculate_ticket_price_additional(age, seat_type, expected):
    assert calculate_ticket_price(age, seat_type) == expected