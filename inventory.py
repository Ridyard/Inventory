# Python script
""" i) create a dictionary of inventory items
    ii) take inventory contents from a list and add to inventory dictionary
    iii) take user input and add to inventory dictionary"""



"""part 1"""
# inventory of items (dictionary)
inventory = {'rope' : 1, 'torch' : 6, 'gold coin' : 42,
            'dagger' : 1, 'arrow' : 12}


def displayInventory(inventoryIn):
    totalItems = 0
    print('-----------------\nitems in inventory:\n')

    # print each inventory item and add v-value to totalItems
    for k, v in inventoryIn.items():
        print(str(v) + ' ' + k)
        totalItems += v
        
    print('\ntotal number of items: ' + str(totalItems))
    print('\n-----------------\n')


print('======START======\n')
displayInventory(inventory)





"""part 2"""
# list of items (to be added to inventory dict)
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# send in the inventory dict and the list of items to add
def addToDict(inventoryIn, addedItems):

    print('add additional items from list...\n')
    # for each item in the addedItems list...
    for i in range(len(addedItems)):

        # ...add the list item to the inventory dict & set default value to 0
        inventoryIn.setdefault(addedItems[i], 0)
        # increment the quantity
        inventoryIn[addedItems[i]] += 1
        print(addedItems[i] + ' added to the inventory')
    print('')

    #return the updated inventory dict
    return inventoryIn
        
      
addToDict(inventory, loot)
displayInventory(inventory)






"""part 3"""
def addItem(inventoryIn, addInvIn):
    for k, v in addInvIn.items():
        # add the key from addInv to the inventory dict and set to 0
        inventoryIn.setdefault(k, 0)
        # set the key/value (item/qty) in the inventory dict
        inventoryIn[k] += v
        print(k + ' ' + str(v) + ' added')

    return inventoryIn   
    



while True:
    # prompt user, to add to the inventory dictionary
    print('add an item & quantity to the inventory, leave blank to proceed')
    print('enter item...')
    item = input()
    if item == '':
        print('=======END=======')
        break
    else:
        print('enter quantity')
        qty = input()
        # create 'holding-dict' to be added to inventory dictionary
        addInv = {}
        addInv[item] = int(qty)

        # call function to add contents of holding-dict to inventory dict
        addItem(inventory, addInv)
    displayInventory(inventory)



    
        
    
