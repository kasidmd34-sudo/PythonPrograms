def find_missing_number(numbers):
  n = len(numbers) + 1

  expected_sum = n * (n + 1) // 2
  actual_sum = sum(numbers)

  return expected_sum - actual_sum


if __name__ == "__main__":
  numbers = list(map(int, input("Enter numbers: ").split()))

  print("Missing number:", find_missing_number(numbers))