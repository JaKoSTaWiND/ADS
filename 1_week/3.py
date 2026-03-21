k_value = int(input("Enter K value: "))
n_value = int(input("Enter N value: "))

def count_routes(k_value, n_value) -> int:
    if n_value == 0:
        return 1
    
    if n_value < 0:
        return 0
    
    total_routes = 0
    
    for i in range(1, k_value + 1):
        total_routes += count_routes(k_value, n_value - i)

    return total_routes

if __name__ == "__main__":
    result = count_routes(k_value=k_value, n_value=n_value)
    print(f"Total routes: {result}")