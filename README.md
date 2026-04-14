# ColabMediaSuite 🚀
[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://pypi.org/project/ColabMediaSuite/)
[![Version](https://img.shields.io/badge/version-0.0-blue.svg)](https://pypi.org/project/ColabMediaSuite/)
[![License](https://img.shields.io/github/license/ThauhidMahmud/ColabMediaSuite.svg)](https://github.com/ThauhidMahmud/ColabMediaSuite/blob/main/LICENSE)

---

## 🚀 ColabMediaSuite

**ColabMediaSuite** is a lightweight Python library designed for Data Scientists and Jupyter Notebook users. It allows you to seamlessly render live websites and embed YouTube videos directly within your `.ipynb` environment (Jupyter Notebook, JupyterLab, Google Colab).

👉 No more switching tabs—view everything right next to your code.
**ColabMediaSuite** is a lightweight Python library designed for Data Scientists and Jupyter Notebook users. It allows you to seamlessly render live websites and embed YouTube videos directly within your `.ipynb` environment (Jupyter Notebook, JupyterLab, Google Colab).

Stop switching tabs to read documentation or watch tutorials—view them right next to your code!

---

## ✨ Features

- **🌐 Website Rendering:** Render any HTTPS website directly in an output cell.
- **▶️ YouTube Integration:** intelligent parsing of YouTube URLs to embed the video player automatically.
- **📏 Customizable:** easily adjust width, height, and alignment of the viewport.
- **⚡ Lightweight:** Zero heavy dependencies; built on top of standard IPython display tools.

---

## 📦 Installation

You can install ColabMediaSuite via pip:

```bash
pip install ColabMediaSuite
```

```python
from NexusViewPro.youtube import render_youtube_video

render_youtube_video("https://www.youtube.com/watch?v=h25pePMdoPA&t=712s")
```

```python
from NexusViewPro.site import render_site

render_site("https://www.google.com")
```

# How to Install this package in Your System

```bash
conda create -n colabMediaSuite_env python=3.8 -y
```

```bash
conda activate colabMediaSuite_env
```

```bash
pip install -r requirements_dev.txt
```