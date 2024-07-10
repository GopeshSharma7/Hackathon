# PDF Table Extraction Tool

This tool extracts tables from system-generated PDFs and saves them into Excel sheets.

## Summary

The PDF Table Extraction Tool leverages the PyMuPDF library to read and extract text from PDF files. It then uses a heuristic approach to identify and extract tables from the extracted text. The identified tables are saved into an Excel file using the pandas and openpyxl libraries. This solution does not rely on image conversion or third-party tools like Tabula or Camelot, making it suitable for system-generated PDFs where table structures are consistently formatted in text.

## Requirements

- Python 3.6 or higher
- `PyMuPDF` (Python wrapper for MuPDF)
- `pandas` (Data manipulation library)
- `openpyxl` (Library for reading and writing Excel files)
