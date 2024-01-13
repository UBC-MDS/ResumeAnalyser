def plot_wordcloud(text):
    """Plot the wordcloud of the input resume text.
    
    Parameters
    ----------
    text : str
        Text to plot wordcloud on.

    Returns
    -------
    matplotlib.image.AxesImage
        wordcloud plot of important words.

    Examples
    --------
    >>> from resumeanalyser.plotting import plot_wordcloud
    >>> txt = 'a b c d e f g a a a a a'
    >>> plot_wordcloud(txt)
    """
    return 

def plot_topwords(text, n=10):
    """Plot a bar chart of word counts in the input resume text.
    
    Parameters
    ----------
    text : str
        Text to plot top frequency barchart on.
    n : int, optional
        Plot the top n words. By default, 10.

    Returns
    -------
    matplotlib.container.BarContainer
        Bar chart of word counts.

    Examples
    --------
    >>> from resumeanalyser.plotting import plot_topword
    >>> txt = 'a b c d e f g a a a a a'
    >>> plot_topwords(txt,n=5)
    """
    return

def plot_suite(text, n=10):
    """Plot the comprehensive plot suite for the input resume text.
    
    Parameters
    ----------
    text : str
        Text to plot suite on.
    n : int, optional
        Plot the top n words. By default, 10.

    Returns
    -------
    matplotlib.figure.Figure
        A comprehensive visualization of the resume text keywords.

    Examples
    --------
    >>> from resumeanalyser.plotting import plot_suite
    >>> txt = 'a b c d e f g a a a a a'
    >>> plot_suite(txt,n=10)
    """
    return 