from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("text_file/*")
print(filepaths)

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for path in filepaths:

    pdf.add_page()
    print(path)

    with open(f"{path}", 'r') as file:
        text = file.read()
        print(text)
