---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/users/importSshPublicKey/
title: Method: users.importSshPublicKey \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:30:10.721310+00:00
---

# Method: users.importSshPublicKey  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/users/importSshPublicKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: users.importSshPublicKey Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Adds an SSH public key and returns the profile information. Default POSIX account information is set when no username and UID exist as part of the login profile.

### HTTP request

`POST https://oslogin.googleapis.com/v1alpha/{parent=users/*}:importSshPublicKey`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The unique ID for the user in format `users/{user}`.  
  
### Query parameters

Parameters  
---  
`projectId` |  `string` The project ID of the Google Cloud Platform project.  
`view` |  `enum (`[LoginProfileView](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfileView)`)` The view configures whether to retrieve security keys information.  
`regions[]` |  `string` Optional. The regions to which to assert that the key was written. If unspecified, defaults to all regions. Regions are listed at <https://cloud.google.com/about/locations#region>.  
  
### Request body

The request body contains an instance of `[SshPublicKey](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/SshPublicKey)`.

### Response body

A response message for importing an SSH public key.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "loginProfile": {
        object ([LoginProfile](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile))
      },
      "details": string
    }  
  
Fields  
---  
`loginProfile` |  `object (`[LoginProfile](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1alpha/LoginProfile)`)` The login profile information for the user.  
`details` |  `string` Detailed information about import results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/compute`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
