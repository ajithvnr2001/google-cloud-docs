---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse/
title: ApplyWorkloadUpdateResponse \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:30.842465+00:00
---

# ApplyWorkloadUpdateResponse  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  ApplyWorkloadUpdateResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * WorkloadUpdate
    * JSON representation
  * UpdateDetails
    * JSON representation
  * OrgPolicyUpdate
    * JSON representation
  * OrgPolicy
    * JSON representation
  * PolicyRule
    * JSON representation
  * StringValues
    * JSON representation



Response for ApplyWorkloadUpdate endpoint.

JSON representation  
---  
      
    
    {
      "appliedUpdate": {
        object ([WorkloadUpdate](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#WorkloadUpdate))
      }
    }  
  
Fields  
---  
`appliedUpdate` |  `object (`[WorkloadUpdate](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#WorkloadUpdate)`)` The update that was applied.  
  
## WorkloadUpdate

A workload update is a change to the workload's compliance configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum (State),
      "createTime": string,
      "updateTime": string,
      "details": {
        object ([UpdateDetails](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#UpdateDetails))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Immutable. Identifier. Resource name of the WorkloadUpdate. Format: organizations/{organization}/locations/{location}/workloads/{workload}/updates/{update}  
`state` |  `enum (`State`)` Output only. The state of the update.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the update was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the update was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`details` |  `object (`[UpdateDetails](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#UpdateDetails)`)` The details of the update.  
  
## UpdateDetails

The details of the update.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "orgPolicyUpdate": {
        object ([OrgPolicyUpdate](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#OrgPolicyUpdate))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The type of the update. This can be an update to a org policy of a resource e.g. gcp.resourceLocation org policy. `kind` can be only one of the following:  
`orgPolicyUpdate` |  `object (`[OrgPolicyUpdate](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#OrgPolicyUpdate)`)` Update to one org policy, e.g. gcp.resourceLocation.  
  
## OrgPolicyUpdate

Represents an update for an org policy control applied on an Assured Workload resource. The inherited org policy is not considered.

JSON representation  
---  
      
    
    {
      "appliedPolicy": {
        object ([OrgPolicy](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#OrgPolicy))
      },
      "suggestedPolicy": {
        object ([OrgPolicy](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#OrgPolicy))
      }
    }  
  
Fields  
---  
`appliedPolicy` |  `object (`[OrgPolicy](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#OrgPolicy)`)` The org policy currently applied on the assured workload resource.  
`suggestedPolicy` |  `object (`[OrgPolicy](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#OrgPolicy)`)` The suggested org policy that replaces the applied policy.  
  
## OrgPolicy

This assured workload service object is used to represent the org policy attached to a resource. It servces the same purpose as the orgpolicy.v2.Policy object but with functionality that is limited to what is supported by Assured Workloads(e.g. only one rule under one OrgPolicy object, no conditions, etc).

JSON representation  
---  
      
    
    {
      "resource": string,
      "constraint": string,
      "rule": {
        object ([PolicyRule](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#PolicyRule))
      },
      "inherit": boolean,
      "reset": boolean
    }  
  
Fields  
---  
`resource` |  `string` Resource that the OrgPolicy attaches to. Format: folders/123" projects/123".  
`constraint` |  `string` The constraint name of the OrgPolicy. e.g. "constraints/gcp.resourceLocations".  
`rule` |  `object (`[PolicyRule](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#PolicyRule)`)` The rule of the OrgPolicy.  
`inherit` |  `boolean` If `inherit` is true, policy rules of the lowest ancestor in the resource hierarchy chain are inherited. If it is false, policy rules are not inherited.  
`reset` |  `boolean` Ignores policies set above this resource and restores to the `constraint_default` value. `reset` can only be true when `rules` is empty and `inherit` is false.  
  
## PolicyRule

A rule used to express this policy.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "values": {
        object ([StringValues](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#StringValues))
      },
      "allowAll": boolean,
      "denyAll": boolean,
      "enforce": boolean
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of the rule. `kind` can be only one of the following:  
`values` |  `object (`[StringValues](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ApplyWorkloadUpdateResponse#StringValues)`)` ListPolicy only when custom values are specified.  
`allowAll` |  `boolean` ListPolicy only when all values are allowed.  
`denyAll` |  `boolean` ListPolicy only when all values are denied.  
`enforce` |  `boolean` BooleanPolicy only.  
  
## StringValues

The values allowed for a ListPolicy.

JSON representation  
---  
      
    
    {
      "allowedValues": [
        string
      ],
      "deniedValues": [
        string
      ]
    }  
  
Fields  
---  
`allowedValues[]` |  `string` List of values allowed at this resource.  
`deniedValues[]` |  `string` List of values denied at this resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-27 UTC."],[],[]] 
