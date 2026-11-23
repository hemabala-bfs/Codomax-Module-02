"""
Student Grade Calculator
------------------------
Author: Hemabalaji R (Codomax Digital Solutions Intern)
Description: A beginner-friendly console application to manage student marks,
             calculate totals, averages, determine grades, enforce passing rules,
             and generate detailed student performance reports.
Demonstrates: Variables, Data Types, Input/Output, Loops, Conditionals,
             Functions, Lists, Dictionaries, and Exception Handling.
"""


def display_welcome_banner():
    """Displays the welcome banner for the application."""
    print("=" * 65)
    print(" " * 18 + "STUDENT GRADE CALCULATOR")
    print(" " * 14 + "Codomax Digital Solutions Internship")
    print("=" * 65)
    print("Welcome! This tool calculates total marks, percentage,")
    print("highest/lowest scores, and final grades for your students.")
    print("=" * 65)
    print()


def get_valid_student_name():
    """
    Prompts the user for a valid non-empty student name.
    
    Returns:
        str: The trimmed, validated student name.
    """
    while True:
        name = input("Enter student name: ").strip()
        if not name:
            print("[Error] Student name cannot be empty. Please try again.")
            continue
        # Check if name contains at least one alphabetic character
        if not any(char.isalpha() for char in name):
            print("[Error] Please enter a valid name containing letters.")
            continue
        return name


def get_valid_subject_count():
    """
    Prompts the user for the number of subjects with validation.
    
    Returns:
        int: A positive integer representing total subjects.
    """
    while True:
        user_input = input("Enter the number of subjects: ").strip()
        try:
            count = int(user_input)
            if count <= 0:
                print("[Error] Number of subjects must be greater than 0.")
            elif count > 20:
                print("[Error] Please enter a realistic number of subjects (1 to 20).")
            else:
                return count
        except ValueError:
            print("[Error] Invalid input! Please enter a valid whole number (e.g., 3, 5).")


def get_subject_marks(num_subjects):
    """
    Collects subject names and validated marks (0 to 100) from the user.
    Demonstrates: Lists, Dictionaries, Loops, and Exception Handling (try-except).
    
    Args:
        num_subjects (int): The number of subjects to input.
        
    Returns:
        list of dict: List containing dictionaries with 'subject' and 'marks'.
    """
    subject_records = []
    print("\n--- Enter Subject Details ---")
    print("Tip: You can enter custom subject names or press Enter to use default names.")

    for i in range(1, num_subjects + 1):
        # 1. Get Subject Name (Optional default: Subject 1, Subject 2...)
        sub_name_input = input(f"\nEnter name for Subject {i} [Press Enter for 'Subject {i}']: ").strip()
        if not sub_name_input:
            subject_name = f"Subject {i}"
        else:
            subject_name = sub_name_input

        # 2. Get Valid Numeric Mark between 0 and 100
        while True:
            mark_input = input(f"Enter marks obtained in {subject_name} (0 - 100): ").strip()
            try:
                mark = float(mark_input)
                if 0 <= mark <= 100:
                    # Store as integer if whole number for clean display, else float
                    if mark.is_integer():
                        mark = int(mark)
                    
                    # Store as a dictionary in our records list
                    record = {
                        "subject": subject_name,
                        "marks": mark
                    }
                    subject_records.append(record)
                    break
                else:
                    print(f"[Error] Marks must be between 0 and 100. You entered: {mark}")
            except ValueError:
                print(f"[Error] Invalid input '{mark_input}'! Marks must be a numeric value.")

    return subject_records


def calculate_total_marks(subject_records):
    """
    Calculates the total marks scored across all subjects.
    Demonstrates: Loops and Accumulation.
    
    Args:
        subject_records (list of dict): List of subject records.
        
    Returns:
        float: Total marks.
    """
    total = 0
    for record in subject_records:
        total += record["marks"]
    return total


def calculate_average_marks(total_marks, num_subjects):
    """
    Calculates the average percentage marks.
    
    Args:
        total_marks (float): Total marks scored.
        num_subjects (int): Total number of subjects.
        
    Returns:
        float: Average marks.
    """
    if num_subjects == 0:
        return 0.0
    return total_marks / num_subjects


def find_highest_and_lowest(subject_records):
    """
    Finds the highest and lowest marks along with their corresponding subject names.
    Demonstrates: List iteration and min/max comparison.
    
    Args:
        subject_records (list of dict): List of subject records.
        
    Returns:
        tuple: (highest_dict, lowest_dict)
    """
    if not subject_records:
        return None, None

    highest = subject_records[0]
    lowest = subject_records[0]

    for record in subject_records:
        if record["marks"] > highest["marks"]:
            highest = record
        if record["marks"] < lowest["marks"]:
            lowest = record

    return highest, lowest


def check_failing_subjects(subject_records, pass_mark=35):
    """
    Checks if any subject has marks below the passing threshold (35).
    Requirement: If a student scores below 35 in ANY subject, overall result is FAIL.
    
    Args:
        subject_records (list of dict): List of subject records.
        pass_mark (int): Minimum mark required to pass a subject (default 35).
        
    Returns:
        list of dict: List of failed subject records.
    """
    failed_subjects = []
    for record in subject_records:
        if record["marks"] < pass_mark:
            failed_subjects.append(record)
    return failed_subjects


