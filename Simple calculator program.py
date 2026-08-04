#simple calculator program

operator = input("Select your operator(+ - * /): ")

num1 = float(input("Enter your number: "))
num2 = float(input("Enter your number: "))

sum = num1+num2
difference = num1-num2
product = num1*num2
divide = num1/num2
modulus = num1%num2

if operator == "+":
    print(f"Your sum is {sum}")
elif operator == "-":
    print(f"Your result is {difference}")
elif operator == "*":
    print(f"The product is {product}")
elif operator == "/":
    print(f"The division is {divide}")
    print(f"The remainder is{modulus}")
else:
    print('Select correct operator!')
