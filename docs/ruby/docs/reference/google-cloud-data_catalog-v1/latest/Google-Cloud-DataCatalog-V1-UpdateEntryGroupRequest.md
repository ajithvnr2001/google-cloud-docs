---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-UpdateEntryGroupRequest/
title: Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::UpdateEntryGroupRequest (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:36.728854+00:00
---

# Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::UpdateEntryGroupRequest (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-UpdateEntryGroupRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::UpdateEntryGroupRequest (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.1  2.2.2  2.1.1  2.0.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.2  0.20.1  0.19.0  0.18.1  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1 

Reference documentation and code samples for the Data Catalog V1 API class Google::Cloud::DataCatalog::V1::UpdateEntryGroupRequest.

Request message for [UpdateEntryGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DataCatalog-Client#Google__Cloud__DataCatalog__V1__DataCatalog__Client_update_entry_group_instance_ "Google::Cloud::DataCatalog::V1::DataCatalog::Client#update_entry_group \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #entry_group
    
    
    def entry_group() -> ::Google::Cloud::DataCatalog::V1::EntryGroup

**Returns**

  * ([::Google::Cloud::DataCatalog::V1::EntryGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-EntryGroup)) — Required. Updates for the entry group. The `name` field must be set. 



### #entry_group=
    
    
    def entry_group=(value) -> ::Google::Cloud::DataCatalog::V1::EntryGroup

**Parameter**

  * **value** ([::Google::Cloud::DataCatalog::V1::EntryGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-EntryGroup)) — Required. Updates for the entry group. The `name` field must be set. 



**Returns**

  * ([::Google::Cloud::DataCatalog::V1::EntryGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-EntryGroup)) — Required. Updates for the entry group. The `name` field must be set. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-FieldMask)) — Names of fields whose values to overwrite on an entry group.

If this parameter is absent or empty, all modifiable fields are overwritten. If such fields are non-required and omitted in the request body, their values are emptied. 




### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-FieldMask)) — Names of fields whose values to overwrite on an entry group.

If this parameter is absent or empty, all modifiable fields are overwritten. If such fields are non-required and omitted in the request body, their values are emptied. 




**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-FieldMask)) — Names of fields whose values to overwrite on an entry group.

If this parameter is absent or empty, all modifiable fields are overwritten. If such fields are non-required and omitted in the request body, their values are emptied. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
