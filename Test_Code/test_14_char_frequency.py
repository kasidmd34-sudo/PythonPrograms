import importlib.util

spec = importlib.util.spec_from_file_location(
    "char_frequency",
    "Code/14_char_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.character_frequency("hello") == {
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}

assert module.character_frequency("aabbc") == {
    "a": 2,
    "b": 2,
    "c": 1
}

assert module.character_frequency("") == {}

assert module.character_frequency("abcabc") == {
    "a": 2,
    "b": 2,
    "c": 2
}

print("All test cases passed.")