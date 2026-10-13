---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-ClassificationModelOptions/
title: Natural Language V1 API - Class Google::Cloud::Language::V1::ClassificationModelOptions (v1.7.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:56.231315+00:00
---

# Natural Language V1 API - Class Google::Cloud::Language::V1::ClassificationModelOptions (v1.7.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-ClassificationModelOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Natural Language V1 API - Class Google::Cloud::Language::V1::ClassificationModelOptions (v1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Natural Language V1 API class Google::Cloud::Language::V1::ClassificationModelOptions.

Model options available for classification requests.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #v1_model
    
    
    def v1_model() -> ::Google::Cloud::Language::V1::ClassificationModelOptions::V1Model

**Returns**

  * ([::Google::Cloud::Language::V1::ClassificationModelOptions::V1Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-ClassificationModelOptions-V1Model)) — Setting this field will use the V1 model and V1 content categories version. The V1 model is a legacy model; support for this will be discontinued in the future.

Note: The following fields are mutually exclusive: `v1_model`, `v2_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #v1_model=
    
    
    def v1_model=(value) -> ::Google::Cloud::Language::V1::ClassificationModelOptions::V1Model

**Parameter**

  * **value** ([::Google::Cloud::Language::V1::ClassificationModelOptions::V1Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-ClassificationModelOptions-V1Model)) — Setting this field will use the V1 model and V1 content categories version. The V1 model is a legacy model; support for this will be discontinued in the future.

Note: The following fields are mutually exclusive: `v1_model`, `v2_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Language::V1::ClassificationModelOptions::V1Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-ClassificationModelOptions-V1Model)) — Setting this field will use the V1 model and V1 content categories version. The V1 model is a legacy model; support for this will be discontinued in the future.

Note: The following fields are mutually exclusive: `v1_model`, `v2_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #v2_model
    
    
    def v2_model() -> ::Google::Cloud::Language::V1::ClassificationModelOptions::V2Model

**Returns**

  * ([::Google::Cloud::Language::V1::ClassificationModelOptions::V2Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-ClassificationModelOptions-V2Model)) — Setting this field will use the V2 model with the appropriate content categories version. The V2 model is a better performing model.

Note: The following fields are mutually exclusive: `v2_model`, `v1_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #v2_model=
    
    
    def v2_model=(value) -> ::Google::Cloud::Language::V1::ClassificationModelOptions::V2Model

**Parameter**

  * **value** ([::Google::Cloud::Language::V1::ClassificationModelOptions::V2Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-ClassificationModelOptions-V2Model)) — Setting this field will use the V2 model with the appropriate content categories version. The V2 model is a better performing model.

Note: The following fields are mutually exclusive: `v2_model`, `v1_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Language::V1::ClassificationModelOptions::V2Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-ClassificationModelOptions-V2Model)) — Setting this field will use the V2 model with the appropriate content categories version. The V2 model is a better performing model.

Note: The following fields are mutually exclusive: `v2_model`, `v1_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
