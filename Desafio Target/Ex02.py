def fibonacci(n):
    a, b = 0, 1

    if n == 0 or n == 1:
        return (f"O número {n} pertence à sequência de Fibonacci.")
    
    while b < n:
        a, b = b, a+b

    if b == n:
        return (f"O número {n} pertence à sequência de Fibonacci.")
    else:
        return (f"O número {n} não pertence à sequência de Fibonacci.")
    
num = int(input("Digite um número:"))
print(fibonacci(num))




