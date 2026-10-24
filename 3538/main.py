"""[LEARNING LOGS] Pair Dance"""


def main():
    """Find unpaired characters in initial order of appearance."""
    text = input().strip()

    # นับจำนวนตัวอักษรโดยรักษาลำดับการพบครั้งแรกไว้
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1

    # กรองเอาเฉพาะตัวอักษรที่จำนวนเป็นเลขคี่ (ไม่มีคู่)
    unpaired = [char for char, count in counts.items() if count % 2]

    # แสดงผลลัพธ์
    if unpaired:
        print("".join(unpaired))
    else:
        print("fully paired")


main()
