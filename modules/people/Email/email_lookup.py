import requests
import json
import re


def findemail(mail_input):
    user_input = mail_input
    # Public api from https://leak-lookup.com/api
    api_key = "f25559540f0d654d70c08db6156348f5"
    url = "https://leak-lookup.com/api/search"
    params = {
        "key": api_key,
        "type": "email_address",
        "query": user_input
    }
    data_list = []
    response = requests.post(url, data=params)

    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            del data["error"]
        clear_data = re.sub(
            r'[\"\'\,\[\]\{\}]', '', json.dumps(data, indent=2))
        data_list.append({
            "index":1,
            'name': user_input,
            'leaked_site': clear_data
        })
        return data_list
    else:
        return "Error Message:", response.text


