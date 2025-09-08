#!/usr/bin/env python3
"""
Python Course Environment Verification Script
============================================

This script verifies that all required packages for the Python Course
are properly installed and working.

Run this script to ensure your environment is ready for the course.
"""

import sys
import importlib

def test_import(package_name, display_name=None):
    """Test if a package can be imported and get its version."""
    if display_name is None:
        display_name = package_name
    
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'Unknown version')
        print(f"✅ {display_name}: {version}")
        return True
    except ImportError as e:
        print(f"❌ {display_name}: FAILED - {e}")
        return False

def main():
    """Run comprehensive environment tests."""
    print("=" * 60)
    print("🐍 PYTHON COURSE ENVIRONMENT VERIFICATION")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print()
    
    # Test results tracking
    results = []
    
    print("📦 CORE DATA SCIENCE PACKAGES")
    print("-" * 40)
    results.append(test_import("numpy", "NumPy"))
    results.append(test_import("pandas", "Pandas"))
    results.append(test_import("scipy", "SciPy"))
    print()
    
    print("🤖 MACHINE LEARNING PACKAGES")
    print("-" * 40)
    results.append(test_import("sklearn", "Scikit-learn"))
    results.append(test_import("xgboost", "XGBoost"))
    results.append(test_import("lightgbm", "LightGBM"))
    print()
    
    print("📊 VISUALIZATION PACKAGES")
    print("-" * 40)
    results.append(test_import("matplotlib", "Matplotlib"))
    results.append(test_import("seaborn", "Seaborn"))
    results.append(test_import("plotly", "Plotly"))
    results.append(test_import("bokeh", "Bokeh"))
    print()
    
    print("🔧 JUPYTER ENVIRONMENT")
    print("-" * 40)
    results.append(test_import("jupyter", "Jupyter"))
    results.append(test_import("ipywidgets", "IPython Widgets"))
    print()
    
    print("🧪 DEVELOPMENT TOOLS")
    print("-" * 40)
    results.append(test_import("pytest", "Pytest"))
    results.append(test_import("black", "Black"))
    results.append(test_import("flake8", "Flake8"))
    print()
    
    # Summary
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"🎉 SUCCESS: All {total} packages are working correctly!")
        print("✅ Your Python Course environment is ready!")
        print("📚 You can now run all course modules without issues.")
        return 0
    else:
        print(f"⚠️  WARNING: {total - passed} out of {total} packages failed.")
        print("❌ Please install missing packages before starting the course.")
        print("💡 Run: pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
