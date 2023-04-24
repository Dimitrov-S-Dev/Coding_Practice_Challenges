# Create a script that lets the user submit a pass until 3 conditions are met.
# 1 contains at least one number
# 2 Has one uppercase letter
# 3 It is at least 5 chars long
# Give the exact reason why the password is not correct

while True:
    notes = []
    psw = input("Enter your password: ")

    if not any(i.isdigit() for i in psw):
        notes.append("You need at least on number")

    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")

    if len(psw) < 5:
        notes.append("You need at least 5 characters")

    if notes:
        print("Password is not fine:")
        for note in notes:
            print(note)
    else:
        print("Password is fine")
        break