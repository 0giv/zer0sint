import requests
import json
from time import sleep
import re

def nslookup(domain):

    try:
        url = "https://networkcalc.com/api/dns/lookup/"
        complete_url = url + domain
        request = requests.get(complete_url)
        
        data = json.loads(request.text)
        cleaned_json = re.sub(r'[\"\'\,\[\]\{\}]', '', json.dumps(data, indent=2))

        return cleaned_json

    except json.JSONDecodeError:
        return "No valid JSON Data found."

