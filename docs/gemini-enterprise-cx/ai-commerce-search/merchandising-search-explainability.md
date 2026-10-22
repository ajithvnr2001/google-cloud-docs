---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/merchandising-search-explainability/
title: Enable search explainability \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:15.570994+00:00
---

# Enable search explainability  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/merchandising-search-explainability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Enable search explainability Stay organized with collections  Save and categorize content based on your preferences. 

For a given query, you might wonder why certain unintended products show up in searches or why the products you want showing up don't.

Take _running shoes_ for example. You wonder why a known brand of running is not showing up in test searches.

You are confronted with the dilemma of having to be a detective to discover why your search results are not rendering as expected.

The Merchandising console provides a search explainability feature, which lets you gain insights about potential problems with their search results and does the diagnosis for you.

Essentially, Merchandising console breaks down the building blocks of a query to help you examine what is going on, how your products are positioned and why, so that you're left not guessing why one product is ranked higher than another.

## Self-serve search explainability

Merchandising console enables a self service to explain potential issues in your search results. It exposes the relevance and revenue scores of each product. It also shows the active controls applied to it by clearly highlighting which product is pinned by this campaign, or this product is buried by this global rule. It will surface key [analytics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/merchandising/analytics), telling you this product was deleted, or this query is new and undertrained.

**Key Point:** Revenue score measures expected revenue, an advanced AI model that captures: 

  * Anticipated clicks
  * Add-to-cart rates
  * Actual purchase conversions
  * All weighted against the product's price



Potential issues | Self-serve explanation  
---|---  
Product is relevant? | Show me relevance and revenue expected scores  
Product is a best seller? | Show me relevance and revenue expected scores  
Control is applied? | Show me controls impacting this product  
Product is in catalog? | Show me analytics  
Undertrained query? | Show me analytics  
  
## Query explain

![Merchandisers can investigate how queries are affecting search results.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-query-explain.png)Merchandisers can investigate how queries are affecting search results.

Usually, issues arise out of seemingly irrelevant search results being surfaced. The **Query explain** feature lets you hone in on the issue for each query across products right in the Merchandising console.

![Query explain functionality in the console](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-explain-not-relevance-1.png)![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-explain-not-relevance-1.png)

![Product details shed light on relevance to query.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-explain-not-relevance-2.png)![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-explain-not-relevance-2.png)

Each product appears as tile with the revenue and relevance scores on each card.

For example, if you run a query _running shoes_ in the **Preview** , **Query explain** can provide insight as to why a certain running shoe might not be showing up in the search results preview as expected.

By looking at the product details on each product tile, you can determine why a given product is behaving differently than expected for the given query.

This could be due to:

  * A control that governs the targeted behavior not being applied. For example, if you want the product boosted, ensure that a boost or bury control is applied.
  * Low relevance, which indicates a need to adjust the product description in the catalog.
  * Low revenue score.
  * If a product is out of stock (no longer in the catalog), it can cause it to not show up in the search results, despite the right controls being applied and serving configs activated.



If the product doesn't show up in your test query, it's time to do more investigation.

**Note:** Scores (relevance and revenue) are only available when the search model for data quality is trained. 

## Impact of controls on search results

Imagine climbing shoes show up in _running shoes_ queries and you want to get to the root cause of why.

  1. Click the slider controls page to view which controls you have published. Be sure you have controls configured for the exact _running shoes_ query.

  2. If you find a _running shoes_ control, return to **Home**.

  3. Run a **Preview** search for _running shoes._ Do your climbing shoes show up there?

     * If so, click the climbing shoe product tile to see its description in order to explore whether it is a relevance issue.

     * If it has a high revenue score, ensure you don't have any other controls on _running shoes_ that boost or pin high-revenue products. If so, that could be the problem and you should remove that control so that the climbing shoe no longer appears in _running shoes_ searches.

  4. Click **Query controls** to explore the global behavior of the _running shoes_ query across products by highlighting controls to visualize which ones appear when applying them. Toggle the highlights on or off to see which products appear and disappear in the preview to observe their behavior. By testing the controls before making actual changes to them or to your products, you can gauge which control could be impacting the behavior or which one needs to be applied.

  5. If you have still not found the problem — or conversely, if you want the climbing shoes to appear in _running shoes_ searches and they don't — try repeating these steps for a wider _shoes_ query and see which products appear.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
