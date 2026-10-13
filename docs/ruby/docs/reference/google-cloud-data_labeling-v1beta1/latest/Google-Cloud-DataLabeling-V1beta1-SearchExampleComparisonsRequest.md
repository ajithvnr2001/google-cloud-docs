---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-SearchExampleComparisonsRequest/
title: AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::SearchExampleComparisonsRequest (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:38.148983+00:00
---

# AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::SearchExampleComparisonsRequest (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-SearchExampleComparisonsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::SearchExampleComparisonsRequest (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.0 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the AI Platform Data Labeling Service V1beta1 API class Google::Cloud::DataLabeling::V1beta1::SearchExampleComparisonsRequest.

Request message of SearchExampleComparisons.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Requested page size. Server may return fewer results than requested. Default value is 100. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Requested page size. Server may return fewer results than requested. Default value is 100. 



**Returns**

  * (::Integer) — Optional. Requested page size. Server may return fewer results than requested. Default value is 100. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A token identifying a page of results for the server to return. Typically obtained by the [nextPageToken][SearchExampleComparisons.next_page_token] of the response to a previous search rquest.

If you don't specify this field, the API call requests the first page of the search. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A token identifying a page of results for the server to return. Typically obtained by the [nextPageToken][SearchExampleComparisons.next_page_token] of the response to a previous search rquest.

If you don't specify this field, the API call requests the first page of the search. 




**Returns**

  * (::String) — Optional. A token identifying a page of results for the server to return. Typically obtained by the [nextPageToken][SearchExampleComparisons.next_page_token] of the response to a previous search rquest.

If you don't specify this field, the API call requests the first page of the search. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Name of the [Evaluation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-Evaluation "Google::Cloud::DataLabeling::V1beta1::Evaluation \(class\)") resource to search for example comparisons from. Format:

"projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}" 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the [Evaluation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-Evaluation "Google::Cloud::DataLabeling::V1beta1::Evaluation \(class\)") resource to search for example comparisons from. Format:

"projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}" 




**Returns**

  * (::String) — Required. Name of the [Evaluation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-Evaluation "Google::Cloud::DataLabeling::V1beta1::Evaluation \(class\)") resource to search for example comparisons from. Format:

"projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}" 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
