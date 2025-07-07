"""
DATA TYPES / OBJECT TYPES

1: Number(int,float)
2: String
3: Boolean
4: List
5: Tuple
6: Dictionary
7: None
"""
                                #Number
a=int(5)        #integer
b=float(2.5)    #float
c=complex(1j)   #complex
sum = a+b+c
print(sum)          #output: 7.5+1j
print(type(sum))    #To check type of any object in python
                    #print(type(sum)) \\output: complex
                    
                    
                                # Original string
                                
text = "   hello World! Welcome to Python 123.   "

# Case Conversion Methods

# Converts first character to uppercase, rest to lowercase
print("1.", text.capitalize())
# Converts entire string to lowercase (more aggressive than lower())
print("2.", text.casefold())
print("3.", text.lower())          # Converts string to lowercase
print("4.", text.upper())          # Converts string to uppercase
# Swaps uppercase to lowercase and vice versa
print("5.", text.swapcase())
print("6.", text.title())          # Capitalizes the first letter of each word

#Check Methods

# Checks if all characters are alphanumeric (letters or digits)
print("7.", text.strip().isalnum())
# Checks if all characters are alphabetic
print("8.", "Python".isalpha())
# Checks if all characters are decimals
print("9.", "123".isdecimal())
print("10.", "123".isdigit())             # Checks if all characters are digits
# Checks if all characters are numeric (including other digit systems)
print("11.", "١٢٣".isnumeric())
# Checks if it's a valid Python identifier
print("12.", "var_1".isidentifier())
print("13.", text.isascii())              # Checks if all characters are ASCII
# Checks if all characters are lowercase
print("14.", "hello".islower())
# Checks if all characters are uppercase
print("15.", "HELLO".isupper())
print("16.", "Hello World".istitle())     # Checks if it follows title case
# Checks if the string contains only whitespace
print("17.", "     ".isspace())
# Checks if all characters are printable
print("18.", "Visible!".isprintable())

# Trimming and Padding

print("19.", text.strip())                # Removes spaces from both ends
print("20.", text.lstrip())               # Removes spaces from the left side
print("21.", text.rstrip())               # Removes spaces from the right side
# Centers the string with '-' padding
print("22.", text.strip().center(40, "-"))
# Left-justifies string with '.' padding
print("23.", text.strip().ljust(30, "."))
# Right-justifies string with '.' padding
print("24.", text.strip().rjust(30, "."))
# Pads string with zeros on the left to make length 5
print("25.", "42".zfill(5))

# Search and Count

print("26.", text.count("o"))             # Counts how many times 'o' appears
# Finds the first occurrence of "Python"
print("27.", text.find("Python"))
print("28.", text.rfind("o"))             # Finds the last occurrence of 'o'
# Returns the index of "World", error if not found
print("29.", text.index("World"))
# Returns the last index of 'o', error if not found
print("30.", text.rindex("o"))
# Checks if the string starts with "   hello"
print("31.", text.startswith("   hello"))
# Checks if the string ends with "123.   "
print("32.", text.endswith("123.   "))

# Split and Join

# Splits string by whitespace into a list
print("33.", text.strip().split())
print("34.", "name,age,city".split(","))        # Splits string by comma
print("35.", "-".join(["Python", "is", "fun"]))  # Joins list elements with "-"
# Splits string at line breaks
print("36.", "Line1\nLine2\nLine3".splitlines())
# Splits string into 3 parts at first "-"
print("37.", "Python-is-fun".partition("-"))
# Splits string into 3 parts at last "-"
print("38.", "Python-is-fun".rpartition("-"))
print("39.", "one-two-three".rsplit("-", 1))    # Splits from the right once

# Replace and Format

# Replaces "Python" with "Programming"
print("40.", text.replace("Python", "Programming"))
# Inserts values into placeholders
print("41.", "Hello {}, welcome to {}.".format("Ali", "Python"))
print("42.", "Hello {name}, welcome to {lang}.".format_map(
    {"name": "Sara", "lang": "Java"}))  # Uses dict for formatting

# Encoding and Translation

# Encodes string into bytes using UTF-8
encoded = "hello".encode("utf-8")
print("43.", encoded)

trans = str.maketrans("aeiou", "12345")      # Creates a translation map
# Translates characters using the map
print("44.", "hello world".translate(trans))

# Expand Tabs

# Replaces tab characters with spaces (tab size = 4)
print("45.", "Python\tis\tfun".expandtabs(4))


                                #boolean
                                
x = int(2)
y = float(3.5)
print(y>x)          #True
print(x==y)         #False

                                
                                #list
                                 
my_list = [10, 20, 30, 40]

# 1. append() – Adds an element to the end of the list
my_list.append(50)
print("1. append():", my_list)  # [10, 20, 30, 40, 50]

