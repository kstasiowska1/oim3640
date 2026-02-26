## My Project Proposal

**What I'm building:** A Python app that evaluates whether a house flip is financially worth doing based on user inputs.

**Why I chose this:** I’m interested in real estate and house flipping, and I want a simple tool to quickly analyze potential deals before spending time researching them further.

**Core features:**
- Ask the user for basic house flip inputs (purchase price, repair costs, expected sale price)
- Calculate total project cost, estimated profit, and ROI
- Estimate selling costs using a simple percentage
- Provide a clear deal rating (Good / Maybe / Risky) with explanations
- Allow the user to analyze multiple deals in one session

**What I don't know yet:**
- How to validate user input so the program doesn’t crash
- How to structure the program cleanly using functions
- How to improve realism without making the math too complicated
- How to organize and track improvements as the project grows

**After getting feedback, I will implement the following changes:**
- Add a welcome that introduces the app and what it does before it prompts the user
- From AI:
    - Add Selling Costs: Update calculate_flip() to include selling costs (e.g., 6% of sell_price) for realism. Modify profit calculation accordingly. This addresses your proposal's "Estimate selling costs using a simple percentage."
    - Enhance Rating: Make it consistent with generated (check profit>0 first, use 15%/5% thresholds). Keep the reasons list for clarity.
    - Add Welcome and Session Summary: Add a welcome message at the start of main(). Store deals in a list (e.g., append dicts) and print a summary (e.g., "Analyzed X deals") when quitting. This improves user experience without complexity.
    - Improve Input Validation: Add min_value checks in get_number() to prevent negatives (e.g., if value < 0, retry).
    - Minor Tweaks: Change menu to y/n for deals (simpler than 1/2). Add docstrings if missing. Test with edge cases (e.g., zero profit, high ROI).
    - Tracking Improvements: As per your unknowns, use Git commits for changes and consider a CHANGELOG.md in the project folder for growth.