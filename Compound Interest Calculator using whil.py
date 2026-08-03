#Compound Interest Calculator using while loop

principle = 0
rate = 0
time = 0

while principle<=0:
    principle = float(input("Enter your invested amount: "))
    if principle<=0:
        print("Principle cannot be less than or equal to o")

while rate<=0:
    rate = float(input("Enter your Rate of Interest: "))
    if rate<=0:
        print("Rate of interest cannot be less than or equal to o") 

while time<=0:
    time = int(input("Enter your time in years: "))
    if time<=0:
        print("Time cannot be less than or equal to o")

interest = principle * pow((1 + rate/100), time)
print(f"The interest value is {round(interest,2)}")

final_amount = principle + interest
print(f"Total amount is {round(final_amount,2)}")
