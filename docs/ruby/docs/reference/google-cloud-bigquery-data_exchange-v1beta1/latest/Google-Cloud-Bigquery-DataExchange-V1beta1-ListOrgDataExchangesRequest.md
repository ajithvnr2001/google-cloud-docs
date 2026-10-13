---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_exchange-v1beta1/latest/Google-Cloud-Bigquery-DataExchange-V1beta1-ListOrgDataExchangesRequest/
title: Analytics Hub V1beta1 API - Class Google::Cloud::Bigquery::DataExchange::V1beta1::ListOrgDataExchangesRequest (v0.13.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:17.859380+00:00
---

# Analytics Hub V1beta1 API - Class Google::Cloud::Bigquery::DataExchange::V1beta1::ListOrgDataExchangesRequest (v0.13.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_exchange-v1beta1/latest/Google-Cloud-Bigquery-DataExchange-V1beta1-ListOrgDataExchangesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Analytics Hub V1beta1 API - Class Google::Cloud::Bigquery::DataExchange::V1beta1::ListOrgDataExchangesRequest (v0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.1  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Analytics Hub V1beta1 API class Google::Cloud::Bigquery::DataExchange::V1beta1::ListOrgDataExchangesRequest.

Message for requesting the list of data exchanges from projects in an organization and location.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #organization
    
    
    def organization() -> ::String

**Returns**

  * (::String) — Required. The organization resource path of the projects containing DataExchanges. e.g. `organizations/myorg/locations/US`. 



### #organization=
    
    
    def organization=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The organization resource path of the projects containing DataExchanges. e.g. `organizations/myorg/locations/US`. 



**Returns**

  * (::String) — Required. The organization resource path of the projects containing DataExchanges. e.g. `organizations/myorg/locations/US`. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. 



**Returns**

  * (::Integer) — The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Page token, returned by a previous call, to request the next page of results. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Page token, returned by a previous call, to request the next page of results. 



**Returns**

  * (::String) — Page token, returned by a previous call, to request the next page of results. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
