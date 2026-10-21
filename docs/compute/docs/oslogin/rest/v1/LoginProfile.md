---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/LoginProfile/
title: LoginProfile \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:11:08.178866+00:00
---

# LoginProfile  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/LoginProfile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  LoginProfile Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The user profile information used for logging in to a virtual machine on Google Compute Engine.

JSON representation  
---  
      
    
    {
      "name": string,
      "posixAccounts": [
        {
          object ([PosixAccount](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/PosixAccount))
        }
      ],
      "sshPublicKeys": {
        string: {
          object ([SshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/SshPublicKey))
        },
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Required. A unique user ID.  
`posixAccounts[]` |  `object (`[PosixAccount](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/PosixAccount)`)` The list of POSIX accounts associated with the user.  
`sshPublicKeys` |  `map (key: string, value: object (`[SshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/SshPublicKey)`))` A map from SSH public key fingerprint to the associated key object.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
