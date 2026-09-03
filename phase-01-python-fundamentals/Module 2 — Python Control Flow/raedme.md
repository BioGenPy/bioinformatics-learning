
#  ----- 1. if Statement
if allows Python to make a decision
if condition:
    # code runs when condition is True
    sequence_length = 1500
if sequence_length > 1000:
    print("Sequence is long")
    gc_content = 55.2

if gc_content > 50:
    print("High GC content")
# ------------2. if + else

Usually we want to do something when the condition is True and something else when it is False.
gc_content = 42.5

if gc_content > 50:
    print("High GC content")
else:
    print("Low or normal GC content")

    if condition:
    # True
else:
    # False
#  ⚠️ Indentation is important

Correct:

if gc_content > 50:
    print("High GC content")

The indentation tells Python that the print() belongs to the if.

# -- Next: elif
elif is used when we have more than two possible conditions.
sequence_length = int(input("Enter sequence length: "))
if sequence_length >= 2000:
    print("Very long sequence")
elif sequence_length >= 1000:
    print("Long sequence")
else:
    print("Short sequence")
    Python checks if → elif → elif → else from top to bottom and executes the first matching condition.

                 gc_content
                  ↓
            >= 60 ?
           /       \
        Yes         No
        ↓            ↓
      High         >= 40 ?
                  /      \
                Yes       No
                 ↓         ↓
              Normal      Low
# --- Next: Nested if
Nested if means putting an if inside another if.
We'll use a bioinformatics example such as:
First check whether a sequence is long enough. If it is, then check its GC content.
That's the next concept.
First condition
     ↓
   True?
   ↓
Second condition
     ↓
   True/False

# ------- 5. for Loop

A for loop is used when you want to repeat code for each item in a sequence.

This is extremely important in bioinformatics because DNA/RNA sequences contain many bases that we often need to process one by one.

# ---- for with a List

A for loop also works with lists:
genes = ["BRCA1", "TP53", "EGFR"]

for gene in genes:
    print(gene)

#  ----- Next: range()

Before we move deeper into loops, let's learn range().

for i in range(5):
    print(i)
# --- Next: while loop
A while loop repeats code as long as a condition is True.

# -- Next: break

break is used when you want to stop a loop immediately.