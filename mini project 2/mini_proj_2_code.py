
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

def count_words(words):
    """
    Counts how many times each word appears using a dictionary.
    This makes it easy to track word frequencies across the full text.
    """
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def get_top_words(word_counts, top_n=10):
    """
    Sorts the dictionary by frequency from highest to lowest.
    It returns the top words so I can see which words appear the most.
    """
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:top_n]

#based on the words, can I categorize and listing as GOOD/OKAY/RISKY

def main():
    """
    This is the main app. It loads the text file, cleans and splits the text,
    counts word frequencies, and prints the top 10 words along with basic stats.
    """
    print("Real Estate Listing Text Analyzer")

    file_name = "real_estate_listings.txt"

    text = load_text(file_name)
    words = clean_and_split_text(text)
    word_counts = count_words(words)
    top_words = get_top_words(word_counts)

    print("\n--- Basic Stats ---")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(word_counts)}")

    print("\n--- Top 10 Most Common Words ---")
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()