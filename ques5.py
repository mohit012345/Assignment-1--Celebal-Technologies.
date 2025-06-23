from itertools import combinationsAdd 

n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))
count_with_a = sum(1 for combo in all_combinations if 'a' in combo)

total_combinations = len(all_combinations)

probability = count_with_a / total_combinations
print(f"{probability:.4f}")
