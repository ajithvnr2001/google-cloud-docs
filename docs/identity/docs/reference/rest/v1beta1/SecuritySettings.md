---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/SecuritySettings/
title: SecuritySettings \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:57.803206+00:00
---

# SecuritySettings  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/SecuritySettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  SecuritySettings Stay organized with collections  Save and categorize content based on your preferences. 

The definiion of security settings.

JSON representation  
---  
      
    
    {
      "name": string,
      "memberRestriction": {
        object ([MemberRestriction](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/SecuritySettings#MemberRestriction))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the security settings.Shall be of the form `groups/{groupId}/securitySettings`.  
`memberRestriction` |  `object (`[MemberRestriction](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/SecuritySettings#MemberRestriction)`)` The Member Restriction value  
  
## MemberRestriction

The definition of MemberRestriction

JSON representation  
---  
      
    
    {
      "query": string,
      "evaluation": {
        object ([RestrictionEvaluation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/SecuritySettings#RestrictionEvaluation))
      }
    }  
  
Fields  
---  
`query` |  `string` Member Restriction as defined by CEL expression. Supported restrictions are: `member.customer_id` and `member.type`.Valid values for `member.type` are `1`, `2` and `3`. They correspond to USER, SERVICE_ACCOUNT, and GROUP respectively.The value for `member.customer_id` only supports `groupCustomerId()` currently which means the customer id of the group will be used for restriction.Supported operators are `&&`, `||` and `==`, corresponding to AND, OR, and EQUAL.Examples: Allow only service accounts of given customer to be members.`member.type == 2 && member.customer_id == groupCustomerId()`Allow only users or groups to be members.`member.type == 1 || member.type == 3`  
`evaluation` |  `object (`[RestrictionEvaluation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/SecuritySettings#RestrictionEvaluation)`)` The evaluated state of this restriction on a group.  
  
## RestrictionEvaluation

The evaluated state of this restriction.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/SecuritySettings#State))
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/SecuritySettings#State)`)` Output only. The current state of the restriction  
  
## State

All possible states of a restriction.

Enums  
---  
`STATE_UNSPECIFIED` | Default. Should not be used.  
`EVALUATING` | The restriction state is currently being evaluated.  
`COMPLIANT` | All transitive memberships are adhering to restriction.  
`FORWARD_COMPLIANT` | Some transitive memberships violate the restriction. No new violating memberships can be added.  
`NON_COMPLIANT` | Some transitive memberships violate the restriction. New violating direct memberships will be denied while indirect memberships may be added.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-06 UTC."],[],[]] 
