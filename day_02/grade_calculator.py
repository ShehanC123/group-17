def main():
    print("--- Grade calculator ---")
    
    name = input("Enter student's name: ")
    marks = []
    subjects = ["Subject 1", "Subject 2", "Subject 3"]
    
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Error: Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid numerical value.")
    
    average = sum(marks) / len(marks)
    
    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {average:.2f}")
    
    if average >= 75:
        print("Result: A pass")
    elif average >= 60:
        print("Result: B pass")
    elif average >= 40:
        print("Result: C pass")
    else:
        print("Result: Fail")

if __name__ == "__main__":
    main()
