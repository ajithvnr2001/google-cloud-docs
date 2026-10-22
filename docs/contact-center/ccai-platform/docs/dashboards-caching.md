---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-caching/
title: Caching \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:04.793585+00:00
---

# Caching  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)



Send feedback 

#  Caching Stay organized with collections  Save and categorize content based on your preferences. 

In computing, a cache is a high-speed data storage layer that stores a subset of data to make repeated requests for that data faster than they would be if accessing the data's primary storage location. Caching data makes it faster to retrieve and reuse previously viewed data from the database.

Data is stored in the cache and retrieved when using the reload and refresh buttons in your dashboard filters.

## Clear cache and refresh dashboards

The **Clear cache and refresh** button clears the cache and fetches the requested data from the backend database. In contrast, the **Reload** button first attempts to fetch data from the cache, and if it's not present, it then retrieves data from the database. If the requested data is in the cache, the reload button should provide a faster experience from the user's perspective.

If a filter is applied or another change, such as the date, is made and the reload button is used, the dashboard will display new data. It is crucial that if users want to see up-to-the-moment results and haven't made any changes to filters on the dashboard, they should clear the cache and refresh to observe the latest data.

## Reload

If there are no changes made to the dashboard, when you click the reload button, it will return the same results from the cached data.

## Refresh

Use the refresh button to clear the cache and fetch requested data from the backend database.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
