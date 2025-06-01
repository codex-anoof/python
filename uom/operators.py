# Operators are used to perform operation on variables and values.
'''
🧮 1. Arithmetic Operators
Used to perform mathematical operations.

Operator	Description	Example
+	Addition	a + b
-	Subtraction	a - b
*	Multiplication	a * b
/	Division	a / b
//	Floor Division	a // b
%	Modulus	a % b
**	Exponentiation	a ** b

🔍 2. Comparison (Relational) Operators
Used to compare values.

Operator	Description	Example
==	Equal to	a == b
!=	Not equal to	a != b
>	Greater than	a > b
<	Less than	a < b
>=	Greater or equal	a >= b
<=	Less or equal	a <= b

🧠 3. Logical Operators
Used to combine conditional statements.

Operator	Description	Example
and	Logical AND	a > 5 and b < 10
or	Logical OR	a > 5 or b < 10
not	Logical NOT	not (a > 5)

📦 4. Assignment Operators
Used to assign values to variables.

Operator	Description	Example
=	Assign	a = b
+=	Add and assign	a += b
-=	Subtract and assign	a -= b
*=	Multiply and assign	a *= b
/=	Divide and assign	a /= b
//=	Floor divide and assign	a //= b
%=	Modulus and assign	a %= b
**=	Exponent and assign	a **= b

🔢 5. Bitwise Operators
Used to perform operations on binary representations.

Operator	Description	Example
&	Bitwise AND	a & b
`	`	Bitwise OR
^	Bitwise XOR	a ^ b
~	Bitwise NOT	~a
<<	Left shift	a << 2
>>	Right shift	a >> 2

🗂️ 6. Membership Operators
Used to check if a value is present in a sequence.

Operator	Description	Example
in	In sequence	'x' in list
not in	Not in sequence	'x' not in list

🧬 7. Identity Operators
Used to compare object identity (whether two references point to the same object).

Operator	Description	Example
is	Same identity	a is b
is not	Different identity	a is not b
'''
# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)          # 1
print("Exponentiation:", a ** b)  # 1000
print()

# 2. Comparison Operators
print("Comparison Operators:")
print("Equal:", a == b)           # False
print("Not equal:", a != b)       # True
print("Greater than:", a > b)     # True
print("Less than:", a < b)        # False
print("Greater or equal:", a >= b) # True
print("Less or equal:", a <= b)    # False
print()

# 3. Logical Operators
x = True
y = False
print("Logical Operators:")
print("AND:", x and y)            # False
print("OR:", x or y)              # True
print("NOT x:", not x)            # False
print()

# 4. Assignment Operators
c = 5
print("Assignment Operators:")
c += 2  # c = c + 2
print("Add and assign:", c)       # 7
c *= 3  # c = c * 3
print("Multiply and assign:", c)  # 21
c -= 5  # c = c - 5
print("Subtract and assign:", c)  # 16
c /= 4  # c = c / 4
print("Divide and assign:", c)    # 4.0
print()

# 5. Bitwise Operators
m = 5     # 0b0101
n = 3     # 0b0011
print("Bitwise Operators:")
print("AND:", m & n)              # 1
print("OR:", m | n)               # 7
print("XOR:", m ^ n)              # 6
print("NOT m:", ~m)               # -6 (in 2's complement)
print("Left Shift:", m << 1)      # 10
print("Right Shift:", m >> 1)     # 2
print()

# 6. Membership Operators
my_list = [1, 2, 3, 4]
print("Membership Operators:")
print("2 in list:", 2 in my_list)          # True
print("5 not in list:", 5 not in my_list)  # True
print()

# 7. Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("Identity Operators:")
print("x is y:", x is y)           # True (same object)
print("x is z:", x is z)           # False (same content, different object)
print("x is not z:", x is not z)   # True
