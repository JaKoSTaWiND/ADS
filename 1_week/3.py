stair_count = int(input("Enter number of stairs: "))
max_jump = int(input("Enter maximum jump distance: "))

def count_climbing_ways(stairs, jump_limit):
    if stairs == 0:
        return 1
    if stairs < 0:
        return 0
    
    total_ways = 0
    for step in range(1, jump_limit + 1):
        total_ways += count_climbing_ways(stairs - step, jump_limit)
        
    return total_ways

if __name__ == "__main__":
    result = count_climbing_ways(stairs=stair_count, jump_limit=max_jump)
    print(f"Result: {result}")