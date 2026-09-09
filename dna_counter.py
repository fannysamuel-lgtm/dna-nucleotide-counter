# DNA Nucleotide Counter

dna_sequence = input("Enter a DNA sequence: ").upper()

# Count each nucleotide
a_count = dna_sequence.count("A")
t_count = dna_sequence.count("T")
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

# Display the results
print("\nNucleotide Count:")
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)  