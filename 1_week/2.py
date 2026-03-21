first_value = int(input("Enter first value: "))
second_value = int(input("Enter second value: "))

def calculate_gcd(first_value, second_value) -> int:

    if first_value > second_value or first_value == second_value:
        min_value = second_value
    else:
        min_value = first_value

    print(f"Min value: {min_value}")
    
    gcd = 1

    for i in range(2, min_value + 1):
        if first_value % i == 0 and second_value % i == 0:
            gcd = i
    
    print(f"GCD: {gcd}")
    return gcd

if __name__ == "__main__":
    calculate_gcd(first_value=first_value, second_value=second_value)
