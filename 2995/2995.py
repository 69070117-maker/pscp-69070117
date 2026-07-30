"""2995len"""
def main():
    """main"""
    student_id = str(input())
    check = len(student_id)
    if check == 8 :
        if student_id[2] == "1" and student_id[3] == "6" :
            print("yes")
        else :
            print("no")
main()
