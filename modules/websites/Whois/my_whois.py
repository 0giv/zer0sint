import whois #tool
import json
import re





def main_whois(domain):
    try:
        whois_result_json = str(whois.whois(domain))
        data = json.loads(whois_result_json)
        cleaned_json = re.sub(r'[\"\'\,\[\]\{\}]', '', json.dumps(data, indent=2))

        print( cleaned_json)

    except:
        return "No valid JSON Data found."
