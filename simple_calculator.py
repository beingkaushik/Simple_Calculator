"""
Production-Ready CLI Calculator
--------------------------------
Features:
- Handles invalid numeric input
- Handles division by zero
- Handles unexpected runtime errors
- Continuous loop until user exits
- Clean OOP structure
- Logging support
"""

import logging
from typing import Callable


# Configure logging (production style)
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Calculator:
    """A simple calculator class with safe operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b


def get_number(prompt: str) -> float:
    """Safely get a numeric input from user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            logging.warning("Invalid numeric input entered.")
            print("❌ Invalid input! Please enter a valid number.")


def main():
    calculator = Calculator()

    operations: dict[str, Callable[[float, float], float]] = {
        "1": calculator.add,
        "2": calculator.subtract,
        "3": calculator.multiply,
        "4": calculator.divide
    }

    while True:
        try:
            print("\n===== Simple Calculator =====")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "5":
                print("👋 Exiting calculator. Goodbye!")
                logging.info("Calculator exited successfully.")
                break

            if choice not in operations:
                logging.warning("Invalid menu choice selected.")
                print("❌ Invalid choice! Please select a valid option.")
                continue

            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            result = operations[choice](num1, num2)

            print(f"✅ Result: {result}")
            logging.info(f"Operation successful: {num1}, {num2}, choice={choice}")

        except ZeroDivisionError as zde:
            logging.error(str(zde))
            print(f"❌ Error: {zde}")

        except KeyboardInterrupt:
            print("\n👋 Program interrupted by user. Exiting safely.")
            logging.info("Program interrupted by user.")
            break

        except Exception as e:
            logging.exception("Unexpected error occurred.")
            print("❌ An unexpected error occurred. Please try again.")


if __name__ == "__main__":
    main()
3