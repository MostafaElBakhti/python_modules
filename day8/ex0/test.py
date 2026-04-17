import importlib

try:
    module = importlib.import_module("allo")
    version = getattr(module, "__version__", "unknown")

    if version is None:
        version = importlib.metadata.version("allo")
    print(f"Module: {module}\n\n, Version: {version}")
except ImportError:
    print("Module 'allo' not found.")