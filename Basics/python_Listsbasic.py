# Example of how to use lists in Python

# Creating a list
my_list = [1, 2, 3, 4, 5]
'''
my_list=[0.]*n
-- "n" will be the  number of items that I'll have and "0." will be the type of "my_list"
'''

# Printing the list
print("Original list:", my_list)

# Accessing elements by index
first_element = my_list[0]
last_element = my_list[-1]
print("First element:", first_element)
print("Last element:", last_element)

# Slicing the list
sub_list = my_list[1:4]  # Elements from index 1 to 3 (4 is excluded)
print("Sliced list (from index 1 to 3):", sub_list)

# Adding elements to the list
my_list.append(6)  # Adds 6 at the end
print("List after append:", my_list)

my_list.insert(2, 10)  # Adds 10 at index 2
print("List after insert:", my_list)

# Removing elements from the list
my_list.remove(3)  # Removes the first occurrence of 3
print("List after remove:", my_list)

popped_element = my_list.pop()  # Removes the last element and returns it
print("Popped element:", popped_element)
print("List after pop:", my_list)

# List comprehension
squared_list = [x**2 for x in my_list]
print("Squared list (list comprehension):", squared_list)

# Checking if an element is in the list
contains_five = 5 in my_list
print("Does the list contain 5?", contains_five)

# Sorting the list
my_list.sort()  # Sorts the list in ascending order
print("Sorted list:", my_list)

# Reversing the list
my_list.reverse()  # Reverses the list in place
print("Reversed list:", my_list)

# Nested list (list of lists)
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)

# Accessing elements from the nested list
element_from_nested = nested_list[1][1]  # Accesses element 4
print("Element from nested list:", element_from_nested)

# Length of the list
list_length = len(my_list)
print("Length of the list:", list_length)

# Iterating through the list
print("Iterating through the list:")
for item in my_list:
    print(item)

# Clear the entire list
my_list.clear()
print("List after clear:", my_list)




'''
[expression for item in iterable]

1. expression: The operation you want to perform on each item.
2. item: The current element being processed.
3. iterable: The list (or any iterable object) you're going through.

-- [x for x in numbers if x % 2 == 0] --

'''

words = ["apple", "banana", "cherry", "date"]

# Create a list of the lengths of the words, but only if the word has more than 5 letters
word_lengths = [len(word) for word in words if len(word) > 5]
print(word_lengths)