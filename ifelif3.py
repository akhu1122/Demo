marks = int(input("enter your marks: "))

if 90 <= marks <= 100:
    print("grade: A")
elif 75 <= marks <= 89:
    print("grade: B")
elif 50 <= marks <= 74:
    print("grade: C")
elif 35 <= marks <=49:
    print("grade: D")
else:
    print("fail")
