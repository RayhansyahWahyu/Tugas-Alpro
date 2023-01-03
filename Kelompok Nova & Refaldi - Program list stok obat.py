stock_items = []

def create_item(name, quantity):
  stock_items.append({'name': name, 'quantity': quantity})

def read_item(name):
  for item in stock_items:
    if item['name'] == name:
      return item
  return None

def update_item(name, quantity):
  for item in stock_items:
    if item['name'] == name:
      item['quantity'] = quantity
      return

def delete_item(name):
  for item in stock_items:
    if item['name'] == name:
      stock_items.remove(item)
      break

def print_stock():
  for item in stock_items:
    print(f"{item['name']}: {item['quantity']}")

create_item('apple', 10)
create_item('banana', 5)
create_item('orange', 8)

print_stock()

update_item('banana', 3)

print_stock()

delete_item('orange')

# Print the updated stock
print_stock()