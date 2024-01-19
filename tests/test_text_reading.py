from resumeanalyser.text_reading import docx_to_text
from resumeanalyser.text_reading import pdf_to_text
from resumeanalyser.text_reading import website_to_text
import pytest

docx_path = "/Users/user/git/mds/524_DSCI/resumeanalyser/tests/data/simple_text.docx"
pdf_path = "/Users/user/git/mds/524_DSCI/resumeanalyser/tests/data/simple_text_pdf.pdf"

def test_docx_extraction():
    """Tests if the text from a Word document is saved as a string."""
    test_word_text = docx_to_text(docx_path)
    assert type(test_word_text) == str, "Did not save as string."

def test_docx_accuracy():
    """Tests if the text saved from the Word document is accurately saved."""
    test_word_text = docx_to_text(docx_path)
    assert test_word_text == "This is a simple word file. Do you see this text?", "Wrong text"

def test_docx_wrong_path():
    """Tests if an exception is raised when the wrong file type is given (here, PDF instead of Word)."""
    with pytest.raises(ValueError):
        docx_to_text(pdf_path)