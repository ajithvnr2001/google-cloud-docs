---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-DataStoreTool-BoostSpecs/
title: Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::DataStoreTool::BoostSpecs (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:04.158321+00:00
---

# Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::DataStoreTool::BoostSpecs (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-DataStoreTool-BoostSpecs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::DataStoreTool::BoostSpecs (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1 API class Google::Cloud::Ces::V1::DataStoreTool::BoostSpecs.

Boost specifications to boost certain documents. For more information, please refer to <https://cloud.google.com/generative-ai-app-builder/docs/boosting>.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #data_stores
    
    
    def data_stores() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}. 



### #data_stores=
    
    
    def data_stores=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}. 



**Returns**

  * (::Array<::String>) — Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}. 



### #spec
    
    
    def spec() -> ::Array<::Google::Cloud::Ces::V1::DataStoreTool::BoostSpec>

**Returns**

  * (::Array<[::Google::Cloud::Ces::V1::DataStoreTool::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-DataStoreTool-BoostSpec)>) — Required. A list of boosting specifications. 



### #spec=
    
    
    def spec=(value) -> ::Array<::Google::Cloud::Ces::V1::DataStoreTool::BoostSpec>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Ces::V1::DataStoreTool::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-DataStoreTool-BoostSpec)>) — Required. A list of boosting specifications. 



**Returns**

  * (::Array<[::Google::Cloud::Ces::V1::DataStoreTool::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-DataStoreTool-BoostSpec)>) — Required. A list of boosting specifications. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
