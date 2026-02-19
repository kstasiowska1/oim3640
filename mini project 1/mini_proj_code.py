def calculate_flip(buy_price, rehab_cost, sell_price):
    """
    Calculates total project cost, profit, and ROI for a house flip. 
    It adds purchase price + repair costs to get the total cost, 
    subtracts total cost from the expected sale price to get profit,
    and calculates ROI as a percentage. I can update the math here if
    I want to add more costs later wihout changing the rest of the code.
    """
    total_cost = buy_price + rehab_cost
    profit = sell_price - total_cost

    # ROI = profit / total cost (as a percent) and check total_cost > 0 just to be safe
    if total_cost > 0:
        roi = (profit / total_cost) * 100
    else:
        roi = 0

    return total_cost, profit, roi