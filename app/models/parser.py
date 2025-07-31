import fitz
from docx import Document
from typing import List, Dict
import requests
import tempfile
import os
from urllib.parse import urlparse

def download_file(url: str) -> str:
    response = requests.get(url)
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(response.content)
    temp.close()
    return temp.name

def parse_pdf(file_path: str) -> List[Dict]:
    doc = fitz.open(file_path)
    chunks = [{"page": i+1, "text": page.get_text().strip()} for i, page in enumerate(doc)]
    doc.close()
    return chunks

def parse_docx(file_path: str) -> List[Dict]:
    doc =Document(file_path)
    return [{"paragraph": i+1, "text": para.text.strip()} for i, para in enumerate(doc.paragraphs) if para.text.strip()]

def parse_document_from_url(url: str) -> dict:
    local_path = download_file(url)
    ext = os.path.splitext(urlparse(url).path)[1].lower()

    if ext == ".pdf":
        parsed = parse_pdf(local_path)
        doc_type = "pdf"
    elif ext == ".docx":
        parsed = parse_docx(local_path)
        doc_type = "docx"
    else:
        raise ValueError("Unsupported file type")

    os.remove(local_path)
    return {"doc_type": doc_type, "chunks": parsed}
