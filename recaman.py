
L = int(input("Length of sequence: "))

sequence = []
seen = set()

a = 0
for k in range(L):
    sequence.append(a)
    seen.add(a)
    
    next_value = a - (k + 1)
    if next_value > 0 and next_value not in seen:
        a = next_value
    else:
        a = a + (k + 1)

[print(item) for item in sequence]