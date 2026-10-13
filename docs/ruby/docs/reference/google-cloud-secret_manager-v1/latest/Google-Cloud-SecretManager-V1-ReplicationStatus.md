---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ReplicationStatus/
title: Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::ReplicationStatus (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:38.878115+00:00
---

# Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::ReplicationStatus (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ReplicationStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::ReplicationStatus (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.21.0  0.20.0  0.19.2  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Secret Manager V1 API class Google::Cloud::SecretManager::V1::ReplicationStatus.

The replication status of a [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion "Google::Cloud::SecretManager::V1::SecretVersion \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #automatic
    
    
    def automatic() -> ::Google::Cloud::SecretManager::V1::ReplicationStatus::AutomaticStatus

**Returns**

  * ([::Google::Cloud::SecretManager::V1::ReplicationStatus::AutomaticStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ReplicationStatus-AutomaticStatus)) — Describes the replication status of a [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion "Google::Cloud::SecretManager::V1::SecretVersion \(class\)") with automatic replication.

Only populated if the parent [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") has an automatic replication policy.

Note: The following fields are mutually exclusive: `automatic`, `user_managed`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #automatic=
    
    
    def automatic=(value) -> ::Google::Cloud::SecretManager::V1::ReplicationStatus::AutomaticStatus

**Parameter**

  * **value** ([::Google::Cloud::SecretManager::V1::ReplicationStatus::AutomaticStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ReplicationStatus-AutomaticStatus)) — Describes the replication status of a [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion "Google::Cloud::SecretManager::V1::SecretVersion \(class\)") with automatic replication.

Only populated if the parent [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") has an automatic replication policy.

Note: The following fields are mutually exclusive: `automatic`, `user_managed`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::SecretManager::V1::ReplicationStatus::AutomaticStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ReplicationStatus-AutomaticStatus)) — Describes the replication status of a [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion "Google::Cloud::SecretManager::V1::SecretVersion \(class\)") with automatic replication.

Only populated if the parent [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") has an automatic replication policy.

Note: The following fields are mutually exclusive: `automatic`, `user_managed`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #user_managed
    
    
    def user_managed() -> ::Google::Cloud::SecretManager::V1::ReplicationStatus::UserManagedStatus

**Returns**

  * ([::Google::Cloud::SecretManager::V1::ReplicationStatus::UserManagedStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ReplicationStatus-UserManagedStatus)) — Describes the replication status of a [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion "Google::Cloud::SecretManager::V1::SecretVersion \(class\)") with user-managed replication.

Only populated if the parent [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") has a user-managed replication policy.

Note: The following fields are mutually exclusive: `user_managed`, `automatic`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #user_managed=
    
    
    def user_managed=(value) -> ::Google::Cloud::SecretManager::V1::ReplicationStatus::UserManagedStatus

**Parameter**

  * **value** ([::Google::Cloud::SecretManager::V1::ReplicationStatus::UserManagedStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ReplicationStatus-UserManagedStatus)) — Describes the replication status of a [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion "Google::Cloud::SecretManager::V1::SecretVersion \(class\)") with user-managed replication.

Only populated if the parent [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") has a user-managed replication policy.

Note: The following fields are mutually exclusive: `user_managed`, `automatic`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::SecretManager::V1::ReplicationStatus::UserManagedStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ReplicationStatus-UserManagedStatus)) — Describes the replication status of a [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion "Google::Cloud::SecretManager::V1::SecretVersion \(class\)") with user-managed replication.

Only populated if the parent [Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret "Google::Cloud::SecretManager::V1::Secret \(class\)") has a user-managed replication policy.

Note: The following fields are mutually exclusive: `user_managed`, `automatic`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
