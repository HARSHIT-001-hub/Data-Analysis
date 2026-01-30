while True:
    name = input("Enter Name: ")
    total = 0
    while True:
        quantity = int(input("Enter a Quantity: "))
        amount = int(input("Enter Amonut of Item: "))
        total = amount*quantity
        repeat = input("Another Item Yes/No: ")
        if repeat == "no" or repeat == "No":
            break
    
    print("-"*40)
    print("Name: ",name)
    print("TOtal Bill: ",total)
    print("-"*40)
    repeat1 = input("Do YOu Want to add Next Customer: ")
    if repeat1 == "no" or repeat1 == "No":
        break
