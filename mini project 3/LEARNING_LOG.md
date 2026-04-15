## Date: 2026-04-10
**What I asked AI to do:**
- Help me understand how to structure a Flask app based on the class slides  
- Help me decide what functions I should create and where they should go  
- Explain what should go in `app.py` vs `mbta_helper.py`  
- Help me fix errors when my app was not running correctly  
- Help me set up my folder structure and required files  

**What I didn't understand in the generated code:**
- I was confused about how Flask routes work and how they connect to HTML pages  
- I didn’t fully understand how data was passed from the form to Python and then back to the results page  
- I was unsure why we separate logic into a helper file instead of keeping everything in one file  

**What I learned:**
- Flask routes act like different pages and control what gets displayed  
- The `request.form` is how user input gets passed into Python  
- `render_template` sends data from Python to HTML using variables  
- Separating logic into a helper file keeps the code cleaner and easier to manage  


## Date: 2026-04-14
**What I asked AI to do:**
- Help me connect the Mapbox API and MBTA API to my app  
- Help me debug why my API key was not working  
- Explain how `.env` files and API keys work  
- Help me test if my functions were returning the correct values  
- Help me understand how the full flow of the app works from input to output  

**What I didn't understand in the generated code:**
- I did not fully understand why my API key was returning “not authorized”  
- I was confused about how environment variables are loaded and used  
- I wasn’t sure how to debug API responses or what the JSON data meant  

**What I learned:**
- API keys need to be stored correctly in `.env` and loaded using `load_dotenv()`  
- If an API key is incorrect or not loaded, the request will fail  
- APIs return data in JSON format, which can be accessed like dictionaries  
- Debugging with print statements is very helpful when working with APIs  


## Date: 2026-04-15
**What I asked AI to do:**
- Help me improve the user interface and make the app look more professional  
- Show me how to add CSS for colors, spacing, and layout  
- Help me add a map to the results page using Mapbox  
- Explain how to add a marker (pin) to the map  
- Help me keep the project simple while still improving the user experience  

**What I didn't understand in the generated code:**
- I wasn’t fully sure how the map image URL was being generated  
- I didn’t completely understand how CSS styling connects to the HTML templates  
- I was unsure how much design is expected vs too advanced for the project  

**What I learned:**
- A static Mapbox image can be used to show a map without needing complex JavaScript  
- CSS can significantly improve how a web app looks without changing the backend logic  
- Small UI improvements like spacing, colors, and layout make a big difference  
- It’s important to balance making the app better without making it too complex  