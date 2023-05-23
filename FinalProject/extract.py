import PyPDF2
import os
import re
import docx
from docx import Document
from pdfdocument.document import PDFDocument

def _clean_text(text):
    max_char_seq = 3
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,;\-_\'?()/&%$#\"!\\@£€{}\[\]+*~^<>]', '', text)
    symbols = ['.', ',', ';', '-', '_', "'", '?', '(', ')', '/', '&', '%', '$', '#', '"', '!', '\\', 
                    '@', '£', '€', '{', '[', ']', '}', '+', '*', '~', '^', '<', '>']

    pattern = r'({})'.format('|'.join('(?:{}{{{},}})'.format(re.escape(sym), max_char_seq + 1) for sym in symbols))
    cleaned_text = re.sub(pattern, '', text)
    cleaned_text = re.split(r'(\.\.\.|\.+|\?|!|\n\n)', cleaned_text)

    cleaned_text = [substring.strip() for substring in cleaned_text if substring.strip()]

    cleaned_text = [cleaned_text[index] + cleaned_text[index+1] for index in range(0, len(cleaned_text)-1, 2)]
    
    return tuple(cleaned_text)

def _extract_pdf(pdf_path):
    text = ""
    
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
            
    return _clean_text(text)

def _extract_docx(file_path):
    doc = docx.Document(file_path)
    text = ' '.join([paragraph.text for paragraph in doc.paragraphs])
    return _clean_text(text)

def _extract_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return _clean_text(text)

def extract_text(file: str) -> tuple[str, ...]:
    ext = os.path.splitext(file)[-1].lower()

    match ext:
        case ".pdf":
            return _extract_pdf(file)
        case ".docx":
            return _extract_docx(file)
        case ".txt":
            return _extract_txt(file)
        case _:
            raise Exception(("File format {} not supported").format(ext))

def join_text(sentences) -> str:
    return ' '.join(sentences)

if(__name__ == '__main__'):

    files = os.listdir("samples")
    for file in files:
        print("Extracting {}".format(file))

        try:
            text = extract_text("samples/" + file)

            with open('output/{}.txt'.format(file), 'w', encoding="utf-8") as f:
                for t in text:
                    f.write("start: " + t + " :end\n")
                    
        except Exception as e:
            print("An error occurred:\n", str(e))
        
