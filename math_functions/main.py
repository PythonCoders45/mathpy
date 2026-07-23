
SCALE = 10**30

def to_float(scaled_val):
    """Utility function to convert 30-digit fixed-point integer back to float."""
    return scaled_val / 1e30

# ------------------------------------------------------------------------------
# MATHEMATICAL CONSTANTS
# ------------------------------------------------------------------------------

# Archimedes' constant pi
PI = 3141592653589793238462643383279

# Euler's number e
E = 2718281828459045235360287471352

# Golden ratio (phi)
PHI = 1618033988749894848204586834365

# Euler-Mascheroni constant (gamma)
EULER_MASCHERONI = 577215664901532860606512090082

# Catalan's constant
CATALAN = 915965594177219015054603514932

# Apery's constant zeta(3)
APERY = 1202056903159594285399738161511

# Glaisher-Kinkelin constant (A)
GLAISHER = 1282427129100622636875342568869

# Khinchin's constant
KHINCHIN = 2685452001065306445309714835481

# Twin prime constant
TWIN_PRIME = 660161815846861953927202150381

# Mertens constant
MERTENS = 315718432053890529285038318182

# Meissel-Mertens constant
MEISSEL_MERTENS = 261497212847642783755426838608

# Sierpinski constant K
SIERPINSKI = 258498175957925321706589358738

# Cahen's constant
CAHEN = 643410546288338026182254307757

# Landau-Ramanujan constant
LANDAU_RAMANUJAN = 764223653589220662990698731250

# Bernstein's constant
BERNSTEIN = 280169499023869133036436491230

# Gauss's constant G
GAUSS_CONSTANT = 834626841674073186281429732799

# Ramanujan-Soldner constant
RAMANUJAN_SOLDNER = 145136923488338105028396848589

# Backhouse's constant
BACKHOUSE = 145607494858268967139959535111

# Viswanath's constant
VISWANATH = 113198824000100000000000000000

# Conway's constant (look-and-say)
CONWAY = 130357726903429639125709911215

# Plastic ratio (rho)
PLASTIC_RATIO = 132471795724474602596090885447

# Silver ratio (delta_S)
SILVER_RATIO = 241421356237309504880168872420

# Supergolden ratio
SUPERGOLDEN_RATIO = 146557123187676802665673122521

# Tribonacci constant
TRIBONACCI = 183928675521416113255185256465

# Kepler-Bouwkamp constant
KEPLER_BOUWKAMP = 114942044853296200701040157469

# Universal parabolic constant
UNIVERSAL_PARABOLIC = 229558714939263807403429804918

# Lemniscate constant varpi
LEMNISCATE = 262205755429211981046483958989

# Feigenbaum constant delta
FIRST_FEIGENBAUM = 466920160910299067185320382046

# Feigenbaum constant alpha
SECOND_FEIGENBAUM = 250290787509589282228390287321

# Brun's constant for twin primes B2
BRUN_TWIN_PRIMES = 190216058310400000000000000000

# Brun's constant for prime quadruplets B4
BRUN_PRIME_QUADS = 87058838000000000000000000000

# Golden angle in radians
GOLDEN_ANGLE = 239996322972808836372319088126

# Square root of e
EULER_NUMBER_SQRT = 164872127070012814684865078781

# Natural logarithm of 2
LN_2 = 693147180559945309417232121458

# Natural logarithm of 10
LN_10 = 2302585092994045684017991454684

# Base-2 logarithm of e
LOG2_E = 1442695040888963407359924681001

# Base-10 logarithm of e
LOG10_E = 434294481903251827651128918916

# Square root of 2
SQRT_2 = 1414213562373095048801688724209

# Square root of 3
SQRT_3 = 1732050807568877293527446341505

# Square root of 5
SQRT_5 = 2236067977499789696409173668731

# Square root of 6
SQRT_6 = 2449489742783178098197284074705

# Square root of 7
SQRT_7 = 2645751311064590590501615753639

# Square root of 8
SQRT_8 = 2828427124746190097603377448419

# Square root of 10
SQRT_10 = 3162277660168379331998893544432

# Cube root of 2
CUBE_ROOT_2 = 1259921049894873164767210607278

# Cube root of 3
CUBE_ROOT_3 = 1442249570307408382321638310780

# Riemann zeta function zeta(2)
ZETA_2 = 1644934066848226436472415166646

# Riemann zeta function zeta(4)
ZETA_4 = 1082323233711138191516003696541

# Riemann zeta function zeta(5)
ZETA_5 = 1036927755143369926331365486457

# Riemann zeta function zeta(7)
ZETA_7 = 1008349277381922826839797549849

# Dirichlet beta function beta(2)
DIRICHLET_BETA_2 = 915965594177219015054603514932

# Dirichlet beta function beta(3)
DIRICHLET_BETA_3 = 968946146259369380483634845876

# Ramanujan's constant e^(pi*sqrt(163))
RAMANUJAN_CONSTANT = 2625374126407687439999999999992

# Gelfond's constant e^pi
E_TO_PI = 2314069263277926900572908636794

# pi^e
PI_TO_E = 2245915771836104547342715220454

# i^i = e^(-pi/2)
I_TO_I = 207879576350761908546955619834

# Porter's constant
PORTER_CONSTANT = 146707807943397547289779848564

# Erdos-Borwein constant
ERDOS_BORWEIN = 160669515241529176378330152319

# Nielsen-Ramanujan constant
NIELSEN_RAMANUJAN = 822467033424113218236207583323

# Lochs' constant
LOCHS_CONSTANT = 970270140134440785121404101867

# Golomb-Dickman constant
GOLOMB_DICKMAN = 624329988543550870992936383100

# Alladi-Grinstead constant
ALLADI_GRINSTEAD = 809394020500000000000000000000

# Devroye constant
DEVROYE_CONSTANT = 1250000000000000000000000000000

# Foias constant
FOIAS_CONSTANT = 118745235112650105559404283833

# Hausdorff dimension of Cantor set
HAUSDORFF_DIM_CANTOR = 630929753571457437099527114342

# Tau constant (2*pi)
TAU = 6283185307179586476925286766559

# Half pi (pi/2)
HALF_PI = 1570796326794896619231321691639

# Quarter pi (pi/4)
QUARTER_PI = 785398163397448309615660845819

# Square root of pi
SQRT_PI = 1772453850905516027298167483341

