import os 
import pdf2docx 
import docx

def convert_pdf_to_docx(pdf_path, docx_path):
    converter = pdf2docx.Converter(pdf_path)
    converter.convert(docx_path, start=0, end=None)
    converter.close()

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    full_text = []
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        # Check if entire row is not only white space chars
        if text:
            full_text.append(text)
    return "\n".join(full_text)

def get_files_in_folder(folder_path):
    files = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            files.append(file)
    return files
