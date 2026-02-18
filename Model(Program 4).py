# Mobile Dataset

# Features: RAM, Storage, Battery
# Target: PriceRange

data = [
    ["Low", "Low", "Low", "Low"],
    ["Low", "Medium", "Medium", "Medium"],
    ["Medium", "Medium", "Medium", "Medium"],
    ["High", "High", "High", "High"],
    ["Medium", "High", "High", "High"],
    ["Low", "Low", "Medium", "Low"],
    ["High", "Medium", "High", "High"],
    ["Medium", "Low", "Medium", "Medium"]
]

# Separate features and labels
X = [row[:-1] for row in data]
y = [row[-1] for row in data]
