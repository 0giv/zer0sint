import requests

def hudsonrock(username: str):
    try:
        """Fetch the 'stealers' details from the API response for a given username."""
        url = "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-username"
        params = {"username": username}
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for HTTP status codes 4xx/5xx
            data = response.json()
            
            # Extract 'stealers' details
            stealers = data.get("stealers", [])
            if not stealers:
                return "No stealer data found."
            
            details = []
            for stealer in stealers:
                ip = stealer.get("ip", "N/A")
                computer_name = stealer.get("computer_name", "N/A")
                operating_system = stealer.get("operating_system", "N/A")
                malware_path = stealer.get("malware_path", "N/A")
                
                # Format the information
                details.append(
                    f"IP: {ip}\n"
                    f"Computer Name: {computer_name}\n"
                    f"Operating System: {operating_system}\n"
                    f"Malware Path: {malware_path}\n"
                    f"{'-'*40}"
                )
            
            return "\n".join(details)
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
