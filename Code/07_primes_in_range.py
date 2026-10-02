def is_prime(number):
  if number < 2:
    return False

  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False

    return True


def primes_in_range(start, end):
  primes = []

  for number in range(start, end + 1):
    if is_prime(number):
      primes.append(number)

    return primes


if __name__ == "__main__":
  start = int(input("Enter start: "))
  end = int(input("Enter end: "))

  print(primes_in_range(start, end))