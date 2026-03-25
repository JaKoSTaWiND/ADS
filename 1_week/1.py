value = int(input("Enter value: "))
power = int(input("Enter power: "))


def calculate_power(value, power):
    if power == 0:
        return 1
    elif power % 2 == 0:
        return calculate_power(value, power // 2) * calculate_power(value, power // 2)
    else:
        return calculate_power(value, (power - 1) // 2) * calculate_power(value, (power - 1) // 2) * value   

if __name__ == "__main__":

    result = calculate_power(value=value, power=power)

    print(f"Result: {result}") 