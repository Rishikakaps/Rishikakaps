shoppinglist = []
items = input('how many items do you want to add to your shopping list? ')
for items in range(int(items)):
    shopping_item = input('Enter item: ')
    shoppinglist.append(items)
    if items == 'done':
     break
item_to_find = input('Enter item to find: ')
found_at = None 
for index in range(len(shoppinglist)):
    if shoppinglist[index] == item_to_find:
        found_at = index
        print(f'Item found at position {found_at}')
    else:
        print(f'{item_to_find} was not found on the list')
        
        