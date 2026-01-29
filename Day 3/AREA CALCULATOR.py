print("*******AREA CALCULATOR*********")
print("Press 1 for Area of Square" \
"\nPress 2 for Area of Triangle" \
"\nPress 3 for Area of Rectangle")

choice = int(input("Enter Number Between 1 to 3: "))

if choice == 1:
    side = float(input("Enter the Side of Square: "))
    area = side*side
    print("Area of Square is: ",area)
elif choice == 2:
    base = float(input("Enter the base of triangle: "))
    height = float(input("Enter the Height of Triangle"))
    area_tri = 0.5*base*height
    print("Area of Tringle is: ",area_tri)
elif choice == 3:
    length = float(input("Enter the Length of Rectangle: "))
    width = float(input("Enter the width of Rectangle: "))
    area_rec = length*width
    print("Area of Rectangle is: ",area_rec)
else:
    print("Choice Correct Option")