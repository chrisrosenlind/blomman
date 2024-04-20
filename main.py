from utils import convert_pdf_to_docx, extract_text_from_docx, get_files_in_folder

pdf_files = get_files_in_folder("pdf/")
for file_name in pdf_files:
    docx_file = file_name.replace(".pdf", ".docx")
    convert_pdf_to_docx("pdf/" + file_name, "docx/" + docx_file)

docx_files = get_files_in_folder("docx/")
for file_name in docx_files:
    text = extract_text_from_docx("docx/" + file_name)
    print(text)
