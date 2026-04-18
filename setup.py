
import setuptools


# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()



# __version__ = "0.0.1"

# REPO_NAME = "ColabMediaSuite" 
# AUTHOR_USER_NAME = "Thauhid Mahmud"
# AUTHOR_EMAIL = "thauhidmahmud2000@gmail.com"
# SRC_REPO = "ColabMediaSuite" 




import setuptools

# README ফাইল থেকে লং ডেসক্রিপশন পড়া হচ্ছে
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# আপনার প্যাকেজের ভার্সন এবং অন্যান্য তথ্য
__version__ = "0.0.1"
REPO_NAME = "ColabMediaSuite"
SRC_REPO = "ColabMediaSuite"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Thauhid Mahmud",
    author_email="thauhidmahmud2000@gmail.com",
    description="A small python package for rendering media in Colab/Jupyter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/ThauhidMahmud/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "ensure==1.0.2",
        "py-youtube==1.1.7"
    ],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
