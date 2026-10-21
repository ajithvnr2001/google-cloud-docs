---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-case-generate-refactor-code/
title: Generate and refactor code \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:37:21.420873+00:00
---

# Generate and refactor code  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-case-generate-refactor-code/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Generate and refactor code Stay organized with collections  Save and categorize content based on your preferences. 

Boost coding productivity by generating or refactoring code.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    Can you generate a Python function to parse a JSON file and extract specific
    keys? Also, can you refactor the code in the attached file to improve its
    readability and efficiency?
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Of course. I can help with both of your requests.
> 
> First, here is a general-purpose Python function to parse a JSON file and extract a list of specified keys. It includes error handling for common issues like a missing file or invalid JSON content.
> 
> ### Function to Parse JSON and Extract Keys
>     
>     
>     import json
>     
>     def extract_keys_from_json(file_path, keys_to_extract):
>         """
>         Parses a JSON file and extracts values for a specific list of keys.
>     
>         Args:
>             file_path (str): The path to the JSON file.
>             keys_to_extract (list): A list of strings representing the keys to extract.
>     
>         Returns:
>             dict: A dictionary containing the extracted keys and their values.
>                   Returns an empty dictionary if the file is not found or is invalid.
>         """
>         extracted_data = {}
>         try:
>             with open(file_path, 'r') as f:
>                 data = json.load(f)
>                 # ...
>     
> 
> * * *
> 
> ### Refactored Code
> 
> Here is the refactored version of the `hi.py` file you provided. The primary improvements focus on making the code safer and more readable by removing the deeply nested `if` statements.
> 
> This version uses the `.get()` method, which is a more "Pythonic" way to access dictionary keys that might not exist. It helps avoid `KeyError` exceptions and makes the code flatter and easier to follow.
>     
>     
>     import json
>     
>     def update_user_status_refactored(json_data):
>         """
>         Parses user data, updates status, and handles nested keys safely.
>         """
>         data = json.loads(json_data)
>     
>         # Safely get the email using .get() to avoid errors if keys are missing
>         # .get('user', {}) returns an empty dict if 'user' is not found
>         email = data.get('user', {}).get('details', {}).get('email')
>     
>         if email:
>             print(f"Processing user: {email}")
>     
>         # Update the user status
>         if 'user' in data:
>             # ...
>     

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
