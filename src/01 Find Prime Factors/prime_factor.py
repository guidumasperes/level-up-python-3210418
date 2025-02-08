def prime_factor(number):
  prime_number = 2
  prime_factors = []
  while number > 1:
    if number % prime_number == 0:
      number //= prime_number
      prime_factors.append(prime_number)
    else:
      prime_number += 1
      while True:
        for i in range(2,prime_number+1):
          if prime_number % i == 0:
            break
        if prime_number > i:
          prime_number += 1
        else:
          break
  return prime_factors

if __name__ == '__main__':
  print(prime_factor(13))
  print(prime_factor(630))
  print(prime_factor(220))