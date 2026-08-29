
# Hardware & Software Requirements for Basic Machine Learning

## Hardware Requirements

### RAM (Memory)
- **Minimum:** 4 GB
- **Recommended:** 16 GB
- **Why it matters:** Most critical component for basic ML. Allows loading and working with larger datasets in memory. Scikit-learn relies heavily on RAM.

### CPU (Processor)
- **Minimum:** 1 GHz dual-core
- **Recommended:** Intel Core i5 (10th gen+) or AMD Ryzen 5
- **Why it matters:** Affects training time and data preprocessing speed. Benefits diminish after mid-range CPU.

### Storage
- **Minimum:** 5 GB free space
- **Recommended:** 256 GB SSD or larger
- **Why it matters:** SSD significantly speeds up dataset and project loading compared to HDD.

### GPU (Graphics Card)
- **Minimum:** Not required
- **Recommended:** Optional (for deep learning only)
- **Why it matters:** Provides NO performance benefit for basic ML (scikit-learn is CPU-based). Only needed for deep learning (TensorFlow/PyTorch) with computer vision or NLP.

---

## Software Requirements

### Operating System
- Windows, macOS, or Linux
- **Preferred:** Linux (Ubuntu) for better compatibility and ease of setup

### Programming Language
- **Python 3.10 or higher**

### Core Libraries

| Library | Purpose |
|:--------|:--------|
| **NumPy** | Scientific computing foundation |
| **SciPy** | Scientific computing foundation |
| **scikit-learn** | Classical ML algorithms (classification, regression, clustering) |
| **pandas** | Data manipulation, loading, and cleaning |
| **Matplotlib** | Data visualization and plotting |

### Development Environment
- **Text Editor:** VS Code, Sublime Text, or similar
- **IDE:** PyCharm
- **Interactive:** Jupyter Notebook / JupyterLab (recommended for data exploration)

---

## Quick Start Option

### Google Colab
- Free cloud-based Jupyter environment
- No local hardware setup required
- Includes access to GPUs and TPUs
- Perfect for beginners

---

## Summary Checklist

- [ ] 16 GB RAM
- [ ] Modern mid-range CPU (i5/Ryzen 5)
- [ ] SSD storage (256 GB+)
- [ ] GPU not needed for basic ML
- [ ] Python 3.10+
- [ ] Install: NumPy, SciPy, scikit-learn, pandas, Matplotlib
- [ ] Choose: VS Code, PyCharm, or Jupyter
- [ ] Option: Start with Google Colab
