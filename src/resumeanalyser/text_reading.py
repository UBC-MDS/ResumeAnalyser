# Imports
import os
from docx import Document
from PyPDF2 import PdfReader

def docx_to_text(filepath):
    """
    Basic function to extract text from a Word document, given a specified file path.

    Parameters:
    filepath (str): A string containing the filepath.

    Returns:
    text (str): A string containing the extracted text.

    Example:
    >>> pdf_to_text('~/alphabet.docx')
    'abcdefghijklmnopqrstuvwxyz'
    """
    # Check that file path ends with docx
    if not filepath.lower().endswith('.docx'):
        raise ValueError("Please provide a .docx file. Consider the other functions if you want to use different file formats.")
    document = Document(filepath)
    full_text = []
    for paragraph in document.paragraphs:
        full_text.append(paragraph.text)

    return '\n'.join(full_text)

def pdf_to_text(filepath):
    """
    Basic function to extract text from a PDF file, given a specified file path.

    Parameters:
    filepath (str): A string containing the filepath.

    Returns:
    text (str): A string containing the extracted text.

    Example:
    >>> pdf_to_text('~/alphabet.pdf')
    'abcdefghijklmnopqrstuvwxyz'
    """

    return text

def website_to_text(url):
    """
    Basic function to extract text from a website, given a URL.

    Parameters:
    url (str): A string containing the filepath.

    Returns:
    text (str): A string containing the extracted text.

    Example:
    >>> website_to_text('www.alphabet.com')
    'abcdefghijklmnopqrstuvwxyz'
    """

    return text

