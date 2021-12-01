with open("input.txt", "r") as input_file:
    depths = [int(depth) for depth in input_file]
print(sum([depths[i] > depths[i - 1] for i in range(1, len(depths))]))

sums = [sum(depths[i : i + 3]) for i in range(0, len(depths) - 2)]
print(sum([sums[i] > sums[i - 1] for i in range(1, len(sums))]))
