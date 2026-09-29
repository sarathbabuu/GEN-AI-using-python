def calculate_grade(mark):
    """Convert a mark into a letter grade."""
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    else:
        return "E"


def main():
    print("Grade System")
    print("-" * 20)

    try:
        mark = float(input("Enter your mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100.")
            return

        grade = calculate_grade(mark)

        print(f"Entered mark: {mark:g}")
        print(f"Grade: {grade}")

    except ValueError:
        print("Error: Please enter a valid number.")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ended safely.")


if __name__ == "__main__":
    main()
