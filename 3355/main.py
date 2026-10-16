"""[LEARNING LOGS] Shorten"""
nums = []
while True:
    v = int(input())
    if v == -1:
        break
    nums.append(v)

parts = []
if nums:
    start = prev = nums[0]
    for v in nums[1:]:
        if v == prev + 1:
            prev = v
            continue
        parts.append(str(start) if start == prev else f"{start}-{prev}")
        start = prev = v
    parts.append(str(start) if start == prev else f"{start}-{prev}")
    print(", ".join(parts))