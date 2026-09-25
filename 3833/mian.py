"""3833"""
def main():
    """main"""
    A = int(input())
    B = int(input())
    set_a = {int(input().strip()) for _ in range(A)}
    set_b = {int(input().strip()) for _ in range(B)}
    diff_set = set_a - set_b
    sorted_result = sorted(diff_set)
    for element in sorted_result:
        print(element, end=" ")
main()
