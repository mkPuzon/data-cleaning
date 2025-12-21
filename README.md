# Data Cleaning Resources
[![Python](https://img.shields.io/badge/Python-3.12.3-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)

A growing collection of notebooks and scripts to clean and preprocess data for machine learning tasks.

# Cleaning Up Data Using Pandas
Useful operations for cleaning up a Pandas DataFrame can be found in `data_pipeline.ipynb'. This notebook uses example data to walk through common operations in data processing, including normalizing data types, dealing with outliers, rectifying typos, and feature extraction.

# Extracting Text From Documents
Extracting text from formats like .pdf and .pptx can be a headache when trying to build custom AI systems. The `document_processing.ipynb` notebook shows walks through extracting information from a research paper featuring tables and diagrams that are often hard to read for LLMs. 

It compares two different packages for this task: `pypdf` and `Docling`. It also covers setting up Docling with a PostgreSQL database using pgvector.