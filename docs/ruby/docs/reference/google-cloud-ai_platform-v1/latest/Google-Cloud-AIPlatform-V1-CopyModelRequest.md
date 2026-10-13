---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CopyModelRequest/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::CopyModelRequest (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:19.302902+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::CopyModelRequest (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CopyModelRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::CopyModelRequest (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::CopyModelRequest.

Request message for [ModelService.CopyModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ModelService-Client#Google__Cloud__AIPlatform__V1__ModelService__Client_copy_model_instance_ "Google::Cloud::AIPlatform::V1::ModelService::Client#copy_model \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #custom_service_account
    
    
    def custom_service_account() -> ::String

**Returns**

  * (::String) — Optional. The user-provided custom service account to use to do the copy model. If empty, [Vertex AI Service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) will be used to access resources needed to upload the model. This account must belong to the destination project where the model is copied to, i.e., the project specified in the `parent` field of this request and have the Vertex AI Service Agent role in the source project.

Requires the user copying the Model to have the `iam.serviceAccounts.actAs` permission on this service account. 




### #custom_service_account=
    
    
    def custom_service_account=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The user-provided custom service account to use to do the copy model. If empty, [Vertex AI Service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) will be used to access resources needed to upload the model. This account must belong to the destination project where the model is copied to, i.e., the project specified in the `parent` field of this request and have the Vertex AI Service Agent role in the source project.

Requires the user copying the Model to have the `iam.serviceAccounts.actAs` permission on this service account. 




**Returns**

  * (::String) — Optional. The user-provided custom service account to use to do the copy model. If empty, [Vertex AI Service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) will be used to access resources needed to upload the model. This account must belong to the destination project where the model is copied to, i.e., the project specified in the `parent` field of this request and have the Vertex AI Service Agent role in the source project.

Requires the user copying the Model to have the `iam.serviceAccounts.actAs` permission on this service account. 




### #encryption_spec
    
    
    def encryption_spec() -> ::Google::Cloud::AIPlatform::V1::EncryptionSpec

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key options. If this is set, then the Model copy will be encrypted with the provided encryption key. 



### #encryption_spec=
    
    
    def encryption_spec=(value) -> ::Google::Cloud::AIPlatform::V1::EncryptionSpec

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key options. If this is set, then the Model copy will be encrypted with the provided encryption key. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key options. If this is set, then the Model copy will be encrypted with the provided encryption key. 



### #model_id
    
    
    def model_id() -> ::String

**Returns**

  * (::String) — Optional. Copy source_model into a new Model with this ID. The ID will become the final component of the model resource name.

This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.

Note: The following fields are mutually exclusive: `model_id`, `parent_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #model_id=
    
    
    def model_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Copy source_model into a new Model with this ID. The ID will become the final component of the model resource name.

This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.

Note: The following fields are mutually exclusive: `model_id`, `parent_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. Copy source_model into a new Model with this ID. The ID will become the final component of the model resource name.

This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.

Note: The following fields are mutually exclusive: `model_id`, `parent_model`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`



**Returns**

  * (::String) — Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`



### #parent_model
    
    
    def parent_model() -> ::String

**Returns**

  * (::String) — Optional. Specify this field to copy source_model into this existing Model as a new version. Format: `projects/{project}/locations/{location}/models/{model}`

Note: The following fields are mutually exclusive: `parent_model`, `model_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #parent_model=
    
    
    def parent_model=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specify this field to copy source_model into this existing Model as a new version. Format: `projects/{project}/locations/{location}/models/{model}`

Note: The following fields are mutually exclusive: `parent_model`, `model_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. Specify this field to copy source_model into this existing Model as a new version. Format: `projects/{project}/locations/{location}/models/{model}`

Note: The following fields are mutually exclusive: `parent_model`, `model_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #source_model
    
    
    def source_model() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Model to copy. That Model must be in the same Project. Format: `projects/{project}/locations/{location}/models/{model}`



### #source_model=
    
    
    def source_model=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Model to copy. That Model must be in the same Project. Format: `projects/{project}/locations/{location}/models/{model}`



**Returns**

  * (::String) — Required. The resource name of the Model to copy. That Model must be in the same Project. Format: `projects/{project}/locations/{location}/models/{model}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
