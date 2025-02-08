from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from modules.websites.DNS import dnslookup
from modules.websites.ip import iplookup_clean_list
from modules.websites.scam import scammerdb_web
from modules.websites.Whois import my_whois
from modules.people.DiscordId import discordid_lookup
from modules.people.Email import email_lookup
from modules.websites.Ransom import ransomlookup
from modules.creditcardscom import creditcards
from modules.people.username import checker
from modules.people.DiscordId import discordid_lookupBot
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()  # Parse the JSON request
    query = data.get('query', '')  # Get the search query
    tool = data.get('tool', '').lower()  # Get the selected tool

    results = []

    # Route the search to the appropriate tool based on selection
    if tool == 'whois':
        results = my_whois.main_whois(query)
    elif tool == 'dns':
        results = dnslookup.nslookup(query)
    elif tool == 'ip':
        results = iplookup_clean_list.ip_whois(query)
    elif tool == 'scam':
        results = scammerdb_web.scammerdb(query)
    elif tool == 'discord':
        results = discordid_lookup.findthem(query)
    elif tool == 'discordbot':
        results = discordid_lookupBot.findthem(query)
    elif tool == 'email':
        results = email_lookup.findemail(query)
    elif tool == 'username':
        results = checker.main(query)
    elif tool == 'ransom':
        results = ransomlookup.ransomlookup(query)
    elif tool == 'creditcard':
        results = creditcards.main(query)

    # Render the response in response.html with the results
    return render_template('response.html', response1=results)

if __name__ == '__main__':
    app.run(port=80)
