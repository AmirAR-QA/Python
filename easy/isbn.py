ISBN = input("Please enter the ISBN You'd like to process: ")
if len(ISBN) != 12:
    print("Your ISBN isn't exactly 12 digits, please enter a valid ISBN - No dashes please!")
else:
    D0 = int(ISBN[0])
    D1 = int(ISBN[1])*3
    D2 = int(ISBN[2])
    D3 = int(ISBN[3])*3
    D4 = int(ISBN[4])
    D5 = int(ISBN[5])*3
    D6 = int(ISBN[6])
    D7 = int(ISBN[7])*3
    D8 = int(ISBN[8])
    D9 = int(ISBN[9])*3
    D10 = int(ISBN[10])
    D11 = int(ISBN[11])*3
    sum = (D0+D1+D2+D3+D4+D5+D6+D7+D8+D9+D10+D11)
    rem = sum % 10
    key = 10 - rem
    print (ISBN,key)
    