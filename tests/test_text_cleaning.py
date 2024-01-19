import pytest
from resumeanalyser.text_cleaning import tokenize
from resumeanalyser.text_cleaning import to_lower
from resumeanalyser.text_cleaning import remove_stop_words
from resumeanalyser.text_cleaning import lemmatize
from resumeanalyser.text_cleaning import clean_text


# Test cases for tokenize
def test_tokenize_normal_sentence():
    assert tokenize("Hello, world!") == ['Hello', ',', 'world', '!']


def test_tokenize_sentence_with_numbers():
    assert tokenize("The price is $5.99!") == [
        'The', 'price', 'is', '$', '5.99', '!']


def test_tokenize_empty_string():
    assert tokenize("") == []


# Test cases for to_lower
def test_to_lower_mixed_case():
    assert to_lower(['Hello', 'WORLD']) == ['hello', 'world']


def test_to_lower_already_lower():
    assert to_lower(['hello', 'world']) == ['hello', 'world']


def test_to_lower_empty_list():
    assert to_lower([]) == []


# Test cases for remove_stop_words
def test_remove_stop_words_with_stop_words():
    assert remove_stop_words(['this', 'is', 'a', 'sample']) == ['sample']


def test_remove_stop_words_without_stop_words():
    assert remove_stop_words(['important', 'words', 'only']) == [
        'important', 'words', 'only']


def test_remove_stop_words_empty_list():
    assert remove_stop_words([]) == []


# Test cases for lemmatize
def test_lemmatize_different_forms():
    assert lemmatize(['running', 'jumps']) == ['running', 'jump']


def test_lemmatize_no_lemmatization_needed():
    assert lemmatize(['cat', 'dog']) == ['cat', 'dog']


def test_lemmatize_empty_list():
    assert lemmatize([]) == []


# Test cases for clean_text
def test_clean_text_normal_sentence():
    assert clean_text(
        "This is a sample sentence, showing off the stop words filtration.") == 'sample sentence showing stop word filtration'


def test_clean_text_different_cases_and_forms():
    assert clean_text(
        "Running fast, the JUMPING Foxes!") == 'running fast jumping fox'


def test_clean_text_empty_string():
    assert clean_text("") == ''
