# ******************************
# Make your Code
# ******************************
numbes = list(map(str, input().split()))
longest = 0
shortest = 99
for i in range(len(names)):
    if len(names[i]) > longest:
        longest = name[i]
    if len(names[i]) < shortest:
        shortest = names[i]
print(shortest, longest)