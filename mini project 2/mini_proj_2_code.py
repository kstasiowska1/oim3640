
def load_text(file_name):
    """
    Opens a text file and returns all of its contents as one string.
    I keep this separate so the program can load text first before analyzing it.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

def clean_and_split_text(text):
    """
    Converts the text to lowercase and removes common punctuation.
    Then it splits the text into a list of individual words.
    """
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace("-", "")
    text = text.replace(":", "")
    text = text.replace(";", "")
    words = text.split()
    return words