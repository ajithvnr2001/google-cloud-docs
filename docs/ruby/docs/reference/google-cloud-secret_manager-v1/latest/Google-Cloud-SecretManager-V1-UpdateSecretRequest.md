---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-UpdateSecretRequest/
title: Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::UpdateSecretRequest (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:06.154232+00:00
---

# Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::UpdateSecretRequest (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-UpdateSecretRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::UpdateSecretRequest (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.21.0  0.20.0  0.19.2  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Secret Manager V1 API class Google::Cloud::SecretManager::V1::UpdateSecretRequest.

Request message for [SecretManagerService.UpdateSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Client#Google__Cloud__SecretManager__V1__SecretManagerService__Client_update_secret_instance_ "Google::Cloud::SecretManager::V1::SecretManagerService::Client#update_secret \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #secret
    
    
    def secret() -> ::Google::Cloud::SecretManager::V1::Secret

**Returns**

  * ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) — Required. [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") with updated field values. 



### #secret=
    
    
    def secret=(value) -> ::Google::Cloud::SecretManager::V1::Secret

**Parameter**

  * **value** ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) — Required. [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") with updated field values. 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) — Required. [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") with updated field values. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-FieldMask)) — Required. Specifies the fields to be updated. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-FieldMask)) — Required. Specifies the fields to be updated. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-FieldMask)) — Required. Specifies the fields to be updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
