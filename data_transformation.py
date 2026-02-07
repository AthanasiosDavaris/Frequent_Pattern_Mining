import collections

groups = {
  'Main_Dish': ['γύρο_χοιρινό', 'γύρο_κοτόπουλο', 'μπιφτέκι_λαχανικών', 'καλαμάρι', 'κοτομπέικον', 'κοτομπουκιές'],
  'Side_Dish': ['πατάτες', 'σαγανάκι', 'τυροκροκέτες'],
  'Bread': ['ψωμί_λευκό', 'ψωμί_μαύρο', 'ψωμί_πολύσπορο'],
  'Salad': ['χωριάτικη', 'καίσαρα', 'αγγουροντομάτα', 'μαρούλι'],
  'Drink': ['αναψυκτικό', 'μπύρα', 'νερό', 'χυμός', 'μιλκσέικ'],
  'Dessert': ['παγωτό', 'γιαούρτι-μέλι', 'φρουτοσαλάτα']
}

input_file = 'orders.txt'
output_file = 'orders_grouped.arff'

# Read and process
with open(input_file, 'r', encoding='utf-8') as f:
  lines = [line.strip() for line in f if line.strip()]

transactions = []

for line in lines:
  parts = line.split(',')
  age = parts[1]
  items = parts[2:]
  transactions.append({'age': age, 'items': items})

with open(output_file, 'w', encoding='utf-8') as f:
  f.write("@RELATION psistiri_grouped\n\n")

  f.write("@ATTRIBUTE age NUMERIC\n")

  for group_name in groups.keys():
    f.write(f"@ATTRIBUTE {group_name} {{True, False}}\n")
  
  f.write("\n@DATA\n")

  for trans in transactions:
    row = [trans['age']]
    for group_name, items_in_group in groups.items():
      has_item_from_group = any(item in trans['items'] for item in items_in_group)
      row.append("True" if has_item_from_group else "False")
    
    f.write(",".join(row) + "\n")

print(f"Success! Created {output_file} with grouped categories.")