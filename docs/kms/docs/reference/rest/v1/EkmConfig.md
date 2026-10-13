---
url: https://docs.cloud.google.com/kms/docs/reference/rest/v1/EkmConfig/
title: EkmConfig \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:51.902068+00:00
---

# EkmConfig  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/reference/rest/v1/EkmConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Reference ](https://docs.cloud.google.com/kms/docs/apis)



Send feedback 

#  EkmConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



An `[EkmConfig](https://docs.cloud.google.com/kms/docs/reference/rest/v1/EkmConfig)` is a singleton resource that represents configuration parameters that apply to all `[CryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)` and `[CryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` with a `[ProtectionLevel](https://docs.cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel)` of `[EXTERNAL_VPC](https://docs.cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel#ENUM_VALUES.EXTERNAL_VPC)` in a given project and location.

JSON representation  
---  
      
    
    {
      "name": string,
      "defaultEkmConnection": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name for the `[EkmConfig](https://docs.cloud.google.com/kms/docs/reference/rest/v1/EkmConfig)` in the format `projects/*/locations/*/ekmConfig`.  
`defaultEkmConnection` |  `string` Optional. Resource name of the default `[EkmConnection](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections#EkmConnection)`. Setting this field to the empty string removes the default.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
