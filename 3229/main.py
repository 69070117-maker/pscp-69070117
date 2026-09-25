"""ระบบคิดคะแนนเกมออนไลน์"""


def get_rank_code(score):
    """คำนวณรหัสอันดับ"""
    if score >= 1500:
        return 5
    if score >= 1000:
        return 4
    if score >= 500:
        return 3
    if score >= 200:
        return 2
    return 1


def get_special_code(rank, streak, bonus):
    """คำนวณรหัสสถานะพิเศษ"""
    if rank == 5 and streak >= 7:
        return 99
    if rank == 4 and bonus > 300:
        return 88
    return 0


def main():
    """main"""
    base = int(input())
    bonus = int(input())
    streak = int(input())

    total = base + bonus
    if streak > 3:
        total = int(total * 1.5)

    rank = get_rank_code(total)
    special = get_special_code(rank, streak, bonus)

    print(total)
    print(rank)
    print(special)


main()
