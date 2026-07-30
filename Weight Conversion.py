# Weight Conversion
#lbs to kgs and kgs to lbs

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(K / P): ")

if unit == "K":
    weight = weight * 2.205
    print(f"Your weight in Pounds is {round(weight,1)} lbs")
elif unit == "P":
    weight = weight / 2.205
    print(f"Your weight in Pounds is {round(weight,1)} Kgs")
else:
    print("Select Correctly!")