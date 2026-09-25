"""โปรแกรมแปลงชื่อย่อไพ่เป็นชื่อเต็ม"""


def get_rank_name(rank_str):
    """แปลงแต้มไพ่เป็นชื่อเต็ม"""
    ranks = {
        "A": "ace",
        "J": "jack",
        "Q": "queen",
        "K": "king",
    }
    return ranks.get(rank_str, rank_str)


def get_suit_name(suit_str):
    """แปลงสัญลักษณ์ไพ่เป็นชื่อเต็ม"""
    suits = {
        "D": "diamonds",
        "H": "hearts",
        "S": "spades",
        "C": "clubs",
    }
    return suits.get(suit_str, "")


def main():
        
    """main"""
    card_input = input().strip().upper()

    suit_char = card_input[-1]
    rank_str = card_input[:-1]

    rank_name = get_rank_name(rank_str)
    suit_name = get_suit_name(suit_char)

    print(f"{rank_name} of {suit_name}")


main()
