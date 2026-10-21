---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/extendSchema/
title: Method: domains.extendSchema \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:20.391247+00:00
---

# Method: domains.extendSchema  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/extendSchema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Method: domains.extendSchema Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * Try it!



**Full name** : projects.locations.global.domains.extendSchema

Extend Schema for Domain

### HTTP request

`POST https://managedidentities.googleapis.com/v1beta1/{domain=projects/*/locations/global/domains/*}:extendSchema`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`domain` |  `string` Required. The domain resource name using the form: `projects/{projectId}/locations/global/domains/{domainName}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `domain`:

  * `managedidentities.domains.extendSchema`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "description": string,
    
      // Union field ldif_source can be only one of the following:
      "gcsPath": string,
      "fileContents": string
      // End of list of possible types for union field ldif_source.
    }  
  
Fields  
---  
`description` |  `string` Required. Description for Schema Change.  
Union field `ldif_source`. Required The LDIF file input for Schema Extension can be derived from any one of the given sources. `ldif_source` can be only one of the following:  
`gcsPath` |  `string` File stored in Cloud Storage bucket and represented in the form projects/{projectId}/buckets/{bucket_name}/objects/{object_name} File should be in the same project as the domain.  
`fileContents` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` File uploaded as a byte stream input.A base64-encoded string.  
  
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
