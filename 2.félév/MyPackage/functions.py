def print_rectangle(a, b):
    for i in range(a):
        print("# "*b)
        
def is_palindrome(string):
    if len(string) == 1 or len(string) == 0:
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return True and is_palindrome(string[1:-1])