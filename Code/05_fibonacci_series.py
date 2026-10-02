def fibonacci(n):
  series = []

  a = 0
  b = 1

  for _ in range(n):
    series.append(a)
    a, b = b, a + b

  return series


if __name__ == "__main__":
  n = int(input("Enter number of terms: "))

  if n < 0:
    print("Enter a non-negative number.")
  else:
    print(fibonacci(n))