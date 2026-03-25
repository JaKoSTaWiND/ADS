first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

def find_greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return find_greatest_common_divisor(b, a % b)

if __name__ == "__main__":
    result = find_greatest_common_divisor(a=first_number, b=second_number)
    print(f"Result: {result}")