import time
import sys


sys.set_int_max_str_digits(100000)



def strip_leading_zeros(s):
    return s.lstrip('0') or '0'



def normal_multiply(a, b):
    try:

        result = str(int(a) * int(b))
        return result
    except ValueError as e:
        return f"Error in normal multiplication: {str(e)}"



def karatsuba(x, y):

    x = strip_leading_zeros(x)
    y = strip_leading_zeros(y)


    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))


    n = max(len(x), len(y))
    m = n // 2


    x1, x0 = x[:-m], x[-m:]
    y1, y0 = y[:-m], y[-m:]


    if not x1:
        x1 = '0'
    if not y1:
        y1 = '0'


    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(str(int(x1) + int(x0)), str(int(y1) + int(y0)))
    z1 = str(int(z1) - int(z2) - int(z0))


    result = str(int(z2) * 10 ** (2 * m) + int(z1) * 10 ** m + int(z0))

    return result



def big_exponentiation(base, exp):
    result = 1
    for _ in range(exp):
        result *= int(base)
    return str(result)



def big_divide(dividend, divisor):

    dividend = strip_leading_zeros(dividend)
    divisor = strip_leading_zeros(divisor)

    if int(divisor) == 0:
        return "Division by zero error"


    quotient, remainder = divmod(int(dividend), int(divisor))


    if (dividend[0] == '-' and divisor[0] != '-') or (dividend[0] != '-' and divisor[0] == '-'):
        quotient = -quotient


    result = (f"Division formula: ({dividend}) = ({divisor}) * ({quotient}) + ({remainder})\n"
              f"Dividend: {dividend}\n"
              f"Divisor: {divisor}\n"
              f"Quotient: {quotient}\n"
              f"Remainder: {remainder}")

    return result



def big_factorial(n):
    if n < 1 or n > 100:
        return "Error: Number must be between 1 and 100"

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return str(factorial)



class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0.0

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time is not None:
            self.elapsed_time = time.perf_counter() - self.start_time
            self.start_time = None

    def get_elapsed(self):
        return self.elapsed_time



def main():

    print("Enter two large numbers for multiplication:")
    a = input("Enter first number (can be negative): ").strip()
    b = input("Enter second number (can be negative): ").strip()


    is_negative_a = a[0] == '-'
    is_negative_b = b[0] == '-'

    if is_negative_a:
        a = a[1:]
    if is_negative_b:
        b = b[1:]


    stopwatch = Stopwatch()


    stopwatch.start()
    normal_result = normal_multiply(a, b)
    stopwatch.stop()
    if is_negative_a != is_negative_b:
        normal_result = '-' + normal_result
    print(f"Normal multiplication result: {normal_result}")
    print(f"Time taken for normal multiplication: {stopwatch.get_elapsed():.15f} seconds")


    stopwatch.start()
    karatsuba_result = karatsuba(a, b)
    stopwatch.stop()
    if is_negative_a != is_negative_b:
        karatsuba_result = '-' + karatsuba_result
    print(f"Karatsuba multiplication result: {karatsuba_result}")
    print(f"Time taken for Karatsuba multiplication: {stopwatch.get_elapsed():.15f} seconds")


    print("\nEnter a base number for exponentiation:")
    base = input().strip()
    print("Enter an exponent:")
    exp = int(input().strip())

    stopwatch.start()
    exponentiation_result = big_exponentiation(base, exp)
    stopwatch.stop()
    print(f"Exponentiation result: {exponentiation_result}")


    if stopwatch.get_elapsed() > 1e-12:
        print(f"Time taken for exponentiation: {stopwatch.get_elapsed():.15f} seconds")

    # Division
    print("\nEnter two numbers for division:")
    dividend = input("Enter the dividend: ").strip()
    divisor = input("Enter the divisor: ").strip()

    stopwatch.start()
    division_result = big_divide(dividend, divisor)
    stopwatch.stop()
    print(division_result)


    if stopwatch.get_elapsed() > 1e-12:
        print(f"Time taken for division: {stopwatch.get_elapsed():.15f} seconds")


    print("\nEnter a number for factorial calculation (between 1 and 100): ")
    n = int(input().strip())

    stopwatch.start()
    factorial_result = big_factorial(n)
    stopwatch.stop()
    print(f"Factorial result: {factorial_result}")


    if stopwatch.get_elapsed() > 1e-12:
        print(f"Time taken for factorial: {stopwatch.get_elapsed():.15f} seconds")


if __name__ == "__main__":
    main()
