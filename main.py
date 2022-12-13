lot_size = 100;

# Passive Order Details
p_order_price = float(input("Enter the Passive Order price : "))
while True: # endless loop

    p_order_size = int(input("Enter the passive order size : "))
    if p_order_size % lot_size !=0: # if the ssn is not a number, stop
        print("not supported")
        continue # let the user try again
    else:
        p_order_side = input("Enter the Passive order side : ")
        p_order_owner = input("Enter the passive order owner : ")

        print("--------- Aggressive order details ----------------")
        # Aggressive Order
        a_order_price = float(input("Enter the aggressive Order price : "))

        while True:
            a_order_size = int(input("Enter the aggressive order size : "))
            if a_order_size % lot_size != 0:
                print("Not Supported Lot Size.")
                continue
            else:
                a_order_side = input("Enter the aggressive order side : ")
                a_order_owner = input("Enter the aggressive order owner : ")
            break
    break

if a_order_side == "sell":
    if p_order_price >= a_order_price and p_order_side == "buy":

        if p_order_size == a_order_size:
            remaining = 0
            trade_volume = a_order_size

        elif p_order_size > a_order_size:
            remaining = p_order_size - a_order_size
            trade_volume = a_order_size

        else:
            remaining = a_order_size - p_order_size
            trade_volume = p_order_size

        if remaining == 0:
            print("Trade happens between " + a_order_owner + " and " + p_order_owner + " with the price "
                  + str(p_order_price) + " and Size " + str(trade_volume))
        else:
            print("Trade happens between " + a_order_owner + " and " + p_order_owner + " with the price "
                  + str(p_order_price) + " and Size " + str(trade_volume) + ".Remaining order Qty " + str(remaining))

    # Aggressive side and passive side are same, there is no trade happens
    else:
        print("No trade happend")
else:
    if p_order_price <= a_order_price and p_order_side == "sell":

        if p_order_size == a_order_size:
            remaining = 0
            trade_volume = a_order_size

        elif p_order_size > a_order_size:
            remaining = p_order_size - a_order_size
            trade_volume = a_order_size

        else:
            remaining = a_order_size - p_order_size
            trade_volume = p_order_size

        if remaining == 0:
            print("Trade happens between " + a_order_owner + " and " + p_order_owner + " with the price "
                  + str(p_order_price) + " and Size " + str(trade_volume))
        else:
            print("Trade happens between " + a_order_owner + " and " + p_order_owner + " with the price "
                  + str(p_order_price) + " and Size " + str(trade_volume) + ".Remaining order Qty " + str(remaining))

    # Aggressive side and passive side are same, there is no trade happens
    else:
        print("No trade happens")

