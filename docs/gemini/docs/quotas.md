---
url: https://docs.cloud.google.com/gemini/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:11.598096+00:00
---

# Quotas and limits  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Resources ](https://docs.cloud.google.com/gemini/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Gemini for Google Cloud.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Gemini for Google Cloud resources. System limits can't be changed. 

## Requests per second

Gemini for Google Cloud enforces quotas on requests per second for each user in a project.

Quota | Value  
---|---  
Requests per second | 2  
  
## Requests per day

Gemini for Google Cloud enforces quotas for the total number of requests per day for each user in a project.

Quota | Value  
---|---  
Requests per day for Gemini Code Assist or Gemini in BigQuery code requests, such as code generation and code completion. | 6000  
Requests per day for chat, visualization, data insight table scans, metadata generation, data preparation, and other requests that display responses in the **Cloud Assist** panel in the Google Cloud console and IDEs.  | 960  
  
## Quotas for Gemini Code Assist

Gemini Code Assist enforces quotas for certain features.

Quota | Value  
---|---  
Local codebase awareness | 1,000,000 token context window  
Code customization repositories  | 20,000  
  
### Quotas for agent mode and Gemini CLI

Quotas for requests from Gemini Code Assist agent mode and Gemini CLI are combined. When in agent mode or when using the Gemini CLI, one prompt might result in multiple model requests. Requests are limited per user per minute and are subject to the availability of the service in times of high demand. These daily request limits are aggregated across all interactions with any model version or family (for example, Pro, Flash) used with the Gemini CLI or agent mode. Once the maximum number of requests per day is reached, no further requests can be made through these interfaces to any model until the quota resets.

Quota | Gemini Code Assist edition | Value  
---|---|---  
Maximum requests per user per day | Standard | 1500  
Enterprise | 2000  
  
### Quotas for Gemini Code Assist on GitHub

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms for Google Cloud](https://cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [Google Cloud launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Usage of [Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code) is not counted as part of the general quotas for Gemini Code Assist.

  * An [installation](https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github) of the Gemini Code Assist on GitHub app has a quota of at least 100 pull request reviews per day.

    * The exact number of pull request reviews depends on the codebase and how many model calls are required to complete each code review. Because of this, in some cases the quota can be significantly greater than 100.



Gemini Code Assist on GitHub quotas reset in alignment with resets for [Google Cloud quotas](https://docs.cloud.google.com/docs/quotas/overview#running_out).

## Request a quota increase

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
