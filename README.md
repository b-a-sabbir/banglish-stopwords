# Banglish Stopwords 🇧🇩

[![PyPI version](https://badge.fury.io/py/banglish-stopwords.svg)](https://pypi.org/project/banglish-stopwords/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

**Banglish Stopwords** is a lightweight, high-performance Python library designed to filter out stopwords from Banglish text (Bengali written in Latin/English script). It includes a comprehensive dataset of **350+ Bengali words** and their common chating variations.

## ✨ Features
- **350+ Core Words:** Covers almost all common Bengali stopwords.
- **Lazy Typing Support:** Automatically handles repeated characters (e.g., `naaaa` -> `na`, `hbeee` -> `hbe`).
- **Punctuation Handling:** Smartly cleans text while keeping punctuation intact where necessary.
- **Fast Lookup:** Uses optimized Python sets for $O(1)$ performance.

## 🚀 Installation

You can install the library directly from PyPI using pip:

```bash
pip install banglish-stopwords