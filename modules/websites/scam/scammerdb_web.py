import requests
from bs4 import BeautifulSoup
from os import system
from time import sleep



def scammerdb(input_data):
    url = f"https://scamsearch.io/search_report?searchoption=all&search={input_data}"
    response = requests.get(url)
    response.text

    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all('tr')

    for row in rows:
        if "Report Count" in row.get_text():
            if "0" in row.get_text():
                return "No report found."
            elif "0" not in row.get_text():
                datedata = soup.find_all('th')
                for row in datedata:
                    if "DATE" in row.get_text() and "ScamType" in row.get_text():
                        Date = soup.find('td', class_="wi10")
                        span_element = Date.find('span', class_='wis10')
                        date_value = span_element.get_text(strip=True)
                        return f"'{input_data}' has already been reported. \nReport date: {date_value} \nScam Description: {ScamTypeValue}\n"
                    elif "Scam Type" in row.get_text() and not "DATE" in row.get_text():
                        ScamType = soup.find('td', class_="desc_td")
                        span_element = ScamType.find('span', class_="desc_tab")
                        ScamTypeValue = span_element.get_text(strip=True)
                        return f"'{input_data}' has already been reported.\nReport date: N/A Scam Description: {ScamTypeValue}\n"
                        