# Base-10 logarithm of 2
LOG10_2 = 301029995663981195213738894724

# ------------------------------------------------------------------------------
# PHYSICAL & ASTRONOMICAL CONSTANTS (SI / CODATA Units)
# ------------------------------------------------------------------------------

# Speed of light in vacuum (m/s)
SPEED_OF_LIGHT = 29979245800000000000000000000000000008

# Planck constant (J s) -> 6.62607015e-34
PLANCK_CONSTANT_MANTISSA = 662607015000000000000000000000
PLANCK_CONSTANT_EXPONENT = -34

# Reduced Planck constant h-bar (J s) -> 1.054571817646156e-34
REDUCED_PLANCK_MANTISSA = 105457181764615639126242800000
REDUCED_PLANCK_EXPONENT = -34

# Gravitational constant (m^3 kg^-1 s^-2) -> 6.67430e-11
GRAVITATIONAL_CONSTANT_MANTISSA = 667430150000000000000000000000
GRAVITATIONAL_CONSTANT_EXPONENT = -11

# Elementary charge (C) -> 1.602176634e-19
ELEMENTARY_CHARGE_MANTISSA = 160217663400000000000000000000
ELEMENTARY_CHARGE_EXPONENT = -19

# Electron mass (kg) -> 9.1093837015e-31
ELECTRON_MASS_MANTISSA = 910938370152800000000000000000
ELECTRON_MASS_EXPONENT = -31

# Proton mass (kg) -> 1.67262192369e-27
PROTON_MASS_MANTISSA = 167262192369510000000000000000
PROTON_MASS_EXPONENT = -27

# Neutron mass (kg) -> 1.6749274980e-27
NEUTRON_MASS_MANTISSA = 167492749804950000000000000000
NEUTRON_MASS_EXPONENT = -27

# Avogadro constant (mol^-1) -> 6.02214076e23
AVOGADRO_CONSTANT_MANTISSA = 602214076000000000000000000000
AVOGADRO_CONSTANT_EXPONENT = 23

# Boltzmann constant (J K^-1) -> 1.380649e-23
BOLTZMANN_CONSTANT_MANTISSA = 138064900000000000000000000000
BOLTZMANN_CONSTANT_EXPONENT = -23

# Stefan-Boltzmann constant (W m^-2 K^-4) -> 5.670374419e-8
STEFAN_BOLTZMANN_MANTISSA = 567037441918442945397099670000
STEFAN_BOLTZMANN_EXPONENT = -8

# Vacuum permittivity epsilon_0 (F m^-1) -> 8.8541878128e-12
VACUUM_PERMITTIVITY_MANTISSA = 885418781281300000000000000000
VACUUM_PERMITTIVITY_EXPONENT = -12

# Vacuum permeability mu_0 (N A^-2) -> 1.2566370621e-6
VACUUM_PERMEABILITY_MANTISSA = 125663706212000000000000000000
VACUUM_PERMEABILITY_EXPONENT = -6

# Fine-structure constant (alpha)
FINE_STRUCTURE = 7297352569311000000000000000

# Inverse fine-structure constant (1/alpha)
INVERSE_FINE_STRUCTURE = 137035999084000000000000000000

# Rydberg constant (m^-1)
RYDBERG_CONSTANT = 109737315681600000000000000000000000

# Bohr radius (m) -> 5.291772109e-11
BOHR_RADIUS_MANTISSA = 529177210903800000000000000000
BOHR_RADIUS_EXPONENT = -11

# Faraday constant (C mol^-1)
FARADAY_CONSTANT = 96485332123310000000000000000000000

# Molar gas constant R (J mol^-1 K^-1)
MOLAR_GAS_CONSTANT = 831446261815324000000000000000

# Standard atmosphere (Pa)
STANDARD_ATMOSPHERE = 101325000000000000000000000000000000

# Standard acceleration of gravity (m s^-2)
STANDARD_GRAVITY = 980665000000000000000000000000

# Wien displacement constant (m K)
WIEN_DISPLACEMENT = 2897771955000000000000000000

# Hubble constant (s^-1) -> 2.184e-18
HUBBLE_CONSTANT_MANTISSA = 218400000000000000000000000000
HUBBLE_CONSTANT_EXPONENT = -18

# Astronomical unit (m)
ASTRONOMICAL_UNIT = 1495978707000000000000000000000000000041

# Light-year (m)
LIGHT_YEAR = 946073047258080000000000000000000000000000

# Parsec (m)
PARSEC = 308567758149136730000000000000000000000000

# Solar mass (kg) -> 1.98847e30
SOLAR_MASS_MANTISSA = 198847000000000000000000000000
SOLAR_MASS_EXPONENT = 30

# Earth mass (kg) -> 5.97217e24
EARTH_MASS_MANTISSA = 597217000000000000000000000000
EARTH_MASS_EXPONENT = 24

# Solar radius (m)
SOLAR_RADIUS = 696340000000000000000000000000000000

# Earth equatorial radius (m)
EARTH_RADIUS_EQUATORIAL = 6378137000000000000000000000000000



def _parse_args(args):
    if not args:
        return []
    if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
        return list(args[0])
    return list(args)

def mean(*args):
    data = _parse_args(args)
    if not data:
        return 0.0
    return sum(data) / len(data)

def median(*args):
    data = _parse_args(args)
    if not data:
        return None
    sorted_list = sorted(data)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 != 0:
        return sorted_list[mid]
    return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0

def mode(*args):
    data = _parse_args(args)
    if not data:
        return None
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

def data_range(*args):
    data = _parse_args(args)
    if not data:
        return 0
    return max(data) - min(data)

def variance(*args, sample=True):
    data = _parse_args(args)
    if len(data) < 2:
        return 0.0
    avg = mean(data)
    sq_diff_sum = sum((x - avg) ** 2 for x in data)
    divisor = (len(data) - 1) if sample else len(data)
    return sq_diff_sum / divisor

def std_dev(*args, sample=True):
    return variance(*args, sample=sample) ** 0.5

def percentile(data, p):
    data = _parse_args((data,))
    if not data:
        return None
    if not (0 <= p <= 100):
        raise ValueError("Percentile must be between 0 and 100.")
    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * (p / 100.0)
    f = int(k)
    c = f + 1 if f + 1 < len(sorted_data) else f
    if f == c:
        return sorted_data[f]
    d0 = sorted_data[f] * (c - k)
    d1 = sorted_data[c] * (k - f)
    return d0 + d1

