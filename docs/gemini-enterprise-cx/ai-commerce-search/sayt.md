---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/sayt/
title: Dynamic search \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:39.774462+00:00
---

# Dynamic search  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/sayt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Dynamic search Stay organized with collections  Save and categorize content based on your preferences. 

The modern ecommerce search bar is far more than just an input field. It's an interactive, dynamic assistant that guides your users to the right products before they even finish entering text. This search-as-you-enter (SAYE) experience, which displays query suggestions, popular brands, relevant categories, and even top product results in real-time, drives user engagement and increases the likelihood of conversion.

While AI Commerce Search provides distinct APIs for query autocompletion and product search, it intentionally leaves the final implementation of a SAYE user experience open-ended.

This guide to building with AI Commerce Search explores two primary design patterns for implementing a robust SAYE widget using the AI Commerce Search APIs, detailing the trade-offs of each approach.

## Understand the core components

To build a comprehensive SAYE feature, you need to understand the two fundamental APIs provided by AI Commerce Search:

  1. **`CompleteQuery` API**: This is the brains behind your autocomplete suggestions.

     * **Function** : For a given input string, such as _lipst,_ it returns a list of suggested query completions, including _lipstick_ and _lip gloss,_ associated popular brands, and relevant categories.
     * **Cost** : This API is included in the AI Commerce Search package pricing.
     * **Performance** : It's a high-throughput API designed for the rapid, low-latency responses required for a keystroke-by-keystroke experience. It leverages auto-learning features, including spell correction and suggestions that are designed to yield results, all trained on your store's daily search events. See the [spell correction API specifications](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec) for more details.
  2. **`Search` API**:This is your core product discovery engine.

     * **Function** :For a given query, it returns a ranked list of relevant product results.
     * **Cost** :This is a paid API, and its usage directly impacts your operational costs.
     * **Events** : For model training and analytics, each `Search` API call should ideally be paired with a search event to track user behavior and improve the relevance models over time.



![Search as you enter](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/Search-as-you-type.png)

To create the SAYE experience, you must write a wrapper API or frontend logic that calls both these APIs and combines their results into a single, cohesive user interface.

## Implementation pattern 1: Direct but costlier approach

This is the most straightforward method to implement. The logic is for every keystroke, you make parallel calls to both the `CompleteQuery` and `Search` APIs.

### Flow

The flow follows this sequential path:

  1. A user enters a character, such as _l._
  2. Your application sends _l_ to the `CompleteQuery` API.
  3. Simultaneously, your application sends _l_ to the `Search` API.
  4. The results are combined and displayed.
  5. The user enters another character (_l,_ making the query _li)._
  6. The process repeats for the new query _li._



### Advantages

The advantages include fast implementation, allowing you to quickly write and deploy the log.

### Disadvantages

  * **High`Search` API volume**: This approach dramatically inflates the number of `Search` API calls. A query like _lipstick_ would trigger eight separate search requests, leading to a significant increase in volume.
  * **Increased cost** : Since the `Search` API is a paid service, this high volume directly translates to higher operational costs, making it difficult to achieve a positive return on investment (ROI).
  * **Event management complexity** : Every `Search` API call should be logged with a corresponding search event for accurate model training and measurement. The high volume of calls makes it challenging to ensure every event is captured, potentially leading to data loss and skewed analytics.
  * **Potentially lower quality results** : Searches for one or two characters, such as _l, li_ can return noisy or overly broad results, leading to a less relevant initial experience.



## Implementation pattern 2: The optimized and recommended approach

This pattern optimizes for cost, performance, and relevance by using the `CompleteQuery` API to intelligently decide when to call the `Search` API.

### Flow

The flow follows this sequential path:

  1. A user enters a partial text query, such as _lip._
  2. Your application sends _lip_ to the `CompleteQuery` API.
  3. The API returns a list of suggestions, with _lipstick_ likely being the first result.
  4. Your application takes the first suggestion _(lipstick)_ and makes a single call to the `Search` API with that term.
  5. The autocomplete suggestions and the product results for _lipstick_ are displayed.
  6. As the user continues to enter _lips, lipst, ..._ you can add logic to only make a new search call if the first autocomplete suggestion changes.



### Advantages

  * **Significant cost reduction** : By drastically reducing the number of `Search` API calls, this method keeps costs under control.
  * **Controlled API and event volume** : API and event volumes are manageable and predictable, ensuring more reliable data for model training and analytics.
  * **Higher relevance** : You are searching for more complete and probable terms, which provides higher-quality product results in the SAYE widget.
  * **Better ROI** : Lower costs and a better user experience contribute to a stronger return on investment.



### Handling edge cases

This approach is superior but requires handling a few corner cases:

  * **No suggestions** : If the `CompleteQuery` API returns no suggestions, your logic should fall back to calling the `Search` API with the user's raw input.
  * **Partial vs. suggested query** : In rare cases, a user might want to see results for their partial term, such as _eye_ rather than the top suggestion, _eye shadow._ While this is a minor trade-off, the optimized approach prioritizes the most likely user intent.



## Measure success with experiment IDs

Regardless of the implementation you choose, it's important to measure the performance of your SAYE widget independently from your main search results page. If you use the same tracking for both, you'll be unable to determine if the SAYE feature is truly improving click-through rates and conversions.

The solution to measuring click-through and conversation rates of the SAYE widget specifically is to use distinct `experimentIds` in your search events that differentiate these metrics from those of the main search events.

  * **SAYE events** : Assign a specific ID, such as `"experimentId": "saye-widget"`, to all search events originating from the search-as-you-enter capability.
  * **Main search events** : Use a different ID (or no ID) for searches initiated when a user presses **Enter** or clicks **Search** to go to the main search results page.



By segmenting your events this way, you can use the analytics dashboards in the Vertex AI console to filter and compare the performance of your SAYE widget against the standard search experience, giving you clear, actionable insights.

## Conclusion

AI Commerce Search provides the components for creating a search-as-you-enter experience. By acting as the architect who designs the interaction between the `CompleteQuery` and `Search` APIs, you can build a search capability that builds the bridge between user experience and performance. For most use cases, the optimized approach delivers a user-relevant experience while avoiding compute-heavy operations.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
