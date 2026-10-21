---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/SshPublicKey/
title: SshPublicKey \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:30:02.816415+00:00
---

# SshPublicKey  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/SshPublicKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  SshPublicKey Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The SSH public key information associated with a Google account.

JSON representation  
---  
      
    
    {
      "key": string,
      "expirationTimeUsec": string,
      "fingerprint": string,
      "name": string
    }  
  
Fields  
---  
`key` |  `string` Required. Public key text in SSH format, defined by [RFC4253](https://www.ietf.org/rfc/rfc4253.txt) section 6.6.  
`expirationTimeUsec` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` An expiration time in microseconds since epoch.  
`fingerprint` |  `string` Output only. The SHA-256 fingerprint of the SSH public key.  
`name` |  `string` Output only. The canonical resource name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