def iqr(*args):
    data = _parse_args(args)
    if not data:
        return 0.0
    q75 = percentile(data, 75)
    q25 = percentile(data, 25)
    return q75 - q25

def describe(*args):
    data = _parse_args(args)
    if not data:
        return {}
    return {
        "count": len(data),
        "mean": round(mean(data), 4),
        "std": round(std_dev(data), 4),
        "min": min(data),
        "25%": round(percentile(data, 25), 4),
        "50% (median)": median(data),
        "75%": round(percentile(data, 75), 4),
        "max": max(data),
        "range": data_range(data),
        "iqr": round(iqr(data), 4),
        "mode": mode(data)
    }

def sin(x, terms=10):
    x = x % (2 * 3.141592653589793)
    result = 0.0
    for n in range(terms):
        sign = (-1) ** n
        fact = 1
        for i in range(1, 2 * n + 2):
            fact *= i
        result += sign * (x ** (2 * n + 1)) / fact
    return result

def cos(x, terms=10):
    x = x % (2 * 3.141592653589793)
    result = 0.0
    for n in range(terms):
        sign = (-1) ** n
        fact = 1
        for i in range(1, 2 * n + 1):
            fact *= i
        result += sign * (x ** (2 * n)) / fact
    return result

def tan(x):
    c = cos(x)
    if abs(c) < 1e-15:
        raise ValueError("Tangent undefined for this angle.")
    return sin(x) / c

def cot(x):
    s = sin(x)
    if abs(s) < 1e-15:
        raise ValueError("Cotangent undefined for this angle.")
    return cos(x) / s

def sec(x):
    c = cos(x)
    if abs(c) < 1e-15:
        raise ValueError("Secant undefined for this angle.")
    return 1.0 / c

def csc(x):
    s = sin(x)
    if abs(s) < 1e-15:
        raise ValueError("Cosecant undefined for this angle.")
    return 1.0 / s

def asin(x, terms=20):
    if not (-1.0 <= x <= 1.0):
        raise ValueError("Domain error: asin input must be between -1 and 1.")
    result = 0.0
    for n in range(terms):
        num = 1
        den = 1
        for i in range(1, 2 * n + 1):
            num *= i
        for i in range(1, n + 1):
            den *= i
        coef = num / ((4 ** n) * (den ** 2) * (2 * n + 1))
        result += coef * (x ** (2 * n + 1))
    return result

def acos(x):
    return (3.141592653589793 / 2.0) - asin(x)

def atan(x, terms=30):
    if abs(x) <= 1.0:
        result = 0.0
        for n in range(terms):
            sign = (-1) ** n
            result += sign * (x ** (2 * n + 1)) / (2 * n + 1)
        return result
    else:
        sign_x = 1 if x > 0 else -1
        res = 3.141592653589793 / 2.0
        tail = 0.0
        for n in range(terms):
            sign = (-1) ** n
            tail += sign / ((2 * n + 1) * (x ** (2 * n + 1)))
        return sign_x * (res - (tail if x > 0 else -tail))

def sinh(x, terms=10):
    result = 0.0
    for n in range(terms):
        fact = 1
        for i in range(1, 2 * n + 2):
            fact *= i
        result += (x ** (2 * n + 1)) / fact
    return result

def cosh(x, terms=10):
    result = 0.0
    for n in range(terms):
        fact = 1
        for i in range(1, 2 * n + 1):
            fact *= i
        result += (x ** (2 * n)) / fact
    return result

def tanh(x):
    return sinh(x) / cosh(x)

def radians(degrees):
    return degrees * (3.141592653589793 / 180.0)

def degrees(rad):
    return rad * (180.0 / 3.141592653589793)

def exp(x, terms=20):
    result = 0.0
    fact = 1
    for n in range(terms):
        if n > 0:
            fact *= n
        result += (x ** n) / fact
    return result

def log(x, terms=100):
    if x <= 0:
        raise ValueError("Domain error: log undefined for non-positive numbers.")
    if x == 1:
        return 0.0
    y = (x - 1) / (x + 1)
    y_sq = y * y
    result = 0.0
    curr_y = y
    for n in range(1, terms * 2, 2):
        result += curr_y / n
        curr_y *= y_sq
    return 2.0 * result

def log10(x):
    return log(x) / log(10)

def log2(x):
    return log(x) / log(2)

def sqrt(x):
    if x < 0:
        raise ValueError("Domain error: sqrt undefined for negative numbers.")
    if x == 0:
        return 0.0
    guess = x / 2.0
    for _ in range(50):
        guess = (guess + x / guess) / 2.0
    return guess

def pow_fn(x, y):
    if x < 0 and int(y) != y:
        raise ValueError("Domain error: negative base with non-integer exponent.")
    if x == 0:
        return 0.0
    if x < 0:
        return ((-1) ** int(y)) * exp(y * log(abs(x)))
    return exp(y * log(x))

def hypot(x, y):
    return sqrt(x * x + y * y)

def asinh(x):
    return log(x + sqrt(x * x + 1))

def acosh(x):
    if x < 1:
        raise ValueError("Domain error: acosh undefined for values less than 1.")
    return log(x + sqrt(x * x - 1))

def atanh(x):
    if not (-1 < x < 1):
        raise ValueError("Domain error: atanh defined for -1 < x < 1.")
    return 0.5 * log((1 + x) / (1 - x))

def csch(x):
    sh = sinh(x)
    if abs(sh) < 1e-15:
        raise ValueError("Csch undefined for 0.")
    return 1.0 / sh

def sech(x):
    return 1.0 / cosh(x)

def coth(x):
    sh = sinh(x)
    if abs(sh) < 1e-15:
        raise ValueError("Coth undefined for 0.")
    return cosh(x) / sh

def factorial(n):
    if n < 0 or int(n) != n:
        raise ValueError("Factorial requires non-negative integer.")
    result = 1
    for i in range(2, int(n) + 1):
        result *= i
    return result

def gcd(a, b):
    a, b = abs(int(a)), abs(int(b))
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(int(a) * int(b)) // gcd(a, b)

def floor(x):
    i = int(x)
    return i if x >= i else i - 1

def ceil(x):
    i = int(x)
    return i if x <= i else i + 1

