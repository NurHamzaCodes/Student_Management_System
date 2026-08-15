import work
def opening():
    print("\nChoose what do you want:\n\n  1. Search student\n  2. Add student\n  3. Remove student\n  4. Update student\n  5. Show all\n")
    n = int(input("Your Chose: "))
    return n

def system():

    op = "y"
    while op == "y":
        n = opening()

        if n <= 0 or n > 5:
            print("\nInvaild chose!! 1,2,3,4 and 5 is the only acceptable chose.")
            continue

        else:
            work.works(n)

        op = input("\nAre you want to continue (y/n): ")

if __name__ == "__main__":

    print()
    print(35*"=")
    print("||   STUDENT MANAGEMENT SYSTEM   ||")
    print(35*"=")

    system()

    print("\n||   Thank you, hope this is useful.   ||\n")