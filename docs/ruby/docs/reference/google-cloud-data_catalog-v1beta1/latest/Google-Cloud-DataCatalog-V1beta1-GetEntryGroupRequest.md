---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1beta1/latest/Google-Cloud-DataCatalog-V1beta1-GetEntryGroupRequest/
title: Google Cloud Data Catalog V1BETA1 API - Class Google::Cloud::DataCatalog::V1beta1::GetEntryGroupRequest (v0.13.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:15.005520+00:00
---

# Google Cloud Data Catalog V1BETA1 API - Class Google::Cloud::DataCatalog::V1beta1::GetEntryGroupRequest (v0.13.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1beta1/latest/Google-Cloud-DataCatalog-V1beta1-GetEntryGroupRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Data Catalog V1BETA1 API - Class Google::Cloud::DataCatalog::V1beta1::GetEntryGroupRequest (v0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.12.0  0.11.0  0.10.1  0.9.1  0.8.4  0.7.0  0.6.0  0.5.2  0.4.0  0.3.2  0.2.1  0.1.1 

Reference documentation and code samples for the Google Cloud Data Catalog V1BETA1 API class Google::Cloud::DataCatalog::V1beta1::GetEntryGroupRequest.

Request message for [GetEntryGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1beta1/latest/Google-Cloud-DataCatalog-V1beta1-DataCatalog-Client#Google__Cloud__DataCatalog__V1beta1__DataCatalog__Client_get_entry_group_instance_ "Google::Cloud::DataCatalog::V1beta1::DataCatalog::Client#get_entry_group \(method\)").

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

  * (::String) — Required. The name of the entry group. For example, `projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the entry group. For example, `projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}`. 



**Returns**

  * (::String) — Required. The name of the entry group. For example, `projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}`. 



### #read_mask
    
    
    def read_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1beta1/latest/Google-Protobuf-FieldMask)) — The fields to return. If not set or empty, all fields are returned. 



### #read_mask=
    
    
    def read_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1beta1/latest/Google-Protobuf-FieldMask)) — The fields to return. If not set or empty, all fields are returned. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1beta1/latest/Google-Protobuf-FieldMask)) — The fields to return. If not set or empty, all fields are returned. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
