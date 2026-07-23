class Array:
    """
    A pure Python N-dimensional array class supporting element-wise operations,
    slicing, reshape, matrix algebra, reductions, and visual emoticons.
    """
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Data must be provided as a nested Python list.")
        self.data = data
        self.shape = self._infer_shape(data)
        self.ndim = len(self.shape)
        self.size = self._calc_size(self.shape)

    def _infer_shape(self, lst):
        shape = []
        curr = lst
        while isinstance(curr, list):
            shape.append(len(curr))
            if len(curr) == 0:
                break
            curr = curr[0]
        return tuple(shape)

    def _calc_size(self, shape):
        tot = 1
        for s in shape:
            tot *= s
        return tot

    def flatten(self):
        """Flattens an N-dimensional array into a 1D Array."""
        def _flat_list(lst):
            res = []
            for item in lst:
                if isinstance(item, list):
                    res.extend(_flat_list(item))
                else:
                    res.append(item)
            return res
        return Array(_flat_list(self.data))

    def reshape(self, new_shape):
        """Reshapes array to new_shape if total size matches."""
        flat = self.flatten().data
        if self._calc_size(new_shape) != len(flat):
            raise ValueError(f"Cannot reshape array of size {len(flat)} into shape {new_shape}")

        def _build(shape_idx, curr_idx):
            if shape_idx == len(new_shape) - 1:
                sz = new_shape[shape_idx]
                return flat[curr_idx:curr_idx + sz], curr_idx + sz
            
            sub = []
            for _ in range(new_shape[shape_idx]):
                item, curr_idx = _build(shape_idx + 1, curr_idx)
                sub.append(item)
            return sub, curr_idx

        new_data, _ = _build(0, 0)
        return Array(new_data)

    def transpose(self):
        """Transposes a 2D Array."""
        if self.ndim != 2:
            raise ValueError("Transpose currently supports 2D arrays.")
        r, c = self.shape
        transposed = [[self.data[i][j] for i in range(r)] for j in range(c)]
        return Array(transposed)

    # --------------------------------------------------------------------------
    # ELEMENT-WISE MAPPING & ARITHMETIC OVERLOADS
    # --------------------------------------------------------------------------
    def apply(self, func):
        """Applies a scalar function element-wise across the array."""
        def _apply_rec(lst):
            if not isinstance(lst, list):
                return func(lst)
            return [_apply_rec(item) for item in lst]
        return Array(_apply_rec(self.data))

    def _elementwise_op(self, other, op):
        if isinstance(other, (int, float)):
            return self.apply(lambda x: op(x, other))
        elif isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError(f"Shape mismatch for operation: {self.shape} vs {other.shape}")
            def _rec(a, b):
                if not isinstance(a, list):
                    return op(a, b)
                return [_rec(x, y) for x, y in zip(a, b)]
            return Array(_rec(self.data, other.data))
        else:
            raise TypeError("Unsupported operand type.")

    def __add__(self, other): return self._elementwise_op(other, lambda x, y: x + y)
    def __sub__(self, other): return self._elementwise_op(other, lambda x, y: x - y)
    def __mul__(self, other): return self._elementwise_op(other, lambda x, y: x * y)
    def __truediv__(self, other): return self._elementwise_op(other, lambda x, y: x / y)
    def __pow__(self, p): return self.apply(lambda x: x ** p)
    def __neg__(self): return self.apply(lambda x: -x)

    # --------------------------------------------------------------------------
    # MATRIX MULTIPLICATION & REDUCTIONS
    # --------------------------------------------------------------------------
    def matmul(self, other):
        """2D Matrix Multiplication (A @ B)."""
        if self.ndim != 2 or other.ndim != 2:
            raise ValueError("Matrix multiplication requires 2D arrays.")
        r1, c1 = self.shape
        r2, c2 = other.shape
        if c1 != r2:
            raise ValueError(f"Cannot multiply shapes {self.shape} and {other.shape}")

        res = [[0.0 for _ in range(c2)] for _ in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    res[i][j] += self.data[i][k] * other.data[k][j]
        return Array(res)

    def sum(self):
        """Returns the sum of all elements."""
        return sum(self.flatten().data)

    def mean(self):
        """Returns the arithmetic mean of all elements."""
        return self.sum() / float(self.size)

    def std(self):
        """Computes standard deviation across all elements."""
        m = self.mean()
        var = sum((x - m) ** 2 for x in self.flatten().data) / float(self.size)
        return var ** 0.5

    def max(self):
        """Returns the maximum element."""
        return max(self.flatten().data)

    def min(self):
        """Returns the minimum element."""
        return min(self.flatten().data)

    def __getitem__(self, idx):
        return self.data[idx]

    # --------------------------------------------------------------------------
    # EMOTE & VISUALIZATION TOOLS
    # --------------------------------------------------------------------------
    def to_emote(self, threshold=0.0, positive_emote="🟢", negative_emote="🔴"):
        """Converts array values into a visual emote map based on a threshold."""
        def _convert(item):
            if isinstance(item, list):
                return [_convert(x) for x in item]
            return positive_emote if item >= threshold else negative_emote

        emote_data = _convert(self.data)
        if self.ndim == 2:
            return "\n".join(" ".join(row) for row in emote_data)
        return str(emote_data)

    def heat_map(self):
        """Converts array values into an ASCII intensity visualization."""
        blocks = ["░", "▒", "▓", "█"]
        min_v, max_v = self.min(), self.max()
        rng = (max_v - min_v) if max_v != min_v else 1.0

        def _map_block(x):
            norm_val = (x - min_v) / rng
            idx = min(int(norm_val * len(blocks)), len(blocks) - 1)
            return blocks[idx]

        if self.ndim == 1:
            return "".join(_map_block(x) for x in self.flatten().data)
        elif self.ndim == 2:
            return "\n".join("".join(_map_block(x) for x in row) for row in self.data)
        return str(self.data)

    def __repr__(self):
        return f"Array(shape={self.shape}, data={self.data})"


# ==============================================================================
# SECTION 2: ARRAY CREATION & NUMPY-LIKE UTILITIES
# ==============================================================================

def zeros(shape):
    """Creates an Array filled with 0.0."""
    def _create(s):
        if len(s) == 1:
            return [0.0] * s[0]
        return [_create(s[1:]) for _ in range(s[0])]
    return Array(_create(shape))

def ones(shape):
    """Creates an Array filled with 1.0."""
    return zeros(shape).apply(lambda x: 1.0)

def full(shape, value):
    """Creates an Array filled with constant value."""
    return zeros(shape).apply(lambda x: value)

def eye(n):
    """Creates an n x n identity matrix Array."""
    mat = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    return Array(mat)

def arange(start, stop=None, step=1):
    """Creates a 1D Array with evenly spaced values."""
    if stop is None:
        stop = start
        start = 0
    res = []
    curr = start
    while curr < stop:
        res.append(float(curr))
        curr += step
    return Array(res)

def linspace(start, stop, num=50):
    """Creates a 1D Array of num evenly spaced numbers."""
    if num <= 1:
        return Array([float(start)])
    step = (stop - start) / float(num - 1)
    return Array([start + i * step for i in range(num)])

def where(condition_array, x_array, y_array):
    """Selects elements from x_array where condition is True, else y_array."""
    flat_cond = condition_array.flatten().data
    flat_x = x_array.flatten().data if isinstance(x_array, Array) else [x_array] * len(flat_cond)
    flat_y = y_array.flatten().data if isinstance(y_array, Array) else [y_array] * len(flat_cond)

    res = [flat_x[i] if flat_cond[i] else flat_y[i] for i in range(len(flat_cond))]
    return Array(res).reshape(condition_array.shape)

def clip(arr, min_val, max_val):
    """Limits array values within [min_val, max_val]."""
    def _clip_val(val):
        if val < min_val: return min_val
        if val > max_val: return max_val
        return val
    return arr.apply(_clip_val)

def norm(arr, p=2):
    """Computes Lp norm of an Array."""
    flat = arr.flatten().data
    if p == 1:
        return sum(abs(x) for x in flat)
    elif p == 2:
        return sum(x ** 2 for x in flat) ** 0.5
    else:
        return sum(abs(x) ** p for x in flat) ** (1.0 / p)


# ==============================================================================
# SECTION 3: TRANSCENDENTAL & TRIGONOMETRIC MATHEMATICS
# ==============================================================================

def array_sin(arr):
    """Element-wise sine via Taylor series."""
    pi = 3.14159265358979323846
    two_pi = 2.0 * pi
    def _sin_val(x):
        x = x % two_pi
        if x > pi: x -= two_pi
        elif x < -pi: x += two_pi
        res, term, num, den = 0.0, x, x, 1.0
        for i in range(1, 30, 2):
            res += term
            num *= -1.0 * x * x
            den *= (i + 1) * (i + 2)
            term = num / den
        return res
    return arr.apply(_sin_val)

def array_cos(arr):
    """Element-wise cosine via Taylor series."""
    pi = 3.14159265358979323846
    two_pi = 2.0 * pi
    def _cos_val(x):
        x = x % two_pi
        if x > pi: x -= two_pi
        elif x < -pi: x += two_pi
        res, term, num, den = 0.0, 1.0, 1.0, 1.0
        for i in range(0, 30, 2):
            res += term
            num *= -1.0 * x * x
            den *= (i + 1) * (i + 2)
            term = num / den
        return res
    return arr.apply(_cos_val)

def array_tan(arr):
    """Element-wise tangent."""
    s = array_sin(arr)
    c = array_cos(arr)
    def _div(a, b):
        if abs(b) < 1e-12: raise ValueError("Tangent undefined (div by 0).")
        return a / b
    return Array([_div(a, b) for a, b in zip(s.flatten().data, c.flatten().data)]).reshape(arr.shape)

def array_exp(arr):
    """Element-wise exponential e^x."""
    def _exp_val(x):
        res, term = 1.0, 1.0
        for i in range(1, 30):
            term *= x / i
            res += term
        return res
    return arr.apply(_exp_val)

def array_ln(arr):
    """Element-wise natural log."""
    e = 2.71828182845904523536
    def _ln_val(x):
        if x <= 0: raise ValueError("Natural log undefined for non-positive values.")
        k = 0
        while x > 1.5: x /= e; k += 1
        while x < 0.5: x *= e; k -= 1
        y = (x - 1.0) / (x + 1.0)
        y2 = y * y
        res, term = 0.0, y
        for i in range(1, 40, 2):
            res += term / i
            term *= y2
        return 2.0 * res + k
    return arr.apply(_ln_val)

def array_sqrt(arr):
    """Element-wise square root via Newton-Raphson."""
    def _sqrt_val(x):
        if x < 0: raise ValueError("Cannot compute sqrt of negative number.")
        if x == 0: return 0.0
        val = x
        for _ in range(20):
            val = 0.5 * (val + x / val)
        return val
    return arr.apply(_sqrt_val)


# ==============================================================================
# SECTION 4: COMPLEX NUMBERS & FAST FOURIER TRANSFORM (FFT)
# ==============================================================================

class ComplexNumber:
    """Pure Python complex number implementation."""
    def __init__(self, real=0.0, imag=0.0):
        self.real = float(real)
        self.imag = float(imag)

    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __add__(self, other):
        if isinstance(other, (int, float)): return ComplexNumber(self.real + other, self.imag)
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        if isinstance(other, (int, float)): return ComplexNumber(self.real - other, self.imag)
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        if isinstance(other, (int, float)): return ComplexNumber(self.real * other, self.imag * other)
        return ComplexNumber(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        if isinstance(other, (int, float)): return ComplexNumber(self.real / other, self.imag / other)
        denom = other.real ** 2 + other.imag ** 2
        return ComplexNumber((self.real * other.real + self.imag * other.imag) / denom,
                             (self.imag * other.real - self.real * other.imag) / denom)

    def __repr__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"({self.real} {sign} {abs(self.imag)}i)"

def fft_cooley_tukey(x_samples):
    """Cooley-Tukey Radix-2 FFT algorithm."""
    N = len(x_samples)
    if N <= 1:
        return x_samples if isinstance(x_samples[0], ComplexNumber) else [ComplexNumber(x_samples[0], 0.0)]
    if (N & (N - 1)) != 0:
        raise ValueError("FFT length must be a power of 2.")

    even = fft_cooley_tukey(x_samples[0::2])
    odd = fft_cooley_tukey(x_samples[1::2])

    combined = [ComplexNumber(0, 0)] * N
    pi = 3.14159265358979323846
    for k in range(N // 2):
        angle = -2.0 * pi * k / N
        cos_a = array_cos(Array([angle])).data[0]
        sin_a = array_sin(Array([angle])).data[0]
        twiddle = ComplexNumber(cos_a, sin_a) * odd[k]
        combined[k] = even[k] + twiddle
        combined[k + N // 2] = even[k] - twiddle
    return combined

def ifft_cooley_tukey(X_freq):
    """Inverse Fast Fourier Transform."""
    N = len(X_freq)
    conjugated = [x.conjugate() for x in X_freq]
    transformed = fft_cooley_tukey(conjugated)
    return [ComplexNumber(x.real / N, -x.imag / N) for x in transformed]


# ==============================================================================
# SECTION 5: POLYNOMIALS, QUATERNIONS & MATRIX DECOMPOSITIONS
# ==============================================================================

class Polynomial:
    """Operations for 1D Polynomials."""
    def __init__(self, coeffs):
        self.coeffs = [float(c) for c in coeffs]

    def evaluate(self, x):
        return sum(c * (x ** i) for i, c in enumerate(self.coeffs))

    def derivative(self):
        return Polynomial([i * c for i, c in enumerate(self.coeffs)][1:])

    def antiderivative(self, C=0.0):
        return Polynomial([C] + [c / (i + 1) for i, c in enumerate(self.coeffs)])

    def __repr__(self):
        terms = [f"{c}x^{i}" if i > 0 else f"{c}" for i, c in enumerate(self.coeffs) if c != 0]
        return " + ".join(terms) if terms else "0"

class Quaternion:
    """3D Spatial Rotations & Quaternions."""
    def __init__(self, w=1.0, x=0.0, y=0.0, z=0.0):
        self.w, self.x, self.y, self.z = float(w), float(x), float(y), float(z)

    def norm(self):
        return (self.w**2 + self.x**2 + self.y**2 + self.z**2) ** 0.5

    def normalize(self):
        n = self.norm()
        return Quaternion(self.w / n, self.x / n, self.y / n, self.z / n) if n != 0 else Quaternion(1,0,0,0)

    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def __mul__(self, o):
        w = self.w*o.w - self.x*o.x - self.y*o.y - self.z*o.z
        x = self.w*o.x + self.x*o.w + self.y*o.z - self.z*o.y
        y = self.w*o.y - self.x*o.z + self.y*o.w + self.z*o.x
        z = self.w*o.z + self.x*o.y - self.y*o.x + self.z*o.w
        return Quaternion(w, x, y, z)

    def rotate_point_3d(self, pt):
        p_quat = Quaternion(0, pt[0], pt[1], pt[2])
        q_norm = self.normalize()
        rotated = (q_norm * p_quat) * q_norm.conjugate()
        return [rotated.x, rotated.y, rotated.z]

def qr_decomposition_gram_schmidt(matrix_2d):
    """Computes Q and R matrices such that A = Q * R."""
    rows, cols = len(matrix_2d), len(matrix_2d[0])
    A_cols = [[matrix_2d[r][c] for r in range(rows)] for c in range(cols)]
    Q_cols = []
    R = [[0.0 for _ in range(cols)] for _ in range(cols)]

    for j in range(cols):
        v = list(A_cols[j])
        for i in range(j):
            R[i][j] = sum(Q_cols[i][k] * A_cols[j][k] for k in range(rows))
            for k in range(rows): v[k] -= R[i][j] * Q_cols[i][k]
        norm_v = sum(x ** 2 for x in v) ** 0.5
        R[j][j] = norm_v
        Q_cols.append([x / norm_v for x in v] if norm_v > 1e-12 else [0.0] * rows)

    Q = [[Q_cols[c][r] for c in range(cols)] for r in range(rows)]
    return Array(Q), Array(R)


# ==============================================================================
# SECTION 6: SOLVERS, SIGNAL PROCESSING & GRAPH THEORY
# ==============================================================================

def array_convolve_1d(signal_arr, kernel_arr):
    """1D Discrete Linear Convolution."""
    sig, ker = signal_arr.flatten().data, kernel_arr.flatten().data
    n_s, n_k = len(sig), len(ker)
    res_len = n_s + n_k - 1
    res = [0.0] * res_len
    for i in range(res_len):
        tmp = 0.0
        for j in range(n_k):
            if 0 <= i - j < n_s: tmp += sig[i - j] * ker[j]
        res[i] = tmp
    return Array(res)

def solve_ode_rk4(f, y0, t0, t_end, steps=100):
    """Solves dy/dt = f(t, y) using 4th-Order Runge-Kutta."""
    dt = (t_end - t0) / float(steps)
    t_list, y_list = [t0], [y0]
    t, y = t0, y0
    for _ in range(steps):
        k1 = f(t, y)
        k2 = f(t + 0.5 * dt, y + 0.5 * dt * k1)
        k3 = f(t + 0.5 * dt, y + 0.5 * dt * k2)
        k4 = f(t + dt, y + dt * k3)
        y += (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        t += dt
        t_list.append(t)
        y_list.append(y)
    return Array(t_list), Array(y_list)

def dijkstra_shortest_path(graph_matrix, start_node):
    """Computes shortest paths from start_node using an adjacency matrix."""
    num_nodes = len(graph_matrix)
    visited = [False] * num_nodes
    distances = [float('inf')] * num_nodes
    distances[start_node] = 0.0

    for _ in range(num_nodes):
        min_dist, u = float('inf'), -1
        for v in range(num_nodes):
            if not visited[v] and distances[v] < min_dist:
                min_dist, u = distances[v], v
        if u == -1: break
        visited[u] = True

        for v in range(num_nodes):
            w = graph_matrix[u][v]
            if w > 0 and not visited[v]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
    return Array(distances)
