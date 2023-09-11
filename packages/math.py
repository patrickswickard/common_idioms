import math

print("math.ceil(x) returns the ceiling of x (smallest integer greater than x)")
print("a = math.ceil(5.5)")
a = math.ceil(5.5)
print(a)

print("\n")

print("math.comb(n,k) returns the number of ways to choose k items from n items without replacement without order")
print("a = math.comb(6,2)")
a = math.comb(6,2)
print(a)

print("\n")

print("math.copysign(x,y) returns a number with magnitude of x but sign of y, which is kinda niche")
print("a = math.copysign(7.5,-3)")
a = math.copysign(7.5,-3)
print(a)

print("\n")

print("math.fabs(x) returns the absolute value of x")
print("a = math.fabs(-3)")
a = math.fabs(-3)
print(a)

print("\n")

print("math.factorial(n) returns n factorial n! (integer values only)")
print("a = math.factorial(5)")
a = math.factorial(5)
print(a)

print("\n")

print("math.floor(x) returns the floor of x (greatest integer smaller than x)")
print("a = math.floor(5.5)")
a = math.floor(5.5)
print(a)

print("\n")

print("math.fmod(x,y) is basically preferred floating point version for mod, x & y is generally fine for integers")
print("a = math.fmod(17.5,4)")
a = math.fmod(17.5,4)
print(a)
print("a = 17 % 4")
a = 17 % 4
print(a)

print("\n")

print("math.frexp(x) is a little weird.  Returns (m,e) such that x = m*2^e (i.e. x = m*(2**e)) so that m is between 0 and 1.  This lets you see how a float is 'built'.")
print("Kinda like scientific notation base 2...")
print("a = math.frexp(8)")
a = math.frexp(8)
print(a)
print("a = math.frexp(12)")
a = math.frexp(12)
print(a)
print("a = math.frexp(5)")
a = math.frexp(5)
print(a)
print("a = math.frexp(10.5)")
a = math.frexp(10.5)
print(a)

print("\n")

print("math.fsum(iterable) is a more accurate version of sum(iterable) which avoids stupid rounding errors for floats")
print("myarray = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]")
print("a = sum(myarray)")
myarray = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
a = sum(myarray)
print(a)
print("a = math.fsum(myarray)")
a = math.fsum(myarray)
print(a)

print("\n")

print("math.gcd(*integers) takes arbitrary number of integers and returns gcd")
print("a = math.gcd(3,5,7)")
a = math.gcd(3,5,7)
print(a)
print("a = math.gcd(6,10,14,18)")
a = math.gcd(6,10,14,18)
print(a)

print("\n")

print("math.isclose(a,b,*,rel_tol=PERCENTAGE,abs_tol=NUM determines if at least two numbers are close to each other or not")
print("The default values for close are relative tolerance 1xe-09 and absolute tolerance 0.0")
print("which can be reset if desired (percent is relative to largest number")
print("If you set rel_tol to a percent then you get whether it is 'close' as in within x percent of the larger magnitude number")
print("This function is great for horseshoes and hand grenades")
print("math.isclose(100, 104, rel_tol=0.05)")
a = math.isclose(96, 100,rel_tol=0.05)
print(a)
print("math.isclose(94, 100, rel_tol=0.05)")
a = math.isclose(94, 100,rel_tol=0.05)
print(a)
print("math.isclose(96, 100, abs_tol=5)")
a = math.isclose(96, 100,abs_tol=5)
print(a)
print("math.isclose(94, 100, abs_tol=5)")
a = math.isclose(94, 100,abs_tol=5)
print(a)

print("\n")

print("math.isfinite(x) is uh not surprising")
print("a = math.isfinite(5)")
a = math.isfinite(5)
print(a)
print("math.isinf(x) is unsurprising too - just tells you if infinite (pos or neg)")
print("a = math.isinf(5)")
a = math.isnan(5)
print(a)
print("math.isnan(x) is unsurprising too - just tells you if NaN (not a number)")
print("a = math.isnan(5)")
a = math.isnan(5)
print(a)

print("\n")

print("math.isqrt(n) returns the 'integer square root' of n, i.e. the biggest number x such that x^2 < n")
print("a = math.isqrt(50)")
a = math.isqrt(50)
print(a)

print("\n")

print("math.lcm(*integers) takes some integers and returns least common multiple")
print("a = math.lcm(2,3,4,5)")
a = math.lcm(2,3,4,5)
print(a)

print("\n")

print("math.ldexp(x, i) returns x*2^i (x*2**i) which is essentially inverse of math.frexp()")
print("a = math.ldexp(5,4))")
a = math.ldexp(5,4)
print(a)

print("\n")

print("math.modf returns the fractional and integer parts of x (both sharing x's sign)")
print("a = math.modf(2.25)")
a = math.modf(2.25)
print(a)
print("a = math.modf(-2.25)")
a = math.modf(-2.25)
print(a)

print("\n")

print("math.nextafter(x,y) returns the next floating-point value of x toward y.  LOL!")
print("This is how you anger Georg Cantor's ghost.")
print("This has great uses and can also be used to write hilariously inefficient loops")
print("a = math.nextafter(1.0,math.inf)")
a = math.nextafter(1.0,math.inf)
print(a)

print("\n")

print("math.perm(n,k) gives you how many ways to choose k items from n items no repetition with order")
print("a = math.perm(6,3)")
a = math.perm(6,3)
print(a)

print("\n")

print("math.prod(iterable) returns the product of all the elements in the iterable")
print("mylist = [2,3,5.5]")
print("a = math.prod(mylist)")
mylist = [2,3,5.5]
a = math.prod(mylist)
print(a)

print("\n")

print("math.remainder(x,y) returns floaty remainder when x is divided by y")
print("a = math.remainder(14.75,7)")
a = math.remainder(14.75,7)
print(a)

print("\n")

print("math.trunc(x) truncates x rounding toward zero")
print("a = math.trunc(14.5)")
a = math.trunc(14.5)
print(a)
print("a = math.trunc(-14.5)")
a = math.trunc(-14.5)
print(a)

print("\n")

print("math.ulp(x) returns value of least significant bit of the float x")
print("Stands for 'unit in the last place' and god only knows how you use this")
print("a = math.ulp(14.5)")
a = math.ulp(14.5)
print(a)
print("a = math.ulp(14400)")
a = math.ulp(14400)
print(a)
