from resumeanalyser.metrics import SimilarityCV
from resumeanalyser.metrics import SimilaritySpacy
import pytest

import pytest

def test_similarity_cv():
    # Test similar texts
    assert SimilarityCV("Data Science is interesting", "I find Data Science fascinating") == 50.0
    # Test different texts
    assert SimilarityCV("Python programming", "Machine learning algorithms") == 0.0
    # Test empty string inputs
    with pytest.raises(ValueError):
        SimilarityCV("", "Some text")
    with pytest.raises(ValueError):
        SimilarityCV("Non-empty text", "")
    # Test for non-string inputs
    with pytest.raises(ValueError):
        SimilarityCV(123, "Some text")

def test_similarity_spacy():
    # Test similar texts
    assert round(SimilaritySpacy("Data Science is interesting", "I find Data Science fascinating"),2) == 0.52
    # Test different texts
    assert round(SimilaritySpacy("Python programming", "Machine learning algorithms"),2) == 0.68
    # Test empty string inputs
    with pytest.raises(ValueError):
        SimilaritySpacy("", "Some text")
    with pytest.raises(ValueError):
        SimilaritySpacy("Non-empty text", "")
    # Test for non-string inputs
    with pytest.raises(ValueError):
        SimilaritySpacy(123, "Some text")
