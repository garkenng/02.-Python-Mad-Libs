"""
This program generates passages that are generated in mad-lib format
The program will prompt the user for various types of words. Eventually generating a strange and / or funny story
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print('Mad Libs has started!')
name = input('Enter a name: ')
ad1 = input('Enter an adjective: ')
ad2 = input('Enter another adjective: ')
ad3 = input('Enter final adjective: ')
verb = input('Enter a verb: ')
noun1 = input('Enter a noun: ')
noun2 = input('Enter another noun: ')
animal = input('Animal: ')
food = input('Enter a food: ')
fruit = input('Enter a fruit: ')
superhero = input('Enter a superhero: ')
country = input('Enter a country: ')
dessert = input('Enter a dessert: ')
year = input('Enter a year: ')

print (STORY % (name, ad1, ad2, animal, food, verb, noun1, fruit, ad3, name, superhero, name, country, name, dessert, name, year, noun2))