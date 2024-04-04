def calculate_usiu_grade(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 70 <= marks < 89:
        return 'B'
    elif 65 <= marks < 69:
        return 'C'
    elif 50 <= marks < 64:
        return 'D'
    elif 0 <= marks < 49:
        return 'F'
    else:
        return 'Invalid'

def main():
    subjects = ['Math', 'English', 'Science', 'Chemistry', 'Physics', 'Programming', 'Spanish']  
    while True:
        total_subjects = len(subjects)
        total_marks = 0

        for subject in subjects:
            marks = float(input(f"Enter marks for {subject}: "))
            if not (0 <= marks <= 100):
                print("Invalid marks. Marks should be between 0 and 100.")
                break  
            total_marks += marks

        else:  
            average_marks = total_marks / total_subjects
            grade = calculate_usiu_grade(average_marks)

            print(f"\nAverage marks: {average_marks:.2f}")
            print(f"Grade: {grade}")

        terminate = input("Do you want to terminate the program? (yes/no): ")
        if terminate.lower() == 'yes':
            print("Program terminated.")
            break

if __name__ == "__main__":
    main()
