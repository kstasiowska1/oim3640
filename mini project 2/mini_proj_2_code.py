import pandas as pd

def load_excel_data(file_name):
    """
    Opens the Excel file and returns it as a data frame.
    I keep this separate so the program can load the listing data first
    before analyzing it.
    """
    df = pd.read_excel(r"C:\Users\kstasiowska1\OneDrive - Babson College\Documents\GitHub\oim3640\mini project 2\west_hartford_zillow_database.xlsx")
    return df

def combine_descriptions(df):
    """
    Takes the full description column from the excel file, removes empty
    cells, and combines all descriptions into one string. This lets me analyze
    all listing description together.
    """
    descriptions = df["Full Description"].dropna()
    full_text = " ".join(descriptions)
    return full_text

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

def categorize_listing(description):
    """
    Looks for positive and regative real estate words in listing descriptions.
    Based on the words found, it labels the listing as GOOD, MAYBE, or RISKY.
    """
    if not isinstance(description, str):
        return "MAYBE"

    description = description.lower()

    good_words = [
        "updated", "renovated", "move-in ready", "remodeled", "spacious",
        "hardwood", "modern", "beautiful", "charming", "great location"
    ]

    risky_words = [
        "as-is", "needs work", "investor", "tlc", "repair",
        "fixer", "unfinished", "damage"
    ]

    good_score = 0
    risky_score = 0

    for word in good_words:
        if word in description:
            good_score += 1

    for word in risky_words:
        if word in description:
            risky_score += 1

    if risky_score >= 2:
        return "RISKY"
    elif good_score >= 2 and risky_score == 0:
        return "GOOD"
    else:
        return "MAYBE" 

def main():
    """
    This is the main app. It loads the text file, cleans and splits the text,
    counts word frequencies, and prints the top 10 words along with basic stats.
    It also creates a basic GOOD/MAYBE/RISKY category for each listing.
    """
    print("Real Estate Listing Text Analyzer")

    file_name = r"C:\Users\kstasiowska1\OneDrive - Babson College\Documents\GitHub\oim3640\mini project 2\west_hartford_zillow_database.xlsx"
    df = load_excel_data(file_name)

    print("\n--- Column Names ---")
    print(df.columns)

    full_text = combine_descriptions(df)
    words = clean_and_split_text(full_text)
    word_counts = count_words(words)
    top_words = get_top_words(word_counts)

    print("\n--- Basic Stats ---")
    print(f"Number of listings: {len(df)}")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(word_counts)}")

    print("\n--- Top 10 Most Common Words ---")
    for word, count in top_words:
        print(f"{word}: {count}")

    df["Category"] = df["Full Description"].apply(categorize_listing)

    print("\n--- Listing Categories ---")
    for index, row in df.iterrows():
        print(f"{row['Address']}: {row['Category']}")

    df.to_excel("updated_real_estate_analysis.xlsx", index=False)
    print("\nUpdated file saved as updated_real_estate_analysis.xlsx")

if __name__ == "__main__":
    main()