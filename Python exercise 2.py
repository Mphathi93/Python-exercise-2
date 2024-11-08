# Question 1: Arithmetic and Assignment Operators
x=5
y=1
# TODO: Add 3 to x using the += operator
x +=3
# TODO: Multiply y by 2 using the *= operator
y *=2
# TODO: Divide x by y and store the result in a variable called 'result'
result = int(x/y)
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a = 6 
b = 4  
c = 1
# TODO: Create a condition that checks if a is greater than b
a > b
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b % 2 ==0
# TODO: Create a condition that checks if c is less than or equal to a
c <= a
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = a > b and b%2==0 or c<=a
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
print("Please put in your test score")
score = int(input('Score: '))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if 90<score<100:
    print("A")
elif 80<score<89:
    print("B")
elif 70<score<79:
    print("C")
elif 60<score<69:
    print("D")
else: 
    print("F")
# TODO: Print the grade for the given score

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
print("Can you put in two numbers")
num1 = int(input("number1: "))
num2 = int(input("number2: "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
print("Can you put in one of the operations(*,+,-,/)")
Operation = input("operation: ")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2

if Operation == '+':
    result = num1 + num2
    print(result)
elif Operation == '-':
    result = num1 - num2
    print(result)
elif Operation == '*':
    result = num1 * num2
    print(result)
elif Operation == '/':
    result = num1 / num2
    print(result)
else:
    print("Error: Cannot divide by zero")
# TODO: Handle the case of division by zero

# TODO: Print the result of the operation
