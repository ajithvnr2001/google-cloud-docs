---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/optimize-performance/
title: Optimize performance \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:40.762898+00:00
---

# Optimize performance  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/optimize-performance/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Optimize performance Stay organized with collections  Save and categorize content based on your preferences. 

Improve code efficiency by identifying bottlenecks.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    Analyze this code snippet for potential performance bottlenecks. Can you
    suggest alternative data structures or algorithms that might be more efficient?
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Of course. I can analyze this code for you and suggest more efficient alternatives.
> 
> ### Performance Analysis
> 
> The primary performance bottleneck in your `find_matching_users` function lies in this line:
>     
>     
>     if user in all_users:
>     
> 
> When `all_users` is a list, checking for the existence of an element (`user in all_users`) requires iterating through the list until a match is found. In the worst-case scenario, this operation has a time complexity of O(n), where 'n' is the number of items in `all_users`.
> 
> Since this check is performed for every `user` in `users_to_check` (let's say it has 'm' items), the total time complexity of the function becomes **O(n * m)**. This can become very inefficient if both lists are large.
> 
> * * *
> 
> ### Suggested Alternatives
> 
> Here are two more efficient approaches to accomplish the same task.
> 
> #### 1\. Convert to a Set for Faster Lookups
> 
> You can significantly speed up the lookup process by converting `all_users` into a `set`. Checking for an element's existence in a set is, on average, an O(1) operation.
> 
> This reduces the overall time complexity to roughly O(n + m), which is a massive improvement.
> 
> ...

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
