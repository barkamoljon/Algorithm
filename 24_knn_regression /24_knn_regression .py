import numpy as np

class KNNRegression:
    
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X, y):
        self.X_train = X
        self.Y_train = y
        
    def predict(self, X_test):
        distances = np.linalg.norm(X_test - self.X_train, axis=1)
        nearest_neighbors = np.argsort(distances)[:self.k]
        pedicted_values = np.mean(self.y_train[nearest_neighbours], axis =0)
        return predicted_values


# Create the model 
model = KNNRegression(k=5)

# Fit the model to the training data
model.fit(X_train, t_yrain)

# Make a prediction
prediction = model.predict(X_test)
