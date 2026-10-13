---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation/
title: Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::Rotation (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:35.840061+00:00
---

# Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::Rotation (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::Rotation (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.21.0  0.20.0  0.19.2  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Secret Manager V1 API class Google::Cloud::SecretManager::V1::Rotation.

The rotation time and period for a [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)"). At next_rotation_time, Secret Manager will send a Pub/Sub notification to the topics configured on the Secret. [Secret.topics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret#Google__Cloud__SecretManager__V1__Secret_topics_instance_ "Google::Cloud::SecretManager::V1::Secret#topics \(method\)") must be set to configure rotation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #managed_rotation_status
    
    
    def managed_rotation_status() -> ::Google::Cloud::SecretManager::V1::Rotation::ManagedRotationStatus

**Returns**

  * ([::Google::Cloud::SecretManager::V1::Rotation::ManagedRotationStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation-ManagedRotationStatus)) — Output only. The current status of the managed rotation. This field is only applicable to Typed Secrets. This field is set by the service and cannot be set by the user. 



### #next_rotation_time
    
    
    def next_rotation_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-Timestamp)) — Optional. Timestamp in UTC at which the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") is scheduled to rotate. Cannot be set to less than 300s (5 min) in the future and at most 3153600000s (100 years).

[next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") MUST be set if [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_rotation_period_instance_ "Google::Cloud::SecretManager::V1::Rotation#rotation_period \(method\)") is set. 




### #next_rotation_time=
    
    
    def next_rotation_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-Timestamp)) — Optional. Timestamp in UTC at which the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") is scheduled to rotate. Cannot be set to less than 300s (5 min) in the future and at most 3153600000s (100 years).

[next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") MUST be set if [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_rotation_period_instance_ "Google::Cloud::SecretManager::V1::Rotation#rotation_period \(method\)") is set. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-Timestamp)) — Optional. Timestamp in UTC at which the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") is scheduled to rotate. Cannot be set to less than 300s (5 min) in the future and at most 3153600000s (100 years).

[next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") MUST be set if [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_rotation_period_instance_ "Google::Cloud::SecretManager::V1::Rotation#rotation_period \(method\)") is set. 




### #rotation_period
    
    
    def rotation_period() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-Duration)) — Input only. The Duration between rotation notifications. Must be in seconds and at least 3600s (1h) and at most 3153600000s (100 years).

If [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_rotation_period_instance_ "Google::Cloud::SecretManager::V1::Rotation#rotation_period \(method\)") is set, [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") must be set. [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") will be advanced by this period when the service automatically sends rotation notifications. 




### #rotation_period=
    
    
    def rotation_period=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-Duration)) — Input only. The Duration between rotation notifications. Must be in seconds and at least 3600s (1h) and at most 3153600000s (100 years).

If [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_rotation_period_instance_ "Google::Cloud::SecretManager::V1::Rotation#rotation_period \(method\)") is set, [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") must be set. [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") will be advanced by this period when the service automatically sends rotation notifications. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-Duration)) — Input only. The Duration between rotation notifications. Must be in seconds and at least 3600s (1h) and at most 3153600000s (100 years).

If [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_rotation_period_instance_ "Google::Cloud::SecretManager::V1::Rotation#rotation_period \(method\)") is set, [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") must be set. [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Rotation#Google__Cloud__SecretManager__V1__Rotation_next_rotation_time_instance_ "Google::Cloud::SecretManager::V1::Rotation#next_rotation_time \(method\)") will be advanced by this period when the service automatically sends rotation notifications. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
