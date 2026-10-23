---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/website-data-store/
title: Website data store tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:21.319780+00:00
---

# Website data store tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/website-data-store/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Website data store tools Stay organized with collections  Save and categorize content based on your preferences. 

This tool is used to search and retrieve information from specific websites by connecting to a data store.

When you first create the tool, you provide:

  * **Name** : A descriptive name that helps the AI understand the tool's job. Names should start with a verb (for example, search_knowledge_base).

  * **Description** : (Optional) An explanation of what the tool does and when the AI should use it.

  * **Location** : The region where the data store is hosted (for example, global).

  * **Mock tool response** : An optional configuration used to simulate the tool's output for testing purposes before the data is fully indexed.

  * **Sites to include** : A list of URLs to index. Use `yoursite.com/*` to index an entire site or `yoursite.com/page/*` to index a specific page.

  * **Sites to exclude** : Specific URLs or patterns that the tool should ignore.




## Limitations:

  * You must [verify your domain](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification) when using website content as a source.
  * Files from public URLs must have been crawled by the Google Search indexer, so that they exist in the search index. You can check this with the [Google Search Console](https://search.google.com/search-console).
  * A maximum of 200,000 pages are indexed. If the data store contains more pages, indexing will fail at that point. Any content already indexed will remain.



See also [Create a data store using website content](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#website).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
