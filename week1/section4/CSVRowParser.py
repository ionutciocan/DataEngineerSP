#ultimele 3 subpuncte de la acest exercitiu sunt facute full ai, doar voiam sa vad o rezolvare ca sa le am aici

def split_in_tuples(strr):
    return [tuple(row.split(',')) for row in strr.strip().split('\n')]


def string_to_dict(strr):
    res = {}
    parsed_dat = split_in_tuples(strr)
    headers = parsed_dat[0]
    for i in range(len(headers)):
        res[headers[i]] = []
    for j in range(1, len(parsed_dat)):
        for i in range(len(headers)):
            res[headers[i]].append(parsed_dat[j][i])
    return res


def convert_numeric_columns(data):
    data['price'] = [float(p) for p in data['price']]
    data['quantity'] = [int(q) for q in data['quantity']]
    return data


def build_summary(data):
    total_rows = len(data['name'])

    return {
        'total_rows': total_rows,
        'column_names': list(data.keys()),
        'price_min': min(data['price']),
        'price_max': max(data['price']),
        'price_avg': sum(data['price']) / total_rows,
        'qty_min': min(data['quantity']),
        'qty_max': max(data['quantity']),
        'qty_avg': sum(data['quantity']) / total_rows
    }


def find_highest_value_row(data):
    total_rows = len(data['name'])
    max_total_value = -1
    best_row_index = -1

    for i in range(total_rows):
        total_value = data['price'][i] * data['quantity'][i]
        if total_value > max_total_value:
            max_total_value = total_value
            best_row_index = i

    best_row = {col: data[col][best_row_index] for col in data.keys()}
    return best_row, max_total_value

csv_data = '''name,category,price,quantity
Widget A,Electronics,29.99,100
Widget B,Electronics,49.99,50
Gadget C,Accessories,9.99,300
Gadget D,Accessories,14.99,0
Device E,Electronics,199.99,25'''


parsed_data = split_in_tuples(csv_data)

for row in parsed_data:
    print(row)

print(string_to_dict(csv_data))

raw_dict = string_to_dict(csv_data)
clean_data = convert_numeric_columns(raw_dict)
summary = build_summary(clean_data)
best_item, max_val = find_highest_value_row(clean_data)


print("--- Sumar Date ---")
print(f"Număr total rânduri: {summary['total_rows']}")
print(f"Coloane: {', '.join(summary['column_names'])}")
print(f"Preț      -> Min: ${summary['price_min']:.2f} | Max: ${summary['price_max']:.2f} | Mediu: ${summary['price_avg']:.2f}")
print(f"Cantitate -> Min: {summary['qty_min']} | Max: {summary['qty_max']} | Mediu: {summary['qty_avg']:.1f}\n")

print("--- Produsul cu cea mai mare valoare totală ---")
print(f"Nume: {best_item['name']}")
print(f"Categorie: {best_item['category']}")
print(f"Preț Unitar: ${best_item['price']:.2f}")
print(f"Cantitate: {best_item['quantity']}")
print(f"Valoare Totală (Preț × Cantitate): ${max_val:,.2f}")