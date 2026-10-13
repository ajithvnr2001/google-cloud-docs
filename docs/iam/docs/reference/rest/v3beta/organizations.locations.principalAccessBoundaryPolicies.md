---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies
title: REST Resource: organizations.locations.principalAccessBoundaryPolicies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:36.788067+00:00
---

# REST Resource: organizations.locations.principalAccessBoundaryPolicies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.principalAccessBoundaryPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PrincipalAccessBoundaryPolicy
    * JSON representation
  * PrincipalAccessBoundaryPolicyDetails
    * JSON representation
  * PrincipalAccessBoundaryPolicyRule
    * JSON representation
  * Effect
  * Methods



## Resource: PrincipalAccessBoundaryPolicy

An IAM principal access boundary policy resource.

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
        object ([PrincipalAccessBoundaryPolicyDetails](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies#PrincipalAccessBoundaryPolicyDetails))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the principal access boundary policy.The following format is supported: `organizations/{organizationId}/locations/{location}/principalAccessBoundaryPolicies/{policyId}`  
`uid` |  `string` Output only. The globally unique ID of the principal access boundary policy.  
`etag` |  `string` Optional. The etag for the principal access boundary. If this is provided on update, it must match the server's etag.  
`displayName` |  `string` Optional. The description of the principal access boundary policy. Must be less than or equal to 63 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User defined annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitationsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the principal access boundary policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the principal access boundary policy was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`details` |  `object (`[PrincipalAccessBoundaryPolicyDetails](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies#PrincipalAccessBoundaryPolicyDetails)`)` Optional. The details for the principal access boundary policy.  
  
## PrincipalAccessBoundaryPolicyDetails

Principal access boundary policy details

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([PrincipalAccessBoundaryPolicyRule](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies#PrincipalAccessBoundaryPolicyRule))
        }
      ],
      "enforcementVersion": string
    }  
  
Fields  
---  
`rules[]` |  `object (`[PrincipalAccessBoundaryPolicyRule](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies#PrincipalAccessBoundaryPolicyRule)`)` Required. A list of principal access boundary policy rules. The number of rules in a policy is limited to 500.  
`enforcementVersion` |  `string` Optional. The version number (for example, `1` or `latest`) that indicates which permissions are able to be blocked by the policy. If empty, the PAB policy version will be set to the most recent version number at the time of the policy's creation.  
  
## PrincipalAccessBoundaryPolicyRule

Principal access boundary policy rule that defines the resource boundary.

JSON representation  
---  
      
    
    {
      "description": string,
      "resources": [
        string
      ],
      "effect": enum ([Effect](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies#Effect))
    }  
  
Fields  
---  
`description` |  `string` Optional. The description of the principal access boundary policy rule. Must be less than or equal to 256 characters.  
`resources[]` |  `string` Required. A list of Resource Manager resources. If a resource is listed in the rule, then the rule applies for that resource and its descendants. The number of resources in a policy is limited to 500 across all rules in the policy.The following resource types are supported:

  * Organizations, such as `//cloudresourcemanager.googleapis.com/organizations/123`.
  * Folders, such as `//cloudresourcemanager.googleapis.com/folders/123`.
  * Projects, such as `//cloudresourcemanager.googleapis.com/projects/123` or `//cloudresourcemanager.googleapis.com/projects/my-project-id`.

  
`effect` |  `enum (`[Effect](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies#Effect)`)` Required. The access relationship of principals to the resources in this rule.  
  
## Effect

An effect to describe the access relationship.

Enums  
---  
`EFFECT_UNSPECIFIED` | Effect unspecified.  
`ALLOW` | Allows access to the resources in this rule.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/create)`

|  Creates a principal access boundary policy, and returns a long running operation.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/delete)`

|  Deletes a principal access boundary policy.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/get)`

|  Gets a principal access boundary policy.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/list)`

|  Lists principal access boundary policies.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/patch)`

|  Updates a principal access boundary policy.  
  
### `[searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/searchPolicyBindings)`

|  Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-28 UTC."],[],[]] 
