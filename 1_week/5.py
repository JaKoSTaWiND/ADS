target_number = int(input("Enter number: "))

def calculate_digits_sum(number):
    if number < 10:
        return number
    else:
        return (number % 10) + calculate_digits_sum(number // 10)

if __name__ == "__main__":
    result = calculate_digits_sum(number=target_number)
    print(f"Result: {result}")