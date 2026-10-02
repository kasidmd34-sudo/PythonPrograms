import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_number",
    "Code/09_palindrome_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome(121) is True
assert module.is_palindrome(1221) is True
assert module.is_palindrome(123) is False
assert module.is_palindrome(10) is False
assert module.is_palindrome(0) is True
assert module.is_palindrome(-121) is False

print("All test cases passed.")