"""3298"""
def main():
    """main"""
    raw_text = input().strip()
    text = raw_text.upper()
    n = len(text)
    u_count = []
    for i in range(n):
        if text[i] == "B":
            count = 0
            j = i + 1
            while j < n and text[j] == "U":
                count += 1
                j += 1
            if count >= 2:
                u_count.append(count)
    if u_count:
        print(f"Yes {max(u_count)}")
    elif "B" in text:
        b_index = text.index("B")
        print(raw_text[: b_index + 1] + ("U" * (n - b_index - 1)))
    else:
        print(("BUU" * (n // 3 + 1))[:n])


main()
    