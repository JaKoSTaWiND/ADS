value = int(input("Enter integer value: "))

def calculate_to_binary(value) -> int:
    if value == 0:
        print(value)
        return 0
    elif value > 1:
        calculate_to_binary(value=value // 2)

    print(value % 2, end="")

if __name__ == "__main__":
    calculate_to_binary(value=value)