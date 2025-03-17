from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import ast
from modules.websites.scam import scammerdb_web
from modules.people.Email import email_lookup
from modules.websites.Ransom import ransomlookup
from modules.creditcardscom import creditcards
from modules.websites.hudsonrock import hudsonrock

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/usage")
def usage():
    return render_template("usage.html")


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    tool = data.get("tool", "").lower()

    results = "Error fetching data"

    try:
        if tool == "scam":
            results = scammerdb_web.scammerdb(query)
        elif tool == "email":
            results = email_lookup.findemail(query)

            if isinstance(results, str):
                try:
                    results = ast.literal_eval(results)
                except:
                    pass

            if isinstance(results, list) and isinstance(results[0], dict):
                cleaned_results = []
                for item in results:
                    leaked_sites = item.get("leaked_site", "").strip().split("\n")
                    cleaned_results.extend(
                        [site.strip() for site in leaked_sites if site.strip()]
                    )
                results = cleaned_results

        elif tool == "ransom":
            results = ransomlookup.ransomlookup(query)
        elif tool == "creditcard":
            results = creditcards.main(query)
            if isinstance(results, str):
                parsed_results = {}
                lines = results.split(" ")
                current_key = None
                current_value = []

                for item in lines:
                    if ":" in item:
                        if current_key:
                            parsed_results[current_key] = " ".join(current_value)
                        key_value = item.split(":", 1)
                        current_key = key_value[0].strip()
                        current_value = (
                            [key_value[1].strip()] if len(key_value) > 1 else []
                        )
                    else:
                        current_value.append(item.strip())

                if current_key:
                    parsed_results[current_key] = " ".join(current_value)

                results = parsed_results
        elif tool == "hudsonrock":
            results = hudsonrock.hudsonrock(query)

    except Exception as e:
        results = [f"Error: {str(e)}"]

    return render_template("response.html", response1=results, tool=tool)


if __name__ == "__main__":
    app.run(debug=True, port=80)
