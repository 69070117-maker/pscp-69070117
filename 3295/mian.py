"""3095"""
def main():
    """main"""
    unit = int(input())

    if unit <= 10:
        base_cost = unit * 5
    elif unit <= 50:
        base_cost = 50 + (unit - 10) * 7
    elif unit <= 100:
        base_cost = 330 + (unit - 50) * 10
    elif unit <= 200:
        base_cost = 830 + (unit - 100) * 12
    else:
        base_cost = 2030 + (unit - 200) * 15

    vat = base_cost * 0.07
    ft_cost = unit * 0.50
    total_spend = base_cost + vat + ft_cost
    print(f"{total_spend + 1e-9:.1f}")
main()
