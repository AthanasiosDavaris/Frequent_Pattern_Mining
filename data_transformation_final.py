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
output_file = 'orders_final.arff'

# Read and process
with open(input_file, 'r', encoding='utf-8') as f:
  lines = [line.strip() for line in f if line.strip()]

transactions = []
for line in lines:
  parts = line.split(',')
  age = int(parts[1])
  
  if age <= 25:
    age_group = 'Age_15_25'
  elif age <= 45:
    age_group = 'Age_26_45'
  else:
    age_group = 'Age_46_Plus'
  
  items = parts[2:]
  transactions.append({'age_group': age_group, 'items': items})

with open(output_file, 'w', encoding='utf-8') as f:
  f.write("@RELATION psistiri_final\n\n")

  f.write("@ATTRIBUTE age_group {Age_15_25, Age_26_45, Age_46_Plus}\n")

  for group_name in groups.keys():
    f.write(f"@ATTRIBUTE {group_name} {{True, False}}\n")
  
  f.write("\n@DATA\n")
  for trans in transactions:
    row = [trans['age_group']]
    for group_name, items_in_group in groups.items():
      has_item = any(item in trans['items'] for item in items_in_group)
      row.append("True" if has_item else "False")
    f.write(",".join(row) + "\n")

print(f"Final ARFF created: orders_final.arff")