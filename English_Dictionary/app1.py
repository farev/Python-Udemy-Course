import json
from difflib import get_close_matches

data = json.load(open("data.json"))
#data = json.load(open("dictionary.json"))

def definition(Word):
    Word = Word.lower()
    if Word in data:
        return data[Word]
    elif Word.title() in data:
        return data[Word.title()]
    elif Word.upper() in data:
        return data[Word.upper()]
    elif len(get_close_matches(Word, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y is yes, or N if no: " % get_close_matches(Word, data.keys())[0])
        if yn == "Y" or "y":
            return data[get_close_matches(Word, data.keys())[0]]
        elif yn == "N" or "n":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand that"
    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter word: ")

output = definition(word)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)