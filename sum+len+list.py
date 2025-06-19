'''
shopping_list = ["Milk", "Eggs", "Bread", "Banna"]
shopping_list.append("Apples")
shopping_list.pop(2)

def show_list():
  for items in shopping_list:
    print(items)
    

def total_items(shopping_list):
  print(len(shopping_list))

print(f"Your shopping list: {shopping_list}")
print(f"Total items: {len(shopping_list)}")
'''

ticket_counts = [12, 15, 10, 13, 14, 20, 17]
#print(sum(ticket_counts)/(len(ticket_counts)))
print(sum(ticket_counts[0:5]))
print(sum(ticket_counts[5:7]))
