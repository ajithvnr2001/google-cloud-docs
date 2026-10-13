---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies
title: REST Resource: projects.locations.spaces.applicationTemplates.policies \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:10.545692+00:00
---

# REST Resource: projects.locations.spaces.applicationTemplates.policies  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.applicationTemplates.policies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Policy
    * JSON representation
  * PolicyType
  * Methods



## Resource: Policy

A Policy is a resource within an Application Template that refers to a Policy that you author outside of Application Design Center and attach to an application template.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "policyType": enum ([PolicyType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies#PolicyType)),
      "applyConditions": [
        {
          object ([ApplyCondition](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate#ApplyCondition))
        }
      ],
      "createTime": string,
      "updateTime": string,
    
      // Union field uri can be only one of the following:
      "policyUri": string,
      "policyRevisionUri": string
      // End of list of possible types for union field uri.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The policy name in the following format: `projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate/policies/$policy`  
`displayName` |  `string` Optional. The policy display name.  
`description` |  `string` Optional. The policy description.  
`policyType` |  `enum (`[PolicyType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies#PolicyType)`)` Required. The policy type. Policy type is used to determine the domain of the policy.  
`applyConditions[]` |  `object (`[ApplyCondition](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate#ApplyCondition)`)` Optional. Conditions for applying the policy. Condition accepts the `criticality` and `environment` parameters from the application template.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The policy creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The policy update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `uri`. URI of the policy or the policy revision. `uri` can be only one of the following:  
`policyUri` |  `string` Optional. URI of the policy.  
`policyRevisionUri` |  `string` Optional. URI of the policy revision.  
  
## PolicyType

The policy type.

Enums  
---  
`POLICY_TYPE_UNSPECIFIED` | Default.  
`COMPLIANCE_FRAMEWORK` | Compliance framework policy.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/create)`

|  Creates a policy for an application template.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/delete)`

|  Deletes a policy.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/get)`

|  Policy related APIs.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/list)`

|  Lists policies for an application template.  
  
### `[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/patch)`

|  Updates a policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
