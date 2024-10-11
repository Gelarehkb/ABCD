a = int(input('Give me a: '))
b = int(input('Give me b: '))
c = int(input('Give me c: '))
d = int(input('Give me d: '))

sum = a + b + d
product = a*b*c*d
sums = (a+c) * (b+d)
intDev = a//c
regDev = a / b
modulo = a % d
negPower = a**-c
squareroot= d**(1/2)
equation= (c/3)*((a**(b+(c/2)))-1) + d



print(f'Sum of a, b and d: {sum}')
print(f'Product of all numbers: {product}')
print(f'The sum of a and c times the sum of b and d: {sums}')
print(f'a divided by c (int): {intDev}')
print(f'a divided by b (float): {regDev}')
print(f'Remainder of a divided by d: {modulo}')
print(f'a to the power of -c: {negPower}')
print(f'd to the power of 1/2 (square root): {squareroot}')
print(f'Complex equation: {equation}')
