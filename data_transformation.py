import collections

# Read the data
input_file = 'orders.txt'
output_file = 'orders.arff'

with open(input_file, 'r', encoding='utf-8') as f:
  lines = [line.strip() for line in f if line.strip()]

# Extract unique items and prepare transactions
transactions = []
all_items = set()

for line in lines:
  parts = line.split(',')
  # parts[0] is customer_id, parts[1] is age, parts[2:] are items
  age = parts[1]
  items = parts[2:]
  transactions.append({'age': age, 'items': set(items)})
  for item in items:
    all_items.add(item)
  
sorted_items = sorted(list(all_items))

# Write the ARFF file
with open(output_file, 'w', encoding='utf-8') as f:
  f.write("@RELATION psistiri_orders\n\n")

  # Age as a numeric attribute
  f.write("@ATTRIBUTE age NUMERIC\n")

  # Each product as a nominal attribute {True, False}
  for item in sorted_items:
    f.write(f"@ATTRIBUTE {item} {{True, False}}\n")
  
  f.write("\n@DATA\n")

  for trans in transactions:
    row = [trans['age']]
    for item in sorted_items:
      if item in trans['items']:
        row.append("True")
      else:
        row.append("False")
    f.write(",".join(row) + "\n")

print(f"Success! {output_file} created with {len(sorted_items)} unique products.")