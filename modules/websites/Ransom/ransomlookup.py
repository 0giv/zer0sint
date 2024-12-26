import json
import os

with open("ressources/leaks.json", "r") as file:
    json_data = file.read()


data = json.loads(json_data)

def ransomlookup(user_input):
    os.system("cls || clear")

    result = next((item for item in data if item["name"] == user_input), None)
    if result:
        return f"{user_input} is reported as a ransom website be sure to not visit it"
    else:
        return f"No info about {user_input}"

