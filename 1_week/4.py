value = int(input("Enter value: "))
result = int(input("Enter answer: "))

def calculate_power(value, result) -> int:

    power = 0

    while value ** power < result:
        power += 1
    
    if value ** power == result:
        print("YES")
    else:
        print("NO")

    return power

if __name__ == "__main__":
    calculate_power(value=value, result=result)