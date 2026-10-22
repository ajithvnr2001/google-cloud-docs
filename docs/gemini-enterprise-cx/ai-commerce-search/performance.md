---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/performance/
title: Measure performance \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:47.022302+00:00
---

# Measure performance  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Measure performance Stay organized with collections  Save and categorize content based on your preferences. 

The AI Commerce Search in Gemini Enterprise for Customer Experience console provides metrics to help you determine how incorporating AI Commerce Search is affecting your business.

## View metrics

For metrics specific to your serving configs, in your project, go to the [**Serving configs**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/) page. Click a serving config name and select the [**Analytics**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/analytics/) page to see its summary metrics. See Configuration-specific metrics for metrics definitions.

## Metrics definitions

This table provides definitions of the summary metrics that AI Commerce Search displays on the **Analytics** page.

**Metric** | **Description** | **Details** | Total revenue |  The total revenue from all recorded purchase events.  | This value includes shipping and tax.  
---|---|---  
Results-engaged revenue |  The revenue for purchase events that include at least one product that was selected from a recommendation or search result.  |  This value includes shipping and tax and any discount applied.   
Average order value (AOV) |  The average value of orders from all purchase events.  |  Total revenue divided by the number of orders.   
Results-engaged AOV |  The average value of orders that include at least one item selected from a recommendation or search result.  |  Results-engaged revenue divided by the number of orders with at least one item that was selected from a recommendation or search result.   
  
### Configuration-specific metrics

You can see metrics for a specific serving config on the [**Serving Configs**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/) page. For metric graphs, click the configuration name and select the [**Analytics**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/analytics/) page.

This table provides definitions for configuration-specific metrics.

**Metric** | **Description** | **Details** | Click-through rate (CTR) |  The number of product detail views from a serving config divided by the total number of `predict` or `search` queries for this configuration.  |  For example, if a recommendations serving config points to a **Frequently Bought Together** model, then the CTR would be the number of product detail pages viewed from the shopping cart recommendation panel divided by the number of `predict` queries on the shopping cart page.   
---|---|---  
Add-to-cart events |  The number of add-to-cart events from a serving config divided by the total number of predict or search queries for that configuration.   
Purchase events |  The total purchase events from the recommendations or search results from this serving config.   
  
To track clicks from a serving config, AI Commerce Search aligns the recommendations in `predict` responses and search results in `search` responses with ingested user events. If a clicked item appears in the `predict` or `search` responses for the same visitor ID within a one hour time window, the click and purchase is treated as a result of the recommendation or search result.

When you configure your recommendations or search requests for the first time, you should confirm that:

  * Visitor IDs in the request are the same as the visitor IDs you used in event ingestions.
  * The timestamp in the response roughly matches the timestamp for that event.



When AI Commerce Search metrics are compared to the ideal expected result, or ground truth, the values might be lower, but the trends align.

Unlike for recommendations, the process of attributing click to search requests is not fully automatic. So for metrics to work for AI Commerce Search, an [attribution token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribution-tokens) is required. However, attribution tokens are not needed for recommendations user events.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