def erf(x, terms=50):
    result = 0.0
    fact = 1
    for n in range(terms):
        if n > 0:
            fact *= n
        sign = (-1) ** n
        term = (sign * (x ** (2 * n + 1))) / (fact * (2 * n + 1))
        result += term
    return result * (2.0 / (3.141592653589793 ** 0.5))

def combinations(n, r):
    if r < 0 or r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def permutations(n, r):
    if r < 0 or r > n:
        return 0
    return factorial(n) // factorial(n - r)

def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))

def relu(x):
    return max(0.0, float(x))

def leaky_relu(x, alpha=0.01):
    return float(x) if x > 0 else alpha * float(x)

def softmax(vector):
    max_val = max(vector)
    exps = [exp(x - max_val) for x in vector]
    sum_exps = sum(exps)
    return [e / sum_exps for e in exps]

def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")
    return sum(x * y for x, y in zip(v1, v2))

def vector_norm(v, p=2):
    if p <= 0:
        raise ValueError("Norm order p must be positive.")
    return sum(abs(x) ** p for x in v) ** (1.0 / p)

def euclidean_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")
    return sqrt(sum((x - y) ** 2 for x, y in zip(v1, v2)))

def manhattan_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")
    return sum(abs(x - y) for x, y in zip(v1, v2))

def chebyshev_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")
    return max(abs(x - y) for x, y in zip(v1, v2))

def cosine_similarity(v1, v2):
    dot = dot_product(v1, v2)
    norm1 = vector_norm(v1, 2)
    norm2 = vector_norm(v2, 2)
    if norm1 == 0 or norm2 == 0:
        raise ValueError("Cannot calculate cosine similarity for zero vectors.")
    return dot / (norm1 * norm2)

def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        raise ValueError("Incompatible matrix dimensions for multiplication.")
    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    n = int(abs(n))
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def fibonacci(n):
    if n < 0 or int(n) != n:
        raise ValueError("Fibonacci requires non-negative integer.")
    a, b = 0, 1
    for _ in range(int(n)):
        a, b = b, a + b
    return a

def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def geometric_mean(*args):
    data = _parse_args(args)
    if not data or any(x <= 0 for x in data):
        raise ValueError("Geometric mean requires positive numbers.")
    product = 1.0
    for x in data:
        product *= x
    return product ** (1.0 / len(data))

def harmonic_mean(*args):
    data = _parse_args(args)
    if not data or any(x <= 0 for x in data):
        raise ValueError("Harmonic mean requires positive numbers.")
    return len(data) / sum(1.0 / x for x in data)

def rms(*args):
    data = _parse_args(args)
    if not data:
        return 0.0
    return sqrt(sum(x ** 2 for x in data) / len(data))

def covariance(x_vals, y_vals, sample=True):
    if len(x_vals) != len(y_vals) or len(x_vals) < 2:
        raise ValueError("Lists must be equal length with at least two elements.")
    mean_x = mean(x_vals)
    mean_y = mean(y_vals)
    total = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, y_vals))
    divisor = (len(x_vals) - 1) if sample else len(x_vals)
    return total / divisor

def correlation(x_vals, y_vals):
    cov = covariance(x_vals, y_vals)
    std_x = std_dev(x_vals)
    std_y = std_dev(y_vals)
    if std_x == 0 or std_y == 0:
        raise ValueError("Standard deviation cannot be zero.")
    return cov / (std_x * std_y)

def skewness(*args):
    data = _parse_args(args)
    n = len(data)
    if n < 3:
        raise ValueError("Skewness requires at least 3 data points.")
    m = mean(data)
    s = std_dev(data)
    if s == 0:
        return 0.0
    return (n / ((n - 1) * (n - 2))) * sum(((x - m) / s) ** 3 for x in data)

def kurtosis(*args):
    data = _parse_args(args)
    n = len(data)
    if n < 4:
        raise ValueError("Kurtosis requires at least 4 data points.")
    m = mean(data)
    s = std_dev(data)
    if s == 0:
        return 0.0
    term1 = (n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))
    term2 = sum(((x - m) / s) ** 4 for x in data)
    term3 = (3 * ((n - 1) ** 2)) / ((n - 2) * (n - 3))
    return term1 * term2 - term3

def lerp(a, b, t):
    return a + t * (b - a)

def remap(val, in_min, in_max, out_min, out_max):
    if in_min == in_max:
        raise ValueError("Input range cannot be zero.")
    return out_min + (val - in_min) * (out_max - out_min) / (in_max - in_min)

def mse(y_true, y_pred):
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Lists must be non-empty and equal length.")
    return sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)

def mae(y_true, y_pred):
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Lists must be non-empty and equal length.")
    return sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

def binary_cross_entropy(y_true, y_pred, eps=1e-15):
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Lists must be non-empty and equal length.")
    total = 0.0
    for y, p in zip(y_true, y_pred):
        p_clamped = clamp(p, eps, 1.0 - eps)
        total += y * log(p_clamped) + (1.0 - y) * log(1.0 - p_clamped)
    return -total / len(y_true)

def softplus(x):
    return log(1.0 + exp(x))

def swish(x, beta=1.0):
    return float(x) * sigmoid(beta * float(x))

def derivative(func, x, h=1e-7):
    return (func(x + h) - func(x - h)) / (2.0 * h)

def integrate(func, a, b, n=1000):
    if n <= 0:
        raise ValueError("Subdivisions n must be positive.")
    h = (b - a) / float(n)
    total = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        total += func(a + i * h)
    return total * h

def moving_average(data, window_size):
    if window_size <= 0 or window_size > len(data):
        raise ValueError("Invalid window size.")
    result = []
    window_sum = sum(data[:window_size])
    result.append(window_sum / window_size)
    for i in range(len(data) - window_size):
        window_sum += data[i + window_size] - data[i]
        result.append(window_sum / window_size)
    return result

def exponential_moving_average(data, alpha):
    if not (0 < alpha <= 1):
        raise ValueError("Alpha must be in (0, 1].")
    if not data:
        return []
    result = [data[0]]
    for x in data[1:]:
        result.append(alpha * x + (1.0 - alpha) * result[-1])
    return result

