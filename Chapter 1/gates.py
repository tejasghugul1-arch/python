# 🐍 Logic Gates Truth Table

print("A\tB\tAND\tOR\tNAND\tNOR\tXOR")

# Loop through all combinations of A and B (0 and 1)
for A in [0, 1]:
    for B in [0, 1]:
        AND = A & B
        OR = A | B
        NAND = not (A & B)
        NOR = not (A | B)
        XOR = A ^ B

        print(A, "\t", B, "\t", AND, "\t", OR, "\t", int(NAND), "\t", int(NOR), "\t", XOR)

# NOT Gate (separate because single input)
print("\nNOT Gate:")
print("A\tNOT A")

for A in [0, 1]:
    print(A, "\t", int(not A))