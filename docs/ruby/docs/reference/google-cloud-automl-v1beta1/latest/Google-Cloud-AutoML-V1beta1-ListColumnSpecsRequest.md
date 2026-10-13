---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ListColumnSpecsRequest/
title: Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::ListColumnSpecsRequest (v0.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:15.828621+00:00
---

# Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::ListColumnSpecsRequest (v0.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ListColumnSpecsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::ListColumnSpecsRequest (v0.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.1  0.13.1  0.12.0  0.11.1  0.10.2  0.9.0  0.8.0  0.7.0  0.6.1  0.5.5 

Reference documentation and code samples for the Cloud AutoML V1beta1 API class Google::Cloud::AutoML::V1beta1::ListColumnSpecsRequest.

Request message for [AutoMl.ListColumnSpecs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-AutoML-Client#Google__Cloud__AutoML__V1beta1__AutoML__Client_list_column_specs_instance_ "Google::Cloud::AutoML::V1beta1::AutoML::Client#list_column_specs \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #field_mask
    
    
    def field_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-FieldMask)) — Mask specifying which fields to read. 



### #field_mask=
    
    
    def field_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-FieldMask)) — Mask specifying which fields to read. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-FieldMask)) — Mask specifying which fields to read. 



### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Filter expression, see go/filtering. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Filter expression, see go/filtering. 



**Returns**

  * (::String) — Filter expression, see go/filtering. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Requested page size. The server can return fewer results than requested. If unspecified, the server will pick a default size. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Requested page size. The server can return fewer results than requested. If unspecified, the server will pick a default size. 



**Returns**

  * (::Integer) — Requested page size. The server can return fewer results than requested. If unspecified, the server will pick a default size. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A token identifying a page of results for the server to return. Typically obtained from the [ListColumnSpecsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ListColumnSpecsResponse#Google__Cloud__AutoML__V1beta1__ListColumnSpecsResponse_next_page_token_instance_ "Google::Cloud::AutoML::V1beta1::ListColumnSpecsResponse#next_page_token \(method\)") field of the previous [AutoMl.ListColumnSpecs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-AutoML-Client#Google__Cloud__AutoML__V1beta1__AutoML__Client_list_column_specs_instance_ "Google::Cloud::AutoML::V1beta1::AutoML::Client#list_column_specs \(method\)") call. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token identifying a page of results for the server to return. Typically obtained from the [ListColumnSpecsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ListColumnSpecsResponse#Google__Cloud__AutoML__V1beta1__ListColumnSpecsResponse_next_page_token_instance_ "Google::Cloud::AutoML::V1beta1::ListColumnSpecsResponse#next_page_token \(method\)") field of the previous [AutoMl.ListColumnSpecs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-AutoML-Client#Google__Cloud__AutoML__V1beta1__AutoML__Client_list_column_specs_instance_ "Google::Cloud::AutoML::V1beta1::AutoML::Client#list_column_specs \(method\)") call. 



**Returns**

  * (::String) — A token identifying a page of results for the server to return. Typically obtained from the [ListColumnSpecsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ListColumnSpecsResponse#Google__Cloud__AutoML__V1beta1__ListColumnSpecsResponse_next_page_token_instance_ "Google::Cloud::AutoML::V1beta1::ListColumnSpecsResponse#next_page_token \(method\)") field of the previous [AutoMl.ListColumnSpecs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-AutoML-Client#Google__Cloud__AutoML__V1beta1__AutoML__Client_list_column_specs_instance_ "Google::Cloud::AutoML::V1beta1::AutoML::Client#list_column_specs \(method\)") call. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the table spec to list column specs from. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the table spec to list column specs from. 



**Returns**

  * (::String) — Required. The resource name of the table spec to list column specs from. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
