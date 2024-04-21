import fitz
import os


def create_txt(pdf_path, txt_path):
    doc = fitz.open(pdf_path)

    # Remove if exists
    if os.path.exists(txt_path):
        os.remove(txt_path)

    with open(txt_path, "w", encoding="utf8") as out:
        for page in doc:
            text = page.get_text()
            clean_text = text.encode("utf8", "ignore").decode("utf8")
            lines = clean_text.splitlines()
            for line in lines:
                text = line.strip()
                if text:
                    out.write(line)
                    out.write('\n')

    doc.close()
