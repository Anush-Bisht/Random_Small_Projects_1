powers = [3, 8, 9, 7]
mini = maxi = powers[0]
print(mini, maxi)

for power in powers[1:]:
    mini = min(mini, power)
    maxi = max(maxi, power)
    print(mini, maxi)
