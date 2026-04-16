import importlib


def check_package(name):
    try:
        package = importlib.import_module(name)
        version = getattr(package, "__version__", "unknown")
        return package, version
    except ImportError:
        return None, None


required = ["pandas", "numpy", "matplotlib"]
missing = []
all_ok = True

for pkg in required:
    module, _ = check_package(pkg)
    if not module:
        all_ok = False
        missing.append(pkg)

if not all_ok:
    print("\nMissing dependencies!")
    print("Install with:")
    print("pip install -r requirements.txt")
    print("or")
    print("poetry install")
    exit()

np, _ = check_package("numpy")
data = np.random.rand(1)
print(data)

# packages = ["math", "numpy", "something_fake"]

# for pkg in packages:
#     module, version = check_package(pkg)
#     if module:
#         print(f"[OK] {pkg} ({version})")
#     else:
#         print(f"[MISSING] {pkg} ")