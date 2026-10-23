---
url: https://docs.cloud.google.com/vision/product-search/quotas/
title: Quotas and Limits \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:47.512547+00:00
---

# Quotas and Limits  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/quotas/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Resources ](https://docs.cloud.google.com/vision/product-search/docs/resources)



Send feedback 

#  Quotas and Limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains current content limits and rate quotas for the Vision API Product Search. This page will be updated to reflect any changes to these restrictions and usage limits.

## Content limits

The Vision API Product Search enforces the following usage limits:

Content Limit | Value  
---|---  
Image file size | 20 MB  
JSON request object size | 10 MB  
Images per request | 16  
  
Base64-encoded images may exceed the JSON size limit, even if they are within the image file size limit. Larger images should be hosted on Cloud Storage or at a publicly-accessible URL. Note that base64-encoded images can have a larger file size than the original image file (usually about 37% larger).

## Rate quotas

The current API usage quotas for the Vision API Product Search are as follows (and are subject to change):

**General rate quotas** |   
---|---  
Query requests per minute | 1,800  
Resource management requests per minute (***see exception below**) | 2,400 total  
Images per feature per month | No limit  
Maximum number of product sets a product can belong to | 5  
**Rate quotas per method** |   
---|---  
***** Resource management requests per minute (**[`CreateReferenceImage` requests](https://docs.cloud.google.com/vision/product-search/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.CreateReferenceImageRequest)**) | max 1,200 of 2,400 total  
[`ImportProductSets`](https://docs.cloud.google.com/vision/product-search/docs/reference/rpc/google.cloud.vision.v1#importproductsetsrequest) requests per day | 120  
  
These limits apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

Lower quotas can be set per user in the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas).

## Quota increases

You can edit your quotas up to their maximum values by selecting **EDIT QUOTAS** from the **Quotas** page of the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas) page. To request an increase above the maximum quota, edit your quota with your requested increase and justification and submit your update. You will be notified when your request has been received. You might be contacted for more information regarding your request. After your request has been reviewed, you will be notified whether it has been approved or denied.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
