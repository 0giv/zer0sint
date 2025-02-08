import os
import csv
from datetime import datetime
import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


response = []

# List of popular social media platforms and services
PLATFORMS = [
    "facebook",
    "twitter",
    "instagram",
    "snapchat",
    "tiktok",
    "youtube",
    "discord",
    "guilded",
    "pinterest",
    "tumblr",
    "reddit",
    "whatsapp",
    "kik",
    "wechat",
    "viber",
    "quora",
    "tinder",
    "grindr",
    "hinge",
    "bumble",
    "okcupid",
    "zoosk",
    "replit",
    "github",
]

LOG_FILE = "username_checker_log.csv"


def check_username(username):
    results = {}

    for platform in PLATFORMS:
        platform_result = {"platform": platform, "available": False}

        # Implement the code to check username availability on each platform
        available = check_availability(platform, username)
        platform_result["available"] = available

        results[platform] = platform_result

    print (results)


def check_availability(platform, username):
    # Implement username availability using web scraping
    # This is a simplified example and may require updates if website structures change
    url = f"https://www.{platform}.com/{username}/"
    try:
        response = requests.get(url, verify=False, timeout=2)
        return response.status_code == 404
    except requests.exceptions.Timeout:
        print(f"Timeout")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e} ")


def display_results(results):
    print("\nResults:")
    for platform, result in results.items():
        status = "Available" if result["available"] else "Taken"
        response.append([platform, result["available"], status])
    print (response)


def main(username):
    try:
        username_to_check = username
        results = check_username(username_to_check)
        display_results(results)
    except Exception as e:
        print(f"An error occurred: {e}")

