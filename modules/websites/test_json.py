import json

def print_json_keys_values(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print(' ' * indent + f'{key}:')
            print_json_keys_values(value, indent + 2)
    elif isinstance(data, list):
        for item in data:
            print_json_keys_values(item, indent + 2)
    else:
        print(' ' * indent + str(data))

# Example usage:
json_data = '''
{
  "domain_name": "TEST.COM",
  "registrar": "Network Solutions, LLC",
  "whois_server": "whois.networksolutions.com",
  "referral_url": null,
  "updated_date": [
    "2023-04-18 06:47:49",
    "2023-04-18 06:47:56"
  ],
  "creation_date": "1997-06-18 04:00:00",
  "expiration_date": "2025-06-17 04:00:00",
  "name_servers": [
    "NS1.SAFESECUREWEB.COM",
    "NS2.SAFESECUREWEB.COM",
    "NS3.SAFESECUREWEB.COM"
  ],
  "status": "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
  "emails": [
    "domain.operations@web.com",
    "rj9au8e24nq@networksolutionsprivateregistration.com",
    "ju5rq3jg28s@networksolutionsprivateregistration.com"
  ],
  "dnssec": "unsigned",
  "name": "PERFECT PRIVACY, LLC",
  "org": null,
  "address": "5335 Gate Parkway care of Network Solutions PO Box 459",
  "city": "Jacksonville",
  "state": "FL",
  "registrant_postal_code": "32256",
  "country": "US"
}
'''

parsed_data = json.loads(json_data)
print_json_keys_values(parsed_data)
