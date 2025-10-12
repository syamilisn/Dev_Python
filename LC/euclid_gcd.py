def find_gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 32
num2 = 18

gcd_result = find_gcd_euclidean(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")