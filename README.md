
# ColabMediaSuite 🚀
[![PyPI version](https://img.shields.io/badge/pypi-v0.0.1-blue.svg)](https://pypi.org/project/ColabMediaSuite/)
[![License](https://img.shields.io/github/license/ThauhidMahmud/ColabMediaSuite.svg)](https://github.com/ThauhidMahmud/ColabMediaSuite/blob/main/LICENSE)

---

## 🚀 Overview

**ColabMediaSuite** is a lightweight Python library designed for Data Scientists and Jupyter Notebook users. It allows you to seamlessly render live websites and embed YouTube videos directly within your `.ipynb` environment (Jupyter Notebook, JupyterLab, Google Colab).

Stop switching tabs to read documentation or watch tutorials—view them right next to your code!

---

## ✨ Features

- **🌐 Website Rendering:** Render any HTTPS website directly in an output cell.
- **▶️ YouTube Integration:** Intelligent parsing of YouTube URLs to embed the video player automatically.
- **📏 Customizable:** Easily adjust width, height, and alignment of the viewport.
- **⚡ Lightweight:** Zero heavy dependencies; built on top of standard IPython display tools.

---

## 📦 Installation

You can install ColabMediaSuite via pip:

```bash
pip install ColabMediaSuite

from ColabMediaSuite.youtube import render_youtube_video

render_youtube_video("[https://www.youtube.com/watch?v=h25pePMdoPA](https://www.youtube.com/watch?v=h25pePMdoPA)")

from ColabMediaSuite.site import render_site

render_site("[https://www.google.com](https://www.google.com)")

conda create -n colabMediaSuite_env python=3.8 -y
conda activate colabMediaSuite_env
pip install -r requirements_dev.txt
