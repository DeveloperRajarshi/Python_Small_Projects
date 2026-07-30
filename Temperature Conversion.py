# Temperature Conversion

unit = input("Is this temperature is in Celcius or Farenheight?(C/F): ")
temp = float(input("Enter your temperature: "))

if unit == "C":
    temp = (9*temp)/5 + 32
    print(f"Your unit in Farenheight is {temp}")

elif unit == "F":
    temp = (temp-32)*5 / 9
    print(f"Your temperature in Celcius is {temp}")

else:
    print("Take a valid unit")