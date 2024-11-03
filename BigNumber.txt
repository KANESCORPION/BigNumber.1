def add_large_numbers(num1, num2):
    sign1 = -1 if num1[0] == '-' else 1
    sign2 = -1 if num2[0] == '-' else 1

    num1 = num1.lstrip('-')
    num2 = num2.lstrip('-')

    if sign1 == sign2:
        result = add_positive_numbers(num1, num2)
        return f"{result}" if sign1 == 1 else f"-{result}"
    else:
        if compare_large_numbers(num1, num2) >= 0:
            result = subtract_large_numbers(num1, num2)
            return f"{result}" if sign1 == 1 else f"-{result}"
        else:
            result = subtract_large_numbers(num2, num1)
            return f"-{result}" if sign2 == 1 else f"{result}"

def add_positive_numbers(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    carry = 0
    result = []

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

    return ''.join(result[::-1])

def subtract_large_numbers(num1, num2):
    result = []
    borrow = 0

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

    return ''.join(result[::-1]).lstrip('0') or '0'

def compare_large_numbers(num1, num2):
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
    return num.lstrip('-').isdigit()

if __name__ == "__main__":
    num1 = input("Enter the first large number: ")
    num2 = input("Enter the second large number: ")

    if not is_valid_number(num1) or not is_valid_number(num2):
        print("Please enter valid integers.")
    else:
        addition_result = add_large_numbers(num1, num2)
        print(f"Sum: {addition_result}")

        if num2[0] == '-':
            subtraction_result = add_large_numbers(num1, num2.lstrip('-'))
        else:
            subtraction_result = add_large_numbers(num1, '-' + num2)

        print(f"Difference: {subtraction_result}")

        positions = int(input("Enter the number of positions to shift: "))
        print(f"Left Shift of {num1} by {positions} positions: {left_shift(num1, positions)}")
        print(f"Right Shift of {num1} by {positions} positions: {right_shift(num1, positions)}")
        print(f"Left Shift of {num2} by {positions} positions: {left_shift(num2, positions)}")
        print(f"Right Shift of {num2} by {positions} positions: {right_shift(num2, positions)}")
