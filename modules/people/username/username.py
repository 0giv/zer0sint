import json
import requests
import urllib3


account_name = input("Enter Username\n> ")


with open("ressources/wmn-data.json", encoding="utf-8") as f:
    data = json.load(f)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
for site in data.get("sites", []):
    link = site.get("uri_check")
    if link: 
        link_with_account = link.replace("{account}", account_name)
        try:
            response = requests.get(link_with_account, verify=False)
            if response.status_code == 200:
                errors = {"Error","404","this user does not exist"}
                for error in errors:
                    if error in response.text:
                        print(f"Username: {link_with_account}  is not available on  {site['name']}")
                    else:
                        print(f"Username: {link_with_account} is available on {site['name']}")
        except requests.exceptions.Timeout:
            print(f"Timeout: {link_with_account} {site['name']}")
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e} {site['name']}")
