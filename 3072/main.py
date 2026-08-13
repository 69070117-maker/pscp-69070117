"""AEIOU"""
def main():
    """3072"""
    text = input()
    count_a = [0,0,0,0,0]
    aeiou = ['a','e','i','o','u']
    for i in text.lower():
        if i == "a":
            count_a[0] += 1
        elif i == "e":
            count_a[1] += 1
        elif i == "i":
            count_a[2] += 1
        elif i == "o":
            count_a[3] += 1
        elif i == "u":
            count_a[4] += 1
    for i in range(5):
        if count_a[i] > 0:
            print(aeiou[i],":",count_a[i])
main()
