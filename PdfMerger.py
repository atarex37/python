from PyPDF2 import PdfMerger
import os
folder = "D:\\OneDrive\\Documents\\PDF_to_merge"
merged_file = "merged"

pdfs = os.listdir(folder)
pdfs = sorted(pdfs)
if merged_file + ".pdf" in pdfs:
    pdfs.remove(merged_file + ".pdf")
    print("info: remove previous file")

merger = PdfMerger()

if pdfs:
    for pdf in pdfs:
        pdf_path = os.path.join(folder, pdf)
        print(f"-> {pdf_path}")
        merger.append(pdf_path)
else:

    print("info : folder is empty !")

merged_file_path = os.path.join(folder, f"{merged_file}.pdf")
merger.write(merged_file_path)
merger.close()
