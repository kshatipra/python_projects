# Write code here
import requests, json


def get_fact(number):
    if number > 7:
        print("Maximum number of facts per execution is 7")
    elif number < 0:
        print("Minimum number of facts per execution is 1")

    
    while number != 0:
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
        number = number - 1
        content = response.text
        data = json.loads(content)
        fact = data['text']
        print(fact)

user_input = input("Enter a number")
num = int(user_input)
facts = get_fact(num)
