input_string = input("Enter string: ")

def check_if_is_palindrome(text, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(text) - 1
    
    if left_index >= right_index:
        return "YES"
    
    if text[left_index] != text[right_index]:
        return "NO"
    
    return check_if_is_palindrome(text, left_index + 1, right_index - 1)

if __name__ == "__main__":
    result = check_if_is_palindrome(text=input_string)
    print(f"Result: {result}")