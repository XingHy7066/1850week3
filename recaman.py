L = int(input("Length of sequence: "))


if L <= 0:
    sequence = []
else:
    sequence = [0]

    for k in range(1, L):
        prev = sequence[k-1]
        next_value = prev - k
        if next_value > 0 and next_value not in sequence:
            sequence.append(next_value)
        else:
            sequence.append(prev + k)

print(sequence)
