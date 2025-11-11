import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        return np.array([self._predict_single(x) for x in X])
    
    def _predict_single(self, x):
        distances = np.linalg.norm(self.X_train - x, axis=1)
        k_indices = np.argsort(distances)[:self.k]
        k_labels = self.y_train[k_indices]
        most_common = Counter(k_labels).most_common(1)
        return most_common[0][0]


if __name__ == "__main__":
    X_train = np.array([[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]])
    y_train = np.array([0, 0, 0, 1, 1, 1])
    X_test = np.array([[2, 2], [7, 7]])
    
    knn = KNN(k=3)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    print("Predictions:", predictions)