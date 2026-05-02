def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

fact = int(input("enter the number : "))

output = factorial(fact)
print(f"Factorial of {fact} is {output}")