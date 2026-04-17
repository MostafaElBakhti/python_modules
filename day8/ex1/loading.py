import importlib
import sys


def check_package(name):
    try:
        package = importlib.import_module(name)
        version = getattr(package, "__version__", "unknown")
        return package, version
    except ImportError:
        return None, None


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    descriptions = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready",
    }

    required = ["pandas", "numpy", "matplotlib"]
    optional = ["requests"]

    missing = []

    for pkg in required:
        module, version = check_package(pkg)
        if module:
            print(f"[OK] {pkg} ({version}) - {descriptions[pkg]}")
        else:
            print(f"[MISSING] {pkg}")
            missing.append(pkg)

    for pkg in optional:
        module, version = check_package(pkg)
        if module:
            print(f"[OK] {pkg} ({version}) - {descriptions[pkg]}")

    if missing:
        print("\nMissing dependencies!")
        print("Install with:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit()


def main():
    np, _ = check_package("numpy")
    pd, _ = check_package("pandas")
    plt = importlib.import_module("matplotlib.pyplot")

    data = np.random.rand(1000)

    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(data)} data points...")

    df = pd.DataFrame(data, columns=["values"])

    print("Generating visualization...")
    plt.plot(df["values"])
    plt.title("Matrix Data")
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    check_dependencies()
    main()