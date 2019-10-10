# Goal

# Create a Mad Libs style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user inputted. The story doesn't have to be too long, but it should have some sort of story line.

# Tip - It's easiest to write out a quick story on a piece of paper or a word document, and then go back through and see which words the user should be able to change.

# Subgoals

#     If the user has to put in a name, change the first letter to a capital letter. - DONE

#     Change the word "a" to "an" when the next word in the sentence begins with a vowel.


#Story adapted slightly from http://www.teach-nology.com/worksheets/language_arts/madlibs/ml3.pdf
vowels='aeiouy'
story="""
My name is {0}, and I love to go to the arcade.
When I go to the arcade with my {1} there are lots of games to play. 
I spend lots of time there with my friends. 
In "Xmen" you can be different {2}. 
The point of the game is {3} every robot. 
You also need to save people, and then you can go to the next level. 
In "Star Wars" you are Luke Skywalker and you try to destroy every {4} . 
In a car racing / motorcycle racing game you need to beat every computerized vehicle that you are {5} against. 
There are a whole lot of other cool games. When you play some games you win {6} for certain scores. 
Once you're done you can cash in your tickets to get a big {7} . You can save your {8} for another time. 
When I went to this arcade I didn't believe how much fun it would be. 
You might annoy your parents by asking them over and over if you can go back to there. 
So far I have had a lot of fun every time I've been to this great arcade!
"""
types_needed=['name','plural noun','plural noun','verb','noun','"ing" verb','plural noun','noun','plural noun',]

user_entries=[]

for type_needed in types_needed:
    entry=input(f'Type a{"n" if type_needed[0] in vowels else ""} {type_needed}: ').strip()
    if 'name' in type_needed or 'proper' in type_needed:
        entry=entry.title()
    user_entries.append(entry)

print(story.format(*user_entries))