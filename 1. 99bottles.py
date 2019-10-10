# GOAL

# Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

# RULES

#     If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.

#     Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.

#     Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

#     Put a blank line between each verse of the song.





for i in range(10,0,-1):
    print(f'{i} bottle{"s" if i>1 else ""} of beer on the wall, {i} bottle{"s" if i>1 else ""} of beer,')
    print('Take one down, pass it around')
    print(f'{i-1} bottle{"s" if i-1>1 else ""} of beer on the wall' if i-1>0 else 'No more bottles of beer on the wall')
    print()