def determinant(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square.")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0.0
    for c in range(n):
        submatrix = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(submatrix)
    return det

def matrix_inverse_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Matrix must be 2x2.")
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    return [[d / det, -b / det], [-c / det, a / det]]

def matrix_identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def convolution_1d(signal, kernel):
    n_s = len(signal)
    n_k = len(kernel)
    if n_s == 0 or n_k == 0:
        return []
    result = [0.0] * (n_s + n_k - 1)
    for i in range(n_s):
        for j in range(n_k):
            result[i + j] += signal[i] * kernel[j]
    return result

def z_score(x, mean_val, std_val):
    if std_val == 0:
        raise ValueError("Standard deviation cannot be zero.")
    return (x - mean_val) / std_val

def min_max_normalize(vector):
    if not vector:
        return []
    min_v = min(vector)
    max_v = max(vector)
    if min_v == max_v:
        return [0.0] * len(vector)
    return [(x - min_v) / (max_v - min_v) for x in vector]

def z_score_normalize(vector):
    if not vector:
        return []
    m = mean(vector)
    s = std_dev(vector)
    if s == 0:
        return [0.0] * len(vector)
    return [(x - m) / s for x in vector]

def outer_product(v1, v2):
    return [[x * y for y in v2] for x in v1]

def cross_product_3d(v1, v2):
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product requires 3-dimensional vectors.")
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

def matrix_add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have equal dimensions.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtract(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have equal dimensions.")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_scalar_multiply(matrix, scalar):
    return [[cell * scalar for cell in row] for row in matrix]

def matrix_trace(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square.")
    return sum(matrix[i][i] for i in range(n))

def matrix_hadamard(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have equal dimensions.")
    return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def gelu(x):
    return 0.5 * float(x) * (1.0 + tanh((2.0 / 3.141592653589793) ** 0.5 * (float(x) + 0.044715 * (float(x) ** 3))))

def elu(x, alpha=1.0):
    return float(x) if x > 0 else alpha * (exp(float(x)) - 1.0)

def selu(x):
    scale = 1.0507009873554804934193349852946
    alpha = 1.6732632423543772848170429916717
    return scale * (float(x) if x > 0 else alpha * (exp(float(x)) - 1.0))

def huber_loss(y_true, y_pred, delta=1.0):
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Lists must be non-empty and equal length.")
    total = 0.0
    for t, p in zip(y_true, y_pred):
        err = abs(t - p)
        if err <= delta:
            total += 0.5 * (err ** 2)
        else:
            total += delta * (err - 0.5 * delta)
    return total / len(y_true)

def log_loss(y_true, y_pred, eps=1e-15):
    return binary_cross_entropy(y_true, y_pred, eps=eps)

def gradient_descent_step(weights, gradients, learning_rate):
    if len(weights) != len(gradients):
        raise ValueError("Weights and gradients must be same length.")
    return [w - learning_rate * g for w, g in zip(weights, gradients)]

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def next_power_of_two(n):
    if n <= 0:
        return 1
    p = 1
    while p < n:
        p <<= 1
    return p

def solve_linear_2x2(A, B):
    det = determinant(A)
    if det == 0:
        raise ValueError("System has no unique solution.")
    inv = matrix_inverse_2x2(A)
    return [inv[0][0] * B[0] + inv[0][1] * B[1], inv[1][0] * B[0] + inv[1][1] * B[1]]

def simpson_integrate(func, a, b, n=1000):
    if n % 2 != 0 or n <= 0:
        raise ValueError("Subdivisions n must be an even positive integer.")
    h = (b - a) / float(n)
    total = func(a) + func(b)
    for i in range(1, n, 2):
        total += 4.0 * func(a + i * h)
    for i in range(2, n - 1, 2):
        total += 2.0 * func(a + i * h)
    return total * (h / 3.0)

def secant_method(func, x0, x1, tol=1e-7, max_iter=100):
    for _ in range(max_iter):
        f0 = func(x0)
        f1 = func(x1)
        if abs(f1 - f0) < 1e-15:
            raise ValueError("Zero division encountered in Secant method.")
        x_next = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x_next - x1) < tol:
            return x_next
        x0, x1 = x1, x_next
    return x1

def newton_method(func, x0, tol=1e-7, max_iter=100):
    x = float(x0)
    for _ in range(max_iter):
        df = derivative(func, x)
        if abs(df) < 1e-15:
            raise ValueError("Derivative near zero encountered.")
        x_next = x - func(x) / df
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return x

def bisection_method(func, a, b, tol=1e-7, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have different signs at endpoints a and b.")
    for _ in range(max_iter):
        c = (a + b) / 2.0
        if abs(func(c)) < tol or (b - a) / 2.0 < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

def runaway_variance(vector):
    if not vector:
        return 0.0
    m = mean(vector)
    return sum((x - m) ** 2 for x in vector)

def root_mean_square_error(y_true, y_pred):
    return sqrt(mse(y_true, y_pred))

def r2_score(y_true, y_pred):
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Lists must be non-empty and equal length.")
    m = mean(y_true)
    ss_tot = sum((y - m) ** 2 for y in y_true)
    ss_res = sum((y - p) ** 2 for y, p in zip(y_true, y_pred))
    if ss_tot == 0:
        return 0.0
    return 1.0 - (ss_res / ss_tot)

def adjusted_r2_score(y_true, y_pred, num_predictors):
    r2 = r2_score(y_true, y_pred)
    n = len(y_true)
    if n <= num_predictors + 1:
        raise ValueError("Sample size must be greater than num_predictors + 1.")
    return 1.0 - ((1.0 - r2) * (n - 1) / (n - num_predictors - 1))

def exponential_decay(initial_value, decay_rate, time):
    return initial_value * exp(-decay_rate * time)

def logistic_growth(t, max_val, growth_rate, t_mid):
    return max_val / (1.0 + exp(-growth_rate * (t - t_mid)))

def linear_regression(x_vals, y_vals):
    if len(x_vals) != len(y_vals) or len(x_vals) < 2:
        raise ValueError("Inputs must be equal length with at least two points.")
    m_x = mean(x_vals)
    m_y = mean(y_vals)
    num = sum((x - m_x) * (y - m_y) for x, y in zip(x_vals, y_vals))
    den = sum((x - m_x) ** 2 for x in x_vals)
    if den == 0:
        raise ValueError("X values cannot all be equal.")
    slope = num / den
    intercept = m_y - slope * m_x
    return slope, intercept

def predict_linear(x, slope, intercept):
    return slope * x + intercept

def polynomial_eval(coefficients, x):
    result = 0.0
    for coef in coefficients:
        result = result * x + coef
    return result

def poly_derivative(coefficients):
    n = len(coefficients)
    if n <= 1:
        return [0]
    return [coefficients[i] * (n - 1 - i) for i in range(n - 1)]

def poly_integrate(coefficients, constant=0.0):
    n = len(coefficients)
    result = [coefficients[i] / (n - i) for i in range(n)]
    result.append(constant)
    return result

def matrix_determinant_3x3(matrix):
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Matrix must be 3x3.")
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def matrix_inverse_3x3(matrix):
    det = matrix_determinant_3x3(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    inv = [
        [(e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det],
        [(f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det],
        [(d * h - e * g) / det, (g * b - a * h) / det, (a * e - b * d) / det]
    ]
    return inv

def solve_linear_3x3(A, B):
    inv = matrix_inverse_3x3(A)
    return [
        sum(inv[0][j] * B[j] for j in range(3)),
        sum(inv[1][j] * B[j] for j in range(3)),
        sum(inv[2][j] * B[j] for j in range(3))
    ]

def running_sum(data):
    result = []
    current = 0.0
    for x in data:
        current += x
        result.append(current)
    return result

def running_product(data):
    result = []
    current = 1.0
    for x in data:
        current *= x
        result.append(current)
    return result

def diff(data):
    if len(data) < 2:
        return []
    return [data[i] - data[i - 1] for i in range(1, len(data))]

def softmin(vector):
    neg_vec = [-x for x in vector]
    return softmax(neg_vec)

def huber_loss_gradient(y_true, y_pred, delta=1.0):
    if len(y_true) != len(y_pred):
        raise ValueError("Lists must be equal length.")
    grads = []
    for t, p in zip(y_true, y_pred):
        err = p - t
        if abs(err) <= delta:
            grads.append(err)
        else:
            grads.append(delta * (1 if err > 0 else -1))
    return grads

def smooth_step(edge0, edge1, x):
    t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)

def smoother_step(edge0, edge1, x):
    t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

def bisection_method(func, a, b, tol=1e-7, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have different signs at endpoints a and b.")
    for _ in range(max_iter):
        c = (a + b) / 2.0
        if abs(func(c)) < tol or (b - a) / 2.0 < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

def runaway_variance(vector):
    if not vector:
        return 0.0
    m = mean(vector)
    return sum((x - m) ** 2 for x in vector)

def root_mean_square_error(y_true, y_pred):
    return sqrt(mse(y_true, y_pred))

def r2_score(y_true, y_pred):
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Lists must be non-empty and equal length.")
    m = mean(y_true)
    ss_tot = sum((y - m) ** 2 for y in y_true)
    ss_res = sum((y - p) ** 2 for y, p in zip(y_true, y_pred))
    if ss_tot == 0:
        return 0.0
    return 1.0 - (ss_res / ss_tot)

def adjusted_r2_score(y_true, y_pred, num_predictors):
    r2 = r2_score(y_true, y_pred)
    n = len(y_true)
    if n <= num_predictors + 1:
        raise ValueError("Sample size must be greater than num_predictors + 1.")
    return 1.0 - ((1.0 - r2) * (n - 1) / (n - num_predictors - 1))

def exponential_decay(initial_value, decay_rate, time):
    return initial_value * exp(-decay_rate * time)

def logistic_growth(t, max_val, growth_rate, t_mid):
    return max_val / (1.0 + exp(-growth_rate * (t - t_mid)))

def linear_regression(x_vals, y_vals):
    if len(x_vals) != len(y_vals) or len(x_vals) < 2:
        raise ValueError("Inputs must be equal length with at least two points.")
    m_x = mean(x_vals)
    m_y = mean(y_vals)
    num = sum((x - m_x) * (y - m_y) for x, y in zip(x_vals, y_vals))
    den = sum((x - m_x) ** 2 for x in x_vals)
    if den == 0:
        raise ValueError("X values cannot all be equal.")
    slope = num / den
    intercept = m_y - slope * m_x
    return slope, intercept

def predict_linear(x, slope, intercept):
    return slope * x + intercept

def polynomial_eval(coefficients, x):
    result = 0.0
    for coef in coefficients:
        result = result * x + coef
    return result

def poly_derivative(coefficients):
    n = len(coefficients)
    if n <= 1:
        return [0]
    return [coefficients[i] * (n - 1 - i) for i in range(n - 1)]

def poly_integrate(coefficients, constant=0.0):
    n = len(coefficients)
    result = [coefficients[i] / (n - i) for i in range(n)]
    result.append(constant)
    return result

def matrix_determinant_3x3(matrix):
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Matrix must be 3x3.")
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def matrix_inverse_3x3(matrix):
    det = matrix_determinant_3x3(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    inv = [
        [(e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det],
        [(f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det],
        [(d * h - e * g) / det, (g * b - a * h) / det, (a * e - b * d) / det]
    ]
    return inv

def solve_linear_3x3(A, B):
    inv = matrix_inverse_3x3(A)
    return [
        sum(inv[0][j] * B[j] for j in range(3)),
        sum(inv[1][j] * B[j] for j in range(3)),
        sum(inv[2][j] * B[j] for j in range(3))
    ]

def running_sum(data):
    result = []
    current = 0.0
    for x in data:
        current += x
        result.append(current)
    return result

def running_product(data):
    result = []
    current = 1.0
    for x in data:
        current *= x
        result.append(current)
    return result

def diff(data):
    if len(data) < 2:
        return []
    return [data[i] - data[i - 1] for i in range(1, len(data))]

def softmin(vector):
    neg_vec = [-x for x in vector]
    return softmax(neg_vec)

def huber_loss_gradient(y_true, y_pred, delta=1.0):
    if len(y_true) != len(y_pred):
        raise ValueError("Lists must be equal length.")
    grads = []
    for t, p in zip(y_true, y_pred):
        err = p - t
        if abs(err) <= delta:
            grads.append(err)
        else:
            grads.append(delta * (1 if err > 0 else -1))
    return grads

def smooth_step(edge0, edge1, x):
    t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)

def smoother_step(edge0, edge1, x):
    t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

def entropy(probabilities):
    if not probabilities:
        return 0.0
    if abs(sum(probabilities) - 1.0) > 1e-5:
        raise ValueError("Probabilities must sum to 1.")
    total = 0.0
    for p in probabilities:
        if p < 0:
            raise ValueError("Probabilities must be non-negative.")
        if p > 0:
            total -= p * log2(p)
    return total

def kl_divergence(p_dist, q_dist):
    if len(p_dist) != len(q_dist):
        raise ValueError("Distributions must be of equal length.")
    total = 0.0
    for p, q in zip(p_dist, q_dist):
        if p > 0:
            if q <= 0:
                raise ValueError("q_dist must be strictly positive where p_dist > 0.")
            total += p * log(p / q)
    return total

def js_divergence(p_dist, q_dist):
    if len(p_dist) != len(q_dist):
        raise ValueError("Distributions must be of equal length.")
    m_dist = [0.5 * (p + q) for p, q in zip(p_dist, q_dist)]
    return 0.5 * kl_divergence(p_dist, m_dist) + 0.5 * kl_divergence(q_dist, m_dist)

def cross_entropy_loss(p_dist, q_dist):
    if len(p_dist) != len(q_dist):
        raise ValueError("Distributions must be of equal length.")
    total = 0.0
    for p, q in zip(p_dist, q_dist):
        if p > 0:
            if q <= 0:
                raise ValueError("q_dist must be positive.")
            total -= p * log(q)
    return total

def gini_impurity(classes):
    if not classes:
        return 0.0
    counts = {}
    for c in classes:
        counts[c] = counts.get(c, 0) + 1
    total = len(classes)
    return 1.0 - sum((count / total) ** 2 for count in counts.values())

def precision_score(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    if tp + fp == 0:
        return 0.0
    return tp / (tp + fp)

def recall_score(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    if tp + fn == 0:
        return 0.0
    return tp / (tp + fn)

def f1_score(y_true, y_pred):
    p = precision_score(y_true, y_pred)
    r = recall_score(y_true, y_pred)
    if p + r == 0:
        return 0.0
    return 2.0 * (p * r) / (p + r)

def accuracy_score(y_true, y_pred):
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Inputs must be non-empty and equal length.")
    return sum(1 for t, p in zip(y_true, y_pred) if t == p) / len(y_true)

def confusion_matrix(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    return [[tn, fp], [fn, tp]]

def min_max_scaler(data, feature_range=(0, 1)):
    if not data:
        return []
    low, high = feature_range
    min_v, max_v = min(data), max(data)
    if min_v == max_v:
        return [low] * len(data)
    return [low + (x - min_v) * (high - low) / (max_v - min_v) for x in data]

def robust_scaler(data):
    if not data:
        return []
    med = median(data)
    q75 = percentile(data, 75)
    q25 = percentile(data, 25)
    iqr_val = q75 - q25
    if iqr_val == 0:
        return [0.0] * len(data)
    return [(x - med) / iqr_val for x in data]

def binarize(data, threshold=0.0):
    return [1 if x > threshold else 0 for x in data]

def polynomial_features_1d(vector, degree=2):
    return [[x ** d for d in range(degree + 1)] for x in vector]

def standardize_matrix(matrix):
    cols = list(zip(*matrix))
    scaled_cols = []
    for col in cols:
        m = mean(col)
        s = std_dev(col)
        scaled_cols.append([(x - m) / s if s != 0 else 0.0 for x in col])
    return [list(row) for row in zip(*scaled_cols)]

def matrix_shape(matrix):
    if not matrix or not isinstance(matrix, list):
        return (0, 0)
    if not isinstance(matrix[0], list):
        return (len(matrix), 1)
    return (len(matrix), len(matrix[0]))

def matrix_zeros(rows, cols):
    return [[0.0 for _ in range(cols)] for _ in range(rows)]

def matrix_ones(rows, cols):
    return [[1.0 for _ in range(cols)] for _ in range(rows)]

def matrix_fill(rows, cols, value):
    return [[value for _ in range(cols)] for _ in range(rows)]

def matrix_flatten(matrix):
    return [elem for row in matrix for elem in row]

def matrix_reshape(flat_list, rows, cols):
    if len(flat_list) != rows * cols:
        raise ValueError("Cannot reshape array of given length into shape.")
    return [flat_list[i * cols:(i + 1) * cols] for i in range(rows)]

def matrix_vertical_stack(A, B):
    if len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have equal column counts.")
    return A + B

def matrix_horizontal_stack(A, B):
    if len(A) != len(B):
        raise ValueError("Matrices must have equal row counts.")
    return [rowA + rowB for rowA, rowB in zip(A, B)]

def matrix_power(matrix, n):
    rows, cols = matrix_shape(matrix)
    if rows != cols:
        raise ValueError("Matrix must be square.")
    result = matrix_identity(rows)
    base = matrix
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        n //= 2
    return result

def frobenius_norm(matrix):
    return sqrt(sum(cell ** 2 for row in matrix for cell in row))

def matrix_rank_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Matrix must be 2x2.")
    det = determinant(matrix)
    if det != 0:
        return 2
    if any(cell != 0 for row in matrix for cell in row):
        return 1
    return 0

def LU_decompose_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Matrix must be 2x2.")
    a, b = matrix[0]
    c, d = matrix[1]
    if a == 0:
        raise ValueError("Zero pivot encountered.")
    L = [[1.0, 0.0], [c / a, 1.0]]
    U = [[a, b], [0.0, d - (c / a) * b]]
    return L, U

def cholesky_decompose_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Matrix must be 2x2.")
    a, b = matrix[0]
    c, d = matrix[1]
    if b != c or a <= 0 or (a * d - b * c) <= 0:
        raise ValueError("Matrix must be symmetric positive-definite.")
    l11 = sqrt(a)
    l21 = b / l11
    l22 = sqrt(d - l21 ** 2)
    return [[l11, 0.0], [l21, l22]]

def eigenvalues_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Matrix must be 2x2.")
    tr = matrix_trace(matrix)
    det = determinant(matrix)
    disc = tr ** 2 - 4 * det
    if disc >= 0:
        return (tr + sqrt(disc)) / 2.0, (tr - sqrt(disc)) / 2.0
    else:
        real = tr / 2.0
        imag = sqrt(-disc) / 2.0
        return complex(real, imag), complex(real, -imag)

def gradient_descent(loss_func, init_params, lr=0.01, steps=100):
    params = list(init_params)
    for _ in range(steps):
        grads = [derivative(lambda p: loss_func(params), p) for p in params]
        params = [p - lr * g for p, g in zip(params, grads)]
    return params

def adam_optimizer_step(params, grads, m, v, t, lr=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
    new_params, new_m, new_v = [], [], []
    for p, g, m_i, v_i in zip(params, grads, m, v):
        m_t = beta1 * m_i + (1.0 - beta1) * g
        v_t = beta2 * v_i + (1.0 - beta2) * (g ** 2)
        m_hat = m_t / (1.0 - beta1 ** t)
        v_hat = v_t / (1.0 - beta2 ** t)
        p_t = p - lr * m_hat / (sqrt(v_hat) + eps)
        new_params.append(p_t)
        new_m.append(m_t)
        new_v.append(v_t)
    return new_params, new_m, new_v

def momentum_step(params, grads, velocities, lr=0.01, momentum=0.9):
    new_params, new_velocities = [], []
    for p, g, v in zip(params, grads, velocities):
        v_t = momentum * v + lr * g
        p_t = p - v_t
        new_params.append(p_t)
        new_velocities.append(v_t)
    return new_params, new_velocities

def rms_prop_step(params, grads, cache, lr=0.01, decay_rate=0.99, eps=1e-8):
    new_params, new_cache = [], []
    for p, g, c in zip(params, grads, cache):
        c_t = decay_rate * c + (1.0 - decay_rate) * (g ** 2)
        p_t = p - (lr * g) / (sqrt(c_t) + eps)
        new_params.append(p_t)
        new_cache.append(c_t)
    return new_params, new_cache

def hard_sigmoid(x):
    return clamp(0.2 * float(x) + 0.5, 0.0, 1.0)

def hard_swish(x):
    return float(x) * hard_sigmoid(x)

def mish(x):
    return float(x) * tanh(softplus(x))

def threshold_relu(x, theta=1.0):
    return float(x) if x > theta else 0.0

def exponential_linear_unit(x, alpha=1.0):
    return elu(x, alpha)

def scaled_exponential_linear_unit(x):
    return selu(x)

def binary_step(x):
    return 1.0 if x >= 0 else 0.0

def gaussian_activation(x):
    return exp(-(x ** 2))

def sinc(x):
    if x == 0:
        return 1.0
    return sin(x) / float(x)

def normalized_sinc(x):
    pi_x = 3.141592653589793 * float(x)
    return sinc(pi_x)

def pad_1d(vector, pad_width, mode="constant", constant_values=0.0):
    left, right = pad_width
    if mode == "constant":
        return [constant_values] * left + list(vector) + [constant_values] * right
    elif mode == "edge":
        if not vector:
            return []
        return [vector[0]] * left + list(vector) + [vector[-1]] * right
    else:
        raise ValueError("Unsupported padding mode.")

def max_pooling_1d(vector, pool_size, stride):
    result = []
    for i in range(0, len(vector) - pool_size + 1, stride):
        result.append(max(vector[i:i + pool_size]))
    return result

def average_pooling_1d(vector, pool_size, stride):
    result = []
    for i in range(0, len(vector) - pool_size + 1, stride):
        result.append(sum(vector[i:i + pool_size]) / float(pool_size))
    return result

def global_average_pooling_1d(vector):
    if not vector:
        return 0.0
    return sum(vector) / len(vector)

def global_max_pooling_1d(vector):
    if not vector:
        return 0.0
    return max(vector)

def dropout(vector, drop_rate=0.5, seed=42):
    if not (0 <= drop_rate < 1):
        raise ValueError("Drop rate must be in [0, 1).")
    scale = 1.0 / (1.0 - drop_rate)
    result = []
    state = seed
    for x in vector:
        state = (1103515245 * state + 12345) % (2 ** 31)
        rand_val = state / float(2 ** 31)
        if rand_val >= drop_rate:
            result.append(x * scale)
        else:
            result.append(0.0)
    return result

def layer_norm_1d(vector, eps=1e-5):
    m = mean(vector)
    s = std_dev(vector)
    return [(x - m) / (s + eps) for x in vector]

def batch_norm_1d(batch, gamma=1.0, beta=0.0, eps=1e-5):
    flat = matrix_flatten(batch)
    m = mean(flat)
    s = std_dev(flat)
    result = []
    for row in batch:
        norm_row = [gamma * ((x - m) / (s + eps)) + beta for x in row]
        result.append(norm_row)
    return result

def triangular_number(n):
    return (n * (n + 1)) // 2

def pentagonal_number(n):
    return (n * (3 * n - 1)) // 2

def hexagonal_number(n):
    return n * (2 * n - 1)

def tetrahedral_number(n):
    return (n * (n + 1) * (n + 2)) // 6

def bell_number(n):
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i][j - 1] + bell[i - 1][j - 1]
    return bell[n][0]

def catalan_number(n):
    return combinations(2 * n, n) // (n + 1)

def eulerian_number(n, k):
    if k >= n or k < 0:
        return 0
    total = 0
    for j in range(k + 2):
        sign = (-1) ** j
        total += sign * combinations(n + 1, j) * ((k + 1 - j) ** n)
    return total

def partition_number(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions[n]

def Collatz_sequence(n):
    if n <= 0:
        raise ValueError("N must be positive.")
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    else:
        return Ackermann(m - 1, Ackermann(m, n - 1))

def is_armstrong(n):
    s = str(n)
    p = len(s)
    return sum(int(c) ** p for c in s) == n

def is_perfect(n):
    if n <= 1:
        return False
    divisors = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return sum(divisors) == n

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(c) ** 2 for c in str(n))
    return n == 1

def digital_root(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def Euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def Mobius_function(n):
    if n == 1:
        return 1
    p_count = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            p_count += 1
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        p_count += 1
    return -1 if p_count % 2 != 0 else 1

def legendre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def mod_inverse(a, m):
    m0, y, x = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x

def chinese_remainder_theorem(n_list, a_list):
    total = 0
    prod = 1
    for n in n_list:
        prod *= n
    for n_i, a_i in zip(n_list, a_list):
        p = prod // n_i
        total += a_i * mod_inverse(p, n_i) * p
    return total % prod

def bernoulli_number_approx(n):
    if n % 2 != 0 and n != 1:
        return 0.0
    if n == 0:
        return 1.0
    if n == 1:
        return -0.5
    s = 0.0
    for k in range(1, 100):
        s += 1.0 / (k ** n)
    sign = (-1) ** (n // 2 + 1)
    return sign * 2.0 * factorial(n) * s / ((2.0 * 3.141592653589793) ** n)
