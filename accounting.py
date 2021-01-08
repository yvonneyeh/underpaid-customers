melon_cost = 1.00

def payment_status(payment_file):
    """Calculate cost of melons and identify customers' incorrect payments 
    = underpaid or overpaid."""

    # open the file
    pay_info = open(payment_file)
    
    # Iterate through lines in file
    for line in pay_info:
        # Split lines to get list of strings
        order = line.split('|')

        # Get customers name
        name = order[1]
        first_name = name.split(" ")[0]
        last_name = name.split(" ")[1]

        # Number of melons ordered
        melons_num = int(order[2])

        # Amount paid
        paid_total = float(order[3])

        # Formula to calculate correct payment price of melons
        correct_price = melons_num * melon_cost

        # Print payment info
        print(f"{name} paid ${paid_total}, correct total = ${correct_price}.")

        # Overpaying customers
        if correct_price < paid_total:
            print (f"{first_name} overpaid.")

        # Underpaying customers
        elif correct_price > paid_total:
            print (f"{first_name} UNDERPAID.")

    # Close file
    pay_info.close()

# Call the function
payment_status("customer-orders.txt")