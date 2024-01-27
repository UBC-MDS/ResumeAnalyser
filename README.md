# resumeanalyser

[![Documentation Status](https://readthedocs.org/projects/resume-analyser/badge/?version=latest)](https://resume-analyser.readthedocs.io/en/latest/?badge=latest)

The ResumeAnalyser package is a comprehensive toolkit designed for automated and efficient parsing, analysis, and evaluation of resumes. Leveraging advanced algorithms, it extracts key information like educational background, professional experience, skills, and certifications from a variety of resume formats. This package also includes features for ranking candidates based on customizable criteria, making it an indispensable tool for HR professionals and recruiters seeking to streamline the hiring process. Its intuitive API and compatibility with multiple programming languages ensure easy integration into existing HR systems, significantly enhancing recruitment workflows.

Given the specificity of the goals of our package, we have not come across many popular Python packages which offer exactly the same functionalities we aim to offer. We found one [package which also aims to extract information from resumes](https://pypi.org/project/resume-parser/), but this package does not appear to offer functions to analyse the text and visualise the results.

## Functions
Our project has 4 parts - the extraction of text from different types of documents (PDF, HTML, docx), the cleaning of the text from these documents, the analysis of the text, and the visualisation of the analysis results. The functions under these parts are as follows:

1. Extraction of text from documents: The goal of all 3 functions under this section is to read text in from different file formats. We have chosen to focus on PDFs and docx files since resumes often come in those formats, and have also chosen to focus on extracting text from websites, where job descriptions are often hosted.
- pdf_to_text
- website_to_text
- docx_to_text

2. Cleaning of text
- tokenize: Tokenizes the input text into individual words.
- to_lower: Converts all tokens in the input list to lowercase.
- remove_stop_words: Removes stop words from the list of tokens.
- lemmatize: Applies lemmatization to each token in the list.
- clean_text: Clean text by applying a series of processing steps: tokenization, converting to lower case,
    removing stop words, and applying lemmatization.

3. Analysis of text
- SimilarityCV: Calculates cosine-similarity score using CountVectorizer between two strings of text
- SimilaritySpacy: To calculate cosine-similarity score using Spacy embeddings between two strings of text

4. Visualisation of results
- plot_wordcloud: Plots the wordcloud of the input resume text.
- plot_topwords: Plots a bar chart of word counts in the input resume text.
- plot_suite: Plots the comprehensive plot suite for the input resume text.


## Installation

```bash
$ pip install resumeanalyser
```

## Usage

`resumeanalyser` provides various functionalities. It covers text extraction from both PDF and docx documents, including handling of formatted text. The text cleaning functions include steps like removing punctuation, tokenization, converting to lower case, removing stop words, and lemmatization, which can be applied step-by-step or using the clean_text function for convenience. For comparing texts, it offers functions for both syntactic and semantic text matching. Additionally, the documentation provides examples of using plotting functions, such as creating word clouds and plotting top-frequency words. This comprehensive guide is designed to help users effectively utilize the resumeanalyser package for analyzing and visualizing resume data.

```python
from resumeanalyser.text_reading import pdf_to_text, docx_to_text
from resumeanalyser.text_cleaning import remove_punctuation, tokenize, to_lower, lemmatize, clean_text
from resumeanalyser.metrics import SimilarityCV
from resumeanalyser.plotting import plot_wordcloud, plot_topwords, plot_suite

file_path_1 = "test.txt"  # path to your file
file_path_2 = "test2.txt"  # path to your file
sample_pdf_text = pdf_to_text(file_path_1)
sample_docx_text = docx_to_text(file_path_2)
cleaned_text_1 = clean_text(sample_pdf_text)
cleaned_text_2 = clean_text(sample_docx_text)
literal_match_score = SimilarityCV(cleaned_text_1, cleaned_text_2)
fig1 = plot_wordcloud(cleaned_text_1)
fig2 = plot_topwords(cleaned_text_1)
fig3 = plot_suite(cleaned_text_1)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`resumeanalyser` was created by group14. It is licensed under the terms of the MIT license.

## Credits

`resumeanalyser` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
