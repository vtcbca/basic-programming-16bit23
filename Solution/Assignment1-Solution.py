def factorial_for_loop(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

num = int(input("Enter a number: "))
print(f"Factorial using for loop: {factorial_for_loop(num)}")