# 2. clear() – Removes all elements from the list
cleared_list = my_list.copy()   # We'll clear a copy to preserve original
cleared_list.clear()
print("2. clear():", cleared_list)  # []

# 3. copy() – Returns a shallow copy of the list
copied_list = my_list.copy()
print("3. copy():", copied_list)  # [10, 20, 30, 40, 50]

# 4. count() – Returns how many times a value occurs
sample_list = [1, 2, 2, 3, 2, 4]
print("4. count():", sample_list.count(2))  # 3

# 5. extend() – Adds multiple elements (from iterable) to the end
my_list.extend([60, 70])
print("5. extend():", my_list)  # [10, 20, 30, 40, 50, 60, 70]

# 6. index() – Returns index of the first occurrence of a value
print("6. index():", my_list.index(30))  # 2

# 7. insert() – Inserts an element at a specific position
my_list.insert(2, 25)  # Insert 25 at index 2
print("7. insert():", my_list)  # [10, 20, 25, 30, 40, 50, 60, 70]

# 8. pop() – Removes and returns item at the given position (default: last)
removed_item = my_list.pop()
print("8. pop():", removed_item)         # 70
print("   List after pop():", my_list)   # [10, 20, 25, 30, 40, 50, 60]

# 9. remove() – Removes the first matching value
my_list.remove(25)
print("9. remove():", my_list)  # [10, 20, 30, 40, 50, 60]

# 10. reverse() – Reverses the order of the list
my_list.reverse()
print("10. reverse():", my_list)  # [60, 50, 40, 30, 20, 10]

# 11. sort() – Sorts the list in ascending order (default)
my_list.sort()
print("11. sort():", my_list)  # [10, 20, 30, 40, 50, 60]

                                #Tuple
my_tuple = (1,2,3,2,4,2)
#1. count() - Counts hoe many times a value appears in the tuple
count2 = my_tuple.count(2)
print("1. count():", count2)    #output: 3
#2. index() - Returns the first index of the given value
index3 = my_tuple.index(3)
print("2. index():", index3)    #output: 2


                                #Initial dictionary
                                
my_dict = {"name": "Hussain", "age": 25, "city": "Kotli"}

# 1. clear() – Removes all elements from the dictionary
temp_dict = my_dict.copy()     # We'll clear a copy to preserve original
temp_dict.clear()
print("1. clear():", temp_dict)  # {}

# 2. copy() – Returns a shallow copy of the dictionary
copy_dict = my_dict.copy()
print("2. copy():", copy_dict)   # {'name': 'Hussain', 'age': 25, 'city': 'Kotli'}

# 3. fromkeys() – Creates a dictionary with given keys and one value
keys = ("a", "b", "c")
new_dict = dict.fromkeys(keys, 0)
print("3. fromkeys():", new_dict)  # {'a': 0, 'b': 0, 'c': 0}

# 4. get() – Returns the value of a key (returns None if key not found)
print("4. get():", my_dict.get("age"))        # 25
print("   get() with missing key:", my_dict.get("gender"))  # None

# 5. items() – Returns all key-value pairs as a list of tuples
print("5. items():", list(my_dict.items()))   # [('name', 'Hussain'), ('age', 25), ('city', 'Kotli')]

# 6. keys() – Returns all keys in the dictionary
print("6. keys():", list(my_dict.keys()))     # ['name', 'age', 'city']

# 7. pop() – Removes the item with the specified key
popped_value = my_dict.pop("city")
print("7. pop():", popped_value)              # 'Kotli'
print("   Dictionary after pop():", my_dict)  # {'name': 'Hussain', 'age': 25}

# 8. popitem() – Removes and returns the last inserted key-value pair
last_item = my_dict.popitem()
print("8. popitem():", last_item)             # ('age', 25)
print("   Dictionary after popitem():", my_dict)  # {'name': 'Hussain'}

# 9. setdefault() – Returns the value if key exists; otherwise adds the key with a default value
value = my_dict.setdefault("gender", "male")
print("9. setdefault():", value)              # 'male'
print("   Dictionary after setdefault():", my_dict)  # {'name': 'Hussain', 'gender': 'male'}

# 10. update() – Updates dictionary with new key-value pairs (or overrides existing keys)
my_dict.update({"age": 30, "country": "pakistan"})
print("10. update():", my_dict)               # {'name': 'Hussain', 'gender': 'male', 'age': 30, 'country': 'pakistan'}

# 11. values() – Returns all values in the dictionary
print("11. values():", list(my_dict.values()))  # ['Hussain', 'male', 30, 'pakistan']

                                    #None
x = None
print(type(x))      #output: NoneType
#None is not the same as 0, False, or "" it has its own type called NoneType
print(None == False)     # False
print(None == 0)         # False
print(None == "")        # False