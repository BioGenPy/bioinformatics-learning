gen = input("Enter the gene name: ")
print("gen:",gen)

# input take 
print("------------Take input------------")
gene_name = input ("Enter the gene name: ")
sequence_length = input ("Enter the sequence length: ")
gc_content = input ("Enter the GC content: ")

print("Gene Name:", gene_name)
print("Sequence Length:", sequence_length)
print("GC Content:", gc_content)

# OR 
while True:
    # Collecting user input
    gene_name = input("Enter gene name (or type 'quit' to exit): ")
    if gene_name.lower() == 'quit':
        break
        
    dna_sequence = input("Enter DNA sequence: ")
    sequence_length = input("Enter sequence length: ")
    gc_content = input ("Enter the GC content: ")

    # Printing the formatted results
    print()
    print(f"Gene: {gene_name}")
    print(f"DNA: {dna_sequence}")
    print(f"Length: {sequence_length}")
    print("-" * 20)  # Separator line for readability
    print("GC Content:", gc_content)