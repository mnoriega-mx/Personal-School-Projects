import random
import csv

# List of all games
ProductsList = [100, 'Fifa', 14.99, 8, 'active', 105, 'Call of Duty', 19.99, 12, 'active', 110, 'NBA 2k 22', 17.99, 24,
                'active', 115, 'Overwatch', 9.99, 0, 'inactive', 120, 'Fortnite', 9.99, 4, 'active', 125, 'Madden 22',
                19.99, 20, 'active', 130, 'Halo', 8.99, 0, 'active', 135, 'Star Wars Battlefront', 5.99, 2, 'active',
                140, 'Super Mario Bros Wii', 7.99, 1, 'inactive', 145, 'Apex Legends', 15.99, 14, 'active', 150,
                'Minecraft', 12.99, 9, 'active', 155, 'Grand Theft Auto V', 4.99, 5, 'inactive', 160,
                'Plants vs Zombies', 5.99, 4, 'active']

CostumersList = []
OrdersList = []
option = 0
order_number = 1722542
amount_due = 0
spaces = 0


# Display the catalog except for the inactive products
def ShowCatalog():
    print('Code Game                 Price  Stock')
    print('------------------------------------')
    for count in range(0, len(ProductsList), 5):
        if ProductsList[count + 4] == 'active':
            print(ProductsList[count], end=" ")
            if len(ProductsList[count + 1]) < 22:
                spaces = 22 - len(ProductsList[count + 1])
            print(ProductsList[count + 1], " " * spaces, end='')
            if len(str(ProductsList[count + 2])) < 7:
                spaces = 7 - len(str(ProductsList[count + 2]))
            print('$' + str(ProductsList[count + 2]), " " * spaces, end='')
            print(ProductsList[count + 3])


def UpdateProducts():
    print('Products update')
    print('---------------')
    game_code = int(input('Enter the video game code: '))

    if game_code in ProductsList:
        position = ProductsList.index(game_code)
        gameInfo(game_code)

        modify = input('''
Enter feature to modify
a.Price
b.Stock
c.Status
d.Cancel update

>''')
        # Replacing the user input of the selected update for the current info in the products list
        if modify == 'a':
            new_price = float(input('Enter new price: '))
            ProductsList[position + 2] = new_price
            print('Product successfully updated')
        elif modify == 'b':
            new_stock = int(input('Enter new stock quantity: '))
            ProductsList[position + 3] = new_stock
            print('Product successfully updated')
        elif modify == 'c':
            new_status = input('Enter new status: ')
            ProductsList[position + 4] = new_status
            print('Product successfully updated')

    else:
        print('Product inexistent')


def RegisterNewCostumer():
    # Join the two inputs into a new string using index to select the letters
    print('Register new costumer')
    print('--------------------')
    costumer_name = input("Enter costumer's name: ")
    costumer_phone = input("Enter costumer's phone number: ")
    costumer_code = str(costumer_phone[-3:]) + costumer_name.upper()[0:3]
    if costumer_code in CostumersList:
        code_position = CostumersList.index(costumer_code)
        print('Costumer already registered with the code:', CostumersList[code_position])
    else:
        CostumersList.append(costumer_code)
        print('Costumer registered with the code:', costumer_code)


def CreateOrder(order_number):
    amount_due = 0
    print('Create new order')
    print('----------------')
    costumer_code = input('Enter costumer code: ')
    # Validate if the costumer is registered, if the product exists, if the product is active, and if the product is in stock
    if costumer_code in CostumersList:
        run_buy_order = 'yes'
        while run_buy_order.lower() == 'yes':
            game_code = int(input('Enter the product code: '))

            if game_code in ProductsList:
                if ProductsList[ProductsList.index(game_code) + 4] == 'active':
                    if ProductsList[ProductsList.index(game_code) + 3] > 0:
                        gameInfo(game_code)

                        amount_to_buy = int(input('Enter amount to buy: '))
                        while amount_to_buy > ProductsList[ProductsList.index(game_code) + 3]:
                            print('Not enough stock')
                            amount_to_buy = int(input('Enter amount to buy: '))
                            # Calculate price with discounts and append info to the order list
                        else:
                            price = ProductsList[ProductsList.index(game_code) + 2]
                            amount_due = round(amount_due + amount_to_buy * price, 2)
                            total_price = price * amount_to_buy

                            ProductsList[ProductsList.index(game_code) + 3] = ProductsList[ProductsList.index(
                                game_code) + 3] - amount_to_buy

                            if amount_to_buy >= 5 and amount_to_buy < 10:
                                amount_due = round(amount_due * 0.95, 2)
                                total_price = round((price * amount_to_buy) * 0.95, 2)
                                print('Congratulations, you have a 5% discount!')
                            elif amount_to_buy >= 10 and amount_to_buy < 20:
                                amount_due = round(amount_due * 0.90, 2)
                                total_price = round((price * amount_to_buy) * 0.90, 2)
                                print('Congratulations, you have a 10% discount!')
                            elif amount_to_buy >= 20:
                                random_discount = random.randint(20, 30)
                                amount_due = round(amount_due * ((100 - random_discount) / 100), 2)
                                total_price = round((price * amount_to_buy) * ((100 - random_discount) / 100), 2)
                                print('Congratulations, you have a ' + str(random_discount) + '% discount!')

                            OrdersList.append(order_number)
                            OrdersList.append(costumer_code)
                            OrdersList.append(game_code)
                            OrdersList.append(amount_to_buy)
                            OrdersList.append(total_price)
                            order_created = "yes"

                            run_buy_order = input('Do you want to add another game?(yes/no): ')
                    else:
                        run_buy_order = input(
                            'Product out of stock, do you want to search for a different product?(yes/no): ')
                        order_created = "yes"

                else:
                    run_buy_order = input('Product inactive, do you want to search for a different product?(yes/no): ')
                    order_created = "no"
            else:
                run_buy_order = input('Product not existent, do you want to search for a different product?(yes/no): ')
                order_created = "no"

        if order_created == "yes":
            print()
            print('Order', order_number, 'has been created')
            print('Amount due: $' + str(amount_due))
            order_number += 1
    else:
        print('Costumer not registered, please select option 3 to register')

