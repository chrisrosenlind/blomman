import fitz
import os
import re

# We convert the PDF version of the annual reports to text files using the Xpdf and QPDF
# software programs. The conversion of PDF files to text can sometimes lead to garbled output and makes it difficult to identify tables. To deal with this, we first use the Lingua::EN::Sentence Perl module to break the text of each report into sentences. Then we remove all ―sentences‖ that do not contain at least 50% alphabetic characters, similar to Li (2008) and Miller (2010), and delete sentences where more than 20% of the characters are not alphanumeric (usually because they contain foreign language characters or symbols added by a conversion error). We also exclude lines consisting of fewer than 50 alphabetic characters, for example page headings. This procedure does not successfully delete all table labels because the PDF conversion process can separate the numbers and labels in tables into separate ―sentences.‖ This adds noise to the fog measure, which is not designed to analyze this type of content, but is appropriate to include in the other textual measures, such as comparability, under the assumption that the text in tables is widely read and includes relevant information for financial statement users. We use the Lingua::EN::Fathom module to calculate the Fog score, total word count, and document word vectors for the remaining text.


def create_txt(pdf_path, txt_path):
    doc = fitz.open(pdf_path)

    # Remove if exists
    if os.path.exists(txt_path):
        os.remove(txt_path)

    with open(txt_path, "w", encoding="utf8") as out:
        for page in doc:
            text = page.get_text()
            text = text.replace("and/or", "and or")
            # TODO - We also exclude lines consisting of fewer than 50 alphabetic characters
            # TODO - Then we remove all ―sentences‖ that do not contain at least 50% alphabetic characters
            # Regex remove redundant chars
            text = re.sub(
                r"\u2014", "",
                re.sub(
                    r"--+|\.+|=+|_+", " ",
                    re.sub(
                        r"and/or", "and or",
                        re.sub(
                            r"\s*\\n\s*", " ",
                            re.sub(
                                r"\n{3,}\s*", "\n\n",
                                re.sub(
                                    r"\s{3,}", " ",
                                    text
                                )
                            )
                        )
                    )
                )
            )

            clean_text = text.encode("utf8", "ignore").decode("utf8")
            lines = clean_text.splitlines()
            for line in lines:
                text = line.strip()
                if text:
                    out.write(line)
                    out.write('\n')

    doc.close()
