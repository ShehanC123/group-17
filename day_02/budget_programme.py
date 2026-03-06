def main():
    print("--- Monthly Budget Programme ---")
    
    try:
        # 1. Ask user for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        total_expenses = 0.0
        
        # 2. Loop to ask for expenses until 'done' is entered
        while True:
            expense_input = input("Enter an expense amount (or type 'done' to finish): ").strip().lower()
            
            if expense_input == 'done':
                break
                
            try:
                expense = float(expense_input)
                total_expenses += expense
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
        
        # 3. Subtract expenses from total budget
        remaining_balance = total_budget - total_expenses
        
        # 4. Display remaining balance to the user
        print(f"\nRemaining Balance: {remaining_balance:.2f}")
        
        if remaining_balance < 500:
            print("Warning: Low Funds")
        
        # Keep the window open
        input("\nPress Enter to exit...")
        
    except ValueError:
        print("Error: Please enter a valid number for the initial budget.")

if __name__ == "__main__":
    main()