# More than one time I have to display the game info so I defined it to write the code once
def gameInfo(game_code):
    position = ProductsList.index(game_code)
    print('Name:', ProductsList[position + 1])
    print('Price:', '$' + str(ProductsList[position + 2]))
    print('Stock:', ProductsList[position + 3])
    print('Status:', ProductsList[position + 4])

# Look for the order number in the orders list and if it is in the list, print the info
def ShowOrder():
    display_order = int(input('Enter the order to display: '))
    if display_order in OrdersList:
        print('Order number:', OrdersList[OrdersList.index(display_order)])
        print('Costumer:', OrdersList[OrdersList.index(display_order) + 1])
        print('Product  Description  Quantity  Price  Total')

    spaces = 0
    if display_order in OrdersList:
        for count in range(0, len(OrdersList), 5):
            if OrdersList[count] == display_order:
                product_position = ProductsList[ProductsList.index(OrdersList[count + 2])]
                print(OrdersList[count + 2], end=" ")
                if len(str(ProductsList[ProductsList.index(product_position) + 1])) < 14:
                    spaces = 14 - len(str(ProductsList[ProductsList.index(product_position) + 1]))
                print(ProductsList[ProductsList.index(product_position) + 1], " " * spaces, end=" ")
                print(OrdersList[count + 3], end=" ")
                print('$' + str(ProductsList[ProductsList.index(product_position) + 2]), end=" ")
                print('$' + str(round(OrdersList[count + 4], 2)))

# Open a new file and use the writer to create a CSV file of the catalog
def SaveData():
    print("Generating CVS file...")
    catalogFile = open("catalog.csv", "w", newline="")
    writer = csv.writer(catalogFile)

    header = ['Code', 'Product', 'Price', 'Stock', 'Status']
    writer.writerow(header)

    for count in range(0, len(ProductsList), 5):
        row = list()
        row.append(ProductsList[count])
        row.append(ProductsList[count + 1])
        row.append('$' + str(ProductsList[count + 2]))
        row.append(ProductsList[count + 3])
        row.append(ProductsList[count + 4])
        writer.writerow(row)

    catalogFile.close()
    print("Catalog CSV file is ready")

# Go through the catalog and print the product name and the stock if the stock is less than 5
# Go through orders list and if the costumer code is in the list print that order info
def ExtraReports():
    print('''
a) Report of low stock products
b) Report of orders for a costumer
        ''')
    option = input('Pick your report option: ')
    if option == 'a':
        print('Report of low stock products')
        print('----------------------------')
        for count in range(0, len(ProductsList), 5):
            if ProductsList[count + 3] < 5:
                print(ProductsList[count + 1], '-', ProductsList[count + 3])
    if option == 'b':
        costumer_code = input('Enter the costumer code: ')
        if costumer_code in OrdersList:
            for count in range(0, len(OrdersList), 5):
                if OrdersList[count + 1] == costumer_code:
                    position_in_prodList = ProductsList.index(OrdersList[count + 2])
                    print(OrdersList[count + 2], end=" ")
                    if len(str(ProductsList[position_in_prodList + 1])) < 14:
                        spaces = 14 - len(str(ProductsList[position_in_prodList + 1]))
                        print(ProductsList[position_in_prodList + 1], " " * spaces, end=" ")
                        print(OrdersList[count + 3], end=" ")
                    print('$' + str(ProductsList[position_in_prodList + 2]), end=" ")
                    print('$' + str(OrdersList[count + 4]))

        else:
            print('No orders for this costumer')

# Keep showing the menu until the costumer exits
while option != 8:
    print('''
Game Stop Order Management System
=================================
1) Show catalog of products
2) Update products
3) Register new costumer
4) Create Order
5) Show order
6) Save data
7) Extra reports
8) Exit
    ''')

    option = int(input('Select an option from 1 to 8: '))
    print()

    while option < 1 or option > 8:
        print('Invalid option')
        option = int(input('Select an option from 1 to 8: '))
        print()

    if option == 1:
        ShowCatalog()

    if option == 2:
        UpdateProducts()

    if option == 3:
        RegisterNewCostumer()

    if option == 4:
        CreateOrder(order_number)

    if option == 5:
        ShowOrder()

    if option == 6:
        SaveData()

    if option == 7:
        ExtraReports()
