"""คืนนี้เป็นคืนวันคริสต์มาส"""


def get_light_sequence(start_color, count):
    """คำนวณและคืนค่ารายการลำดับสีของหลอดไฟแบบชื่อเต็ม"""
    color_names = ["Red", "Green", "Blue"]
    color_keys = ["R", "G", "B"]
    start_index = color_keys.index(start_color)

    result = []
    for i in range(count):
        current_color = color_names[(start_index + i) % 3]
        result.append(current_color)

    return result


def main():
    """main"""
    user_input = input().split()
    start_color = user_input[0]
    count = int(user_input[1])

    sequence = get_light_sequence(start_color, count)
    print(" ".join(sequence))


main()
