import pytest
from ticket_price import calculate_ticket_price  # Thay 'your_module' bằng tên file chứa hàm

#Kiểm thử dòng điều khiển
@pytest.mark.parametrize("age, seat_type, expected", [
    (2, "vip", "invalid"),
    (11, "regular", 50000),
    (30, "vip", 130000),
    (121, "vip", "invalid"),
])
 
def test_calculate_ticket_price(age, seat_type, expected):
    assert calculate_ticket_price(age, seat_type) == expected

#Kiểm thử dòng dữ liệu
@pytest.mark.parametrize("age, seat_type, expected", [
    (2, "regular", 100000),
    (121, "regular", 80000),
    (8, "regular", 100000),
    (8, "regular", 130000),
    (50, "regular", 100000),
    (8, "regular", 80000),
    (8, "regular", 100000),
    (8, "vip", 130000),
])

def test_calculate_ticket_price_additional(age, seat_type, expected):
    assert calculate_ticket_price(age, seat_type) == expected
