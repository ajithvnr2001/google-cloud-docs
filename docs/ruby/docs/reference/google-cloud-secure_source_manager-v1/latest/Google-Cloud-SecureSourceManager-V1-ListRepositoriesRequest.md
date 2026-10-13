---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-ListRepositoriesRequest/
title: Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::ListRepositoriesRequest (v2.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:36.536057+00:00
---

# Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::ListRepositoriesRequest (v2.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-ListRepositoriesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::ListRepositoriesRequest (v2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.0 (latest)  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Secure Source Manager V1 API class Google::Cloud::SecureSourceManager::V1::ListRepositoriesRequest.

ListRepositoriesRequest is request to list repositories.

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

  * (::String) — Optional. Filter results. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filter results. 



**Returns**

  * (::String) — Optional. Filter results. 



### #instance
    
    
    def instance() -> ::String

**Returns**

  * (::String) — Optional. The name of the instance in which the repository is hosted, formatted as `projects/{project_number}/locations/{location_id}/instances/{instance_id}`. When listing repositories via securesourcemanager.googleapis.com, this field is required. When listing repositories via *.sourcemanager.dev, this field is ignored. 



### #instance=
    
    
    def instance=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The name of the instance in which the repository is hosted, formatted as `projects/{project_number}/locations/{location_id}/instances/{instance_id}`. When listing repositories via securesourcemanager.googleapis.com, this field is required. When listing repositories via *.sourcemanager.dev, this field is ignored. 



**Returns**

  * (::String) — Optional. The name of the instance in which the repository is hosted, formatted as `projects/{project_number}/locations/{location_id}/instances/{instance_id}`. When listing repositories via securesourcemanager.googleapis.com, this field is required. When listing repositories via *.sourcemanager.dev, this field is ignored. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Requested page size. If unspecified, a default size of 30 will be used. The maximum value is 100; values above 100 will be coerced to 100. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Requested page size. If unspecified, a default size of 30 will be used. The maximum value is 100; values above 100 will be coerced to 100. 



**Returns**

  * (::Integer) — Optional. Requested page size. If unspecified, a default size of 30 will be used. The maximum value is 100; values above 100 will be coerced to 100. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A token identifying a page of results the server should return. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A token identifying a page of results the server should return. 



**Returns**

  * (::String) — Optional. A token identifying a page of results the server should return. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Parent value for ListRepositoriesRequest. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent value for ListRepositoriesRequest. 



**Returns**

  * (::String) — Required. Parent value for ListRepositoriesRequest. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
