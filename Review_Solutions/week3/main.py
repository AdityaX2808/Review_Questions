user_input = input("Enter the string:")
def first_non_recurring_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

result = first_non_recurring_char(user_input)
print(result)

