"""3156"""
def main():
    """3156"""
    text = input()
    num = int(input())
    char = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for text in char:
        idx = text.index(char)
        newidx = (idx + num) % 26
        result += char[newidx]
    print(result)
main()
