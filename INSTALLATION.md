# Python Course - Package Installation Guide

This guide provides instructions for installing all necessary packages for the Python Course modules.

## Package Requirements Summary

The course uses the following main packages:
- **Core Data Science**: NumPy, Pandas, SciPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **Jupyter Environment**: Jupyter Notebook/Lab
- **Additional Tools**: Plotly, Bokeh (optional)

## Installation Methods

### Method 1: Using pip with requirements.txt (Recommended)

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv python-course-env
   source python-course-env/bin/activate  # On Windows: python-course-env\Scripts\activate
   ```

2. **Install packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Method 2: Using conda (Alternative)

1. **Create conda environment**:
   ```bash
   conda env create -f environment.yml
   conda activate python-course
   ```

2. **Or create manually**:
   ```bash
   conda create -n python-course python=3.11
   conda activate python-course
   conda install -c conda-forge numpy pandas scipy scikit-learn matplotlib seaborn jupyter jupyterlab
   ```

### Method 3: Using specific versions (for reproducibility)

```bash
pip install -r requirements-detailed.txt
```

## Package Descriptions

### Core Packages (Required)

| Package | Purpose | Version |
|---------|---------|---------|
| `numpy` | Numerical computing foundation | >=1.21.0 |
| `pandas` | Data manipulation and analysis | >=1.3.0 |
| `scipy` | Scientific computing | >=1.7.0 |
| `scikit-learn` | Machine learning algorithms | >=1.0.0 |
| `matplotlib` | Basic plotting and visualization | >=3.5.0 |
| `seaborn` | Statistical data visualization | >=0.11.0 |
| `jupyter` | Interactive computing environment | >=1.0.0 |

### Optional Packages

| Package | Purpose | Version |
|---------|---------|---------|
| `plotly` | Interactive visualizations | >=5.0.0 |
| `bokeh` | Interactive web visualizations | >=2.4.0 |
| `xgboost` | Gradient boosting framework | >=1.5.0 |
| `lightgbm` | Light gradient boosting | >=3.2.0 |

## Module-Specific Requirements

### Module 1-2: Python Essentials
- Built-in modules only (no additional packages)

### Module 3: NumPy
- `numpy`
- `scipy` (for advanced functions)

### Module 4-6: Pandas
- `pandas`
- `numpy`

### Module 7: Visualization
- `matplotlib`
- `seaborn`
- `scipy` (for statistical functions)

### Module 8-9: Machine Learning
- `scikit-learn`
- `matplotlib` (for plotting)
- `pandas` (for data handling)
- `numpy` (for numerical operations)

### Module 10: Final Project
- All packages from previous modules

## Verification

After installation, verify your setup by running:

```python
# Test basic imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import scipy.stats

print("All packages imported successfully!")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print(f"Seaborn version: {sns.__version__}")
```

## Troubleshooting

### Common Issues

1. **ImportError: No module named 'X'**
   - Solution: Install the missing package with `pip install X`

2. **Version conflicts**
   - Solution: Use a virtual environment or conda environment

3. **Jupyter not starting**
   - Solution: Install jupyter with `pip install jupyter` or `conda install jupyter`

4. **Matplotlib backend issues**
   - Solution: Install with `pip install matplotlib[all]` or use conda

### Platform-Specific Notes

- **Windows**: Use `python -m pip install` instead of `pip install`
- **macOS**: May need to install Xcode command line tools
- **Linux**: May need to install system dependencies for matplotlib

## Environment Files

- `requirements.txt`: Basic requirements with flexible versions
- `requirements-detailed.txt`: Specific versions for reproducibility
- `environment.yml`: Conda environment specification

## Support

If you encounter issues:
1. Check Python version (3.8+ required)
2. Use virtual environment
3. Update pip: `python -m pip install --upgrade pip`
4. Check package compatibility
