def SimilarityCV(text1, text2):
    """
    To calculate cosine-similarity score using CountVectorizer between two strings of text

    Parameters:
    text1 (str): First string containing the text be compared. eg. Job Description
    text2 (str): Second string containing the text be compared. eg. Resume text

    Returns:
    float: Cosine-Similarity score which shows how similar the two strings are.

    Example:
    >>> SimilarityCV("I am studying Data Science at UBC", "There are many good sources to study Data Science online")
    21.8
    """

    return


def SimilaritySpacy(text1, text2):
    """
    To calculate cosine-similarity score using Spacy embeddings between two strings of text

    Parameters:
    text1 (str): First string containing the text be compared. eg. Job Description
    text2 (str): Second string containing the text be compared. eg. Resume text

    Returns:
    float: Cosine-Similarity score which shows how semantically similar the two strings are.

    Example:
    >>> SimilaritySpacy("I am studying Data Science at UBC", "There are many good sources to study Data Science online")
    45.3
    """

    return
