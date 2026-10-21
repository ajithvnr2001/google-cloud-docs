---
url: https://docs.cloud.google.com/retail/conversational_search_backup/conversational-commerce-agent-best-practices/
title: Additional considerations and testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:33:02.667415+00:00
---

# Additional considerations and testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/retail/conversational_search_backup/conversational-commerce-agent-best-practices/




#  Additional considerations and testing Stay organized with collections  Save and categorize content based on your preferences. 

Additional considerations must be taken into account for best practices and testing your Conversational agent interface.

## Implement best practices

Consider these best practices when implementing your Conversational agent interface:

  * **Visitor ID consistency** : Help to ensure that a unique `visitor_id` is consistently sent with each request for a given end user. This is vital for accurate personalization and model training. This identifier should ideally remain consistent for an end user across sessions and sign in or sign out states.
  * **Branch management** : While `default_branch` is common, ensure you are using the correct branch ID if your product catalog is structured with multiple branches.
  * **Search API interaction** : For `SIMPLE_PRODUCT_SEARCH` and any cases where `refined_search` is provided, remember to make a separate call to the core Search API (`SearchService.Search`) using the `query` from the `refined_search` field or the original query to get the actual product listings. The Conversational API primarily focuses on the conversational experience and user intent understanding rather than directly returning product results.
  * **User interface design** : Design your web interface to clearly present `conversational_text_response`, `followup_question`, and `refined_search` options in an intuitive manner to guide your user.



## Configure attributes for LLM generation

To ensure that the Conversational agent can generate responses, attributes must be set to **Retrievable** in your **Attribute controls**.

If an attribute is **Indexable** but not **Retrievable** , the Conversational agent will find the product but cannot read the details to answer user questions. The Conversational agent often triggers a fallback response, such as **Sorry, we don't have that product**.

For this reason, you should set the semantic attributes (`Title`, `Description`, `Brand`, `Specs`) to **Retrievable: True** so that the LLM can use them. Set the user interface or app attributes (`BrandID`, `SkuID`) to **Retrievable: True** if your frontend requires them for rendering. Set your backend metadata to **Retrievable: False** to optimize context window usage.

## Plan A/B tests

While relevance is an important input metric, AI Commerce Search also takes other variables into account with the goal of optimizing for business results:

Metrics  
---  
Revenue per visit (RPV) | Revenue per visit is the most effective metric for search performance as it takes into account conversion rate, AOV, and relevance.  
Conversion—Average order value (AOV) | Conversion % and AOV both contribute to RPV.  
Relevance—Buyability—Price | Relevance, among other inputs, is used to produce high performing search results.  
  
### A/B readiness checklist

These are the success metrics used:

Revenue per visit (RPV)

Conversation rate (CVR)

Add-to-cart events

Click-through rate

Item | Definition | Stage  
---|---|---  
Event attribution scheme | Work with Google to properly segment the user events for measurement. | Pre-experiment  
Monitoring data inputs | Ability to quickly understand when training data contains anomalies that could impact performance. | Pre-experiment  
Event coverage | Are we instrumenting all possible outcomes associated with search or recommendations AI sessions? | Pre-experiment  
Measurable success criteria | Documented definition of done (in measurable terms). | Pre-experiment  
Ability to measure UX biases | Ensure consistent UX across experiment arms. | During experiment  
Coherency between VAIS data and consumption | Verify attribution tokens, filters, order by, offset, etc., are being passed from API to UserEvents. Visitor/UserIDs match between event and API requests. | During experiment  
Approval to tune during the experiment | Plan for tuning activities, document changes, adjust measurements and interpretation accordingly. | During Experiment  
  
### Implement proof of concept or minimum viable product

