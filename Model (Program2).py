from mobile_dataset import X, y
import math

# Encode categorical values
mapping = {"Low":1, "Medium":2, "High":3}

X_encoded = [[mapping[val] for val in row] for row in X]

def distance(a, b):
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))

# New mobile
new_mobile = ["Medium", "High", "High"]
new_encoded = [mapping[val] for val in new_mobile]

# Calculate distances
distances = []
for i in range(len(X_encoded)):
    d = distance(X_encoded[i], new_encoded)
    distances.append((d, y[i]))

# Sort and take k=3
distances.sort()
k = 3
neighbors = distances[:k]

# Majority vote
votes = [label for (_, label) in neighbors]
prediction = max(set(votes), key=votes.count)

print("Predicted Price Range:", prediction)
