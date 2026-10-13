---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-ListPullRequestFileDiffsRequest/
title: Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::ListPullRequestFileDiffsRequest (v2.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:46.586228+00:00
---

# Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::ListPullRequestFileDiffsRequest (v2.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-ListPullRequestFileDiffsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::ListPullRequestFileDiffsRequest (v2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.0 (latest)  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Secure Source Manager V1 API class Google::Cloud::SecureSourceManager::V1::ListPullRequestFileDiffsRequest.

ListPullRequestFileDiffsRequest is the request to list pull request file diffs.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The pull request to list file diffs for. Format: `projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The pull request to list file diffs for. Format: `projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}`



**Returns**

  * (::String) — Required. The pull request to list file diffs for. Format: `projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}`



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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
