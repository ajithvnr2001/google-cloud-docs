---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-FetchStaticIpsResponse/
title: Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::FetchStaticIpsResponse (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:41.264970+00:00
---

# Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::FetchStaticIpsResponse (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-FetchStaticIpsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::FetchStaticIpsResponse (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Datastream V1alpha1 API class Google::Cloud::Datastream::V1alpha1::FetchStaticIpsResponse.

Response message for a 'FetchStaticIps' response.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



**Returns**

  * (::String) — A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #static_ips
    
    
    def static_ips() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — list of static ips by account 



### #static_ips=
    
    
    def static_ips=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — list of static ips by account 



**Returns**

  * (::Array<::String>) — list of static ips by account 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
