def get_number(prompt):
    """
    Asks the user for a number and keeps asking until they enter a valid positive
    number. This prevents crashes and unrealistic negative outputs. It uses a while
    True loop, which means the code will keep running until we manually stop it by 
    returning a number. Inside the loop, we try to convert the input into a float. 
    If it works, we return the number and exit the loop. If it fails (for example if 
    the user types "abc"), the except block catches the error and asks the user to 
    try again instead of crashing the program.
    """

    while True:
        text = input(prompt).strip().replace(",", "")
        try:
            value = float(text)
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number (example: 250000 or 250,000).")

def calculate_flip(buy_price, rehab_cost, sell_price):
    """
    Calculates total project cost, profit, and ROI for a house flip. 
    It adds purchase price + repair costs to get the total cost, 
    subtracts total cost from the expected sale price to get profit,
    and calculates ROI as a percentage. It includes a 6% selling cost 
    to account for various selling costs that are usually included when 
    selling a property. I can update the math here if I want to add more 
    costs later wihout changing the rest of the code.
    """
    selling_cost_rate = 0.06 # 6% selling costs (agent fees, closing costs, etc.)
    selling_costs = sell_price * selling_cost_rate
    
    total_cost = buy_price + rehab_cost +selling_costs
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
    
def main():
    """
    This is the main app. It displays a welcome message explaning the tool, a simple 
    menu and uses a while True loop so the user can analyze multiple deals without 
    restarting the program. It shows menu options, gets user input for menu selection,
    calls the calculate functions, formats and prints the results, and exits when the 
    user chooses to quit.
    """
    
    print("\nWelcome to the House Flip Deal Analyzer!")
    print("This tool estimates profit, ROI, and gives a simple deal rating.")

    # This loop keeps the program running until the user chooses to quit
    while True:
        print("\nMenu:")
        print("1) Analyze a deal")
        print("2) Quit")

        # Get user's menu choice
        choice = input("Choose 1 or 2: ").strip()

        # If user wants to analyze a deal
        if choice == "1":
            # Get financial inputs using the input function
            buy_price = get_number("Purchase price ($): ")
            rehab_cost = get_number("Repair cost ($): ")
            sell_price = get_number("Expected sale price ($): ")

            # Call the calculation function
            total_cost, profit, roi = calculate_flip(buy_price, rehab_cost, sell_price)

            # Display results in a clean format
            print("\n--- Results ---")
            print(f"Total cost: ${total_cost:,.2f}")
            print(f"Profit: ${profit:,.2f}")
            print(f"ROI: {roi:.2f}%")
            
            rating, reasons = rate_deal(profit, roi)
            
            print(f"Deal rating: {rating}")
            for reason in reasons:
                print(f"- {reason}")

        # If user chooses to quit
        elif choice == "2":
            print("Goodbye.")
            break  # Stops the while loop and ends the program

        # If user types something invalid
        else:
            print("Invalid choice. Please enter 1 or 2.")


# Runs the program
if __name__ == "__main__":
    main()


