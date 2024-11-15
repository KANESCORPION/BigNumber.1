import time
import sys

# Set the maximum number of digits allowed for int conversion (increase limit)
sys.set_int_max_str_digits(100000)  # Increase to a value large enough to handle your numbers


# Utility function to strip leading zeros from numbers
def strip_leading_zeros(s):
    return s.lstrip('0') or '0'


# Normal multiplication for large numbers
def normal_multiply(a, b):
    try:
        # Convert string numbers to integers and multiply
        result = str(int(a) * int(b))  # Multiplying large numbers
        return result
    except ValueError as e:
        return f"Error in normal multiplication: {str(e)}"


# Karatsuba multiplication for large numbers
def karatsuba(x, y):
    # Remove leading zeros from x and y to prevent issues with recursion
    x = strip_leading_zeros(x)
    y = strip_leading_zeros(y)

    # Base case: when either number has only one digit
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))

    # Ensure both numbers have equal length (pad with leading zeros if necessary)
    n = max(len(x), len(y))
    m = n // 2

    # Split the numbers into two halves
    x1, x0 = x[:-m], x[-m:]
    y1, y0 = y[:-m], y[-m:]

    # If x1 or y1 are empty, treat them as '0'
    if not x1:
        x1 = '0'
    if not y1:
        y1 = '0'

    # Recursively calculate three products
    z2 = karatsuba(x1, y1)  # Multiply the high parts
    z0 = karatsuba(x0, y0)  # Multiply the low parts
    z1 = karatsuba(str(int(x1) + int(x0)), str(int(y1) + int(y0)))  # (x1 + x0) * (y1 + y0)

    z1 = str(int(z1) - int(z2) - int(z0))

    # Combine the results using Karatsuba's formula
    result = str(int(z2) * 10 ** (2 * m) + int(z1) * 10 ** m + int(z0))

    return result


# Function for exponentiation (a raised to the power b)
def big_exponentiation(base, exp):
    result = 1
    for _ in range(exp):
        result *= int(base)
    return str(result)


# Function to divide two large numbers
def big_divide(dividend, divisor):
    # Remove leading zeros from the numbers
    dividend = strip_leading_zeros(dividend)
    divisor = strip_leading_zeros(divisor)

    if int(divisor) == 0:
        return "Division by zero error"

    # Perform division and round the result to 6 decimal places
    result = int(dividend) / int(divisor)
    return f"{result:.6f}"


# Function to compute factorial of a number
def big_factorial(n):
    if n < 1 or n > 100:
        return "Error: Number must be between 1 and 100"

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return str(factorial)


# Stopwatch for time tracking
class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0.0

    def start(self):
        self.start_time = time.perf_counter()  # Use perf_counter for high resolution timing

    def stop(self):
        if self.start_time is not None:
            self.elapsed_time = time.perf_counter() - self.start_time  # Stop the timer
            self.start_time = None

    def get_elapsed(self):
        return self.elapsed_time


# Main function to test the multiplication and log the time
def main():
    # Input from user for multiplication
    print("Enter two large numbers for multiplication:")
    a = input("Enter first number (can be negative): ").strip()
    b = input("Enter second number (can be negative): ").strip()

    # Check if numbers are negative
    is_negative_a = a[0] == '-'
    is_negative_b = b[0] == '-'

    if is_negative_a:
        a = a[1:]
    if is_negative_b:
        b = b[1:]

    # Create a stopwatch to track the time for multiplication
    stopwatch = Stopwatch()

    # Timing normal multiplication
    stopwatch.start()
    normal_result = normal_multiply(a, b)
    stopwatch.stop()
    if is_negative_a != is_negative_b:
        normal_result = '-' + normal_result
    print(f"Normal multiplication result: {normal_result}")
    print(f"Time taken for normal multiplication: {stopwatch.get_elapsed():.15f} seconds")

    # Timing Karatsuba multiplication
    stopwatch.start()
    karatsuba_result = karatsuba(a, b)
    stopwatch.stop()
    if is_negative_a != is_negative_b:
        karatsuba_result = '-' + karatsuba_result
    print(f"Karatsuba multiplication result: {karatsuba_result}")
    print(f"Time taken for Karatsuba multiplication: {stopwatch.get_elapsed():.15f} seconds")

    # Exponentiation
    print("\nEnter a base number for exponentiation:")
    base = input().strip()
    print("Enter an exponent:")
    exp = int(input().strip())

    stopwatch.start()
    exponentiation_result = big_exponentiation(base, exp)
    stopwatch.stop()
    print(f"Exponentiation result: {exponentiation_result}")

    # Only show time if it exceeds a small threshold (e.g., 0.000000000001)
    if stopwatch.get_elapsed() > 1e-12:
        print(f"Time taken for exponentiation: {stopwatch.get_elapsed():.15f} seconds")

    # Division
    print("\nEnter two numbers for division:")
    dividend = input("Enter the dividend: ").strip()
    divisor = input("Enter the divisor: ").strip()

    stopwatch.start()
    division_result = big_divide(dividend, divisor)
    stopwatch.stop()
    print(f"Division result: {division_result}")

    # Only show time if it exceeds a small threshold (e.g., 0.000000000001)
    if stopwatch.get_elapsed() > 1e-12:
        print(f"Time taken for division: {stopwatch.get_elapsed():.15f} seconds")

    # Factorial
    print("\nEnter a number for factorial calculation (between 1 and 100): ")
    n = int(input().strip())

    stopwatch.start()
    factorial_result = big_factorial(n)
    stopwatch.stop()
    print(f"Factorial result: {factorial_result}")

    # Only show time if it exceeds a small threshold (e.g., 0.000000000001)
    if stopwatch.get_elapsed() > 1e-12:
        print(f"Time taken for factorial: {stopwatch.get_elapsed():.15f} seconds")


if __name__ == "__main__":
    main()
