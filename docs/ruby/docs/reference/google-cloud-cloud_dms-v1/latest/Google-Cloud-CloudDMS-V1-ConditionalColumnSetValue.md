---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConditionalColumnSetValue/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:21.539006+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConditionalColumnSetValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue.

Options to configure rule type ConditionalColumnSetValue. The rule is used to transform the data which is being replicated/migrated.

The rule filter field can refer to one or more entities.

The rule scope can be one of: Column.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #custom_features
    
    
    def custom_features() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Optional. Custom engine specific features. 



### #custom_features=
    
    
    def custom_features=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Optional. Custom engine specific features. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Optional. Custom engine specific features. 



### #source_numeric_filter
    
    
    def source_numeric_filter() -> ::Google::Cloud::CloudDMS::V1::SourceNumericFilter

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SourceNumericFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceNumericFilter)) — Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

Note: The following fields are mutually exclusive: `source_numeric_filter`, `source_text_filter`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #source_numeric_filter=
    
    
    def source_numeric_filter=(value) -> ::Google::Cloud::CloudDMS::V1::SourceNumericFilter

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SourceNumericFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceNumericFilter)) — Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

Note: The following fields are mutually exclusive: `source_numeric_filter`, `source_text_filter`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SourceNumericFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceNumericFilter)) — Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.

Note: The following fields are mutually exclusive: `source_numeric_filter`, `source_text_filter`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #source_text_filter
    
    
    def source_text_filter() -> ::Google::Cloud::CloudDMS::V1::SourceTextFilter

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SourceTextFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceTextFilter)) — Optional. Optional filter on source column length. Used for text based data types like varchar.

Note: The following fields are mutually exclusive: `source_text_filter`, `source_numeric_filter`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #source_text_filter=
    
    
    def source_text_filter=(value) -> ::Google::Cloud::CloudDMS::V1::SourceTextFilter

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SourceTextFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceTextFilter)) — Optional. Optional filter on source column length. Used for text based data types like varchar.

Note: The following fields are mutually exclusive: `source_text_filter`, `source_numeric_filter`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SourceTextFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceTextFilter)) — Optional. Optional filter on source column length. Used for text based data types like varchar.

Note: The following fields are mutually exclusive: `source_text_filter`, `source_numeric_filter`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #value_transformation
    
    
    def value_transformation() -> ::Google::Cloud::CloudDMS::V1::ValueTransformation

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ValueTransformation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ValueTransformation)) — Required. Description of data transformation during migration. 



### #value_transformation=
    
    
    def value_transformation=(value) -> ::Google::Cloud::CloudDMS::V1::ValueTransformation

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::ValueTransformation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ValueTransformation)) — Required. Description of data transformation during migration. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ValueTransformation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ValueTransformation)) — Required. Description of data transformation during migration. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
