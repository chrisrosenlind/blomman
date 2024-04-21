import pdfextract
import os

files = os.listdir("pdf/")
if len(files) != 0:
    for file in files:
        docx = file.replace("pdf", "docx")
        pdfextract.create_txt("pdf/" + file, "txt/" + docx)
elif len(files) == 0:
    print("No files in dir.")
