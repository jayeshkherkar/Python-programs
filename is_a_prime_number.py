a = int(input("Enter the number = "))
i=2
while (i<a):
    if (a % i == 0):
        break
    i = i+1
if (i==a):
    print("The number is prime")
else:
    print("The given number is not prime")



