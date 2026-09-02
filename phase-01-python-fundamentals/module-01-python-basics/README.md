🐍 1. Data Types
A data type tells Python what kind of value a variable contains.
For example:
gene = "BRCA1"
"BRCA1" is a string (str).
gene_length = 100
100 is an integer (int).
Main Python data types
For now, concentrate on these:
Type	Meaning	Example
str	Text	"BRCA1"
int	Whole number	100
float	Decimal number	98.5
bool	True/False	True
NoneType	No value	None
# 1. String — str
gene = "BRCA1"
dna = "ATGCGTAC"
Check the type:
print(type(gene))
print(type(dna))
Output:
<class 'str'>
<class 'str'>

# 2. Integer — int
sequence_length = 150
gene_count = 25
print(type(sequence_length))
Output:
<class 'int'>

# 3. Float — float
Used for decimal values.
gc_content = 52.7
mutation_rate = 0.03
print(type(gc_content))
Output:
<class 'float'>

# 4. Boolean — bool
A Boolean has only two values:
True
False
Example:
is_dna = True
is_rna = False
print(type(is_dna))
Output:
<class 'bool'>

# 5. None — NoneType
None means that a variable currently has no value.
result = None
print(result)
print(type(result))
Output:
None
<class 'NoneType'>

#  Bioinformatics Example
Let's combine several data types:
gene = "BRCA1"
sequence_length = 120
gc_content = 48.5
is_dna = True
print("Gene:", gene)
print("Length:", sequence_length)
print("GC Content:", gc_content)
print("Is DNA:", is_dna)
Output:
Gene: BRCA1
Length: 120
GC Content: 48.5
Is DNA: True
# type() — Very Important
You can find the type of any value using:
type()
Example:
print(type("ATGC"))
print(type(100))
print(type(45.5))
print(type(True))
print(type(None))
Output:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>

#  Practice — Data Types
Create:
# 03_data_types.py
Exercise 1
Create these variables:
gene = "TP53"
sequence_length = 500
gc_content = 41.7
is_dna = True
Print each value and its type.
Exercise 2
Create:
organism = "Homo sapiens"
chromosome = 17
Print their values and types.
# Exercise 3 🧬
Create:
dna_sequence = "ATGCGTACGTAG"
Then print:
DNA: ATGCGTACGTAG
Type: <class 'str'>
Don't worry about reproducing <class 'str'> manually—use type().
# Interview Questions
Q1. What is a data type?
A data type defines the kind of value stored in a variable and determines what operations can be performed on that value.
Q
str
because "100" is inside quotes.
# Q3. What is the type of 100?
int
# Q4. What is the difference between 100 and "100"?
100     # int
"100"   # str
This distinction becomes very important when we learn input and type conversion.
Your turn
Do Exercises 1–3 and send me your code.
Then we'll move directly to:
#  2. Type Conversion
where you'll learn:
int()
float()
str()
bool()
#  Interview Questions
# Q1. What is a data type?
A data type defines the kind of value stored in a variable and determines what operations can be performed on that value.
# Q2. What is the type of "100"?
str
because "100" is inside quotes.
# Q3. What is the type of 100?
int
# Q4. What is the difference between 100 and "100"?
100     # int
"100"   # str
This distinction becomes very important when we learn input and type conversion.
# ============================ Arithmetic Operators in Python ==================
| Operator | Name              |   Example |     Result |
| -------- | ----------------- | --------: | ---------: |
| `+`      | Addition          |  `10 + 3` |       `13` |
| `-`      | Subtraction       |  `10 - 3` |        `7` |
| `*`      | Multiplication    |  `10 * 3` |       `30` |
| `/`      | Division          |  `10 / 3` | `3.333...` |
| `//`     | Floor Division    | `10 // 3` |        `3` |
| `%`      | Modulus/Remainder |  `10 % 3` |        `1` |
| `**`     | Exponent          | `10 ** 3` |     `1000` |

# comparesion | Operator | Meaning               | Example    | Result  |
| -------- | --------------------- | ---------- | ------- |
| `==`     | Equal to              | `10 == 10` | `True`  |
| `!=`     | Not equal             | `10 != 5`  | `True`  |
| `>`      | Greater than          | `10 > 5`   | `True`  |
| `<`      | Less than             | `10 < 5`   | `False` |
| `>=`     | Greater than or equal | `10 >= 10` | `True`  |
| `<=`     | Less than or equal    | `5 <= 10`  | `True`  |
1. Equal ==

⚠️ Don't confuse = and ==.

x = 10

= means assign.

x == 10

== means compare.

Example:

gene_count = 10

print(gene_count == 10)

Output:

True
2. Not Equal !=
gene_count = 10

print(gene_count != 5)

Output:

True

Because 10 is not equal to 5.

3. Greater Than >
sequence_length = 1500

print(sequence_length > 1000)

Output:

True
4. Less Than <
sequence_length = 500

print(sequence_length < 1000)

Output:

True
5. Greater Than or Equal >=
gc_content = 50.0

print(gc_content >= 50)

Output:

True

Both 50 >= 50 and 60 >= 50 are True.

6. Less Than or Equal <=
gc_content = 45.5

print(gc_content <= 50)

Output:

True
🧬 Bioinformatics Example

Suppose we want to check whether a DNA sequence is long enough for analysis:

sequence_length = 1200

print(sequence_length >= 1000)

Output:

True

Or check GC content:

gc_content = 42.5

print(gc_content > 50)

Output:

False