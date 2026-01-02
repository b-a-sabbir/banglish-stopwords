# Banglish Stopwords

A high-performance, lightweight Python library to filter Banglish (Bengali written in Latin/English script) stopwords. It helps in cleaning text data for NLP, sentiment analysis, and machine learning projects.

## Features
- **Comprehensive Dataset:** Includes 350+ Bengali words and their popular Banglish variations.
- **Lazy Typing Support:** Handles repeated characters automatically (e.g., `naaaa` -> `na`, `hbeee` -> `hbe`).
- **High Performance:** Uses optimized sets for O(1) lookup speed.
- **Punctuation Aware:** Cleans text while respecting common punctuation.

## Installation

You can install the library using pip (after you publish it):
```bash
pip install banglish-stopwords