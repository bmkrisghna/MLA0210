import math
from collections import Counter
from mobile_dataset import X, y

# Calculate Entropy
def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

# Information Gain
def info_gain(X, y, feature_index):
    total_entropy = entropy(y)
    values = set([row[feature_index] for row in X])
    weighted_entropy = 0
    
    for value in values:
        subset_y = [y[i] for i in range(len(X)) if X[i][feature_index] == value]
        weighted_entropy += (len(subset_y)/len(y)) * entropy(subset_y)
    
    return total_entropy - weighted_entropy

# Find Best Feature
gains = []
for i in range(len(X[0])):
    gains.append(info_gain(X, y, i))

best_feature = gains.index(max(gains))
print("Best Feature Index (Root Node):", best_feature)
