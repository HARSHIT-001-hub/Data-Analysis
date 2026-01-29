#if-elif-else
marks = 90

if 35 < marks <= 60:
    print("Third")
elif 60 < marks <= 90:
    print("Second")
elif marks > 90:
    print("First")
else:
    print("Fail")

#Short hand if-else
total_marks = 40
print("Passed") if total_marks > 35 else print("Fail")