# importing random module
from random import randint
# importing copy module
import copy

# Creating a Mad Lib and adding placeholders for the randomly selected words
madlib = (
        "Last month, I went to Disney World with {}. We traveled for {} hour(s) " +
        "by {}. Finally, we arrived and it was very {}. There were {} " +
        "people {} everywhere. There were also people dressed up in {} " +
        "costumes. I wish it had been more {}, but we {} anyway. We also " +
        "went on a(n) {} ride called the Magic {}. {} nearly fell off the ride and " +
        "had to be {}. Later, we went to the hotel and {}. Next year, I " +
        "want to go to {}, where we can {}."
)

# Creating my own dictionary of words that I will use in the Mad Lib
my_dict = {
    'friends name': ['John', 'Katy', 'Emily', 'Susan', 'Anthony', 'Chris', 'Andrea', 'Tom'],
    'number hours': ['2', '10', '10000', '20', '5', '4', '60', '12'],
    'vehicle': ['minivan', 'clown car', 'school bus', 'convertible', 'pickup truck', 'motorcycle', 'Lamborghini',
                'limo'],
    'adjective': ['friendly', 'colorful', 'gigantic', 'hot', 'cold', 'fancy', 'little', 'shiny'],
    '-ing verb': ['dancing', 'singing', 'cartwheeling', 'jumping', 'fighting', 'smoking', 'sitting', 'playing'],
    'animal': ['cow', 'rabbit', 'mouse', 'alligator', 'cat', 'horse', 'giraffe', 'tiger'],
    'past tense verb': ['studied', 'watched', 'danced', 'sang', 'danced', 'ran', 'jogged', 'sat'],
    'noun': ['art', 'camera', 'baby', 'bread', 'eye', 'coffee', 'carpet', 'garden'],
    'place': ['Paris', 'Tokyo', 'arcade', 'Colorado', 'the jungle', 'Miami', 'Canada', 'Mexico'],
    'verb': ['dance', 'sing', 'jump', 'hula-hoop', 'swim', 'skydive', 'hike', 'explore']
}


# Creating a function that will randomly select a word from the dictionary by the category of word
def select_word(category, new_dictionary):
    """ Getting a random word from dictionary based on word category """
    word = new_dictionary[category]
    count = len(word) - 1
    index = randint(0, count)
    return new_dictionary[category].pop(index)


# Creating a function that will grab a random word of the right category into the Mad Lib
def random_madlib():
    """ Creating a random madlib from my_dict """
    new_dictionary = copy.deepcopy(
        my_dict)  # deep copy allows me to make changes to new_dictionary without making changes to my_dict
    return madlib.format(
        select_word('friends name', new_dictionary),
        select_word('number hours', new_dictionary),
        select_word('vehicle', new_dictionary),
        select_word('adjective', new_dictionary),
        select_word('adjective', new_dictionary),
        select_word('-ing verb', new_dictionary),
        select_word('animal', new_dictionary),
        select_word('adjective', new_dictionary),
        select_word('past tense verb', new_dictionary),
        select_word('adjective', new_dictionary),
        select_word('noun', new_dictionary),
        select_word('friends name', new_dictionary),
        select_word('past tense verb', new_dictionary),
        select_word('past tense verb', new_dictionary),
        select_word('place', new_dictionary),
        select_word('verb', new_dictionary),
    )


# Creating a few random Mad libs
madlib1 = random_madlib()
madlib2 = random_madlib()

# Printing the results
print("\n")
print(madlib1)
print("\n")
print(madlib2)
