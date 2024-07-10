import fitz  
import pandas as pd
import re
def extract_text_from_page(page):
    """Extracts text from a PDF page."""
    text = page.get_text("text")
    return text

def extract_tables_from_text(text):
    """Extracts tables from text based on common table structure patterns."""
    tables = []
    lines = text.split('\n')
    table = []
    for line in lines:
        # Check if the line resembles a table row (simple heuristic)
        if re.match(r'(\S+\s+)+\S+', line):
            table.append(line.split())
        elif table:
            tables.append(table)
            table = []
    if table:
        tables.append(table)
    return tables

def save_tables_to_excel(tables, output_path):
    """Saves tables to an Excel file."""
    with pd.ExcelWriter(output_path) as writer:
        for i, table in enumerate(tables):
            df = pd.DataFrame(table)
            df.to_excel(writer, sheet_name=f'Table_{i+1}', index=False)

def main(pdf_path, output_path):
    pdf_document = fitz.open(pdf_path)
    all_tables = []
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = extract_text_from_page(page)
        tables = extract_tables_from_text(text)
        all_tables.extend(tables)

    if all_tables:
        save_tables_to_excel(all_tables, output_path)
        print(f"Tables extracted successfully and saved to {output_path}")
    else:
        print("No tables found in the PDF.")

if __name__ == "__main__":
    pdf_path = "/Users/sharmag/Desktop/ScoreMe/assignment/myenv/test5.pdf"
    output_path = "/Users/sharmag/Desktop/ScoreMe/assignment/myenv/output5.xlsx"
    main(pdf_path, output_path)
