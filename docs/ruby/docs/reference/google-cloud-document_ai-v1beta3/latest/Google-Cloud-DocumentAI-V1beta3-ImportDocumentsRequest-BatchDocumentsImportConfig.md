---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ImportDocumentsRequest-BatchDocumentsImportConfig/
title: Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig (v0.49.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:32.663193+00:00
---

# Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig (v0.49.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ImportDocumentsRequest-BatchDocumentsImportConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig (v0.49.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.49.1 (latest)  0.49.0  0.48.1  0.47.0  0.46.2  0.45.0  0.44.0  0.43.1  0.42.0  0.41.0  0.40.0  0.39.1  0.38.0  0.37.0  0.36.1  0.35.0  0.34.0  0.33.1  0.32.0  0.31.0  0.30.2  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.4 

Reference documentation and code samples for the Document AI V1beta3 API class Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig.

Config for importing documents. Each batch can have its own dataset split type.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auto_split_config
    
    
    def auto_split_config() -> ::Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig::AutoSplitConfig

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig::AutoSplitConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ImportDocumentsRequest-BatchDocumentsImportConfig-AutoSplitConfig)) — If set, documents will be automatically split into training and test split category with the specified ratio.

Note: The following fields are mutually exclusive: `auto_split_config`, `dataset_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #auto_split_config=
    
    
    def auto_split_config=(value) -> ::Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig::AutoSplitConfig

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig::AutoSplitConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ImportDocumentsRequest-BatchDocumentsImportConfig-AutoSplitConfig)) — If set, documents will be automatically split into training and test split category with the specified ratio.

Note: The following fields are mutually exclusive: `auto_split_config`, `dataset_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::ImportDocumentsRequest::BatchDocumentsImportConfig::AutoSplitConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ImportDocumentsRequest-BatchDocumentsImportConfig-AutoSplitConfig)) — If set, documents will be automatically split into training and test split category with the specified ratio.

Note: The following fields are mutually exclusive: `auto_split_config`, `dataset_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #batch_input_config
    
    
    def batch_input_config() -> ::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchDocumentsInputConfig)) — The common config to specify a set of documents used as input. 



### #batch_input_config=
    
    
    def batch_input_config=(value) -> ::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchDocumentsInputConfig)) — The common config to specify a set of documents used as input. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchDocumentsInputConfig)) — The common config to specify a set of documents used as input. 



### #dataset_split
    
    
    def dataset_split() -> ::Google::Cloud::DocumentAI::V1beta3::DatasetSplitType

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::DatasetSplitType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DatasetSplitType)) — Target dataset split where the documents must be stored.

Note: The following fields are mutually exclusive: `dataset_split`, `auto_split_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dataset_split=
    
    
    def dataset_split=(value) -> ::Google::Cloud::DocumentAI::V1beta3::DatasetSplitType

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::DatasetSplitType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DatasetSplitType)) — Target dataset split where the documents must be stored.

Note: The following fields are mutually exclusive: `dataset_split`, `auto_split_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::DatasetSplitType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DatasetSplitType)) — Target dataset split where the documents must be stored.

Note: The following fields are mutually exclusive: `dataset_split`, `auto_split_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #document_type
    
    
    def document_type() -> ::String

**Returns**

  * (::String) — Optional. If set, determines the type of the documents to be imported in this batch. It can be used to auto-label the documents with a single entity of the provided type. This field can only be used with a classifier or splitter processor. Providing this field is mutually exclusive with `entities` and `auto_labeling_config`. 



### #document_type=
    
    
    def document_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. If set, determines the type of the documents to be imported in this batch. It can be used to auto-label the documents with a single entity of the provided type. This field can only be used with a classifier or splitter processor. Providing this field is mutually exclusive with `entities` and `auto_labeling_config`. 



**Returns**

  * (::String) — Optional. If set, determines the type of the documents to be imported in this batch. It can be used to auto-label the documents with a single entity of the provided type. This field can only be used with a classifier or splitter processor. Providing this field is mutually exclusive with `entities` and `auto_labeling_config`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
