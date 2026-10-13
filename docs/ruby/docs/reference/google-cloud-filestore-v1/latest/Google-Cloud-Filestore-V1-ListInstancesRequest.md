---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-filestore-v1/latest/Google-Cloud-Filestore-V1-ListInstancesRequest/
title: Filestore V1 API - Class Google::Cloud::Filestore::V1::ListInstancesRequest (v2.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:25.638578+00:00
---

# Filestore V1 API - Class Google::Cloud::Filestore::V1::ListInstancesRequest (v2.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-filestore-v1/latest/Google-Cloud-Filestore-V1-ListInstancesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Filestore V1 API - Class Google::Cloud::Filestore::V1::ListInstancesRequest (v2.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.1 (latest)  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.1  2.0.0  1.2.0  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Filestore V1 API class Google::Cloud::Filestore::V1::ListInstancesRequest.

ListInstancesRequest lists instances.

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

  * (::String) — List filter. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — List filter. 



**Returns**

  * (::String) — List filter. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Sort results. Supported values are "name", "name desc" or "" (unsorted). 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Sort results. Supported values are "name", "name desc" or "" (unsorted). 



**Returns**

  * (::String) — Sort results. Supported values are "name", "name desc" or "" (unsorted). 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of items to return. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of items to return. 



**Returns**

  * (::Integer) — The maximum number of items to return. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The next_page_token value to use if there are additional results to retrieve for this list request. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The next_page_token value to use if there are additional results to retrieve for this list request. 



**Returns**

  * (::String) — The next_page_token value to use if there are additional results to retrieve for this list request. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The project and location for which to retrieve instance information, in the format `projects/{project_id}/locations/{location}`. In Cloud Filestore, locations map to Google Cloud zones, for example **us-west1-b**. To retrieve instance information for all locations, use "-" for the `{location}` value. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The project and location for which to retrieve instance information, in the format `projects/{project_id}/locations/{location}`. In Cloud Filestore, locations map to Google Cloud zones, for example **us-west1-b**. To retrieve instance information for all locations, use "-" for the `{location}` value. 



**Returns**

  * (::String) — Required. The project and location for which to retrieve instance information, in the format `projects/{project_id}/locations/{location}`. In Cloud Filestore, locations map to Google Cloud zones, for example **us-west1-b**. To retrieve instance information for all locations, use "-" for the `{location}` value. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
