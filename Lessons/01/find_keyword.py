import os

import re
from pathlib import Path

import PyPDF2

# import textract ---> Cannot use due to an error while installing the packet

# start_dir: str = input("Enter the directory from which to start the search: ")
# keyword: str = input("Enter the keyword to search: ")
# output_dir: str = input("Enter the output directory: ")

def search_keyword_fileName(filename: str, string_to_search: str) -> bool:
    if (filename.lower().find(string_to_search.lower())) > -1:
        return True
    else:
        return False
    

def is_pdf(filename: str) -> bool:
    try:
        with open(filename, 'rb') as f:
            return f.read(4) == b'%PDF'
    except Exception as e:
        return False


def search_keyword_filePDF(filename: str, string_to_search: str) -> bool:
    pdf: PyPDF2.PdfReader = PyPDF2.PdfReader(filename)
    pdf_len: int = len(pdf.pages)

    for i in range(0, pdf_len):
        page: PyPDF2.PageObject = pdf.pages[i]
        page_text: str = page.extract_text().lower()
        if (page_text.find(string_to_search) > -1):
            return True
    
    return False    


def is_doc(filename: str) -> bool:
    try:
        with open(filename, 'rb') as f:
            header = f.read(8)
            return header == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
    except Exception as e:
        return False


# def search_keyword_fileDOC(filename: str, string_to_search: str) -> bool:
#     text: str = textract.process(filename).lower()
#     if(text.find(string_to_search.encode())> -1):
#         return True
#     else:
#         return False


def search_keyword_fileContent(filename: str, string_to_search: str) -> bool:
    try:
        content = Path(filename).read_text(encoding='utf-8').lower()
        return re.search(re.escape(string_to_search.lower()), content) is not None
    except Exception as e:
        return False

    


start_dir: str = "./Lezione01"
keyword: str = "Hello! Word"
output_dir: str = "."

keyword_counter: int = 0

for root, subdirs, filenames in os.walk(start_dir):
    print(f"Directory: '{root}' has {len(subdirs)} subdirs and {len(filenames)} files")

    for filename in filenames:

        full_path: str = os.path.join(root, filename)

        # Search for keyword in the filename
        print(f"Searching keyword '{keyword}' in filename '{filename}'")
        if search_keyword_fileName(filename, keyword):
            print(f"Keyword found in filename: '{filename}'")
            keyword_counter += 1

        # Search for keyword in the content of a PDF file
        if is_pdf(filename):
            print(f"Searching keyword '{keyword}' in PDF '{filename}'")
            if search_keyword_filePDF(filename, keyword):
                print(f"Keyword found in filecontent of: '{filename}'")
                keyword_counter += 1

        # Search for keyword in the content of a DOC file
        # elif is_doc(filename):
        #     print(f"Searching keyword '{keyword}' in DOC '{filename}'")
        #     if search_keyword_fileDOC(filename, keyword):
        #         print(f"Keyword found in filecontent of: '{filename}'")
        #         keyword_counter += 1

        # Search for keyword in the content of a TXT file
        else:
            print(f"Searching keyword '{keyword}' in file content of '{filename}'")
            if search_keyword_fileContent(filename, keyword):
                print(f"Keyword found in filecontent of: '{filename}'")
                keyword_counter += 1

# Page 11