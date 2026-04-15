import pandas as pd
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

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
    Then it splits the text into a list of individual words and removes
    common stop words so the results are more meaningful.
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

    # Common words that don’t add much meaning
    stop_words = [
        "the", "and", "with", "in", "a", "to", "of", "for", "on",
        "is", "at", "by", "an", "be", "this", "that", "from",
        "or", "as", "it", "are", "was", "will", "has", "have","west", 
        "hartford", "zillow", "listing", "description"
    ]

    # Remove stop words
    filtered_words = []
    for word in words:
        if word not in stop_words:
            filtered_words.append(word)

    return filtered_words

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

def search_keyword_in_text(word_counts, keyword):
    """
    Looks up a keyword in the word count dictionary and returns how many times
    it appears in the full text.
    """
    keyword = keyword.lower()
    return word_counts.get(keyword, 0)

def count_listings_with_keyword(df, keyword):
    """
    Counts how many listing descriptions contain the keyword at least once.
    This helps show how common a certain term is across listings.
    """
    keyword = keyword.lower()
    count = 0

    for description in df["Full Description"].dropna():
        if keyword in description.lower():
            count += 1

    return count

def plot_top_words(top_words):
    """
    Creates a simple bar chart showing the top 10 most common words.
    This makes the text analysis easier to understand visually.
    """
    words = []
    counts = []

    for word, count in top_words:
        words.append(word)
        counts.append(count)

    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)
    plt.title("Top 10 Most Common Words in Listing Descriptions")
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

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

def get_top_words_by_category(df, category, top_n=10):
    """
    Filters listing descriptions by category and returns the most common words
    within that group. This helps compare language patterns across GOOD,
    MAYBE, and RISKY listings.
    """
    category = category.upper()

    filtered_descriptions = []

    for index, row in df.iterrows():
        if row["Category"] == category and isinstance(row["Full Description"], str):
            filtered_descriptions.append(row["Full Description"])

    if len(filtered_descriptions) == 0:
        return []

    combined_text = " ".join(filtered_descriptions)
    words = clean_and_split_text(combined_text)
    word_counts = count_words(words)

    return get_top_words(word_counts, top_n)

def plot_category_counts(df):
    """
    Creates a simple bar chart showing how many listings were labeled
    GOOD, MAYBE, and RISKY. This makes the results easier to compare visually.
    """
    category_counts = df["Category"].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(category_counts.index, category_counts.values)
    plt.title("Number of Listings by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Listings")
    plt.tight_layout()
    plt.savefig("category_counts_chart.png")
    plt.show()



def main():
    """
    This is the main app. It loads the excel file, combines and cleans the
    listing descriptions, counts word frequencies, and gives the user a menu
    of different text analysis options to choose from.
    """
    console.print(
    Panel(
        "Real Estate Listing Text Explorer\nAnalyze listing descriptions, search keywords, and compare patterns.",
        title="Mini Project 2",
        border_style="blue"
    )
)

    file_name = r"C:\Users\kstasiowska1\OneDrive - Babson College\Documents\GitHub\oim3640\mini project 2\west_hartford_zillow_database.xlsx"

    df = load_excel_data(file_name)
    df["Category"] = df["Full Description"].apply(categorize_listing)
    full_text = combine_descriptions(df)
    words = clean_and_split_text(full_text)
    word_counts = count_words(words)

    while True:
        console.print("\n[bold cyan]Menu:[/bold cyan]")
        console.print("1) Show basic stats")
        console.print("2) Show top 10 most common words")
        console.print("3) Search for a keyword")
        console.print("4) Show a bar chart of top 10 words")
        console.print("5) Show top words by category")
        console.print("6) Show category count chart")
        console.print("7) Quit")

        choice = input("Choose 1, 2, 3, 4, 5, 6, or 7: ").strip()

        if choice == "1":
            console.print("\n[bold green]--- Basic Stats ---[/bold green]")
            console.print(f"Number of listings: [bold]{len(df)}[/bold]")
            console.print(f"Total words: [bold]{len(words)}[/bold]")
            console.print(f"Unique words: [bold]{len(word_counts)}[/bold]")
            console.print()

        elif choice == "2":
            top_words = get_top_words(word_counts)

            table = Table(title="Top 10 Most Common Words")
            table.add_column("Word", style="bold blue")
            table.add_column("Count", style="bold")

            for word, count in top_words:
                table.add_row(word, str(count))

            console.print(table)
            console.print()

        elif choice == "3":
            keyword = input("Enter a keyword to search for: ").strip().lower()

            total_count = search_keyword_in_text(word_counts, keyword)
            listing_count = count_listings_with_keyword(df, keyword)

            console.print(f"\n[bold yellow]Keyword:[/bold yellow] '{keyword}'")
            console.print(f"It appears [bold]{total_count}[/bold] time(s) in the full text.")
            console.print(f"It appears in [bold]{listing_count}[/bold] listing(s).")
            console.print()

        elif choice == "4":
            top_words = get_top_words(word_counts)
            plot_top_words(top_words)
            print()

        elif choice == "5":
            category = input("Enter a category (GOOD, MAYBE, or RISKY): ").strip().upper()

            if category not in ["GOOD", "MAYBE", "RISKY"]:
                print("Invalid category. Please enter GOOD, MAYBE, or RISKY.")
            else:
                top_words = get_top_words_by_category(df, category)

                if len(top_words) == 0:
                    print(f"\nNo listings found in category '{category}'.")
                else:
                    table = Table(title=f"Top Words in {category} Listings")
                    table.add_column("Word", style="bold magenta")
                    table.add_column("Count", style="bold")

                    for word, count in top_words:
                        table.add_row(word, str(count))

                    console.print(table)
                    console.print()

        elif choice == "6":
            plot_category_counts(df)
            print()

        elif choice == "7":
            console.print("[bold green]Goodbye![/bold green]")
            break
            print()

        else:
            console.print("[bold red]Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.[/bold red]")
            print()


if __name__ == "__main__":
    main()