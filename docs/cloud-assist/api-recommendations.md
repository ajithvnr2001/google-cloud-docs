---
url: https://docs.cloud.google.com/cloud-assist/api-recommendations/
title: API recommendations for using Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:07.786165+00:00
---

# API recommendations for using Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/api-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  API recommendations for using Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Cloud Assist can use any enabled Google Cloud API to help you query infrastructure, generate resource designs, optimize project costs, and investigate resources.

Most APIs that Gemini Cloud Assist uses are already enabled for the services in your project. This document lists only the APIs that are generally useful for Gemini Cloud Assist operations or that you might not expect to need for specific investigations. Review the following lists of required, recommended, and use-case-specific APIs, or see [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini) for initial configuration instructions.

## Overview

In order to support questions and requests about your Google Cloud resources, Gemini Cloud Assist sometimes uses other Google Cloud APIs. If such an API isn't enabled, Gemini Cloud Assist can still provide responses to you, but the responses might be more limited in their depth or completeness.

If you enable Gemini Cloud Assist using the Google Cloud console, you are given the option to enable recommended APIs as part of the process. If you enable Gemini Cloud Assist using a tool such as Google Cloud CLI, you must enable each API separately. If you don't enable recommended APIs when you first enable Gemini Cloud Assist, you can enable them at a later time.

### Gemini Cloud Assist APIs

In order to function, Gemini Cloud Assist relies on the [**Gemini Cloud Assist API**](https://console.cloud.google.com/apis/library/geminicloudassist.googleapis.com) (`geminicloudassist.googleapis.com`) and the [**Cloud AI Companion API**](https://console.cloud.google.com/apis/library/cloudaicompanion.googleapis.com) (`cloudaicompanion.googleapis.com`). When you [enable](https://docs.cloud.google.com/service-usage/docs/enable-disable) the Gemini Cloud Assist API, the Gemini for Google Cloud API is also automatically enabled; however, disabling either API does not change the status of the other API.

## Required Google Cloud APIs

The following APIs are required for optimal Gemini Cloud Assist functionality. If you don't enable some or all of these APIs, Gemini Cloud Assist quality can be significantly degraded in some use cases.

Google Cloud API | Notes  
---|---  
[**Cloud Asset API**](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) (`cloudasset.googleapis.com`) | This API provides a metadata inventory service to understand the resources and topology of your environment.  
[**Design Center API**](https://console.cloud.google.com/apis/library/designcenter.googleapis.com) (`designcenter.googleapis.com`) | This API enables design skills that let Gemini Cloud Assist generate resource configurations.  
[**App Optimize API**](https://console.cloud.google.com/apis/library/appoptimize.googleapis.com) (`appoptimize.googleapis.com`) | This API provides cost-utilization information about cloud spend to help improve cost-efficiency of applications.  
[**App Hub API**](https://console.cloud.google.com/apis/library/apphub.googleapis.com) (`apphub.googleapis.com`) | This API lets Gemini Cloud Assist execute queries scoped to App Hub applications, services, and workloads.  
  
## Recommended Google Cloud APIs

Google Cloud API | Notes  
---|---  
[**Cloud Monitoring API**](https://console.cloud.google.com/apis/library/monitoring.googleapis.com) (`monitoring.googleapis.com`) | This API provides resource metrics for analysis and presenting charts. This API is especially useful when performing an [investigation](https://docs.cloud.google.com/cloud-assist/investigations).  
[**Cloud Logging API**](https://console.cloud.google.com/apis/library/logging.googleapis.com) (`logging.googleapis.com`) | This API enables usage of [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access). Data access logs are an additional source of information that Gemini Cloud Assist can analyze and are especially useful when performing an [investigation](https://docs.cloud.google.com/cloud-assist/investigations).  
[**Recommender API**](https://console.cloud.google.com/apis/library/recommender.googleapis.com) (`recommender.googleapis.com`) | This API provides recommendations for improving resource usage and optimizing costs.  
[**App Topology API**](https://console.cloud.google.com/apis/library/apptopology.googleapis.com) (`apptopology.googleapis.com`) | This API lets Gemini Cloud Assist understand the topology of your applications and resources.  
  
## Additional Google Cloud APIs

In addition to recommended APIs, there are several APIs you might want to enable for specific use cases:

Google Cloud API | Notes  
---|---  
[**Cloud Resource Manager API**](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com) (`cloudresourcemanager.googleapis.com`) | This API is recommended for optimal functioning of [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations).  
[**Service Health API**](https://console.cloud.google.com/apis/library/servicehealth.googleapis.com) (`servicehealth.googleapis.com`) | This endpoint must be enabled in order to access information about Google Cloud service outages.  
[**Storage Insights API**](https://console.cloud.google.com/apis/library/storageinsights.googleapis.com) (`storageinsights.googleapis.com`) | This endpoint must be enabled in order to create a [Storage Insights dataset](https://docs.cloud.google.com/storage/docs/insights/datasets), which lets you ask specific questions about your Cloud Storage buckets and objects.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
