import json
from difflib import SequenceMatcher
from difflib import get_close_matches

dictionary = json.load(open("data.json"))



def translate(w):
    if dictionary.get(w) != None:
        print(dictionary.get(w))
    elif len(closest_match) < 1:
        return "That word does not exist."
    else:
        confirmation = input("Did you mean " + closest_match[0] + " instead? Type yes or no.")
        if confirmation == "yes":
            return dictionary.get(closest_match[0])
        elif  confirmation == "no":
            return "Alright, you can try again."
        else:
            return "We didn't understand your entry!"
        
        
user_word = (input('Type your word:')).lower()
closest_match = get_close_matches(user_word,dictionary.keys(), cutoff=0.8)
output = translate(user_word)

if type(output) == list:
    for item in output:
         print(item)
else:
    print(output)
