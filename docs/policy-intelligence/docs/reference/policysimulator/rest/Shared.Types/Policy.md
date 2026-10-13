---
url: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/Policy/
title: Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:29.118860+00:00
---

# Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/Policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/policy-intelligence/docs/apis)



Send feedback 

#  Policy Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Defines an organization policy which is used to specify constraints for configurations of Google Cloud resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "spec": {
        object ([PolicySpec](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/PolicySpec))
      },
      "alternate": {
        object ([AlternatePolicySpec](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/AlternatePolicySpec))
      },
      "dryRunSpec": {
        object ([PolicySpec](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/PolicySpec))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint which this policy configures:

  * `projects/{projectNumber}/policies/{constraint_name}`
  * `folders/{folderId}/policies/{constraint_name}`
  * `organizations/{organizationId}/policies/{constraint_name}`

For example, `projects/123/policies/compute.disableSerialPortAccess`.Note: `projects/{projectId}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number.  
`spec` |  `object (`[PolicySpec](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/PolicySpec)`)` Basic information about the organization policy.  
`alternate  
**(deprecated)**` |  `object (`[AlternatePolicySpec](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/AlternatePolicySpec)`)` This item is deprecated!Deprecated.  
`dryRunSpec` |  `object (`[PolicySpec](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/Shared.Types/PolicySpec)`)` Dry-run policy. Audit-only policy, can be used to monitor how the policy would have impacted the existing and future resources if it's enforced.  
`etag` |  `string` Optional. An opaque tag indicating the current state of the policy, used for concurrency control. This 'etag' is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-16 UTC."],[],[]] 
