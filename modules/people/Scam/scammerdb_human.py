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

    data_list = []

    for row in rows:
        if "Report Count" in row.get_text():
            if "0" in row.get_text():
                return False
            elif "0" not in row.get_text():
                datedata = soup.find_all('th')
                for row in datedata:
                    if "Date" in row.get_text() and "ScamType" in row.get_text():
                        Date = soup.find('td', class_="wi10")
                        span_element = Date.find('span', class_='wis10')
                        date_value = span_element.get_text(strip=True)
                        data = input_data,date_value,ScamTypeValue
                        clean_data = data
                        return clean_data
                    elif "Scam Type" in row.get_text() and not "Date" in row.get_text():
                        ScamType = soup.find('td', class_="desc_td")
                        date_value = "N/A"
                        span_element = ScamType.find('span', class_="desc_tab")
                        ScamTypeValue = span_element.get_text(strip=True)
                        data = input_data,date_value,ScamTypeValue
                        clean_data = data
                        return clean_data

