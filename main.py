# ******************************
# Make your Code
# ******************************
names = list(map(str, input().split()))
longest = int(0)
shortest = int(99)
for i in range(len(names)):
    if len(names[i]) > longest:
        longest = names[i]
    if len(names[i]) < shortest:
        shortest = names[i]
print(shortest, longest)