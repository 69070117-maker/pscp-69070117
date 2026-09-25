"""3293"""
def main():
    """3293"""
    lines = [input() for _ in range(5)]
    max_len = max(len(line) for line in lines)
    fream_w = max_len + 4
    print("*" * fream_w)
    print("*" + " " + (lines[0]).ljust(max_len) + " "+ "*")
    print("*" + " " + (lines[1]).ljust(max_len) + " "+ "*")
    print("*" + " " + (lines[2]).ljust(max_len) + " "+ "*")
    print("*" + " " + (lines[3]).ljust(max_len) + " "+ "*")
    print("*" + " " + (lines[4]).ljust(max_len) + " "+ "*")
    print("*" * fream_w)

main()
