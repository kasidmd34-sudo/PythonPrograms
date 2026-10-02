import importlib.util

spec = importlib.util.spec_from_file_location(
    "even_odd",
    "Code/01_even_odd.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_even_odd(10) == "Even"
assert module.check_even_odd(7) == "Odd"
assert module.check_even_odd(0) == "Even"
assert module.check_even_odd(-5) == "Odd"

print("All test cases passed.")