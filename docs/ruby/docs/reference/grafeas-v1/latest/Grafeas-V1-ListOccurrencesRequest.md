---
url: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ListOccurrencesRequest/
title: Grafeas V1 API - Class Grafeas::V1::ListOccurrencesRequest (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:29.227312+00:00
---

# Grafeas V1 API - Class Grafeas::V1::ListOccurrencesRequest (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ListOccurrencesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Grafeas V1 API - Class Grafeas::V1::ListOccurrencesRequest (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.1  1.0.0  0.16.1  0.15.0  0.14.2  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1 

Reference documentation and code samples for the Grafeas V1 API class Grafeas::V1::ListOccurrencesRequest.

Request to list occurrences.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — The filter expression. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — The filter expression. 



**Returns**

  * (::String) — The filter expression. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Number of occurrences to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of occurrences to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. 



**Returns**

  * (::Integer) — Number of occurrences to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Token to provide to skip to a particular spot in the list. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Token to provide to skip to a particular spot in the list. 



**Returns**

  * (::String) — Token to provide to skip to a particular spot in the list. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — The name of the project to list occurrences for in the form of `projects/[PROJECT_ID]`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the project to list occurrences for in the form of `projects/[PROJECT_ID]`. 



**Returns**

  * (::String) — The name of the project to list occurrences for in the form of `projects/[PROJECT_ID]`. 



### #return_partial_success
    
    
    def return_partial_success() -> ::Boolean

**Returns**

  * (::Boolean) — If set, the request will return all reachable Occurrences and report all unreachable regions in the `unreachable` field in the response.

Only applicable for requests in the global region. 




### #return_partial_success=
    
    
    def return_partial_success=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set, the request will return all reachable Occurrences and report all unreachable regions in the `unreachable` field in the response.

Only applicable for requests in the global region. 




**Returns**

  * (::Boolean) — If set, the request will return all reachable Occurrences and report all unreachable regions in the `unreachable` field in the response.

Only applicable for requests in the global region. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
