age = int(input("What is your age?  >> "))

if age < 18:
    print("You are a minor.")
elif age < 19:
    print("You are a teenager.")
else:
    print("You are an adult.")


score = 91

if score >= 80:
    print("B")
elif score>=90:
    print("A")
elif score >= 70:
    print("C")
else:
    print("F")