text = "Hello"
print(text.isalpha())  # Output: True

text = "12345"
print(text.isdigit())  # Output: True

text = "Python123"
print(text.isalnum())  # Output: True

text = "   "
print(text.isspace())  # Output: True

text = "Hello, World!"
swapped = text.swapcase()
print(swapped)  # Output: "hELLO, wORLD!"

text = "123"
padded = text.zfill(5)
print(padded)  # Output: "00123"

text = "Python"
centered = text.center(10, "-")
print(centered)  # Output: "--Python--"

text = "Python"
print(text.rjust(10, "-"))  # Output: "----Python"
print(text.ljust(10, "-"))  # Output: "Python----"

text = "I love Python"
result = text.partition("love")
print(result)  # Output: ('I ', 'love', ' Python')

text = "I love Python and I love coding"
result = text.rpartition("love")
print(result)  # Output: ('I love Python and I ', 'love', ' coding')

template = "Hello, {}. Welcome to {}!"
message = template.format("Alice", "Python")
print(message)  # Output: "Hello, Alice. Welcome to Python!"
