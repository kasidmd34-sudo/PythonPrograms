import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_string",
    "Code/13_palindrome_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_string("madam") is True
assert module.is_palindrome_string("level") is True
assert module.is_palindrome_string("hello") is False
assert module.is_palindrome_string("Racecar") is True
assert module.is_palindrome_string("") is True

print("All test cases passed.")