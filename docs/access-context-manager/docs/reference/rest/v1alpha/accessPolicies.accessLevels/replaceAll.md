---
url: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/replaceAll/
title: Method: accessPolicies.accessLevels.replaceAll \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:30.253834+00:00
---

# Method: accessPolicies.accessLevels.replaceAll  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/replaceAll/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Method: accessPolicies.accessLevels.replaceAll Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Replaces all existing `[access levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` in an `[access policy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies#AccessPolicy)` with the `[access levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` provided. This is done atomically. The long-running operation from this RPC has a successful status after all replacements propagate to long-lasting storage. If the replacement contains errors, an error response is returned for the first error encountered. Upon error, the replacement is cancelled, and existing `[access levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` are not affected. The Operation.response field contains ReplaceAccessLevelsResponse. Removing `[access levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` contained in existing `[service perimeters](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#ServicePerimeter)` result in an error.

### HTTP request

`POST https://accesscontextmanager.googleapis.com/v1alpha/{parent=accessPolicies/*}/accessLevels:replaceAll`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name for the access policy which owns these `[Access Levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)`.Format: `accessPolicies/{policyId}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "accessLevels": [
        {
          object ([AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel))
        }
      ],
      "etag": string
    }  
  
Fields  
---  
`accessLevels[]` |  `object (`[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)`)` Required. The desired `[Access Levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` that should replace all existing `[Access Levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` in the `[Access Policy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies#AccessPolicy)`.  
`etag` |  `string` Optional. The etag for the version of the `[Access Policy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies#AccessPolicy)` that this replace operation is to be performed on. If, at the time of replace, the etag for the Access Policy stored in Access Context Manager is different from the specified etag, then the replace operation will not be performed and the call will fail. This field is not required. If etag is not provided, the operation will be performed as if a valid etag is provided.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
