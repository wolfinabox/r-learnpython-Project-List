# MAIN GOAL

# Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.

# SUBGOALS

#     If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side. - DONE

#     Loop the program so the user can use it more than once without having to restart the program. - DONE

while True:
    inp=input('Enter 3 sides of a triangle (separated by spaces): ').strip().split()
    inp=sorted(map(lambda i:int(i),inp))
    a,b,c=inp
    if a**2+b**2==c**2:
        print('This is a Pythagorean Triple')
    else:
        print('This is not a Pythagorean Triple')