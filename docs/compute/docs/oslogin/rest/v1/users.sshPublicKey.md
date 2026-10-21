---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKey
title: REST Resource: users.sshPublicKey \u00a0|\u00a0 Compute Engine: Virtual Machines (VMs) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:17:08.424084+00:00
---

# REST Resource: users.sshPublicKey  |  Compute Engine: Virtual Machines (VMs)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKey

  * [ Home ](https://docs.cloud.google.com/)
  * [ Compute Engine ](https://docs.cloud.google.com/compute)



Send feedback 

#  REST Resource: users.sshPublicKey Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SshPublicKey
    * JSON representation
  * Methods



## Resource: SshPublicKey

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
`key` |  `string` Public key text in SSH format, defined by [RFC4253](https://www.ietf.org/rfc/rfc4253.txt) section 6.6.  
`expirationTimeUsec` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` An expiration time in microseconds since epoch.  
`fingerprint` |  `string` Output only. The SHA-256 fingerprint of the SSH public key.  
`name` |  `string` Output only. The canonical resource name.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKey/create)`

|  Create an SSH public key  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
