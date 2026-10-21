---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/users.projects.locations/signSshPublicKey/
title: Method: users.projects.locations.signSshPublicKey \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:20:04.070345+00:00
---

# Method: users.projects.locations.signSshPublicKey  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/users.projects.locations/signSshPublicKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: users.projects.locations.signSshPublicKey Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Signs an SSH public key for a user to authenticate to a virtual machine on Google Compute Engine.

### HTTP request

`POST https://oslogin.googleapis.com/v1alpha/{parent=users/*/projects/*/locations/*}:signSshPublicKey`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The parent project and region for the signing request.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sshPublicKey": string
    }  
  
Fields  
---  
`sshPublicKey` |  `string` The SSH public key to sign.  
  
### Response body

If successful, the response body contains an instance of `[SignSshPublicKeyResponse](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/SignSshPublicKeyResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/compute`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
