import requests
import json


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote


quote = get_quote()

user_input = input("Do you want a quote? Yes or no: ").casefold()
print()

while user_input != "no":
    if user_input == "no":
        break
    elif user_input == "yes":
        print(quote)
        print()
        user_input = input("Do you want another quote? Yes or no: ").casefold()
        print()

print("Okay cool comeback for more quotes next time. Bye!!!")
