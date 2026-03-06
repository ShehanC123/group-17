def main():
    print("--- Monthly Budget Programme ---")
    
    try:
        # 1. Ask user for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        # 2. Ask for 3 expenses one by one
        expense1 = float(input("Enter first expense: "))
        expense2 = float(input("Enter second expense: "))
        expense3 = float(input("Enter third expense: "))
        
        # 3. Subtract expenses from total budget
        remaining_balance = total_budget - (expense1 + expense2 + expense3)
        
        
        # 4. Display remaining balance to the user
        print(f"\nRemaining Balance: {remaining_balance:.2f}")
        
        if remaining_balance < 500:
            print("Warning: Low Funds")
        
        # Keep the window open
        input("\nPress Enter to exit...")
        
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
