def main():
    print("--- Monthly Budget Programme ---")
    
    try:
        total_budget = float(input("Enter your total monthly budget: "))
        
        expense1 = float(input("Enter first expense: "))
        expense2 = float(input("Enter second expense: "))
        expense3 = float(input("Enter third expense: "))
        
        total_expenses = expense1 + expense2 + expense3
        remaining_balance = total_budget - total_expenses
        
        print(f"\nRemaining Balance: {remaining_balance:.2f}")
        
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
