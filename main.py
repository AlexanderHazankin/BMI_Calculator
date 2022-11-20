height = input("Please, enter your height in m: ")
weight = input("Please, enter your weight in kg: ")

result = (int(int(weight) / (float(height)**2)))

if result < 16.0:
    print("You are underweight (Severe thinness)")
elif 16.0 < result > 16.9:
    print("You are underweight (Moderate thinness)")
elif 17.0 < result > 18.4:
    print("You are underweight (Mild thinness)")
elif 18.5 < result > 24.9:
    print("You are in normal range")
elif 25.0 < result > 29.9:
    print("You are overweight (Pre-obese)")
elif 30.0 < result > 34.9:
    print("You are obese (Class I)")
elif 35.0 < result > 39.9:
    print("You are obese (Class II)")
elif result > 40.0:
    print("You are obese (Class III)")
else:
    print("ValueError")
