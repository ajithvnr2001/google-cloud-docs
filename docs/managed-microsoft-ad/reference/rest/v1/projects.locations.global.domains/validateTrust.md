---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/validateTrust/
title: Method: domains.validateTrust \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:15.190587+00:00
---

# Method: domains.validateTrust  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/validateTrust/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Method: domains.validateTrust Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * Try it!



**Full name** : projects.locations.global.domains.validateTrust

Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.

### HTTP request

`POST https://managedidentities.googleapis.com/v1/{name=projects/*/locations/global/domains/*}:validateTrust`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource domain name, project name, and location using the form: `projects/{projectId}/locations/global/domains/{domainName}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `managedidentities.domains.validateTrust`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "trust": {
        object ([Trust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#Trust))
      }
    }  
  
Fields  
---  
`trust` |  `object (`[Trust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#Trust)`)` Required. The domain trust to validate trust state for.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
