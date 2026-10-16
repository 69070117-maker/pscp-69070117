"""3562"""
def main():
    """count upper, lower, and digits"""
    text = input()

    upper_count = 0
    lower_count = 0
    digit_count = 0

    for char in text:
        if 'A' <= char <= 'Z':
            upper_count += 1
        elif 'a' <= char <= 'z':
            lower_count += 1
        elif '0' <= char <= '9':
            digit_count += 1

    print(f"{upper_count} {lower_count} {digit_count}")

main()
