import pdfextract
import os

files = os.listdir("pdf/")
if len(files) > 0:
    for file in files:
        txt = file.replace("pdf", "txt")
        pdfextract.create_txt("pdf/" + file, "txt/" + txt)
else:
    print("No files in dir.")
