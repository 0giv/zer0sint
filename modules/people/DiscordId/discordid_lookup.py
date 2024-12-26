import requests
import json
import re

def findthem(id):
    api = f"https://discordlookup.mesalytic.moe/v1/user/{id}"
    response = requests.get(api)

    try:
        response.raise_for_status()
        data = response.json()
        formatted_data = re.sub(
            r'[\"\'\,\[\]\{\}]', '', json.dumps(data, indent=2))
        return(formatted_data)
    except requests.exceptions.HTTPError as errh:
        return "HTTP Error:", errh
    except requests.exceptions.ConnectionError as errc:
        return "Error Connecting:", errc
    except requests.exceptions.Timeout as errt:
        return "Timeout Error:", errt
    except requests.exceptions.RequestException as err:
        return "Something went wrong:", err

