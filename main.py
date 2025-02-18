# factorial

def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)


num = int(input("Enter Number For Factorial :"))

if num<0:
    print("Sorry, Factorial doesn't exist for negative numbers.")
elif num==0:
    print("The Factorial of 0 Is 1")
else:
    print("The Factorial of",num,"is",factorial(num))