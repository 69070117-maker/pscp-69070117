"""Surprising" หรือ "Not surprising"""
def main():
    """3024"""
    total = float(input())
    max_val = float(input())
    minest = max(0, (total - max_val) - max_val)
    if total <= 30:
        if max_val - 2 > minest:
            print("Surprising")
        else:
            print("Not surprising")
main()