Data ingestion | A/B test design | Performance metrics | Governance and process  
---|---|---|---  
Up-to-date and complete product catalog ingestion Adherence to recommended events ingestion methods to ensure data synchronization between Google and you.  
Google's recommendation is for real-time event tracking, including impression data. Pass through necessary attributes such as experiment IDs, visitor IDs, and correctly implement search tokens where applicable. |  Incorporate experimentation best practices to ensure reliable results:  


  * Verify integration.
  * Test a single change at a time.
  * Avoid aggressive caching.
  * Ensure web interface fairness between test and control.
  * Ensure traffic fairness with traffic split using visitor ID.
  * Ensure product data consistency.
  * Apply same business rules across test & control.

| All evaluation criteria should be empirical, objectively measured, and driven by metrics.  
Alignment on exact definitions of metrics tracked is critical to measure performance accurately. Standard metrics tracked include: 

  * Search CTR (results relevance)
  * Null search rate (intent understanding)
  * Revenue per visitor / Revenue per user
  * Number of searches to convert

|  Data integration, testing, feature rollout, and optimization will be an iterative process, requiring resources.   
  
### Example experiment cadence

Satisfy minimum viable product dependencies | Calibrate measurement | Deploy production dark mode | Go or no-go decision  
---|---|---|---  
  
  * Contract
  * Trained model and serving configs
  * Product and event data ingestion

| 

  * Compare (client) data with Commerce search telemetry and adjust accordingly
  * Align on measurement baselines

| 

  * Perform offline evaluation
  * Tune configurations
  * A/A test to verify traffic split

| 

  * Obtain QA sign-off
  * Commit to move forward with ramp

  
  
![Example AB experiment cadence](https://screenshot.googleplex.com/93UioZqMyVAUvue.png)

Ongoing testing | Ramp to X% of traffic | Measure, adjust, and repeat | Ramp to X% live traffic  
---|---|---|---  
  
  * Continue tuning/optimization
  * Test incremental features

| 

  * Analyze performance across search segments
  * Make any modeling/rules adjustments

| 

  * Cross-check performance
  * Identify and explain anomalies

| 

  * Initiate experiment
  * Share performance metrics daily
  * Perform tuning

  
  
### Components of a successful experiment

Calibrate measurements and establish success criteria | Maintain experiment fairness | Monitor data quality  
---|---|---  
  
  * Plan time to verify catalog, user event, and API consumption coherency before official launch.
  * Establish quantifiable success criteria up front (ideally, expressed as a change to RPV).
  * Proactively identify and explain regressions or anomalies, then fix them.
  * Share measurements often, understand and document metrics definitions across experiment arms.

| 

  * Minimize UX differences between segments (common layout and visuals, just different data).
  * Be mindful of merchandising / business rules (ensure they don't introduce bias).

| 

  * Measure catalog drift.
  * Properly annotate experiment outcomes (by way of user events).

  
  
### Roles and experiment ownership

| Google | You  
---|---|---  
Quality evaluation | Commerce search outcomes | UX impact  
Measurements | Backup/validate | Authoritative  
Telemetry/data | Platform volumetrics (validating performance)  
Event and index anomalies | Attribution tokens and steps to reproduce (validating issues)  
Search platform |  **Product-level items**

  * Data mapping
  * Model/training adjustments
  * Quality/serving anomalies
  * Platform quotas/limits
  * Product/client library defects

|  **Query/serving items**

  * Request augmentation (including context routing, caching, and intent processing)
  * Serving configs (tuning)
  * Source data enrichment
  * Client performance (for example, WC threads)
  * UX/API/platform/library defects

  
Go or No-go | Recommend | Approve  
  
### Conduct experiments in the console

  1. Go to the **Experiments** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Experiments page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/experiments/)

  2. Use the console for advanced self-service analytics for AI Commerce Search onboarding and A/B testing by applying Google's attribution methodology:



  * Monitor traffic segmentation, business metrics, and search and browse performance.

  * Apply per-search visit level metrics across both keyword search and browse.

  * View experiment performance as a time-series with statistical significance metrics.

  * Use the embedded Looker platform.




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