def determine_grade(average_marks, has_failed_subject):
    """
    Determines student's letter grade and result status based on average marks
    and individual subject pass rules.
    
    Grading Scale:
    - 90–100: Grade A+
    - 80–89:  Grade A
    - 70–79:  Grade B
    - 60–69:  Grade C
    - 50–59:  Grade D
    - Below 50: Grade F
    
    Special Rule:
    If the student scores below 35 in any subject, overall result is FAIL
    regardless of the average grade.
    
    Args:
        average_marks (float): The average percentage.
        has_failed_subject (bool): True if student scored < 35 in any subject.
        
    Returns:
        tuple: (grade, result_status, remarks)
    """
    # 1. Base grade determination using conditional statements
    if average_marks >= 90:
        grade = "A+"
        remarks = "Outstanding Performance!"
    elif average_marks >= 80:
        grade = "A"
        remarks = "Excellent Work!"
    elif average_marks >= 70:
        grade = "B"
        remarks = "Good Performance. Keep it up!"
    elif average_marks >= 60:
        grade = "C"
        remarks = "Fair Performance. Needs more practice."
    elif average_marks >= 50:
        grade = "D"
        remarks = "Pass. Substantial improvement needed."
    else:
        grade = "F"
        remarks = "Needs Immediate Improvement."

    # 2. Check the overriding rule: any subject < 35 -> FAIL
    if has_failed_subject:
        result_status = "FAIL"
        # If overall result is FAIL due to a subject, the final effective grade is F
        final_grade = "F"
        remarks = "Failed: Scored below passing mark (35) in one or more subjects."
    else:
        if grade == "F":
            result_status = "FAIL"
        else:
            result_status = "PASS"
        final_grade = grade

    return final_grade, result_status, remarks


def display_performance_report(student_name, subject_records, total, average,
                               highest, lowest, grade, result, remarks, failed_subjects):
    """
    Prints a formatted, clean performance report in the console.
    
    Demonstrates: String formatting, loops, and conditional output.
    """
    max_possible = len(subject_records) * 100
    
    print("\n" + "=" * 65)
    print(" " * 18 + "STUDENT PERFORMANCE REPORT")
    print("=" * 65)
    print(f" Student Name       : {student_name}")
    print(f" Total Subjects     : {len(subject_records)}")
    print("-" * 65)
    print(f" {'No.':<4} {'Subject Name':<30} {'Marks Obtained':<15} {'Status':<10}")
    print("-" * 65)

    for idx, record in enumerate(subject_records, start=1):
        sub_status = "PASS" if record["marks"] >= 35 else "FAIL (<35)"
        print(f" {idx:<4} {record['subject']:<30} {record['marks']:<15} {sub_status:<10}")

    print("-" * 65)
    print(f" Total Marks Scored : {total} / {max_possible}")
    print(f" Average Percentage : {average:.2f}%")
    print(f" Highest Mark       : {highest['marks']} (in {highest['subject']})")
    print(f" Lowest Mark        : {lowest['marks']} (in {lowest['subject']})")
    print("-" * 65)
    print(f" Final Grade        : Grade {grade}")
    print(f" Overall Result     : {result}")
    print(f" Performance Remarks: {remarks}")

    if failed_subjects:
        print("\n [!] Warning: Failed Subject(s):")
        for f in failed_subjects:
            print(f"     - {f['subject']}: {f['marks']} / 100 (Minimum required: 35)")

    print("=" * 65 + "\n")


def process_single_student():
    """
    Coordinates the grade calculation workflow for one student.
    """
    # Step 1: Input student name
    student_name = get_valid_student_name()

    # Step 2: Input number of subjects
    num_subjects = get_valid_subject_count()

    # Step 3: Input marks for each subject
    subject_records = get_subject_marks(num_subjects)

    # Step 4: Calculate total and average
    total = calculate_total_marks(subject_records)
    average = calculate_average_marks(total, num_subjects)

    # Step 5: Find highest and lowest scores
    highest, lowest = find_highest_and_lowest(subject_records)

    # Step 6: Check failing subject rule (< 35 in any subject)
    failed_subjects = check_failing_subjects(subject_records, pass_mark=35)
    has_failed = len(failed_subjects) > 0

    # Step 7: Determine grade, result status, and remarks
    grade, result, remarks = determine_grade(average, has_failed)

    # Step 8: Display the formatted report
    display_performance_report(
        student_name=student_name,
        subject_records=subject_records,
        total=total,
        average=average,
        highest=highest,
        lowest=lowest,
        grade=grade,
        result=result,
        remarks=remarks,
        failed_subjects=failed_subjects
    )


def ask_to_continue():
    """
    Asks the user if they want to calculate for another student.
    
    Returns:
        bool: True if user wants to continue, False if user chooses to exit.
    """
    while True:
        choice = input("Do you want to calculate grades for another student? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n", "exit", "quit"]:
            return False
        else:
            print("[Error] Invalid choice. Please enter 'yes' or 'no'.")


def main():
    """
    Main entry point of the Student Grade Calculator application.
    Runs a loop allowing multiple student calculations until user exits.
    """
    display_welcome_banner()

    # Loop to process multiple students
    while True:
        process_single_student()

        # Prompt user to continue or exit
        if not ask_to_continue():
            print("\nThank you for using the Student Grade Calculator!")
            print("Codomax Digital Solutions - Python Internship Project.")
            print("Exiting application. Have a great day!\n")
            break
        print("\n" + "-" * 65 + "\n")


if __name__ == "__main__":
    main()
