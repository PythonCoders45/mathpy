class Array:
    """
    Custom N-Dimensional Array class supporting element-wise operations,
    slicing, reshapes, matrix algebra, and integrated mathematical transforms.
    """
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Data must be provided as a nested Python list.")
        self.data = data
        self.shape = self._infer_shape(data)
        self.ndim = len(self.shape)
        self.size = self._calc_size(self.shape)

    # --------------------------------------------------------------------------
    # INTERNAL SHAPE & UTILITY HELPER METHODS
    # --------------------------------------------------------------------------
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
    # MATRIX MULTIPLICATION & REDUCTION OPERATIONS
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
        """Returns the sum of all elements in the array."""
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

    def __repr__(self):
        return f"Array(shape={self.shape}, data={self.data})"


# ==============================================================================
# ARRAY CREATION UTILITIES
# ==============================================================================

def zeros(shape):
    """Creates an Array of specified shape filled with 0.0."""
    def _create(s):
        if len(s) == 1:
            return [0.0] * s[0]
        return [_create(s[1:]) for _ in range(s[0])]
    return Array(_create(shape))

def ones(shape):
    """Creates an Array of specified shape filled with 1.0."""
    return zeros(shape).apply(lambda x: 1.0)

def full(shape, value):
    """Creates an Array filled with constant value."""
    return zeros(shape).apply(lambda x: value)

def eye(n):
    """Creates an n x n identity matrix Array."""
    mat = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    return Array(mat)

def arange(start, stop=None, step=1):
    """Creates a 1D Array with evenly spaced values within a given interval."""
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
    """Creates a 1D Array of num evenly spaced numbers between start and stop."""
    if num <= 1:
        return Array([float(start)])
    step = (stop - start) / float(num - 1)
    return Array([start + i * step for i in range(num)])


# ==============================================================================
# VECTORIZED TRANSCENDENTAL & TRIGONOMETRIC MATHEMATICS
# ==============================================================================

def array_sin(arr):
    """Computes element-wise sine using Taylor series expansion."""
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
    """Computes element-wise cosine using Taylor series expansion."""
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

def array_exp(arr):
    """Computes element-wise e^x."""
    def _exp_val(x):
        res, term = 1.0, 1.0
        for i in range(1, 30):
            term *= x / i
            res += term
        return res
    return arr.apply(_exp_val)

def array_sqrt(arr):
    """Computes element-wise square root via Newton-Raphson."""
    def _sqrt_val(x):
        if x < 0: raise ValueError("Cannot compute sqrt of negative number.")
        if x == 0: return 0.0
        val = x
        for _ in range(20):
            val = 0.5 * (val + x / val)
        return val
    return arr.apply(_sqrt_val)


# ==============================================================================
# INTEGRATED SIGNAL PROCESSING & DIFFERENTIAL SOLVERS
# ==============================================================================

def array_convolve_1d(signal_arr, kernel_arr):
    """Computes 1D discrete convolution between two 1D Arrays."""
    sig = signal_arr.flatten().data
    ker = kernel_arr.flatten().data
    n_s, n_k = len(sig), len(ker)
    res_len = n_s + n_k - 1
    res = [0.0] * res_len

    for i in range(res_len):
        tmp = 0.0
        for j in range(n_k):
            if 0 <= i - j < n_s:
                tmp += sig[i - j] * ker[j]
        res[i] = tmp
    return Array(res)

def solve_ode_rk4(f, y0, t0, t_end, steps=100):
    """
    Solves ODE dy/dt = f(t, y) using 4th-Order Runge-Kutta.
    Returns (t_array, y_array).
    """
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


    def to_emote(self, threshold=0.0, positive_emote="🟢", negative_emote="🔴"):
        """
        Converts array values into a visual emote map based on a threshold.
        Great for visualizing 1D or 2D signals/matrices!
        """
        def _convert(item):
            if isinstance(item, list):
                return [_convert(x) for x in item]
            return positive_emote if item >= threshold else negative_emote

        emote_data = _convert(self.data)
        
        # Pretty print 2D emote grid
        if self.ndim == 2:
            return "\n".join(" ".join(row) for row in emote_data)
        return str(emote_data)

    def heat_map(self):
        """
        Converts array values into a grayscale/intensity block visualization.
        """
        blocks = ["░", "▒", "▓", "█"]
        min_v, max_v = self.min(), self.max()
        rng = (max_v - min_v) if max_v != min_v else 1.0

        def _map_block(x):
            norm = (x - min_v) / rng
            idx = min(int(norm * len(blocks)), len(blocks) - 1)
            return blocks[idx]

        if self.ndim == 1:
            return "".join(_map_block(x) for x in self.flatten().data)
        elif self.ndim == 2:
            return "\n".join("".join(_map_block(x) for x in row) for row in self.data)
        return str(self.data)
