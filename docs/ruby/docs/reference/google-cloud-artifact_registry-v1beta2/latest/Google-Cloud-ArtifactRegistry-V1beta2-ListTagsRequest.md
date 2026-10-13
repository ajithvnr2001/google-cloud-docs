---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-artifact_registry-v1beta2/latest/Google-Cloud-ArtifactRegistry-V1beta2-ListTagsRequest/
title: Artifact Registry V1beta2 API - Class Google::Cloud::ArtifactRegistry::V1beta2::ListTagsRequest (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:57.413689+00:00
---

# Artifact Registry V1beta2 API - Class Google::Cloud::ArtifactRegistry::V1beta2::ListTagsRequest (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-artifact_registry-v1beta2/latest/Google-Cloud-ArtifactRegistry-V1beta2-ListTagsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Artifact Registry V1beta2 API - Class Google::Cloud::ArtifactRegistry::V1beta2::ListTagsRequest (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.1  0.11.2  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the Artifact Registry V1beta2 API class Google::Cloud::ArtifactRegistry::V1beta2::ListTagsRequest.

The request to list tags.

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

  * (::String) — 

An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

    * `version`

An example of using a filter:

    * `version="projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/1.0"` \--> Tags that are applied to the version `1.0` in package `pkg1`.



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

    * `version`

An example of using a filter:

    * `version="projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/1.0"` \--> Tags that are applied to the version `1.0` in package `pkg1`.



**Returns**

  * (::String) — 

An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

    * `version`

An example of using a filter:

    * `version="projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/1.0"` \--> Tags that are applied to the version `1.0` in package `pkg1`.



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of tags to return. Maximum page size is 10,000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of tags to return. Maximum page size is 10,000. 



**Returns**

  * (::Integer) — The maximum number of tags to return. Maximum page size is 10,000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The next_page_token value returned from a previous list request, if any. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The next_page_token value returned from a previous list request, if any. 



**Returns**

  * (::String) — The next_page_token value returned from a previous list request, if any. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — The name of the parent resource whose tags will be listed. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the parent resource whose tags will be listed. 



**Returns**

  * (::String) — The name of the parent resource whose tags will be listed. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
