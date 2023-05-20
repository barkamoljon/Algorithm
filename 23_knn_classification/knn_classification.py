import math
def euclidean_distance(x1, y1, x2, y2):
        """
    Calculates the Euclidean distance between two points.

    Args:
        x1: The x-coordinate of the first point.
        y1: The y-coordinate of the first point.
        x2: The x-coordinate of the second point.
        y2: The y-coordinate of the second point.

    Returns:
        The Euclidean distance between the two points.
    """
    return math.sqrt((x1-x2) ** 2 + (y1 - y2) ** 2)

def find_k_nearest_neighborns(x_train, y_train, x_test, k):
    """
    Finds the k nearest neighbors of a point in a dataset.

    Args:
        x_train: The training data points.
        y_train: The labels of the training data points.
        x_test: The point to find the nearest neighbors of.
        k: The number of nearest neighbors to find.

    Returns:
        A list of the k nearest neighbors of the point, along with their distances.
    """
    distances = []
        for i in range(len(x_train)):
            distance = euclidean_distance(x_train[i][0], x_train[i][1], x_test[0], x_test[1])
            distance.append((distance, y_train[i]))
                
                distances.sort()
                return distances[:k]
def predict_label(x_test, x_train, y_train, k):
    """
    Predicts the label of a point using the KNN algorithm.

    Args:
        x_test: The point to predict the label of.
        x_train: The training data points.
        y_train: The labels of the training data points.
        k: The number of nearest neighbors to use.

    Returns:
        The predicted label of the point.
    """
    nearest_neighbors = find_k_nearest_neighbors(x_train, y_train, x_test, k)
    most_common_label = max(nearest_neighbors, key=lambda x:x[1])[1]
    return most_common_label

        
  
