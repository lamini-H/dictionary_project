# import libraries
import json
from difflib import get_close_matches

#loading json file
data = json.loads(open('data.json').read())

#define a function 
#convert all user input into lowercase to match words in JSON file
# if statements to check if words given exit, suggest possible words, and return an error if word does not exist

def definition(name):
  name = name.lower()
  if name in data:
    return data[name]
  elif len(get_close_matches(name,data.keys())) > 0:
    check = input("Did you mean %s instead? Enter Y if yes, otherwise N to exit: " %
                  get_close_matches(name,data.keys())[0])
    if check == "Y":
      return data[get_close_matches(name, data.keys())[0]]
    elif check == "N":
      return "The word doesn't exist. Please double check it."
    else: 
      return "We didn't understand your entry."
  else:
    return "Sorry, this word is not an English word. Please double check your spelling"

#user input and check it against the set of words passed in the JSON file.
word = input("Enter a name: ")


#the output format
output = definition(word)
if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
