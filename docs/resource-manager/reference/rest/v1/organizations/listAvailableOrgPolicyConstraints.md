---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/listAvailableOrgPolicyConstraints/
title: Method: organizations.listAvailableOrgPolicyConstraints \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:19.801978+00:00
---

# Method: organizations.listAvailableOrgPolicyConstraints  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/listAvailableOrgPolicyConstraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: organizations.listAvailableOrgPolicyConstraints Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Lists `Constraints` that could be applied on the specified resource.

### HTTP request

`POST https://cloudresourcemanager.googleapis.com/v1/{resource=organizations/*}:listAvailableOrgPolicyConstraints`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` Name of the resource to list `Constraints` for. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `resource`:

  * `orgpolicy.policy.get`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`pageSize` |  `integer` Size of the pages to be returned. This is currently unsupported and will be ignored. The server may at any point start using this field to limit page size.  
`pageToken` |  `string` Page token used to retrieve the next page. This is currently unsupported and will be ignored. The server may at any point start using this field.  
  
### Response body

If successful, the response body contains an instance of `[ListAvailableOrgPolicyConstraintsResponse](https://docs.cloud.google.com/resource-manager/reference/rest/v1/ListAvailableOrgPolicyConstraintsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/cloudplatformorganizations`
  * `https://www.googleapis.com/auth/cloudplatformorganizations.readonly`
  * `https://www.googleapis.com/auth/cloudplatformprojects`
  * `https://www.googleapis.com/auth/cloudplatformprojects.readonly`
  * `https://www.googleapis.com/auth/cloudplatformfolders`
  * `https://www.googleapis.com/auth/cloudplatformfolders.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
