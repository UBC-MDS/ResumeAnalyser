def tokenize(text):
    """
    Tokenize the input text into individual words.

    Parameters:
    text (str): A string containing the text to be tokenized.

    Returns:
    list: A list of words (tokens) extracted from the input text.

    Example:
    >>> tokenize("Hello, world!")
    ['Hello', ',', 'world', '!']
    """

    return


def to_lower(tokens):
    """
    Convert all tokens in the input list to lowercase.

    Parameters:
    tokens (list): A list of tokens (words).

    Returns:
    list: A list of tokens in lowercase.

    Example:
    >>> to_lower(['Hello', 'WORLD'])
    ['hello', 'world']
    """

    return


def remove_stop_words(tokens):
    """
    Remove stop words from the list of tokens.

    Parameters:
    tokens (list): A list of tokens (words).

    Returns:
    list: A list of tokens with stop words removed.

    Example:
    >>> remove_stop_words(['this', 'is', 'a', 'sample'])
    ['sample']
    """

    return


def lemmatize(tokens):
    """
    Apply lemmatization to each token in the list.

    Parameters:
    tokens (list): A list of tokens (words).

    Returns:
    list: A list of lemmatized tokens.

    Example:
    >>> lemmatize(['running', 'jumps'])
    ['running', 'jump']
    """

    return


def clean_text(text):
    """
    Clean text by applying a series of processing steps: tokenization, converting to lower case,
    removing stop words, and applying lemmatization.

    Parameters:
    text (str): A string containing the text to be cleaned.

    Returns:
    str: The cleaned text as a single string.

    Example:
    >>> clean_text("This is a sample sentence, showing off the stop words filtration.")
    'sample sentence showing stop word filtration'
    """

    return
