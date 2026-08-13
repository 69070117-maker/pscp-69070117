"""3129"""
def main():
    """maincoffeeee"""
    amount = int(input())
    sales = []
    for _ in range(amount):
        sales.append(float(input()))
    total = sum(sales)
    average = total / amount
    maxxie = max(sales)
    minnie = min(sales)
    print(int(total))
    print(int(maxxie))
    print(int(minnie))
    print(f"{average:.1f}")
main()
