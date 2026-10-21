---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile/
title: LoginProfile \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:32:44.587979+00:00
---

# LoginProfile  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  LoginProfile Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SecurityKey
    * JSON representation
  * UniversalTwoFactor
    * JSON representation
  * WebAuthn
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
      },
      "securityKeys": [
        {
          object ([SecurityKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile#SecurityKey))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. A unique user ID.  
`posixAccounts[]` |  `object (`[PosixAccount](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/PosixAccount)`)` The list of POSIX accounts associated with the user.  
`sshPublicKeys` |  `map (key: string, value: object (`[SshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/SshPublicKey)`))` A map from SSH public key fingerprint to the associated key object.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`securityKeys[]` |  `object (`[SecurityKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile#SecurityKey)`)` The registered security key credentials for a user.  
  
## SecurityKey

The credential information for a Google registered security key.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "privateKey": string,
    
      // Union field protocol_type can be only one of the following:
      "universalTwoFactor": {
        object ([UniversalTwoFactor](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile#UniversalTwoFactor))
      },
      "webAuthn": {
        object ([WebAuthn](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile#WebAuthn))
      }
      // End of list of possible types for union field protocol_type.
      "deviceNickname": string
    }  
  
Fields  
---  
`publicKey` |  `string` Public key text in SSH format, defined by [RFC4253](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile/) section 6.6.  
`privateKey` |  `string` Hardware-backed private key text in SSH format.  
Union field `protocol_type`. The FIDO protocol type used to register this credential. `protocol_type` can be only one of the following:  
`universalTwoFactor` |  `object (`[UniversalTwoFactor](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile#UniversalTwoFactor)`)` The U2F protocol type.  
`webAuthn` |  `object (`[WebAuthn](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile#WebAuthn)`)` The Web Authentication protocol type.  
`deviceNickname` |  `string` The security key nickname explicitly set by the user.  
  
## UniversalTwoFactor

Security key information specific to the U2F protocol.

JSON representation  
---  
      
    
    {
      "appId": string
    }  
  
Fields  
---  
`appId` |  `string` Application ID for the U2F protocol.  
  
## WebAuthn

Security key information specific to the Web Authentication protocol.

JSON representation  
---  
      
    
    {
      "rpId": string
    }  
  
Fields  
---  
`rpId` |  `string` Relying party ID for Web Authentication.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
