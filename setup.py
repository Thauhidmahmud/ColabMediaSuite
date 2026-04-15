
import setuptools


# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()



# __version__ = "0.0.1"

# REPO_NAME = "ColabMediaSuite" 
# AUTHOR_USER_NAME = "Thauhid Mahmud"
# AUTHOR_EMAIL = "thauhidmahmud2000@gmail.com"
# SRC_REPO = "ColabMediaSuite" 




with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="ColabMediaSuite",
    version="0.0.1",
    author="Thauhid Mahmud",
    author_email="your.email@example.com",
    description="A small package for rendering media in Colab/Jupyter",
    long_description=long_description,
    long_description_content_type="text/markdown", # এই লাইনটি খুব গুরুত্বপূর্ণ
    url="https://github.com/ThauhidMahmud/ColabMediaSuite",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
