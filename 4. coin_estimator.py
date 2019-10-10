# Goal Create a program that allows the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters), and then print out how many of each type of wrapper they would need, how many coins they have, and the estimated total value of all of their money.

# Weight of each coin and how many fit inside each type of wrapper

# .

# Subgoals

#     Round all numbers printed out to the nearest whole number. - DONE

#     Allow the user to select whether they want to submit the weight in either grams or pounds.
from math import ceil

coin_weights={'penny':2.5,'nickle':5.0,'dime':2.268,'quarter':5.67}
wrapper_capacities={'penny':50,'nickle':40,'dime':50,'quarter':40}
coin_values={'penny':0.01,'nickle':0.05,'dime':0.1,'quarter':0.25}

user_coin_weights={'penny':0,'nickle':0,'dime':0,'quarter':0}
user_coin_amounts={'penny':0,'nickle':0,'dime':0,'quarter':0}

#Ask user
for coin in user_coin_weights.keys():
    user_coin_weights[coin]=float(input(f'How much do your {coin}s weigh?: '))

print()
#Calculate # of coins from weight
for coin,weight in user_coin_weights.items():
    user_coin_amounts[coin]=ceil(weight/coin_weights[coin])

for coin,capacity in wrapper_capacities.items():
    if user_coin_amounts[coin]==0:continue
    print(f'You have {user_coin_amounts[coin]} {coin}(s) and need {ceil(float(user_coin_amounts[coin])/capacity)} wrapper(s)')

print(f'You have {sum(amt for coin,amt in user_coin_amounts.items())} total coins')
print(f'They are worth ${round(sum(coin_values[coin]*amt for coin,amt in user_coin_amounts.items()),2)} in total')