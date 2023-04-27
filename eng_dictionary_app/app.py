import json
import difflib

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        # Get a list of all dictionary words
        dictionary_words = list(data.keys())

        # Find the most similar word in the dictionary
        closest_word = difflib.get_close_matches(word, dictionary_words, n = 1, cutoff = 0.8)

        # If no close match is found, return an error message
        if not closest_word:
            return 'The word doesn\'t exist. Please double check it.'

        # Ask the user if they meant the closest match
        confirmation = input(f"Did you mean {closest_word[0]}? (Y/N)").lower()

        # If the user confirms the suggested word, return its definition
        if confirmation == 'y':
            return data[closest_word[0]]
        else:
            return 'The word doesn\'t exists. Please double check it.'

word = input('Enter word: ')

print(translate(word))