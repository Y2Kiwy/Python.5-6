import os
import re
from pathlib import Path
import PyPDF2

# import textract ---> Cannot use due to an error while installing the package

start_dir: str = input("Enter the directory from which to start the search: ")
keyword: str = input("Enter the keyword to search: ")
output_dir: str = input("Enter the output directory: ")

def search_keyword_fileName(filename: str, string_to_search: str) -> bool:
    return string_to_search.lower() in filename.lower()
    
def is_pdf(filename: str) -> bool:
    try:
        with open(filename, 'rb') as f:
            header = f.read(4)
            return header == b'%PDF'
    except Exception:
        return False

def search_keyword_filePDF(filename: str, string_to_search: str) -> bool:
    try:
        pdf = PyPDF2.PdfReader(filename)
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text and string_to_search.lower() in page_text.lower():
                return True
    except Exception:
        pass
    return False    

def is_doc(filename: str) -> bool:
    try:
        with open(filename, 'rb') as f:
            header = f.read(8)
            return header == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
    except Exception:
        return False

# def search_keyword_fileDOC(filename: str, string_to_search: str) -> bool:
#     text: str = textract.process(filename).lower()
#     if(text.find(string_to_search.encode()) > -1):
#         return True
#     else:
#         return False

def search_keyword_fileContent(filename: str, string_to_search: str) -> bool:
    try:
        content = Path(filename).read_text(encoding='utf-8').lower()
        return re.search(re.escape(string_to_search.lower()), content) is not None
    except Exception:
        return False

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
        if is_pdf(full_path):
            print(f"Searching keyword '{keyword}' in PDF '{filename}'")
            if search_keyword_filePDF(full_path, keyword):
                print(f"Keyword found in PDF: '{filename}'")
                keyword_counter += 1

        # Search for keyword in the content of a DOC file
        # elif is_doc(filename):
        #     print(f"Searching keyword '{keyword}' in DOC '{filename}'")
        #     if search_keyword_fileDOC(filename, keyword):
        #         print(f"Keyword found in DOC: '{filename}'")
        #         keyword_counter += 1

        # Search for keyword in the content of a TXT file
        else:
            print(f"Searching keyword '{keyword}' in file content of '{filename}'")
            if search_keyword_fileContent(full_path, keyword):
                print(f"Keyword found in file content of: '{filename}'")
                keyword_counter += 1

print(f"Total keyword occurrences: {keyword_counter}")

# Page 11 of 'CercaStringaStepByStep.pdf'
