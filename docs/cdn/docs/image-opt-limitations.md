---
url: https://docs.cloud.google.com/cdn/docs/image-opt-limitations/
title: Limitations \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:54.758653+00:00
---

# Limitations  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/image-opt-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Limitations Stay organized with collections  Save and categorize content based on your preferences. 

Before you enable image optimization, review the technical constraints, [supported formats](https://docs.cloud.google.com/cdn/docs/configure-image-optimization#supported_image_formats), and operational boundaries of the feature. Understanding these limits helps ensure compatibility with your existing media workflows and helps you design an efficient, reliable image delivery pipeline.

This section describes general constraints, quota and capacity limits, fail-safe error handling, and validation rules.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## General constraints

The image optimization data plane validates all incoming requests against strict system boundaries and validation rules. The edge pipeline processes requests that use [valid formats](https://docs.cloud.google.com/cdn/docs/configure-image-optimization#specifying-transformations) and meet the following optimization constraints:

**Constraint** | **Value** | **Input/Output**  
---|---|---  
**Max size** | 20 MB | Input and output  
**Max Dimension** | 8192 px per dimension | Input and output  
**Max Total Resolution** | 67 mpx (67 108 864 megapixels) | Input and output  
**Parameter Case** | Snake_case (words separated by underscores), case-insensitive | Input  
**Strict validation** | If even one parameter is invalid, the system rejects the entire request and returns an `HTTP 400 Bad Request` status code. | Input  
  
## Quota and capacity limits

Cloud CDN dynamically transforms images at the edge. To maintain service stability and prevent resource exhaustion, Cloud CDN manages and enforces data-plane processing capacity for each region (point of presence, or PoP).

If data transfer in a specific region exceeds local processing capacity, Cloud CDN automatically implements the following mitigation strategies to preserve availability:

  * Cloud CDN automatically routes the request to adjacent regions for processing. Although this routing helps ensure that the image is optimized, it introduces inter-region cache-fill latency.

  * If adjacent regions are also at capacity, Cloud CDN rejects the request and returns an **HTTP 429 Too Many Requests** status code.


**Note:** if you expect high-volume traffic, coordinate with your account team before deployment. This helps ensure that Google Cloud provisions adequate processing capacity in the deployment zones of your target region.

## Failsafe error handling

The platform has a strict processing threshold:

  * **Transformation timeout** : if an edge processing action takes too long, the processing sequence times out.

  * If processing takes too long, it terminates and an explicit error code is served to the end user.




## Validation rules

To help ensure that the system successfully processes your images and to prevent errors, make sure your requests stay within the following limits:

  * **Operation limit** : You can include a maximum of 10 image operations (`imop`) in a single query string. Only one operation of a given type can be included in the single query string.

  * **URL length limit** : the entire URL path, including the `imop` parameter modification string, cannot exceed 1,024 characters.




**Parameter validation**

The system validates all incoming parameters against a schema. To prevent your request from being rejected with an `HTTP 400 (Bad Request) error`, verify that all operations and parameters in your query string use correct spelling and formatting.

## What's next

  * [Image optimization use cases](https://docs.cloud.google.com/cdn/docs/image-opt-use-cases)
  * [Securing image transformation requests](https://docs.cloud.google.com/cdn/docs/image-opt-security)
  * [Troubleshoot and Best Practices](https://docs.cloud.google.com/cdn/docs/image-opt-monitor-troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
