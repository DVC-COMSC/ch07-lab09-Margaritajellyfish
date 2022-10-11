# ******************************
# Make your Code
# ******************************
names = list(map(str, input().split()))
shortest = min(names, key=len)
longest = max(names, key=len)
print(shortest, longest)
    