from mobile_dataset import X, y
from collections import Counter

def naive_bayes_predict(new_sample):
    classes = set(y)
    total = len(y)
    class_counts = Counter(y)
    
    probabilities = {}
    
    for c in classes:
        prior = class_counts[c] / total
        likelihood = 1
        
        for i in range(len(new_sample)):
            count = 0
            total_class = 0
            for j in range(len(X)):
                if y[j] == c:
                    total_class += 1
                    if X[j][i] == new_sample[i]:
                        count += 1
            likelihood *= (count + 1) / (total_class + 3)  # Laplace smoothing
        
        probabilities[c] = prior * likelihood
    
    return max(probabilities, key=probabilities.get)

new_mobile = ["Medium", "High", "High"]
prediction = naive_bayes_predict(new_mobile)

print("Predicted Price Range:", prediction)
