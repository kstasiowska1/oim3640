def get_valid_input(prompt, min_value=0):
    """
    Prompts the user for a numeric input and validates it.
    Ensures the input is a non-negative number.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_metrics(purchase_price, repair_costs, sale_price, selling_cost_percent=0.06):
    """
    Calculates total cost, profit, and ROI for a house flip deal.
    Selling costs are estimated as a percentage of the sale price.
    """
    total_cost = purchase_price + repair_costs
    selling_costs = sale_price * selling_cost_percent
    net_sale = sale_price - selling_costs
    profit = net_sale - total_cost
    roi = (profit / total_cost) * 100 if total_cost > 0 else 0
    return total_cost, profit, roi, selling_costs

def rate_deal(roi, profit):
    """
    Rates the deal based on ROI and profit.
    Returns rating and explanation.
    """
    if roi > 15 and profit > 0:
        rating = "Good"
        explanation = "High ROI and positive profit indicate a strong deal."
    elif 5 <= roi <= 15 and profit > 0:
        rating = "Maybe"
        explanation = "Moderate ROI; proceed with caution and further research."
    else:
        rating = "Risky"
        explanation = "Low or negative ROI/profit suggests high risk or loss."
    return rating, explanation

def display_results(total_cost, profit, roi, selling_costs, rating, explanation):
    """
    Displays the deal results in a formatted output.
    """
    print(f"\nDeal Summary:")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Selling Costs (6%): ${selling_costs:.2f}")
    print(f"Estimated Profit: ${profit:.2f}")
    print(f"ROI: {roi:.2f}%")
    print(f"Rating: {rating}")
    print(f"Explanation: {explanation}")

def main():
    """
    Main function to run the house flip evaluator app.
    Allows analyzing multiple deals in one session.
    """
    print("Welcome to the House Flip Evaluator!")
    print("This app helps evaluate if a house flip is financially worth it based on your inputs.")
    
    deals = []
    while True:
        print("\nEnter details for a new deal:")
        purchase_price = get_valid_input("Purchase price: $", min_value=0.01)
        repair_costs = get_valid_input("Repair costs: $", min_value=0)
        sale_price = get_valid_input("Expected sale price: $", min_value=0.01)
        
        total_cost, profit, roi, selling_costs = calculate_metrics(purchase_price, repair_costs, sale_price)
        rating, explanation = rate_deal(roi, profit)
        display_results(total_cost, profit, roi, selling_costs, rating, explanation)
        
        deals.append({
            "purchase": purchase_price,
            "repairs": repair_costs,
            "sale": sale_price,
            "profit": profit,
            "roi": roi,
            "rating": rating
        })
        
        choice = input("\nAnalyze another deal? (y/n): ").strip().lower()
        if choice != 'y':
            break
    
    print(f"\nSession complete. You analyzed {len(deals)} deals.")
    if deals:
        print("Summary of all deals:")
        for i, deal in enumerate(deals, 1):
            print(f"Deal {i}: Profit ${deal['profit']:.2f}, ROI {deal['roi']:.2f}%, Rating {deal['rating']}")

if __name__ == "__main__":
    main()