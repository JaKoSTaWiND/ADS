decimal_number = int(input("Enter decimal number: "))

def convert_to_binary(number):
    
    return convert_to_binary(number // 2) + str(number % 2)

if __name__ == "__main__":
    if decimal_number == 0:
        result = "0"
    else:
        result = convert_to_binary(number=decimal_number)
        
    print(f"Result: {result}")