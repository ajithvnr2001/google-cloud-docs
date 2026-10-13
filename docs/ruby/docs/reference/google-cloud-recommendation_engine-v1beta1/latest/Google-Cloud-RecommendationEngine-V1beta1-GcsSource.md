---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recommendation_engine-v1beta1/latest/Google-Cloud-RecommendationEngine-V1beta1-GcsSource/
title: Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::GcsSource (v0.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:17.324621+00:00
---

# Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::GcsSource (v0.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recommendation_engine-v1beta1/latest/Google-Cloud-RecommendationEngine-V1beta1-GcsSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::GcsSource (v0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.17.1  0.16.0  0.15.1  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.2  0.8.2  0.7.0  0.6.1  0.5.0  0.4.1  0.3.7 

Reference documentation and code samples for the Recommendations AI V1beta1 API class Google::Cloud::RecommendationEngine::V1beta1::GcsSource.

Google Cloud Storage location for input content. format.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #input_uris
    
    
    def input_uris() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. Google Cloud Storage URIs to input files. URI can be up to 2000 characters long. URIs can match the full object path (for example, `gs://bucket/directory/object.json`) or a pattern matching one or more files, such as `gs://bucket/directory/*.json`. A request can contain at most 100 files, and each file can be up to 2 GB. See [Importing catalog information](https://docs.cloud.google.com/recommendations-ai/docs/upload-catalog) for the expected file format and setup instructions. 



### #input_uris=
    
    
    def input_uris=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. Google Cloud Storage URIs to input files. URI can be up to 2000 characters long. URIs can match the full object path (for example, `gs://bucket/directory/object.json`) or a pattern matching one or more files, such as `gs://bucket/directory/*.json`. A request can contain at most 100 files, and each file can be up to 2 GB. See [Importing catalog information](https://docs.cloud.google.com/recommendations-ai/docs/upload-catalog) for the expected file format and setup instructions. 



**Returns**

  * (::Array<::String>) — Required. Google Cloud Storage URIs to input files. URI can be up to 2000 characters long. URIs can match the full object path (for example, `gs://bucket/directory/object.json`) or a pattern matching one or more files, such as `gs://bucket/directory/*.json`. A request can contain at most 100 files, and each file can be up to 2 GB. See [Importing catalog information](https://docs.cloud.google.com/recommendations-ai/docs/upload-catalog) for the expected file format and setup instructions. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
