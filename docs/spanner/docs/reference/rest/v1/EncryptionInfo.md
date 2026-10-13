---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/EncryptionInfo/
title: EncryptionInfo \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:17.794451+00:00
---

# EncryptionInfo  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/EncryptionInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  EncryptionInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Type



Encryption information for a Cloud Spanner database or backup.

JSON representation  
---  
      
    
    {
      "encryptionType": enum ([Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/EncryptionInfo#Type)),
      "encryptionStatus": {
        object ([Status](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Status))
      },
      "kmsKeyVersion": string
    }  
  
Fields  
---  
`encryptionType` |  `enum (`[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/EncryptionInfo#Type)`)` Output only. The type of encryption.  
`encryptionStatus` |  `object (`[Status](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Status)`)` Output only. If present, the status of a recent encrypt/decrypt call on underlying data for this database or backup. Regardless of status, data is always encrypted at rest.  
`kmsKeyVersion` |  `string` Output only. A Cloud KMS key version that is being used to protect the database or backup.  
  
## Type

Possible encryption types.

Enums  
---  
`TYPE_UNSPECIFIED` | Encryption type was not specified, though data at rest remains encrypted.  
`GOOGLE_DEFAULT_ENCRYPTION` | The data is encrypted at rest with a key that is fully managed by Google. No key version or status will be populated. This is the default state.  
`CUSTOMER_MANAGED_ENCRYPTION` | The data is encrypted at rest with a key that is managed by the customer. The active version of the key. `kmsKeyVersion` will be populated, and `encryptionStatus` may be populated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
