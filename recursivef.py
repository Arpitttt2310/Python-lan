# Recursive function to find factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
 
 
if __name__ == '__main__':
 
    n = 5
    print(f'The Factorial of {n} is {factorial(n)}')
 
