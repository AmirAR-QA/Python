a = input("Please enter the number you'd like to multiply: ")
a = int(a)

b = input("Please enter the limit of the multiplication table you'd like to see: ")
b = int(b)

for i in range(1,b+1):
    print(a, 'x', i, '=', a*i)