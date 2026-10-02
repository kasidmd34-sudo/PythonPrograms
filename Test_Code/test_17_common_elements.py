import importlib.util

spec = importlib.util.spec_from_file_location(
    "remove_duplicates",
    "Code/16_remove_duplicates.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]
assert module.remove_duplicates([1, 1, 1]) == [1]
assert module.remove_duplicates([]) == []
assert module.remove_duplicates([5, 4, 5, 4, 3]) == [5, 4, 3]

print("All test cases passed.")