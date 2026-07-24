from setuptools import Extension, setup

extension = Extension(
    "mathpy_advanced",
    sources=["c/mathpy_advanced.c"],
    extra_compile_args=[
        "-O3",  # Maximum compiler optimizations
        "-fopenmp",  # Enable multi-core parallel threading
        "-mavx2",  # Enable 256-bit SIMD Vector Hardware Operations
        "-mfma",  # Fused Multiply-Add instruction acceleration
    ],
    extra_link_args=["-fopenmp"],
)

setup(
    name="MathPyAdvanced",
    version="2.0",
    description="Production-grade Parallel SIMD Math Engine",
    ext_modules=[extension],
)
