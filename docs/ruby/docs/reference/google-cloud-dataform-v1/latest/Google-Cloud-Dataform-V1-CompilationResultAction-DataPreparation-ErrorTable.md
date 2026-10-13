---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-CompilationResultAction-DataPreparation-ErrorTable/
title: Dataform V1 API - Class Google::Cloud::Dataform::V1::CompilationResultAction::DataPreparation::ErrorTable (v1.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:33.590991+00:00
---

# Dataform V1 API - Class Google::Cloud::Dataform::V1::CompilationResultAction::DataPreparation::ErrorTable (v1.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-CompilationResultAction-DataPreparation-ErrorTable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataform V1 API - Class Google::Cloud::Dataform::V1::CompilationResultAction::DataPreparation::ErrorTable (v1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataform V1 API class Google::Cloud::Dataform::V1::CompilationResultAction::DataPreparation::ErrorTable.

Error table information, used to write error data into a BigQuery table.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #retention_days
    
    
    def retention_days() -> ::Integer

**Returns**

  * (::Integer) — Error table partition expiration in days. Only positive values are allowed. 



### #retention_days=
    
    
    def retention_days=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Error table partition expiration in days. Only positive values are allowed. 



**Returns**

  * (::Integer) — Error table partition expiration in days. Only positive values are allowed. 



### #target
    
    
    def target() -> ::Google::Cloud::Dataform::V1::Target

**Returns**

  * ([::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)) — Error Table target. 



### #target=
    
    
    def target=(value) -> ::Google::Cloud::Dataform::V1::Target

**Parameter**

  * **value** ([::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)) — Error Table target. 



**Returns**

  * ([::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)) — Error Table target. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
