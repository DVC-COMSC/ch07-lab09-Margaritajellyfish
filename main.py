# ******************************
# Make your Code
# ******************************
names = list(map(str, input().split()))
longest = 0
shortest = 99
for i in range(len(names)):
    if int(len(names[i])) > longest:
        longest = names[i]
    if int(len(names[i])) < shortest:
        shortest = names[i]
print(shortest, longest)