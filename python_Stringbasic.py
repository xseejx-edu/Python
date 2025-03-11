# Basics of Python with Strings and Dictionaries

# Strings
print("=== Strings ===")
# Creating a string
my_string = "Hello, World!"
print("Original String:", my_string)

# String length
print("Length of String:", len(my_string))

# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print("Concatenated String:", full_greeting)

# String methods
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Stripped:", "   Hello   ".strip())
print("Replaced:", my_string.replace("World", "Python"))
print("Split:", my_string.split(", "))

# Dictionaries
print("\n=== Dictionaries ===")
# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Original Dictionary:", my_dict)

# Accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"
print("Updated Dictionary:", my_dict)

# Updating a value
my_dict["age"] = 31
print("Updated Age:", my_dict)

# Removing a key-value pair
del my_dict["city"]
print("Dictionary after Deletion:", my_dict)

# Looping through a dictionary
print("\nLooping through Dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)

# Checking if a key exists
if "name" in my_dict:
    print("\nKey 'name' exists in the dictionary")

# Dictionary length
print("Length of Dictionary:", len(my_dict))






# Strings

print("\n=== More String Operations ===")

# String slicing
substring = my_string[0:5]  # Extract substring from index 0 to 4
print("Substring (0:5):", substring)

# Check if a string contains a substring
contains = "World" in my_string
print("Contains 'World':", contains)

# String formatting (using f-strings)
age = 30
greeting_message = f"Hello, my name is {my_dict['name']} and I am {age} years old."
print("Formatted String:", greeting_message)

# String with multiple lines (multiline strings)
multiline_string = """This is line 1.
This is line 2.
This is line 3."""
print("Multiline String:")
print(multiline_string)

# Count occurrences of a substring
occurrences = my_string.count("o")
print("Occurrences of 'o':", occurrences)

# Find the index of a substring
index = my_string.find("World")
print("Index of 'World':", index)

# String join (joining a list of strings with a separator)
words = ["Hello", "World"]
joined_string = " ".join(words)
print("Joined String:", joined_string)

# Checking if a string starts or ends with a substring
starts_with_hello = my_string.startswith("Hello")
ends_with_world = my_string.endswith("World!")
print("Starts with 'Hello':", starts_with_hello)
print("Ends with 'World!':", ends_with_world)


# Dictionaries

print("\n=== More Dictionary Operations ===")

# Dictionary with mixed data types
mixed_dict = {
    "name": "Bob",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science"]
}
print("Mixed Dictionary:", mixed_dict)

# Accessing a value with get() method (safe way)
email = my_dict.get("email", "Email not found")
print("Email:", email)

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()
print("Keys:", keys)
print("Values:", values)

# Copying a dictionary
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

# Merging dictionaries (Python 3.9+)
another_dict = {"gender": "female", "country": "USA"}
merged_dict = my_dict | another_dict  # merge using pipe operator
print("Merged Dictionary:", merged_dict)

# Dictionary comprehension (creating a new dictionary)
squared_numbers = {x: x**2 for x in range(5)}
print("Squared Numbers Dictionary:", squared_numbers)

# Nested dictionaries
nested_dict = {
    "user1": {"name": "John", "age": 28},
    "user2": {"name": "Sarah", "age": 25}
}
print("Nested Dictionary:", nested_dict)

# Accessing nested dictionary
user1_name = nested_dict["user1"]["name"]
print("User1's Name:", user1_name)

# Using pop() to remove a key-value pair and return the value
popped_value = my_dict.pop("age", "Key not found")
print("Popped Value:", popped_value)
print("Dictionary after pop:", my_dict)

# Using popitem() to remove and return the last inserted key-value pair
last_item = my_dict.popitem()
print("Last Popped Item:", last_item)
print("Dictionary after popitem:", my_dict)

# Clear the dictionary (removes all items)
my_dict.clear()
print("Dictionary after clear:", my_dict)



# More String Methods
print("\n=== Additional String Methods ===")

# Check if string is alphanumeric
is_alphanumeric = "hello123".isalnum()
print("Is 'hello123' alphanumeric?", is_alphanumeric)

# Check if string is digit
is_digit = "12345".isdigit()
print("Is '12345' a digit?", is_digit)

# Check if string is upper or lower case
is_upper = "HELLO".isupper()
is_lower = "hello".islower()
print("Is 'HELLO' upper case?", is_upper)
print("Is 'hello' lower case?", is_lower)

# Checking if a string contains only spaces
is_space = "   ".isspace()
print("Is '   ' a space string?", is_space)

# Checking if a string is a valid identifier
is_identifier = "my_var".isidentifier()
print("Is 'my_var' a valid identifier?", is_identifier)

# Removing characters from the left (lstrip) or right (rstrip)
stripped_left = "   Hello".lstrip()
stripped_right = "Hello   ".rstrip()
print("Stripped Left:", stripped_left)
print("Stripped Right:", stripped_right)




# More Dictionary Operations

print("\n=== More Dictionary Operations ===")

# Using setdefault() to return the value of a key, and if the key doesn't exist, add the key with the provided default value
default_value = my_dict.setdefault("email", "default@example.com")
print("Email with setdefault:", default_value)

# Using update() to merge two dictionaries
my_dict.update({"city": "Los Angeles", "email": "alice_new@example.com"})
print("Dictionary after update:", my_dict)

# Checking if a value exists in the dictionary
has_value = 31 in my_dict.values()
print("Does the dictionary contain the value 31?", has_value)

# Creating a dictionary from two lists (keys and values)
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
dict_from_lists = dict(zip(keys, values))
print("Dictionary from two lists:", dict_from_lists)

# Dictionary comprehension with condition (filtering)
filtered_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("Filtered Dictionary with only string values:", filtered_dict)
