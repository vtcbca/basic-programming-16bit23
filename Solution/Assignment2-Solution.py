def is_prime_basic(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(f"{num} is {'a prime' if is_prime_basic(num) else 'not a prime'} number.")
