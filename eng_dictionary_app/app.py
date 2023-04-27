import json

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return 'The word doesn\'t exists. Please double check it .'

word = input('Enter word: ')

print(translate(word))