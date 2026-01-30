#Cal Avg
def avg (a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)

avg(12,10,10)


#Factorail Num
def fact (n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
        print(fact)

fact(5)