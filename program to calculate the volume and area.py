# program to calculate the volume and area of ​​several shapes and spaces

phi = 3.14
x = input(" What shapes or spaces do you want to calculate ? \n == ")

if x == "circle" :
    r = int(input("what is the radius of the circle in meters ? \n == "))
    x = phi * r**2
    print("The area of the circle is ", x , "m squared")
elif x == "triangle" :
    base = int(input("what is the base of the triangle in meters ? \n == "))
    tall = int(input("what is the tall of the triangle in meters ? \n == "))
    x = 1/2 * base * tall
    print("The area of the triangle is ", x , "m squared")
elif x == "square" :
    side = int(input("what is the side of the square in meters ? \n == "))
    x = side * side
    print("The area of the square is ", x , "m squared")
elif x == "rectangular" :
    length = int(input("what is the length of the rectangular in meters ? \n == "))
    width = int(input("what is the width of the rectangular in meters ? \n == "))
    x = width * length
    print("The area of the triangle is ", x , "m squared")

 """ Update everyday """

