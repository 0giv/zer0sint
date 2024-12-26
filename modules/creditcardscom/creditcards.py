import csv

# CSV dosyasını okuma
def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]
    return rows

# Sorgu yapma
def filter_data(rows, field, value):
    filtered_rows = [row for row in rows if row[field] == value]
    return filtered_rows

# Ana fonksiyon
def main(value):
    # CSV dosyasını oku
    file_path = 'datas/creditcardscom/legal_contrats.csv'
    rows = read_csv(file_path)

    # Kullanıcıdan sorgu bilgisi al
    field = "Namer"
    

    # Sorguyu çalıştır
    filtered_rows = filter_data(rows, field, value)

    # Sonuçları yazdır
    if filtered_rows:
        for row in filtered_rows:
            return format_data(row)
    else:
        return f"{field} = {value} No Data Found"


def format_data(data):
    # Veriyi sıralı şekilde formatlayıp geri döndürme
    formatted_output = []
    for key, value in data.items():
        formatted_output.append(f"{key}: {value}")
    
    return "\n".join(formatted_output)

