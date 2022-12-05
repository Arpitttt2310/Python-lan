# Python Program to Calculate Cube of a Number
 
def cube(num):
    return num * num * num
 
num = int(input("Enter an any number : "))
 
cb = cube(num)
 
print("Cube of {0} is {1}".format(num, cb))
