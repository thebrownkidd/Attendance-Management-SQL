import Mark
while True:
    print("Welocme to AMS, please select one of the following outputs: ")
    print("\nSno\t| Action\n0. \t| EXIT\n1. \t| View your attendance\n2. \t| Mark Attendance\n")
    action = int(input("\n Enter the S.no of your action: "))
    if action == 0:
        break
    elif action == 1:
        continue
    elif action == 2:
        user = Mark.validate_user()
        if user[0]:
            Mark.present(user[1])
    else:
        print("Enter valid option!!")

print("Thankyou for using!!")