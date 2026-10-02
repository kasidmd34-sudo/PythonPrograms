import importlib.util

spec = importlib.util.spec_from_file_location(
    "word_frequency",
    "Code/20_word_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}

assert module.word_frequency("python is easy python") == {
    "python": 2,
    "is": 1,
    "easy": 1
}

assert module.word_frequency("") == {}

assert module.word_frequency("Python Python PYTHON") == {
    "python": 3
}

print("All test cases passed.")