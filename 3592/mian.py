"""Align"""
def main():
    """Align"""
    size = int(input())
    align = input()
    text = input()
    pad = size - len(text)

    if align == "left":
        result = text + (" " * pad)
    elif align == "right":
        result = (" " * pad) + text
    else:
        left_pad = (pad + 1) // 2
        right_pad = pad // 2
        result = (" " * left_pad) + text + (" " * right_pad)

    print(result)


main()
