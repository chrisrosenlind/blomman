import pdfextract
import os

files = os.listdir("pdf/")
if len(files) > 0:
    for file in files:
        txt = file.replace("pdf", "txt")
        docx = file.replace("pdf", "docx")
        pdfextract.create_file("pdf/" + file, "txt/" + txt)
        pdfextract.create_file("pdf/" + file, "docx/" + docx)
else:
    print("No files in dir.")
