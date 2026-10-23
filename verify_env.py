import sys

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}\n")

libraries = [
    "numpy",
    "pandas",
    "scipy",
    "sklearn",
    "matplotlib",
    "seaborn",
    "xgboost",
    "lightgbm",
    "statsmodels",
    "openpyxl",
    "joblib",
    "ipykernel",
    "tqdm"
]

print("Verifying installed libraries:")
all_ok = True
for lib in libraries:
    try:
        mod = __import__(lib)
        version = getattr(mod, "__version__", "installed")
        print(f"  [OK]   {lib:15} : {version}")
    except Exception as e:
        print(f"  [FAIL] {lib:15} : {e}")
        all_ok = False

if all_ok:
    print("\nAll ML libraries successfully imported!")
else:
    print("\nSome libraries failed to import.")
