def matrix_shape(matrix):
    """Returns (rows, cols) of a 2D matrix list."""
    return len(matrix), len(matrix[0]) if matrix else 0


def matrix_identity(n):
    """Generates an n x n identity matrix."""
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def matrix_det(matrix):
    """Computes the determinant of a square 2D matrix recursively."""
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Determinant requires a square matrix.")
    
    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0.0
    for c in range(n):
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        sign = 1.0 if c % 2 == 0 else -1.0
        det += sign * matrix[0][c] * matrix_det(sub_matrix)
    return det


def matrix_inverse(matrix):
    """Computes the inverse of a square matrix using Gauss-Jordan elimination."""
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Matrix must be square to invert.")
    
    # Create augmented matrix [A | I]
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]
    
    for i in range(n):
        # Pivot
        pivot = aug[i][i]
        if abs(pivot) < 1e-12:
            raise ValueError("Matrix is singular and cannot be inverted.")
        
        # Scale row i
        for j in range(2 * n):
            aug[i][j] /= pivot
        
        # Eliminate other rows
        for k in range(n):
            if k != i:
                factor = aug[k][i]
                for j in range(2 * n):
                    aug[k][j] -= factor * aug[i][j]
                    
    # Extract right side
    inv = [row[n:] for row in aug]
    return inv


def solve_linear_system(A, b):
    """Solves Ax = b using matrix inversion."""
    A_inv = matrix_inverse(A)
    # A_inv @ b
    x = []
    for i in range(len(A_inv)):
        val = sum(A_inv[i][j] * b[j] for j in range(len(b)))
        x.append(val)
    return x


# ==============================================================================
# SECTION 2: NUMERICAL CALCULUS & OPTIMIZATION
# ==============================================================================

def derivative(func, x, h=1e-5):
    """Approximates f'(x) using central differences."""
    return (func(x + h) - func(x - h)) / (2.0 * h)


def integrate_simpson(func, a, b, n=100):
    """Approximates the definite integral of f(x) from a to b using Simpson's Rule."""
    if n % 2 != 0:
        n += 1  # n must be even
    h = (b - a) / float(n)
    integral = func(a) + func(b)
    
    for i in range(1, n):
        x_i = a + i * h
        weight = 4.0 if i % 2 != 0 else 2.0
        integral += weight * func(x_i)
        
    return integral * (h / 3.0)


def gradient_descent(cost_func, grad_func, start_x, learning_rate=0.01, iterations=1000):
    """Finds the local minimum of a function using gradient descent."""
    x = float(start_x)
    for _ in range(iterations):
        grad = grad_func(x)
        x = x - learning_rate * grad
    return x


# ==============================================================================
# SECTION 3: ADVANCED STATISTICS & PROBABILITY
# ==============================================================================

def covariance(x_list, y_list):
    """Calculates covariance between two 1D numerical datasets."""
    if len(x_list) != len(y_list) or len(x_list) < 2:
        raise ValueError("Lists must be of equal length and contain at least 2 points.")
    
    mean_x = sum(x_list) / len(x_list)
    mean_y = sum(y_list) / len(y_list)
    
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_list, y_list))
    return cov / (len(x_list) - 1)


def correlation(x_list, y_list):
    """Calculates Pearson correlation coefficient (-1.0 to 1.0)."""
    cov = covariance(x_list, y_list)
    
    var_x = covariance(x_list, x_list)
    var_y = covariance(y_list, y_list)
    
    std_x = var_x ** 0.5
    std_y = var_y ** 0.5
    
    if std_x == 0 or std_y == 0:
        return 0.0
    return cov / (std_x * std_y)


def normal_pdf(x, mean=0.0, std=1.0):
    """Evaluates the Gaussian/Normal Probability Density Function at x."""
    pi = 3.14159265358979323846
    e = 2.71828182845904523536
    exponent = -0.5 * ((x - mean) / std) ** 2
    coefficient = 1.0 / (std * (2.0 * pi) ** 0.5)
    return coefficient * (e ** exponent)


# ==============================================================================
# SECTION 4: MACHINE LEARNING MODELS
# ==============================================================================

class LinearRegression:
    """
    Ordinary Least Squares (OLS) Simple Linear Regression (y = m*x + b).
    """
    def __init__(self):
        self.slope = 0.0
        self.intercept = 0.0

    def fit(self, X, y):
        """Fits the linear model to 1D feature X and target y."""
        mean_x = sum(X) / float(len(X))
        mean_y = sum(y) / float(len(y))
        
        num = sum((x - mean_x) * (y_val - mean_y) for x, y_val in zip(X, y))
        den = sum((x - mean_x) ** 2 for x in X)
        
        self.slope = num / den if den != 0 else 0.0
        self.intercept = mean_y - self.slope * mean_x

    def predict(self, X):
        """Generates predictions for inputs in X."""
        if isinstance(X, (int, float)):
            return self.slope * X + self.intercept
        return [self.slope * x + self.intercept for x in X]


class KMeans:
    """
    Pure Python K-Means Clustering for 2D points.
    """
    def __init__(self, k=2, max_iter=100):
        self.k = k
        self.max_iter = max_iter
        self.centroids = []

    def _euclidean_dist(self, p1, p2):
        return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

    def fit(self, data):
        """Clusters 2D data points into K groups."""
        # Simple initial centroids: pick first K points
        self.centroids = [data[i][:] for i in range(self.k)]
        
        for _ in range(self.max_iter):
            # Assign clusters
            clusters = [[] for _ in range(self.k)]
            for point in data:
                distances = [self._euclidean_dist(point, c) for c in self.centroids]
                closest = distances.index(min(distances))
                clusters[closest].append(point)
                
            # Update centroids
            new_centroids = []
            for i, cluster in enumerate(clusters):
                if not cluster:
                    new_centroids.append(self.centroids[i])
                    continue
                num_points = len(cluster)
                num_dims = len(cluster[0])
                mean_point = [
                    sum(p[d] for p in cluster) / float(num_points)
                    for d in range(num_dims)
                ]
                new_centroids.append(mean_point)
                
            if new_centroids == self.centroids:
                break
            self.centroids = new_centroids

    def predict(self, points):
        """Returns cluster index for each input point."""
        preds = []
        for point in points:
            distances = [self._euclidean_dist(point, c) for c in self.centroids]
            preds.append(distances.index(min(distances)))
        return preds
