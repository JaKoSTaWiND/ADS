data = str(input("Enter non-negative n: "))

def calculate_sum_of_digits(data) -> int:

    result = 0

    for char in data:
        int_char = int(char)

        result += int_char

    print(f"Result: {result}")

    return result

if __name__ == "__main__":
    calculate_sum_of_digits(data=data) 