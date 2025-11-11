import numpy as np

class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None
    
    def fit(self, X):
        # Initialize centroids randomly
        idx = np.random.choice(len(X), self.k, replace=False)
        self.centroids = X[idx]
        
        for _ in range(self.max_iters):
            # Assign clusters
            labels = self._assign_clusters(X)
            
            # Update centroids
            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
            
            # Check convergence
            if np.allclose(self.centroids, new_centroids):
                break
            
            self.centroids = new_centroids
        
        return labels
    
    def _assign_clusters(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)
    
    def predict(self, X):
        return self._assign_clusters(X)


if __name__ == "__main__":
    X = np.random.randn(100, 2)
    kmeans = KMeans(k=3)
    labels = kmeans.fit(X)
    print("Cluster labels:", labels[:10])
    print("Centroids:", kmeans.centroids)