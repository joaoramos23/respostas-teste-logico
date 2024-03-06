def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def check_fibonacci_number(number):
    fib_sequence = fibonacci_sequence(number)
    if number in fib_sequence:
        return True
    else:
        return False

number_to_check = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if check_fibonacci_number(number_to_check):
    print(f"O número {number_to_check} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number_to_check} não pertence à sequência de Fibonacci.")
