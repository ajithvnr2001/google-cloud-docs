---
url: https://docs.cloud.google.com/generative-ai-app-builder/quotas/
title: Quotas and limits \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:34.952248+00:00
---

# Quotas and limits  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/quotas/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Resources ](https://docs.cloud.google.com/generative-ai-app-builder/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Google Cloud products that use the Discovery Engine API, Agent Search and Gemini Enterprise, share the rate and allocation quotas listed on this page. This means that your search and recommendations apps in Agent Search share these quotas with your apps in Gemini Enterprise. 

This document lists the quotas and system limits for Agent Search. System limits are fixed values that cannot be changed. To increase most quotas, you must submit a quota increase request. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

**Note:** If you want to serve a higher volume of search requests than the default search rate quota allows, don't request a quota increase. Instead, enable configurable pricing and set a queries per minute (QPM) subscription threshold that matches your expected traffic. For more information, see [Set up configurable pricing for custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing).

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Agent Search resources. System limits can't be changed. 

## Allocation quotas

The following table lists the quotas for Discovery Engine API. These quotas don't reset over time. Instead, they're released when you release the resource.

Quota | Value  
---|---  
Total number of data stores per project | 1001  
Total number of engines per project | 1502  
Number of pending import long running operations per project | 300  
Number of pending purge documents long running operations per project | 100  
Number of serving controls per project | 1,000  
Number of boost serving controls per serving config | 100  
Number of filter serving controls per serving config | 100  
Number of redirect serving controls per serving config | 100  
Number of synonym serving controls per serving config | 100  
Regional number of data stores per project per location (Global, US, EU) | 100  
Regional number of documents per project per location (Global, US, EU) | 10,000,000  
Regional number of engines per project per location (Global, US, EU) | 150  
Regional number of user events per project per location (Global, US, EU) | 40,000,000,000  
  
1 Due to a technical limitation, the maximum quota for data stores is 500 per project. If you need more data stores, use new projects.   
Each entity in a data store is counted as a data store instance and, therefore, counts toward this quota. For example, a data store with three entities counts as three data stores against your quota.

2 Due to a technical limitation, the maximum quota for engines is 500 per project. If you need more engines, use new projects. 

**Note:** The number of data stores, documents, user events, and engines across all locations can't exceed the total per-project quota for that resource. For example, if you already have 60 data stores in the `eu` multi-region and 40 in the `us` multi-region, you can't create another data store because the overall data store quota for the project is 100.

## Rate quotas

The following quotas apply to Discovery Engine API requests.

**Note:** The **Regional search requests per minute per project per location** quota can't be increased under the general pricing model. If you need to serve more search traffic, enable configurable pricing and set a queries per minute (QPM) subscription threshold for your project. For more information, see [Set up configurable pricing for custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing).Quota | Value  
---|---  
Complete query requests per minute per project | 300  
Conversational search read requests per minute per project | 600  
Conversational search write requests per minute per project | 600  
Document batch requests (such as inline import and purge) per minute per project | 100  
Document async import (Cloud Storage, BigQuery, etc.) requests per minute per project | 10  
Document purge requests per minute per project | 100  
Document read requests per minute per project | 300  
Document write requests per minute per project | 12,000  
Evaluation create requests per day per project | 5  
Evaluation read requests per minute per project | 100  
Evaluation write requests per minute per project | 100  
Grounded generation check grounding requests per minute per project | 300  
LLM query requests (search summarization, multi-turn search) per minute per project | 60  
Number of pending FHIR or BigQuery streaming writes per minute | 6,000  
Number of sample query sets per project | 100  
Ranking API requests per minute per project | 500  
Recommend requests per minute per project | 60,000  
Sample query read requests per minute per project | 200  
Sample query set read requests per minute per project | 100  
Sample query set write requests per minute per project | 100  
Sample query write requests per minute per project | 200  
Schema read requests per minute per project | 100  
Schema write requests per minute per project | 100  
Regional search requests per minute per project per location (Global, US, EU) | 300  
User event batch requests (such as import and purge) per minute per project | 100  
User event collect requests per minute per project per user | 240  
User event write requests per minute per project | 60,000  
  
## Quota for web page indexing

When you have a data store with [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing) turned on, every web page that you index counts towards the "Number of documents per project" quota in the Allocation quotas list. You can also see the number of pages in your project and the page quota for that project in the **Project pages vs quota** field in the **Data** page for a data store.

If you add websites to a data store in a project and the web pages in those websites exceed the project's quota, the websites are not indexed. If you have websites in your data store that are already indexed, those websites continue to be indexed as before. You can request to [upgrade your quota](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota) at any time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
