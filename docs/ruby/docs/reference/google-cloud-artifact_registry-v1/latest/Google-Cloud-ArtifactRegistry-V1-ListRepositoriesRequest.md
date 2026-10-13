---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-artifact_registry-v1/latest/Google-Cloud-ArtifactRegistry-V1-ListRepositoriesRequest/
title: Artifact Registry V1 API - Class Google::Cloud::ArtifactRegistry::V1::ListRepositoriesRequest (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:18.195469+00:00
---

# Artifact Registry V1 API - Class Google::Cloud::ArtifactRegistry::V1::ListRepositoriesRequest (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-artifact_registry-v1/latest/Google-Cloud-ArtifactRegistry-V1-ListRepositoriesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Artifact Registry V1 API - Class Google::Cloud::ArtifactRegistry::V1::ListRepositoriesRequest (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Artifact Registry V1 API class Google::Cloud::ArtifactRegistry::V1::ListRepositoriesRequest.

The request to list repositories.

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

Optional. An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

    * `name`

Examples of using a filter:

To filter the results of your request to repositories with the name `my-repo` in project `my-project` in the `us-central` region, append the following filter expression to your request:

    * `name="projects/my-project/locations/us-central1/repositories/my-repo"`

You can also use wildcards to match any number of characters before or after the value:

    * `name="projects/my-project/locations/us-central1/repositories/my-*"`
    * `name="projects/my-project/locations/us-central1/repositories/*repo"`
    * `name="projects/my-project/locations/us-central1/repositories/*repo*"`



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

    * `name`

Examples of using a filter:

To filter the results of your request to repositories with the name `my-repo` in project `my-project` in the `us-central` region, append the following filter expression to your request:

    * `name="projects/my-project/locations/us-central1/repositories/my-repo"`

You can also use wildcards to match any number of characters before or after the value:

    * `name="projects/my-project/locations/us-central1/repositories/my-*"`
    * `name="projects/my-project/locations/us-central1/repositories/*repo"`
    * `name="projects/my-project/locations/us-central1/repositories/*repo*"`



**Returns**

  * (::String) — 

Optional. An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

    * `name`

Examples of using a filter:

To filter the results of your request to repositories with the name `my-repo` in project `my-project` in the `us-central` region, append the following filter expression to your request:

    * `name="projects/my-project/locations/us-central1/repositories/my-repo"`

You can also use wildcards to match any number of characters before or after the value:

    * `name="projects/my-project/locations/us-central1/repositories/my-*"`
    * `name="projects/my-project/locations/us-central1/repositories/*repo"`
    * `name="projects/my-project/locations/us-central1/repositories/*repo*"`



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. The field to order the results by. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The field to order the results by. 



**Returns**

  * (::String) — Optional. The field to order the results by. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of repositories to return. Maximum page size is 1,000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of repositories to return. Maximum page size is 1,000. 



**Returns**

  * (::Integer) — The maximum number of repositories to return. Maximum page size is 1,000. 



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

  * (::String) — Required. The name of the parent resource whose repositories will be listed. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the parent resource whose repositories will be listed. 



**Returns**

  * (::String) — Required. The name of the parent resource whose repositories will be listed. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
