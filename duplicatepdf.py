import os
import hashlib
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader

def ocr_pdf_content(file_path):
    images = convert_from_path(file_path)
    text_content = ""
    for image in images:
        text_content += pytesseract.image_to_string(image)
    return text_content

def hash_content(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def find_duplicates(pdf_directory):
    hash_dict = {}
    duplicates = []

    for root, _, files in os.walk(pdf_directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                try:
                    content = ocr_pdf_content(file_path)
                    content_hash = hash_content(content)

                    if content_hash in hash_dict:
                        duplicates.append((file_path, hash_dict[content_hash]))
                    else:
                        hash_dict[content_hash] = file_path
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    return duplicates

# Example usage
pdf_directory = "path/to/your/pdf_directory"
duplicates = find_duplicates(pdf_directory)

if duplicates:
    print("Found duplicate files:")
    for dup in duplicates:
        print(f"Duplicate: {dup[0]} and {dup[1]}")
else:
    print("No duplicates found.")