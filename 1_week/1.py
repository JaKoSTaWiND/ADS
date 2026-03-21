value = int(input("Enter int number: "))
power = int(input("Enter power fo value: "))

def calculate_power(value, power) -> int:
    result = value ** power
    print(f"Result: {result}")
    return result


if __name__ == "__main__":
    calculate_power(value=value, power=power)