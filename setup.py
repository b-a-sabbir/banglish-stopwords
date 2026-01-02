from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="banglish-stopwords",
    version="0.1.1",
    author="Benjir Ahammed Sabbir",
    author_email="bengirahammedsabbir123@gmail.com",
    description="A high-performance library to filter Banglish stopwords from text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/b-a-sabbir/banglish-stopwords.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.6',
    install_requires=[], 
)