"""
Ttile: Shape Program
Author: Jon Burstein
Details: This is a python program to determine the volume of a few different shapes.
It teaches functions.
"""

PI = 3.4159

def rectangle_volume(length, width, height):
    return round(length * width * height,1)

def cir_cylinder_volume(PI,radius, height):
    square = radius ** 2
    vol = (PI * square) * height
    return round(vol,1)

def sphere_volume(PI, radius):
    threefour = 1.33
    cube = radius ** 3
    vol = threefour * PI * cube
    return round(vol,1)

def torus_volume(PI, R, r):
    pi_square = PI ** 2
    r_square = r ** 2
    vol = (2 * pi_square) * (R * r_square)
    return round(vol,1)

def rectangle_display(length, width, height):
    print(f"The rectangle with length = {length}, width = {width} "
         f"and height = {height}, will have a volume {rectangle_volume(length, width, height)} inches")

def cc_display(PI, radius, height):
    print(f"The right circular cylinder with height = {height} and radius = {radius}"
          f",will have a volume = {cir_cylinder_volume(PI,radius,height)} inches")

def sphere_display(PI, radius):
    print(f"The sphere with a radius = {radius}"
          f",will have a volume {sphere_volume(PI, radius)} cubic inches")

def torus_display(PI, R, r):
    print(f"The torus with radius r = {r} and radius R = {R} "
          f",will have a volume = {torus_volume(PI,R,r)} cubic inches")   
choice = 'y'
while choice == 'y' or choice =='yes':
    rectangle_length = input("Please enter the rectangle length: ")
    rectangle_length = float(rectangle_length)
    rectangle_width = input("Please enter the rectangle width: ")
    rectangle_width = float(rectangle_width)
    height = input("Please enter the rectangle and right circular cylinder height: ")
    height = float(height)
    radius = input("Please enter the radius right circular cylinder, sphere and torus r: ")
    radius = float(radius)
    torus_R = input("Please enter the radius torus R: ")
    torus_R = float(torus_R)
    print("---------------------------------------------------------------")
    rectangle_display(rectangle_length, rectangle_width, height)
    cc_display(PI, radius, height)
    sphere_display(PI, radius)
    torus_display(PI, torus_R, radius)

    choice = input("Enter Y or yes to repeat or any other character to quit: ")
    choice = choice.lower()
print("------------------------")    
print("Goodbye!!!")
print("------------------------")