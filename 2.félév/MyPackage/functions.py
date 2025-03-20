from .data import special_chars

def print_rectangle(a, b):
    for i in range(a):
        print("# "*b)
        
def is_palindrome(string, exact_characters = True):
    if not exact_characters:
        new_string = ""
        for char in string:
            if char not in special_chars:
                new_string += char
        string = new_string.lower().replace(" ", "")
    
    if len(string) == 1 or len(string) == 0:
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return True and is_palindrome(string[1:-1])