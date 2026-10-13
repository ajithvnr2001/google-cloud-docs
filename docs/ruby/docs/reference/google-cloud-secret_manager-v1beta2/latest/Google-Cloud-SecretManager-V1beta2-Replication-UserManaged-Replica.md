---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-Replication-UserManaged-Replica/
title: Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::Replication::UserManaged::Replica (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:30.041070+00:00
---

# Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::Replication::UserManaged::Replica (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-Replication-UserManaged-Replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::Replication::UserManaged::Replica (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Secret Manager V1BETA2 API class Google::Cloud::SecretManager::V1beta2::Replication::UserManaged::Replica.

Represents a Replica for this [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-Secret "Google::Cloud::SecretManager::V1beta2::Secret \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #customer_managed_encryption
    
    
    def customer_managed_encryption() -> ::Google::Cloud::SecretManager::V1beta2::CustomerManagedEncryption

**Returns**

  * ([::Google::Cloud::SecretManager::V1beta2::CustomerManagedEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-CustomerManagedEncryption)) — Optional. The customer-managed encryption configuration of the [User-Managed Replica][Replication.UserManaged.Replica]. If no configuration is provided, Google-managed default encryption is used.

Updates to the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-Secret "Google::Cloud::SecretManager::V1beta2::Secret \(class\)") encryption configuration only apply to [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") added afterwards. They do not apply retroactively to existing [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)"). 




### #customer_managed_encryption=
    
    
    def customer_managed_encryption=(value) -> ::Google::Cloud::SecretManager::V1beta2::CustomerManagedEncryption

**Parameter**

  * **value** ([::Google::Cloud::SecretManager::V1beta2::CustomerManagedEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-CustomerManagedEncryption)) — Optional. The customer-managed encryption configuration of the [User-Managed Replica][Replication.UserManaged.Replica]. If no configuration is provided, Google-managed default encryption is used.

Updates to the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-Secret "Google::Cloud::SecretManager::V1beta2::Secret \(class\)") encryption configuration only apply to [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") added afterwards. They do not apply retroactively to existing [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)"). 




**Returns**

  * ([::Google::Cloud::SecretManager::V1beta2::CustomerManagedEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-CustomerManagedEncryption)) — Optional. The customer-managed encryption configuration of the [User-Managed Replica][Replication.UserManaged.Replica]. If no configuration is provided, Google-managed default encryption is used.

Updates to the [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-Secret "Google::Cloud::SecretManager::V1beta2::Secret \(class\)") encryption configuration only apply to [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") added afterwards. They do not apply retroactively to existing [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)"). 




### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — The canonical IDs of the location to replicate data. For example: `"us-east1"`. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — The canonical IDs of the location to replicate data. For example: `"us-east1"`. 



**Returns**

  * (::String) — The canonical IDs of the location to replicate data. For example: `"us-east1"`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
