---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/resetAdminPassword/
title: Method: domains.resetAdminPassword \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:14.532124+00:00
---

# Method: domains.resetAdminPassword  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/resetAdminPassword/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Method: domains.resetAdminPassword Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



**Full name** : projects.locations.global.domains.resetAdminPassword

Resets a domain's administrator password.

### HTTP request

`POST https://managedidentities.googleapis.com/v1/{name=projects/*/locations/global/domains/*}:resetAdminPassword`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The domain resource name using the form: `projects/{projectId}/locations/global/domains/{domainName}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `managedidentities.domains.resetpassword`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for [domains.resetAdminPassword][google.cloud.managedidentities.v1.ResetAdminPassword]

JSON representation  
---  
      
    
    {
      "password": string
    }  
  
Fields  
---  
`password` |  `string` A random password. See `[admin](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#Domain.FIELDS.admin)` for more information.  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
