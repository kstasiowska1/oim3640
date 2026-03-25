## My Project Proposal 

**What I'm building:**  
A Python text analysis app that analyzes real estate listing descriptions and finds common word patterns. The program will use real housing data and try to identify how properties are described using language.

**Why I chose this:**  
I am interested in real estate and I wanted to build on my mini project 1, which was a house flip deal analyzer. That project focused more on the numbers side (cost, profit, ROI), and this one focuses more on the qualitative side.
I thought it would be interesting to see what words show up the most in property listings and how homes are marketed. This could also connect to investing, since certain words might signal better or worse opportunities.

**Inputs:**  
I plan to use web scraping to collect real estate listings from Zillow in areas near where I live. From those listings, I will extract key information, especially the full description text.

Main inputs:
- Listing descriptions (primary focus)
- Address (for reference)
- Optional: beds, baths, price, year built (for possible future features)

**Core features:**
- Load real estate listing data (from Excel)
- Clean and process listing descriptions (lowercase, remove punctuation)
- Count word frequencies using a dictionary
- Print the top 10 most common words
- Show basic stats like:
    - total words
    - unique words
    - number of listings
- Categorize listings as GOOD/MAYBE/RISKY based on keywords in the description
- Save results back to a new Excel file

**Stretch/optional features I would like to add in the future:**
- Remove common words like “the”, “and”, etc.
- Compare descriptions across different types of properties
- Add a simple visualization (bar chart of top words)
- Use more advanced rules for categorizing listings
- Combine this project with mini project 1 (deal analyzer)

**What I don't know yet:**
- How to clean text in the simplest and most efficient way
- How to handle repeated or irrelevant words (like stop words)
- How to make the word frequency results more meaningful
- How to turn the results into a simple visualization
- How to bring in the data from Excel