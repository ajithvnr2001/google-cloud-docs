---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKey/create/
title: Method: users.sshPublicKey.create \u00a0|\u00a0 Compute Engine: Virtual Machines (VMs) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:56:37.332136+00:00
---

# Method: users.sshPublicKey.create  |  Compute Engine: Virtual Machines (VMs)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKey/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Compute Engine ](https://docs.cloud.google.com/compute)



Send feedback 

#  Method: users.sshPublicKey.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Create an SSH public key

### HTTP request

`POST https://oslogin.googleapis.com/v1/{parent=users/*}/sshPublicKey`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The unique ID for the user in format `users/{user}`.  
  
### Request body

The request body contains an instance of `[SshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/SshPublicKey)`.

### Response body

If successful, the response body contains a newly created instance of `[SshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/SshPublicKey)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/compute`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
