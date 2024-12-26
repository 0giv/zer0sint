from os import system #setup libraries
import whois #tool
import json
import re





def main_whois(domain):
    whois_result_json = str(whois.whois(domain))
    
    try:
        data = json.loads(whois_result_json)
        cleaned_json = re.sub(r'[\"\'\,\[\]\{\}]', '', json.dumps(data, indent=2))

        return cleaned_json

    except json.JSONDecodeError:
        return "No valid JSON Data found."
