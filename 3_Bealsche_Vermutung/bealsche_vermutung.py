import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def testBealConjecture(A_range, B_range, C_range, x_range, y_range, z_range):
    for A in A_range:
        for B in B_range:
            for C in C_range:
                for x in x_range:
                    for y in y_range:
                        for z in z_range:
                            if gcd(A, B) == 1 and gcd(A, C) == 1 and gcd(B, C) == 1:
                                sum_powers = pow(A, x) + pow(B, y)
                                C_power = pow(C, z)

                                if sum_powers == C_power:
                                    print(f"Conjecture holds for A={A}, B={B}, C={C}, x={x}, y={y}, z={z}")

def generateFibonacciNumbers(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
    return fibonacci_numbers

# Define the range of values for A, B, C, x, y, and z
A_range = range(1, 16)
B_range = range(1, 16)
C_range = range(1, 16)
x_range = range(3, 12)
y_range = range(3, 12)
z_range = range(3, 12)

# Test 1: Small Values of A, B, and C
print('Testing Small Values of A, B, and C:')
testBealConjecture(A_range, B_range, C_range, x_range, y_range, z_range)

# Test 2: Large Values of A, B, and C
# ----> Wegen langer Laufzeit ausgeblendet
# print('Testing Large Values of A, B, and C:')
# A_range_large = range(10**8, 10**9 + 1)
# B_range_large = range(10**8, 10**9 + 1)
# C_range_large = range(10**8, 10**9 + 1)
# testBealConjecture(A_range_large, B_range_large, C_range_large, x_range, y_range, z_range)

# Test 3: Primes and Prime Powers
print('Testing Primes and Prime Powers:')
primes_range = list(filter(lambda x: all(x % d != 0 for d in range(2, int(math.sqrt(x)) + 1)), range(2, 101)))
primes_powers_range = range(3, 10)
testBealConjecture(primes_range, primes_range, primes_range, primes_powers_range, primes_powers_range, primes_powers_range)

# Test 4: Consecutive Numbers
print('Testing Consecutive Numbers:')
consecutive_range = range(1, 11)
testBealConjecture(consecutive_range, [i+1 for i in consecutive_range], [i+2 for i in consecutive_range], x_range, y_range, z_range)

# Test 5: Fibonacci Numbers
print('Testing Fibonacci Numbers:')
fibonacci_range = generateFibonacciNumbers(20)
testBealConjecture(fibonacci_range[1::2], fibonacci_range[1::2], fibonacci_range[1::2], x_range, y_range, z_range)

# Test 6: Special Exponents
print('Testing Special Exponents:')
special_exponents_range = [42, 43, 44, 45]
testBealConjecture(A_range, B_range, C_range, special_exponents_range, special_exponents_range, special_exponents_range)

# Test 7: Specific Diophantine Equations
print('Testing Specific Diophantine Equations:')
testBealConjecture(A_range, B_range, C_range, x_range, [2 * x for x in x_range], [3 * x for x in x_range])
