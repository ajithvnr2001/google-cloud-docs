---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/setIamPolicy/
title: Method: peerings.setIamPolicy \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:24.541587+00:00
---

# Method: peerings.setIamPolicy  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/setIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Method: peerings.setIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * Try it!



**Full name** : projects.locations.global.peerings.setIamPolicy

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

### HTTP request

`POST https://managedidentities.googleapis.com/v1beta1/{resource=projects/*/locations/global/peerings/*}:setIamPolicy`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "policy": {
        object ([Policy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/Shared.Types/Policy))
      }
    }  
  
Fields  
---  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/Shared.Types/Policy)`)` REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Google Cloud services (such as Projects) might reject them.  
  
### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/Shared.Types/Policy)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
