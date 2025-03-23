def calculate_ticket_price(age, seat_type):
    int 
    if age < 3:
        return "invalid"
    elif age < 12:
        base_price = 50000
    elif age <= 120:
        base_price = 100000
    else:
        return "invalid"

    if seat_type == "vip":
        base_price += 30000

    return base_price
