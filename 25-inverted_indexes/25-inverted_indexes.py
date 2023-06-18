import collections

def create_inverted_index(documents):
    """Creates an inverted index from a list of documents.

    Args:
        documents: A list of documents, where each document is a string.

    Returns:
        An inverted index, where the keys are words and the values are a list of document IDs that contain the word.
    """
    index = collections.defaultdict(list)
    for document in documents:
        for word in document.split():
            index[word].append(document)
     return index
