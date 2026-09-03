"""3156"""
def main():
    """3156"""
    text = input()
    num = int(input())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in text:
        if i in alphabet:
            idx = alphabet.index(i)
            newidx = (idx + num) % 26
            result += alphabet[newidx]
        else:
            result += i
    print(result)
main()
