list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.

def reverse_characters(s):
    return s[::-1]

print(reverse_characters(list_test1))


# b) Within the function, use the 'list' function to split a string into a list of individual characters

def reverse_characters(s):
    char_list = list(s) # split string into list of characters
    return char_list        

print(reverse_characters(list_test2)) # can put any test list instead of one word

# c) 'reverse' your new list.

def reverse_characters(s):
    chars = list(s)     # Step 1: convert to list of characters
    reversed_chars = chars[::-1]  # Step 2: reverse the list
    return reversed_chars
print(reverse_characters("apple"))

# d) Use 'join' to create the reversed string and return that string from the function.
def reverse_characters(value): 
    value_type = type(value)   
    if value_type == int or value_type == float:
        value = str(value)      
    characters = list(value)   
    characters.reverse()        
    return value_type(''.join(characters))

print(reverse_characters(list_test1))

# e) Create a variable of type string to test your new function. 
test_str = str(list(list_test3))

# f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
print(reverse_characters(test_str))

# g) Use method chaining to reduce the lines of code within the function.

def reverse_characters(s):
    return ''.join(reversed(list(s)))

print(reverse_characters("Launchcode"))


# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.

def reverse_characters(char):
    if type(char) == int:
        char = str(char)[::-1]
        return int(char)

print(reverse_characters(1234))

# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
def reverse_characters(x):
    if type(x) == str:
        return x[::-1]
    else: 
        type(x) == int
        return int(str(x)[::-1])  # Convert number to string, reverse, then back to int
   
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.
print(reverse_characters('LC101'))



# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.

# Helper function to reverse characters of a string or digits of a number
def reverse_characters(item):
    return str(item)[::-1]

# Main function to process a list
def reverse_list_items(old_list):
    new_list = []  # a) Initialize empty list

    # b) Loop through the old list
    for element in old_list:
        # c) Reverse characters/digits
        reversed_element = reverse_characters(element)
        # d) Add to new list
        new_list.append(reversed_element)

    # e) Return the final list
    return new_list

print("Test list:", reverse_list_items(list_test3))
