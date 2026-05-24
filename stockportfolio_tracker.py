
STOCK_MARKET = {
    "AAPL": 180,  # Apple
    "TSLA": 250,  # Tesla
    "GOOG": 150,  # Google
    "AMZN": 175,  # Amazon
    "MSFT": 400   # Microsoft
}

def run_portfolio_tracker():
    print("=========================================")
    print("📈 WELCOME TO YOUR STOCK PORTFOLIO TRACKER 📈")
    print("=========================================")
    
   
    print("Available stocks in our system today:")
    for ticker, price in STOCK_MARKET.items():
        print(f"  - {ticker}: ${price}")
    print("=========================================\n")

    user_portfolio = {}
    
    
    while True:
        stock_name = input("Enter the stock ticker symbol you own (or type 'done' to calculate): ").upper().strip()
        
        if stock_name == 'DONE':
            break
       
        if stock_name not in STOCK_MARKET:
            print(f"❌ Sorry, '{stock_name}' is not in our system. Please choose from the list above.\n")
            continue
       
        try:
            quantity = int(input(f"How many shares of {stock_name} do you own? "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0.\n")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a whole number for the quantity.\n")
            continue
            

        if stock_name in user_portfolio:
            user_portfolio[stock_name] += quantity
        else:
            user_portfolio[stock_name] = quantity
            
        print(f"✅ Added {quantity} shares of {stock_name} to your portfolio.\n")

    print("\n=========================================")
    print("          📊 PORTFOLIO SUMMARY 📊        ")
    print("=========================================")
    
    total_portfolio_value = 0
    summary_text = "Your Stock Portfolio Breakdown:\n"
    
    for stock, qty in user_portfolio.items():
        price_per_share = STOCK_MARKET[stock]
        total_stock_value = qty * price_per_share

        total_portfolio_value += total_stock_value

        
        line = f"• {stock}: {qty} shares x ${price_per_share} = ${total_stock_value}\n"
        print(line.strip())
        summary_text += line

    final_total_line = f"\n💰 Total Investment Value: ${total_portfolio_value}"
    print(final_total_line)
    summary_text += final_total_line
    print("=========================================\n")


    save_choice = input("Would you like to save this summary to a text file? (yes/no): ").lower().strip()
    if save_choice == 'yes' or save_choice == 'y':
    
       with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
           file.write(summary_text)
           print("💾 Success! Your summary has been saved to 'portfolio_summary.txt'.")
    else:
        print("👋 Thank you for using the Stock Portfolio Tracker!")

if __name__ == "__main__":
    run_portfolio_tracker()
