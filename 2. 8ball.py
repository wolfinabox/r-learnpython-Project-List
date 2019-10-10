# Goal

# I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it gives an answer by way of a floating die with responses written on it. You can create one in python. You must:

#     Allow the user to enter their question
#     Display an in progress message( i.e. "thinking")
#     Create 20 responses, and show a random response
#     Allow the user to ask another question or quit

# Bonus Using whatever module you like, add a gui. Your gui must have:

#     A box for users to enter the question
#     At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)
from random import choice
from time import sleep

positive_responses=["It is certain","Without a doubt","You may rely on it","Yes definitely","It is decidedly so","As I see it, yes","Most likely","Yes","Outlook good","Signs point to yes"]
neutral_responses=["Reply hazy try again","Better not tell you now","Ask again later","Cannot predict now","Concentrate and ask again"]
negative_responses=["Don’t count on it","Outlook not so good","My sources say no","Very doubtful","My reply is no"]
all_responses=positive_responses+neutral_responses+negative_responses
user_input=''
while True:
    user_input=input('What do you wish to ask the magic 8-ball? (type "quit" to quit): ')
    if user_input.lower().strip()=='quit':
        break
    response=choice(all_responses)
    print('Thinking...')
    sleep(1)
    print(response)
