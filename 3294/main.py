"""School"""
def main():
    """3294"""
    N = int(input())
    A = int(input())
    total_minutes = N * A
    hours = total_minutes // 60
    minutes = total_minutes % 60
    if not total_minutes and not hours:
        print("No teaching")
    elif hours >= 1 and not minutes:
        print(f"{hours} hours")
    elif not hours and minutes >= 1:
        print(f"{minutes} minute")
    else:
        print(f"{hours} hours {minutes} minute")
main()
