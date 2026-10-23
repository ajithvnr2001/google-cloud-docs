---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features/
title: About advanced features \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:18.516815+00:00
---

# About advanced features  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  About advanced features Stay organized with collections  Save and categorize content based on your preferences. 

When you are creating search apps and data stores, you have the option to turn on various advanced settings to get additional features. Here are the advanced features that are available:

  * **Enterprise edition features**

  * **Generative responses**

  * **Advanced website indexing**




## Overview

The following table shows Agent Search features and indicates the advanced settings that are required for each feature:

Feature  | Requires   
---|---  
Website search (basic website search and advanced website indexing)  | Enterprise edition   
CMEK (customer-managed encryption keys)  | Enterprise edition   
Snippets for unstructured search  | No requirements   
Extractive answers for unstructured search  | Enterprise edition   
Extractive segments for unstructured search  | Enterprise edition   
Core generative answer features* | Enterprise edition   
Advanced generative answer features† | Advanced LLM features   
Search summarization without advanced generative answer features† | Enterprise edition   
Search summarization with advanced generative answer features† | Advanced LLM features   
Search tuning for unstructured data stores  | Enterprise edition   
  
* Core generative answer features include all answer generation features except for advanced generative answer features, such as related questions, query simplification, multi-step queries, multi-turn queries, and multimodal answers that return images and charts.   
†Advanced generative answer features include all answer generation features including related questions, query simplification, multi-step queries, multi-turn queries, and multimodal answers that return images and charts. 

## Enterprise edition features

Enterprise edition features add functionality at the app level. Enterprise tier features incur additional cost. For more information, see [Pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing). Turning on Enterprise edition features is required for the following features:

  * [Extractive answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-answers).

  * [Extractive segments](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments).

  * [Search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search).

  * [Core generative answer features](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer).




In addition, turning on Enterprise edition features is required for website search. That is, Enterprise edition features are required for any Agent Search app that uses [website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es#website-data) (basic website search and advanced website indexing). This setting can't be turned off for apps that are attached to website data stores.

If you turn off Enterprise edition for an existing app, any features in your app that require Enterprise edition will no longer work.

To change this setting for an existing app, see [Turn Enterprise edition on or off](https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-edition).

## Generative responses

Generative responses include the following advanced LLM features. You must turn on the [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/advanced-llm) option to obtain search responses with these features:

  * [Search summarization](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries). For website search, this also requires advanced website indexing.

  * [Advanced generative answer features](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer). For website search, this also requires advanced website indexing.




Generative responses incur additional costs. For more information, see [Pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing).

If you turn off the [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/advanced-llm) option for an existing app, any functionality in your app that requires advanced LLM features no longer works.

To change this setting for an existing app, see [Turn generative responses on or off](https://docs.cloud.google.com/generative-ai-app-builder/docs/advanced-llm).

## Advanced website indexing

Turning on advanced website indexing generates an index for the websites that you specify when you create your data store. This requires [domain verification](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification) and imposes a quota on the number of pages that you can index. You can [upgrade this quota](https://docs.cloud.google.com/generative-ai-app-builder/quotas#request-a-quota-increase) if necessary. Advanced website indexing incurs additional cost. For more information, see [Pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing) and [Quota for web page indexing](https://docs.cloud.google.com/generative-ai-app-builder/quotas#quota-for-webpage-indexing).

Advanced website indexing enables the features listed in the following table. The table also indicates other advanced settings that are needed to enable a feature.

Enterprise edition features are required for any Agent Search app that uses [website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es#website-data) for basic website search or advanced website indexing.

**Feature** | **Requires**  
---|---  
Search summarization using the [answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer) or the [search](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries) method | Advanced LLM features and advanced website indexing   
Search with follow-ups using the [answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer) or the [converse](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search) method | Advanced LLM features and advanced website indexing   
[Extractive segments and answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets) | Advanced website indexing  
[Search for an image using an image query](https://docs.cloud.google.com/generative-ai-app-builder/docs/image-search) | Advanced website indexing  
[Sitemap-based index and refresh](https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap) | Advanced website indexing  
[Automatic index refresh](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites) | Advanced website indexing  
[Manual web page refresh](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.siteSearchEngine/recrawlUris) | Advanced website indexing  
[Add structured data to data store schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata) | Advanced website indexing   
Lower search latency than basic website search | Advanced website indexing  
Blended search (multiple data stores in a single app) | Advanced website indexing  
Search tuning | Advanced website indexing  
  
You have the option to turn on advanced website indexing when you create your data store and when you upgrade your data store. To learn more about the upgrade process, see [Turn on advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-on-advanced-indexing).

You cannot turn off advanced website indexing for an existing data store. Instead, you must create a new data store, and during the data store creation process, don't select the **Advanced website indexing** option.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
