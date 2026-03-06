def main():
    print("--- Grade calculator ---")
    
    while True:
        name = input("\nEnter student's name (or type 'Exit' to quit): ")
        if name.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break
            
        marks = []
        subjects = ["Subject 1", "Subject 2", "Subject 3"]
        
        for subject in subjects:
            while True:
                try:
                    mark_input = input(f"Enter marks for {subject}: ")
                    if mark_input.lower() == "exit":
                        return # Exit the entire program if they type exit here too
                    
                    mark = float(mark_input)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Error: Marks must be between 0 and 100.")
                except ValueError:
                    print("Error: Please enter a valid numerical value.")
        
        average = sum(marks) / len(marks)
        
        if average >= 75:
            grade = "A pass"
        elif average >= 60:
            grade = "B pass"
        elif average >= 40:
            grade = "C pass"
        else:
            grade = "Fail"
        
        print(f"\nResult: {name} - Average: {average:.2f} - Grade: {grade}")

if __name__ == "__main__":
    main()
