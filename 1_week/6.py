data = str(input("Enter string: "))

def is_palindrome(data) -> bool:

    if data == data[::-1]:
        print("YES")
        return True
    else:
        print("NO")
        return False
    
if __name__ == "__main__":
    is_palindrome(data=data)