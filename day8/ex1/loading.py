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
    for name in missing:
        print(f"- {name}")
    print("poetry install")
    exit()


def main():
    np, _ = check_package("numpy")
    pd, _ = check_package("pandas")

    data = np.random.rand(1000)

    print("Analyzing Matrix data...")
    print(f"Processing {len(data)} data points...")

    df = pd.DataFrame(data, columns=["values"])

    plt = importlib.import_module("matplotlib.pyplot")

    print("Generating visualization...")
    plt.plot(df["values"])
    plt.title("Matrix Data")
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


main()