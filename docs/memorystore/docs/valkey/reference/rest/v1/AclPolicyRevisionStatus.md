---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/AclPolicyRevisionStatus/
title: AclPolicyRevisionStatus \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:32.108916+00:00
---

# AclPolicyRevisionStatus  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/AclPolicyRevisionStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  AclPolicyRevisionStatus Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * State



AclPolicyRevisionStatus stores the per-revision status for an attached instance.

JSON representation  
---  
      
    
    {
      "aclPolicyRevision": string,
      "aclPolicyRevisionNumber": string,
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/AclPolicyRevisionStatus#State)),
      "errorMessage": string
    }  
  
Fields  
---  
`aclPolicyRevision` |  `string` Output only. The resource name of the ACL policy revision this status refers to. Format: "projects/{project}/locations/{location}/aclPolicies/{aclPolicy}/revisions/{revision}"  
`aclPolicyRevisionNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The revision number of the ACL policy revision this status refers to.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/AclPolicyRevisionStatus#State)`)` Output only. AclPolicyRevision state.  
`errorMessage` |  `string` Output only. Human-readable error message providing more details for FAILED states.  
  
## State

Enum indicating the status of this ACL policy revision on the instance.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`APPLYING` | The instance is attempting to apply this revision.  
`APPLIED` | The instance has successfully applied this revision.  
`FAILED` | The instance failed to apply this revision.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
