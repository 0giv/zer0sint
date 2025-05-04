import csv

def search_records(csv_file, keyword):
    matches = []
    keyword_lower = keyword.lower()

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nom = (row.get('nom') or '').lower()
            prenom = (row.get('prenom') or '').lower()
            if keyword_lower in nom or keyword_lower in prenom:
                matches.append(row)
    return matches

csv_file = 'datas/colicom/colicom.csv'      

def find_records(keyword):
    results = search_records(csv_file, keyword)
    if results:
        for rec in results:
            return rec 
    else:
        return 'No matching records found.' 
