---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretPayload/
title: Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::SecretPayload (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:47.849920+00:00
---

# Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::SecretPayload (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretPayload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::SecretPayload (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Secret Manager V1BETA2 API class Google::Cloud::SecretManager::V1beta2::SecretPayload.

A secret payload resource in the Secret Manager API. This contains the sensitive secret payload that is associated with a [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #data
    
    
    def data() -> ::String

**Returns**

  * (::String) — The secret data. Must be no larger than 64KiB. 



### #data=
    
    
    def data=(value) -> ::String

**Parameter**

  * **value** (::String) — The secret data. Must be no larger than 64KiB. 



**Returns**

  * (::String) — The secret data. Must be no larger than 64KiB. 



### #data_crc32c
    
    
    def data_crc32c() -> ::Integer

**Returns**

  * (::Integer) — Optional. If specified, [SecretManagerService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client \(class\)") will verify the integrity of the received [data](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretPayload#Google__Cloud__SecretManager__V1beta2__SecretPayload_data_instance_ "Google::Cloud::SecretManager::V1beta2::SecretPayload#data \(method\)") on [SecretManagerService.AddSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_add_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#add_secret_version \(method\)") calls using the crc32c checksum and store it to include in future [SecretManagerService.AccessSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_access_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#access_secret_version \(method\)") responses. If a checksum is not provided in the [SecretManagerService.AddSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_add_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#add_secret_version \(method\)") request, the [SecretManagerService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client \(class\)") will generate and store one for you.

The CRC32C value is encoded as a Int64 for compatibility, and can be safely downconverted to uint32 in languages that support this type. https://cloud.google.com/apis/design/design_patterns#integer_types 




### #data_crc32c=
    
    
    def data_crc32c=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. If specified, [SecretManagerService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client \(class\)") will verify the integrity of the received [data](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretPayload#Google__Cloud__SecretManager__V1beta2__SecretPayload_data_instance_ "Google::Cloud::SecretManager::V1beta2::SecretPayload#data \(method\)") on [SecretManagerService.AddSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_add_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#add_secret_version \(method\)") calls using the crc32c checksum and store it to include in future [SecretManagerService.AccessSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_access_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#access_secret_version \(method\)") responses. If a checksum is not provided in the [SecretManagerService.AddSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_add_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#add_secret_version \(method\)") request, the [SecretManagerService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client \(class\)") will generate and store one for you.

The CRC32C value is encoded as a Int64 for compatibility, and can be safely downconverted to uint32 in languages that support this type. https://cloud.google.com/apis/design/design_patterns#integer_types 




**Returns**

  * (::Integer) — Optional. If specified, [SecretManagerService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client \(class\)") will verify the integrity of the received [data](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretPayload#Google__Cloud__SecretManager__V1beta2__SecretPayload_data_instance_ "Google::Cloud::SecretManager::V1beta2::SecretPayload#data \(method\)") on [SecretManagerService.AddSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_add_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#add_secret_version \(method\)") calls using the crc32c checksum and store it to include in future [SecretManagerService.AccessSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_access_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#access_secret_version \(method\)") responses. If a checksum is not provided in the [SecretManagerService.AddSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_add_secret_version_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#add_secret_version \(method\)") request, the [SecretManagerService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client \(class\)") will generate and store one for you.

The CRC32C value is encoded as a Int64 for compatibility, and can be safely downconverted to uint32 in languages that support this type. https://cloud.google.com/apis/design/design_patterns#integer_types 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
