import re

contraction_replacements = [
    [r"\bain'?t\b", "am not"],
    [r"\bwon'?t\b", "will not"],
    [r"\bcan'?t\b", "can not"],
    [r"\bdon'?t\b", "do not"],
    [r"\bshouldn'?t\b", "should not"],
    [r"\bwouldn'?t\b", "would not"],
    [r"\bcouldn'?t\b", "could not"],
    [r"\bdoesn'?t\b", "does not"],
    [r"\bisn'?t\b", "is not"],
    [r"\baren'?t\b", "are not"],
    [r"\bhaven'?t\b", "have not"],
    [r"\bhasn'?t\b", "has not"],
    [r"\bwasn'?t\b", "was not"],
    [r"\bweren'?t\b", "were not"],
    [r"\bwhat'?s\b", "what is"],
    [r"n\'t", " not"],
    [r"\'t", " not"],
    [r"\'re", " are"],
    [r"\'s", " is"],
    [r"\'d", " would"],
    [r"\'ll", " will"],
    [r"\'ve", " have"],
    [r"\'m", " am"]
]

def expand_contractions(word):
    for term in contraction_replacements:
        word = re.sub(r"\b%s\b" % term[0], term[1], word)
    return word

def clean_text(review):
    review = review.lower() # lowercase
    review = re.sub(r'[^\w\s\-\']','',review) # remove numbers and punctuations, except hyphen and apostrophe
    review = expand_contractions(review) # expand contractions
    review = re.sub(' +', ' ', review) # remove multiple spaces
    review = review.strip() # remove special characters at the ends
    return review