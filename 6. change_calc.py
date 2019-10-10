# BASIC GOAL Imagine that your friend is a cashier, but has a hard time counting back change to customers. Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.

# For example, if he inputs 1.47, the program will tell that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.

# SUBGOALS

#     So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him and the price of the item. The program should then tell him the amount of each coin he needs like usual.

#     To make the program even easier to use, loop the program back to the top so your friend can continue to use the program without having to close and open it every time he needs to count change. - DONE
from math import ceil
coin_values={'quarter':0.25,'dime':0.1,'nickle':0.05,'penny':0.01}

while True:
    change_needed=ceil(float(input('How much change is needed?: '))*100)
    for coin,val in coin_values.items():
        amt,change_needed=divmod(change_needed,coin_values[coin]*100)
        if amt==0:continue
        print(f'You need {int(amt)} {coin}s')