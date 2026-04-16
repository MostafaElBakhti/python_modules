import importlib

try:
    pandas = importlib.import_module("test")
    print(pandas.x)
except:
    print("error")


# import importlib

# def check_package(name):
#     try:
#         module = importlib.import_module(name)
#         return module
#     except ImportError:
#         return None
    
# packages = ["pandas", "numpy", "matplotlib", "requests"]

# for pkg in packages:
#     mod = check_package(pkg)
#     if mod:
#         print(f"[OK] {pkg}")
#     else:
#         print(f"[MISSING] {pkg}")