"""3352"""
import ast
def main():
    """main"""
    user_input = input()
    lst = ast.literal_eval(user_input)
    for item in lst:
        print(str(item)[-1])
main()
