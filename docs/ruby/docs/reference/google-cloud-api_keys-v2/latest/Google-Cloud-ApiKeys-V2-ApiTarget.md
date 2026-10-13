---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiTarget/
title: API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiTarget (v0.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:20.899649+00:00
---

# API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiTarget (v0.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiTarget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiTarget (v0.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.2 (latest)  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.1  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the API Keys V2 API class Google::Cloud::ApiKeys::V2::ApiTarget.

A restriction for a specific service and optionally one or multiple specific methods. Both fields are case insensitive.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #methods
    
    
    def methods() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. List of one or more methods that can be called. If empty, all methods for the service are allowed. A wildcard (_) can be used as the last symbol. Valid examples:`google.cloud.translate.v2.TranslateService.GetSupportedLanguage` `TranslateText` `Get_` `translate.googleapis.com.Get*` 



### #methods=
    
    
    def methods=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. List of one or more methods that can be called. If empty, all methods for the service are allowed. A wildcard (_) can be used as the last symbol. Valid examples:`google.cloud.translate.v2.TranslateService.GetSupportedLanguage` `TranslateText` `Get_` `translate.googleapis.com.Get*` 



**Returns**

  * (::Array<::String>) — Optional. List of one or more methods that can be called. If empty, all methods for the service are allowed. A wildcard (_) can be used as the last symbol. Valid examples:`google.cloud.translate.v2.TranslateService.GetSupportedLanguage` `TranslateText` `Get_` `translate.googleapis.com.Get*` 



### #service
    
    
    def service() -> ::String

**Returns**

  * (::String) — The service for this restriction. It should be the canonical service name, for example: `translate.googleapis.com`. You can use [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) to get a list of services that are enabled in the project. 



### #service=
    
    
    def service=(value) -> ::String

**Parameter**

  * **value** (::String) — The service for this restriction. It should be the canonical service name, for example: `translate.googleapis.com`. You can use [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) to get a list of services that are enabled in the project. 



**Returns**

  * (::String) — The service for this restriction. It should be the canonical service name, for example: `translate.googleapis.com`. You can use [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) to get a list of services that are enabled in the project. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
