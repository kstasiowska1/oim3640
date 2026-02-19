def get_number(prompt):
    """
    Asks the user for a number and keeps asking until they enter a valid number.
    It uses a while True loop, which means the code will keep running until we
    manually stop it by returning a number. Inside the loop, we try to convert
    the input into a float. If it works, we return the number and exit the loop.
    If it fails (for example if the user types "abc"), the except block catches
    the error and asks the user to try again instead of crashing the program.
    """

    while True:
        text = input(prompt).strip().replace(",", "")
        try:
            return float(text)
        except ValueError:
            print("Please enter a valid number (example: 250000 or 250,000).")

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

def rate_deal(profit, roi):
    """
    Gives a simple deal rating (GOOD/MAYBE/RISKY) based on profit and ROI.
    I keep this separate so the rating logic is easy to update later.
    """
    reasons = []

    # Profit check
    if profit > 0:
        reasons.append("Profit is positive.")
    else:
        reasons.append("Profit is negative (you would lose money).")
        return "RISKY", reasons  # If you lose money, it's automatically risky

    # ROI check
    if roi >= 15:
        reasons.append("ROI is strong (15% or higher).")
        return "GOOD", reasons
    elif roi >= 5:
        reasons.append("ROI is okay (between 5% and 15%).")
        return "MAYBE", reasons
    else:
        reasons.append("ROI is low (below 5%).")
        return "RISKY", reasons

