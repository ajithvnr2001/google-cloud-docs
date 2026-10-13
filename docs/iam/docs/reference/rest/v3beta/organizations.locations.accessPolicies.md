---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies
title: REST Resource: organizations.locations.accessPolicies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:31.232329+00:00
---

# REST Resource: organizations.locations.accessPolicies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.accessPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AccessPolicy
    * JSON representation
  * Methods



## Resource: AccessPolicy

An IAM access policy resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "etag": string,
      "displayName": string,
      "annotations": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "details": {
        object ([AccessPolicyDetails](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.AccessPolicyDetails))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the access policy.The following formats are supported:

  * `projects/{projectId}/locations/{location}/accessPolicies/{policyId}`
  * `projects/{projectNumber}/locations/{location}/accessPolicies/{policyId}`
  * `folders/{folderId}/locations/{location}/accessPolicies/{policyId}`
  * `organizations/{organizationId}/locations/{location}/accessPolicies/{policyId}`

  
`uid` |  `string` Output only. The globally unique ID of the access policy.  
`etag` |  `string` Optional. The etag for the access policy. If this is provided on update, it must match the server's etag.  
`displayName` |  `string` Optional. The description of the access policy. Must be less than or equal to 63 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User defined annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitationsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the access policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the access policy was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`details` |  `object (`[AccessPolicyDetails](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.AccessPolicyDetails)`)` Optional. The details for the access policy.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/create)`

|  Creates an access policy, and returns a long running operation.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/delete)`

|  Deletes an access policy.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/get)`

|  Gets an access policy.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/list)`

|  Lists access policies.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/patch)`

|  Updates an access policy.  
  
### `[searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/searchPolicyBindings)`

|  Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
