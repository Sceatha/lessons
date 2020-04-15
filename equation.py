import math

# The program asks for the coeficients of the equation
a=input("What is the value of a?")
b=input("What is the value of b?")
c=input("What is the value of c?")

# Calculate the determinant
D=b**2  - (4*a*c)

if D < 0:
    print("There is no solution")

elif D == 0:
    print("There is 1 double solution")
    x = -b/(2*a)
    print(x)

else:
    print("There are 2 solutions") 
    x1 = (-b +math.sqrt(D))/(2*a)
    x2 = (-b -math.sqrt(D))/(2*a) 
    print("The solutions are:")
    print(x1)
    print(x2)


