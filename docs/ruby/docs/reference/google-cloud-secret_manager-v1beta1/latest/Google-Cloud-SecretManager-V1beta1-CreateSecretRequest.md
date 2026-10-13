---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-CreateSecretRequest/
title: Secret Manager V1beta1 API - Class Google::Cloud::SecretManager::V1beta1::CreateSecretRequest (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:53.175107+00:00
---

# Secret Manager V1beta1 API - Class Google::Cloud::SecretManager::V1beta1::CreateSecretRequest (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-CreateSecretRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1beta1 API - Class Google::Cloud::SecretManager::V1beta1::CreateSecretRequest (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.1  0.14.2  0.13.0  0.12.2  0.11.0  0.10.0  0.9.0  0.8.5 

Reference documentation and code samples for the Secret Manager V1beta1 API class Google::Cloud::SecretManager::V1beta1::CreateSecretRequest.

Request message for [SecretManagerService.CreateSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta1__SecretManagerService__Client_create_secret_instance_ "Google::Cloud::SecretManager::V1beta1::SecretManagerService::Client#create_secret \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the project to associate with the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret "Google::Cloud::SecretManager::V1beta1::Secret \(class\)"), in the format `projects/*`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the project to associate with the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret "Google::Cloud::SecretManager::V1beta1::Secret \(class\)"), in the format `projects/*`. 



**Returns**

  * (::String) — Required. The resource name of the project to associate with the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret "Google::Cloud::SecretManager::V1beta1::Secret \(class\)"), in the format `projects/*`. 



### #secret
    
    
    def secret() -> ::Google::Cloud::SecretManager::V1beta1::Secret

**Returns**

  * ([::Google::Cloud::SecretManager::V1beta1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret)) — Required. A [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret "Google::Cloud::SecretManager::V1beta1::Secret \(class\)") with initial field values. 



### #secret=
    
    
    def secret=(value) -> ::Google::Cloud::SecretManager::V1beta1::Secret

**Parameter**

  * **value** ([::Google::Cloud::SecretManager::V1beta1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret)) — Required. A [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret "Google::Cloud::SecretManager::V1beta1::Secret \(class\)") with initial field values. 



**Returns**

  * ([::Google::Cloud::SecretManager::V1beta1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret)) — Required. A [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-Secret "Google::Cloud::SecretManager::V1beta1::Secret \(class\)") with initial field values. 



### #secret_id
    
    
    def secret_id() -> ::String

**Returns**

  * (::String) — Required. This must be unique within the project.

A secret ID is a string with a maximum length of 255 characters and can contain uppercase and lowercase letters, numerals, and the hyphen (`-`) and underscore (`_`) characters. 




### #secret_id=
    
    
    def secret_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. This must be unique within the project.

A secret ID is a string with a maximum length of 255 characters and can contain uppercase and lowercase letters, numerals, and the hyphen (`-`) and underscore (`_`) characters. 




**Returns**

  * (::String) — Required. This must be unique within the project.

A secret ID is a string with a maximum length of 255 characters and can contain uppercase and lowercase letters, numerals, and the hyphen (`-`) and underscore (`_`) characters. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
