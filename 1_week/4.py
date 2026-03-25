target_number = int(input("Enter number to check: "))
base = int(input("Enter potential base: "))

def check_if_is_power(target, b):
    if target == 1:
        return "YES"
    if target == b:
        return "YES"
    if b <= 1 or target % b != 0:
        return "NO"
    
    return check_if_is_power(target // b, b)

if __name__ == "__main__":
    result = check_if_is_power(target=target_number, b=base)
    print(f"Result: {result}")