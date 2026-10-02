def factorial(number):
  if number < 0:
    return None

  result = 1

  for i in range(1, number + 1):
    result *= i

  return result


if __name__ == "__main__":
  number = int(input("Enter a number: "))

  result = factorial(number)

  if result is None:
    print("Factorial is not defined for negative numbers.")
  else:
    print("Factorial:", result)