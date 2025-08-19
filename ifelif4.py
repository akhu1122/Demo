age = int(input("enter your age: "))

if age < 13:
    print("child")
elif 13 <= age <= 19:
    print("teenager")
elif 20 <= age <= 59:
    print("adult")
else:
    print("senior citizen")
