---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-ProductSearch-Paths/
title: Cloud Vision V1p4beta1 API - Module Google::Cloud::Vision::V1p4beta1::ProductSearch::Paths (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:21.409079+00:00
---

# Cloud Vision V1p4beta1 API - Module Google::Cloud::Vision::V1p4beta1::ProductSearch::Paths (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-ProductSearch-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1p4beta1 API - Module Google::Cloud::Vision::V1p4beta1::ProductSearch::Paths (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.1  0.14.1  0.13.0  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Vision V1p4beta1 API module Google::Cloud::Vision::V1p4beta1::ProductSearch::Paths.

Path helper methods for the ProductSearch API.

## Extended By

  * [Google::Cloud::Vision::V1p4beta1::ProductSearch::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-ProductSearch-Paths)



## Included In

  * [Google::Cloud::Vision::V1p4beta1::ProductSearch::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-ProductSearch-Client)
  * [Google::Cloud::Vision::V1p4beta1::ProductSearch::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-ProductSearch-Paths)
  * [Google::Cloud::Vision::V1p4beta1::ProductSearch::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-ProductSearch-Rest-Client)



## Methods 

### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #product_path
    
    
    def product_path(project:, location:, product:) -> ::String

Create a fully-qualified Product resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/products/{product}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **product** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #product_set_path
    
    
    def product_set_path(project:, location:, product_set:) -> ::String

Create a fully-qualified ProductSet resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/productSets/{product_set}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **product_set** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #reference_image_path
    
    
    def reference_image_path(project:, location:, product:, reference_image:) -> ::String

Create a fully-qualified ReferenceImage resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/products/{product}/referenceImages/{reference_image}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **product** (String) 
  * **reference_image** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
