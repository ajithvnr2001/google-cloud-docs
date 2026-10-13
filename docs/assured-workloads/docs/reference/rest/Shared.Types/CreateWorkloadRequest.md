---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/CreateWorkloadRequest/
title: CreateWorkloadRequest \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:31.381486+00:00
---

# CreateWorkloadRequest  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/CreateWorkloadRequest/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  CreateWorkloadRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Request for creating a workload.

JSON representation  
---  
      
    
    {
      "parent": string,
      "workload": {
        object ([Workload](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/Workload))
      },
      "externalId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{locationId}`.  
`workload` |  `object (`[Workload](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/Workload)`)` Required. Assured Workload to create  
`externalId` |  `string` Optional. A identifier associated with the workload and underlying projects which allows for the break down of billing costs for a workload. The value provided for the identifier will add a label to the workload and contained projects with the identifier as the value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
