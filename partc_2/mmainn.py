"""Football Score Calculator"""
def main():
    """Calculate match statistics and total score."""
    n = int(input().strip())

    win_count = 0
    draw_count = 0
    lose_count = 0

    for _ in range(n):
        result = input().strip()
        if result == "WIN":
            win_count += 1
        elif result == "DRAW":
            draw_count += 1
        elif result == "LOSE":
            lose_count += 1

    total_score = (win_count * 3) + (draw_count * 1)

    print(f"{win_count} {draw_count} {lose_count}")
    print(total_score)


main()
