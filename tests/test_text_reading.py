from resumeanalyser.text_reading import docx_to_text
from resumeanalyser.text_reading import pdf_to_text
# from resumeanalyser.text_reading import website_to_text
import pytest

simple_docx_path = "/Users/user/git/mds/524_DSCI/resumeanalyser/tests/data/simple_text.docx"
simple_pdf_path = "/Users/user/git/mds/524_DSCI/resumeanalyser/tests/data/simple_text_pdf.pdf"
fancy_docx_path = "/Users/user/git/mds/524_DSCI/resumeanalyser/tests/data/fancy_text_docx.docx"
fancy_pdf_path = "/Users/user/git/mds/524_DSCI/resumeanalyser/tests/data/fancy_text_pdf.pdf"

def test_docx_extraction():
    """Tests if the text from a Word document is saved as a string."""
    test_word_text = docx_to_text(simple_docx_path)
    assert type(test_word_text) == str, "Did not save as string."

def test_docx_accuracy():
    """Tests if the text saved from the Word document is accurately saved."""
    test_word_text = docx_to_text(simple_docx_path)
    assert test_word_text == "This is a simple word file. Do you see this text?", "Wrong text"

def test_docx_wrong_path():
    """Tests if an exception is raised when the wrong file type is given (here, PDF instead of Word)."""
    with pytest.raises(ValueError):
        docx_to_text(simple_pdf_path)

def test_docx_heading():
    """Tests if the text from a Word document."""
    test_word_text = docx_to_text(fancy_docx_path)
    heading_text = "Heading 1"
    # print(heading_text)
    assert heading_text in test_word_text, "Heading text not saved."

def test_pdf_extraction():
    """Tests if the text from a PDF document is saved as a string."""
    test_pdf_text = pdf_to_text(simple_pdf_path)
    assert type(test_pdf_text) == str, "Did not save as string."

def test_pdf_accuracy():
    """Tests if the text saved from the Word document is accurately saved."""
    test_pdf_text = pdf_to_text(simple_pdf_path)
    expected_text = "This is a simple word file. Do you see this text?"
    # print(test_pdf_text)
    # print(expected_text)
    assert expected_text == test_pdf_text, "Wrong text"

def test_pdf_wrong_path():
    """Tests if an exception is raised when the wrong file type is given (here, Word instead of PDF)."""
    with pytest.raises(ValueError):
        pdf_to_text(simple_docx_path)

def test_pdf_heading():
    """Tests if the text from a Word document."""
    test_pdf_text = pdf_to_text(fancy_pdf_path)
    heading_text = "Heading 1"
    # print(heading_text)
    assert heading_text in test_pdf_text, "Heading text not saved."