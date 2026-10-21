---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/EncryptionInfo/
title: EncryptionInfo \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:46.574043+00:00
---

# EncryptionInfo  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/EncryptionInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  EncryptionInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Type
  * KmsKeyState



EncryptionInfo describes the encryption information of a cluster.

JSON representation  
---  
      
    
    {
      "encryptionType": enum ([Type](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/EncryptionInfo#Type)),
      "kmsKeyVersions": [
        string
      ],
      "kmsKeyPrimaryState": enum ([KmsKeyState](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/EncryptionInfo#KmsKeyState)),
      "lastUpdateTime": string
    }  
  
Fields  
---  
`encryptionType` |  `enum (`[Type](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/EncryptionInfo#Type)`)` Output only. Type of encryption.  
`kmsKeyVersions[]` |  `string` Output only. KMS key versions that are being used to protect the data at-rest.  
`kmsKeyPrimaryState` |  `enum (`[KmsKeyState](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/EncryptionInfo#KmsKeyState)`)` Output only. The state of the primary version of the KMS key perceived by the system. This field is not populated in backups.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time when the encryption info was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Type

Possible encryption types.

Enums  
---  
`TYPE_UNSPECIFIED` | Encryption type not specified. Defaults to GOOGLE_DEFAULT_ENCRYPTION.  
`GOOGLE_DEFAULT_ENCRYPTION` | The data is encrypted at rest with a key that is fully managed by Google. No key version will be populated. This is the default state.  
`CUSTOMER_MANAGED_ENCRYPTION` | The data is encrypted at rest with a key that is managed by the customer. KMS key versions will be populated.  
  
## KmsKeyState

The state of the KMS key perceived by the system. Refer to the public documentation for the impact of each state.

Enums  
---  
`KMS_KEY_STATE_UNSPECIFIED` | The default value. This value is unused.  
`ENABLED` | The KMS key is enabled and correctly configured.  
`PERMISSION_DENIED` | Permission denied on the KMS key.  
`DISABLED` | The KMS key is disabled.  
`DESTROYED` | The KMS key is destroyed.  
`DESTROY_SCHEDULED` | The KMS key is scheduled to be destroyed.  
`EKM_KEY_UNREACHABLE_DETECTED` | The EKM key is unreachable.  
`BILLING_DISABLED` | Billing is disabled for the project.  
`UNKNOWN_FAILURE` | All other unknown failures.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-22 UTC."],[],[]] 
