---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/generate-test-cases/
title: Generate test cases \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:34.116961+00:00
---

# Generate test cases  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/generate-test-cases/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Generate test cases Stay organized with collections  Save and categorize content based on your preferences. 

Ensure code reliability by generating comprehensive test cases.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    Can you generate a comprehensive set of unit tests for this function, covering
    both edge cases and normal scenarios? Also, can you help me create a mock
    object for this external dependency?
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Of course! I can help with that. Unit testing is crucial for ensuring your code is reliable, and mocking external dependencies is a key part of that process.
> 
> Below is a comprehensive set of unit tests for your `is_user_eligible_for_promo` function. I've used Python's built-in `unittest` library to create the test suite and `unittest.mock` to create a mock object for the `UserDatabase`.
> 
> ### Mocking the External Dependency
> 
> First, let's talk about the mock object. We need to isolate the function we are testing (`is_user_eligible_for_promo`) from its external dependency (`UserDatabase`). By creating a mock, we can simulate the behavior of the database in a controlled way, allowing us to test how our function reacts to different scenarios without making actual database calls.
> 
> ### The Unit Test Suite
> 
> Here is the complete file, including the original code, the mock implementation, and a comprehensive set of unit tests covering normal and edge cases.
>     
>     
>     import unittest
>     from unittest.mock import Mock
>     # ...
>     

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
