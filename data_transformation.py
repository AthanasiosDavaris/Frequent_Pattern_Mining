import collections

# Mapping dictionary for transliteration
translation_map = {
  'γύρο_χοιρινό': 'Gyros_Pork',
  'γύρο_κοτόπουλο': 'Gyros_Chicken',
  'κοτομπέικον': 'Kotobeikon',
  'χωριάτικη': 'Choriatiki_Salad',
  'σαγανάκι': 'Saganaki',
  'ψωμί_λευκό': 'Bread_White',
  'ψωμί_μαύρο': 'Bread_Brown',
  'ψωμί_πολύσπορο': 'Bread_Multigrain',
  'αναψυκτικό': 'Soda',
  'φρουτοσαλάτα': 'Fruit_Salad',
  'πατάτες': 'Fries',
  'παγωτό': 'Ice_Cream',
  'χυμός': 'Juice',
  'καίσαρα': 'Caesar_Salad',
  'αγγουροντομάτα': 'Cucumber_Tomato_Salad',
  'μαρούλι': 'Lettuce_Salad',
  'τυροκροκέτες': 'Cheese_Croquettes',
  'μπιφτέκι_λαχανικών': 'Veggie_Burger',
  'γιαούρτι-μέλι': 'Yogurt_Honey',
  'μπύρα': 'Beer',
  'νερό': 'Water',
  'μιλκσέικ': 'Milkshake',
  'καλαμάρι': 'Calamari',
  'κοτομπουκιές': 'Chicken_Nuggets'
}

input_file = 'orders.txt'
output_file = 'orders_latin.arff'

# Read and process
with open(input_file, 'r', encoding='utf-8') as f:
  lines = [line.strip() for line in f if line.strip()]

transactions = []
all_latin_items = set()

for line in lines:
  parts = line.split(',')
  age = parts[1]
  greek_items = parts[2:]

  latin_items = set()
  for item in greek_items:
    latin_name = translation_map.get(item, item)
    latin_items.add(latin_name)
    all_latin_items.add(latin_name)
  
  transactions.append({'age': age, 'items': latin_items})

sorted_items = sorted(list(all_latin_items))

# Write the ARFF file
with open(output_file, 'w', encoding='utf-8') as f:
  f.write("@RELATION psistiri_orders\n\n")
  f.write("@ATTRIBUTE age NUMERIC\n")

  for item in sorted_items:
    f.write(f"@ATTRIBUTE {item} {{True, False}}\n")
  
  f.write("\n@DATA\n")

  for trans in transactions:
    row = [trans['age']]
    for item in sorted_items:
      if item in trans['items']:
        row.append("True" if item in trans['items'] else "False")
    f.write(",".join(row) + "\n")

print(f"Success! {output_file} created with {len(sorted_items)} unique products.")