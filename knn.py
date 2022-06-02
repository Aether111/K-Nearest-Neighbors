# Imports
import numpy as np
from scipy.stats import mode

# Hyperparameters

k = 3 # This the number of nearest neighbors

# Data
# This is example data and it can be changed even to different dimensions.

X_train = np.array([[0,0],[0,1],[1,0],[7,0],[7,1],[8,0]])

y_train = np.array([0,0,0,1,1,1])

X_test = np.array([[4,0]])

y_test = np.array([1])

# Gets the euclidean distance between two points in any dimension
def distance(x,y):
    return np.sqrt(np.sum((x - y)**2))

# Stores the distances between the test point and all train points
distances = []

# Looping over the train points and storing distances to the test point
for x in X_train:
    distances = np.append(distances,distance(x,X_test[0])) # TODO: Adjust to test more than the first test point

nn = []

# Finds the arguments in X_train of the train points closest to the test point
nn = distances.argsort()[:k]

neighbors = []
labels = []

# Storing nearest neighbors and their labels
for c in range(k):
    labels.append(y_train[nn[c]])
    neighbors.append(X_train[nn[c]])

# Stores the labels of the nearest neighbors in a numpy array
classified = np.array(labels)

# Output
print("This classifies as " + str(int(mode(classified)[0])) + ".")
print(neighbors)
