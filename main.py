def add_large_numbers(num1, num2):
    # Determine the signs of the numbers
    sign1 = -1 if num1[0] == '-' else 1
    sign2 = -1 if num2[0] == '-' else 1

    # Remove the signs for easier processing
    num1 = num1.lstrip('-')
    num2 = num2.lstrip('-')

    if sign1 == sign2:
        # Both numbers are either positive or negative
        result = add_positive_numbers(num1, num2)
        return f"{result}" if sign1 == 1 else f"-{result}"
    else:
        # Different signs, we need to subtract
        if compare_large_numbers(num1, num2) >= 0:
            result = subtract_large_numbers(num1, num2)
            return f"{result}" if sign1 == 1 else f"-{result}"
        else:
            result = subtract_large_numbers(num2, num1)
            return f"-{result}" if sign2 == 1 else f"{result}"


def add_positive_numbers(num1, num2):
    # Ensure num1 is the longer number
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    carry = 0
    result = []

    # Reverse the strings to make addition easier
    num1 = num1[::-1]
    num2 = num2[::-1]

    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0
        total = digit1 + digit2 + carry
        result.append(str(total % 10))
        carry = total // 10

    if carry:
        result.append(str(carry))

    # The result needs to be reversed back
    return ''.join(result[::-1])


def subtract_large_numbers(num1, num2):
    # Assume num1 >= num2 for this implementation
    result = []
    borrow = 0

    # Reverse the strings for easier subtraction
    num1 = num1[::-1]
    num2 = num2[::-1]

    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0

        if digit1 < digit2 + borrow:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0

        result.append(str(digit1 - digit2 - borrow))

    # Remove leading zeros and reverse back
    return ''.join(result[::-1]).lstrip('0') or '0'


def compare_large_numbers(num1, num2):
    # Compare absolute values of two numbers
    if len(num1) > len(num2):
        return 1
    if len(num1) < len(num2):
        return -1
    return (num1 > num2) - (num1 < num2)


def left_shift(num, positions):
    return num + '0' * positions


def right_shift(num, positions):
    return num[:-positions] if len(num) > positions else '0'


def is_valid_number(num):
    return num.lstrip('-').isdigit()  # Check if the input is a valid integer


if __name__ == "__main__":
    # User input for two large numbers
    num1 = input("Enter the first large number: ")
    num2 = input("Enter the second large number: ")

    # Validate input
    if not is_valid_number(num1) or not is_valid_number(num2):
        print("Please enter valid integers.")
    else:
        # Adding the two numbers
        addition_result = add_large_numbers(num1, num2)
        print(f"Sum: {addition_result}")

        # Subtracting the two numbers
        try:
            subtraction_result = add_large_numbers(num1,
                                                   '-' + num2)  # num1 - num2 as add_large_numbers can handle signs
            print(f"Difference: {subtraction_result}")
        except ValueError as e:
            print(e)

        # Left and right shift for both numbers
        positions = int(input("Enter the number of positions to shift: "))

        # Shifting the first number
        print(f"Left Shift of {num1} by {positions} positions: {left_shift(num1, positions)}")
        print(f"Right Shift of {num1} by {positions} positions: {right_shift(num1, positions)}")

        # Shifting the second number
        print(f"Left Shift of {num2} by {positions} positions: {left_shift(num2, positions)}")
        print(f"Right Shift of {num2} by {positions} positions: {right_shift(num2, positions)}")
