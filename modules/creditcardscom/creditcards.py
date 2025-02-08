import csv


def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]
    return rows

 
def filter_data(rows, field, value):
    filtered_rows = [row for row in rows if row[field] == value]
    return filtered_rows

 
def main(value):
    try:
        file_path = 'datas/creditcardscom/legal_contrats.csv'
        rows = read_csv(file_path)

        field = "Namer"
        

        filtered_rows = filter_data(rows, field, value)

        if filtered_rows:
            for row in filtered_rows:
                return format_data(row)
        else:
            return f"{value} No Data Found"
    except Exception as e:
        return f"Invalid ID or Error: {e}"

def format_data(data):
    formatted_output = []
    for key, value in data.items():
        formatted_output.append(f"{key}: {value}")
    
    return "\n".join(formatted_output)

