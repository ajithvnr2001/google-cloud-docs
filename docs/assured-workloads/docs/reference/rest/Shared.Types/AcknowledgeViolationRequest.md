---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/AcknowledgeViolationRequest/
title: AcknowledgeViolationRequest \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:30.885699+00:00
---

# AcknowledgeViolationRequest  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/AcknowledgeViolationRequest/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  AcknowledgeViolationRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Request for acknowledging the violation Next Id: 4

JSON representation  
---  
      
    
    {
      "name": string,
      "comment": string,
      "nonCompliantOrgPolicy": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the Violation to acknowledge. Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
`comment` |  `string` Required. Business justification explaining the need for violation acknowledgement  
`nonCompliantOrgPolicy  
**(deprecated)**` |  `string` This item is deprecated!Optional. This field is deprecated and will be removed in future version of the API. Name of the OrgPolicy which was modified with non-compliant change and resulted in this violation. Format: projects/{project_number}/policies/{constraintName} folders/{folderId}/policies/{constraintName} organizations/{organization_id}/policies/{constraintName}  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-27 UTC."],[],[]] 
