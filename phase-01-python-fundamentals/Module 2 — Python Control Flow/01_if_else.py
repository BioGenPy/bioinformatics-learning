# secquence_length = int(input("Enter the length of the sequence: "))

# if secquence_length > 1000 :

#     print("Long sequence.")
    
# else:
  
#     print("Short sequence.")
    
# ------------------ 

# gc_content = float(input("Enter GC content: "))

# if gc_content >= 60:
#     print("High GC content")
# elif gc_content >= 40:
#     print("Normal GC content")
# else:
#     print("Low GC content")
    
# ------------------ Nested if

# sequence_length = int(input("Enter the length of the sequence: "))
# gc_content = float(input("Enter GC content: "))

# if sequence_length > 1500:
#     if gc_content >= 60:
#         print("Sequence is long enough")
#     else:
#         print("High GC content")
# else:
#     if gc_content >= 50:
#         print("Normal or low GC content")
#     else:
#         print("Sequence is too short")
        
# ------------------ for Loop

# dna_sequence = input("Enter a DNA sequence: ")
# for base in dna_sequence:
#   if base == "A":
#     print("Adeine")
#   elif base == "T":
#     print("Thymine")
#   elif base == "C":
#     print("Cytosine")
#   elif base == "G":
#     print("Guanine")

# genes = ["BRCA1", "BRCA2", "TP53", "EGFR"]

# for gene in genes:
#     print(gene)
    
# dna_sequence = "ATGCGTACG"
# a_count = 0
# for base in dna_sequence:
#     if base == "A":
#         a_count += 1
# print(f"Number of A's in the sequence: {a_count}")

#---------------------- Range
# for  Gene in range(1, 11):
#     print(Gene)

# dna_sequence = "ATGCGTACG"
# for i in range(len(dna_sequence)):
#   pssition= i + 1
#   base = dna_sequence[i]
#   print(f"Base at position {pssition}: {base}")
  


# position = 0
# while position <  10:
#   print(f"Base at position {position + 1}")
#   position += 1

dna_sequence = "ATGCGTACG"
position = 0
g_count = 0

while position < len(dna_sequence):
    base = dna_sequence[position]
    if base == "G":
        g_count += 1
    position += 1

print(f"Number of G's in the sequence: {g_count}")  