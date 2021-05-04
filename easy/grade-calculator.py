chemmark = input("Please enter your Chemistry grade")
chemmark = int(chemmark)

mathsmark = input("Please enter your Maths grade")
mathsmark = int(mathsmark)

physicsmark = input("Please enter your Physics grade")
physicsmark = int(physicsmark)

mark = physicsmark + mathsmark + chemmark
percentage = float(mark)/3

if percentage >= 70:
    print("You scored an A, your total mark was", percentage)
elif percentage >= 60:
    print("You scored a B, your total mark was", percentage)
elif percentage >= 50:
    print("You scored a C, your total mark was", percentage)
elif percentage >= 40:
    print("You scored a D, your total mark was", percentage)
elif percentage < 40:
    print("You failed! You didn't score above 40 overall!")