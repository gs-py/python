inp = "zohrhwshjkrykryhyyn"
n = len(inp)

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(inp[i], end="")
        else:
            print("  ", end="")  # Add a space after each regular space for consistent spacing
    print()

print("\n",inp)
