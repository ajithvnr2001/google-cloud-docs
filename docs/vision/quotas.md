---
url: https://docs.cloud.google.com/vision/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:35.090805+00:00
---

# Quotas and limits  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Resources ](https://docs.cloud.google.com/vision/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud Vision.

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

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on Vision resources. System limits can't be changed. 

## Quota types

There are 3 kinds of quota:

  1. Request Quota 
     * The quota counts **per request sent** to Vision API endpoint.
  2. Feature Quota 
     * The quota counts **per image / page sent** to Vision API endpoint.
     * Unless specified explicitly, quota with feature name as prefix is generally a Feature quota.
     * For `files:annotate` requests, if the `pages` field is not specified explicitly, the quota will count 5 pages per file. However, users will only be billed for the actual number of pages processed.
  3. In Processing Quota 
     * The quota counts **per image / page being processed by Vision API** unless specified explicitly.
     * Can be inferred by "in processing" in quota name.
     * This quota determines the maximum number of images/pages that Vision API processes at a time for the asynchronous methods. Users can send more than this quota into the asynchronous methods, but the images/pages over the quota are not processed immediately. The files in excess of the quota are added to a queue to be processed later.



The current API usage quotas for the Vision API are as follows (and are subject to change):

Vision API quota | Quota type | Value  
---|---|---  
Requests per minute (except request types listed below) | Request quota | 1,800  
Celebrity recognition requests per minute | Request quota | zero  
Label detection requests per minute | Feature quota | 1,800  
Text detection requests per minute | Feature quota | 1,800  
Asynchronous image annotation* number of images in processing | In Processing quota | 8,000  
Asynchronous document text detection† number of pages in processing | In Processing quota | 10,000  
* |  `images:asyncBatchAnnotate` requests   
---|---  
† |  `files:asyncBatchAnnotate` requests, `DOCUMENT_TEXT_DETECTION` feature   
Product Search quota | Value  
---|---  
Requests per minute (except request types listed below) | 1,800  
Batch requests per day | 300  
Resource management write requests per minute | 1,200  
Resource management requests per minute | 2,400  
**Note: Celebrity recognition** is deprecated. Before requesting quota, review the conditions for approval in [Celebrity recognition](https://docs.cloud.google.com/vision/docs/celebrity-recognition). 

These limits apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

Lower quotas can be set per user in the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas).

### Quota increases

You can edit your quotas up to their maximum values by selecting **EDIT QUOTAS** from the **Quotas** page of the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas) page. To request an increase above the maximum quota, edit your quota with your requested increase and justification and submit your update. You will be notified when your request has been received. You might be contacted for more information regarding your request. After your request has been reviewed, you will be notified whether it has been approved or denied.

Generally each quota has "per project per user" and "per project" variants, please change them correspondingly to your setup.

When requesting feature a quota increase, consider the overall request quota and intended batch size to assure the following:

  * overall request quota (Requests per minute) * your batch size >= increased feature quota



If you do not fulfill this requirement, you will still be throttled by the overall request quota.

This document contains current content limits and request quotas for the Vision API. This page will be updated to reflect any changes to these restrictions and usage limits.

## Limits

The Vision API enforces the following usage limits:

Content Limit | Value  
---|---  
Image file size | 20 MB  
JSON request object size | 10 MB  
PDF file size | 1 GB  
Images per `images:annotate` request | 16  
Images per `images:asyncBatchAnnotate` request | 2000  
Pages per `files:annotate` request | 5  
Pages per `files:asyncBatchAnnotate` request | 2000  
  
Base64-encoded images may exceed the JSON size limit, even if they are within the image file size limit. Larger images should be hosted on Cloud Storage or at a publicly-accessible URL. Note that base64-encoded images can have a larger file size than the original image file (usually about 37% larger).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
