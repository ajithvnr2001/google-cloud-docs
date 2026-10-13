---
url: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/testIamPermissions/
title: Method: accessPolicies.testIamPermissions \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:39.251654+00:00
---

# Method: accessPolicies.testIamPermissions  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/testIamPermissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Method: accessPolicies.testIamPermissions Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Returns the IAM permissions that the caller has on the specified Access Context Manager resource. The resource can be an `[AccessPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)`, `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)`, or `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`. This method does not support other resources.

**IAM Permissions** :

No specific IAM permission is required to call this method. It returns the subset of the requested permissions that the caller possesses.

### HTTP request

`POST https://accesscontextmanager.googleapis.com/v1/{resource=accessPolicies/*}:testIamPermissions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "permissions": [
        string
      ]
    }  
  
Fields  
---  
`permissions[]` |  `string` The set of permissions to check for the `resource`. Permissions with wildcards (such as `*` or `storage.*`) are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
  
### Response body

If successful, the response body contains an instance of `[TestIamPermissionsResponse](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/TestIamPermissionsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-30 UTC."],[],[]] 
