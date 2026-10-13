---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/PartnerPermissions/
title: PartnerPermissions \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:33.939113+00:00
---

# PartnerPermissions  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/PartnerPermissions/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  PartnerPermissions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Permissions granted to the AW Partner SA account for the customer workload

JSON representation  
---  
      
    
    {
      "dataLogsViewer": boolean,
      "serviceAccessApprover": boolean,
      "assuredWorkloadsMonitoring": boolean,
      "accessTransparencyLogsSupportCaseViewer": boolean
    }  
  
Fields  
---  
`dataLogsViewer` |  `boolean` Optional. Allow the partner to view inspectability logs and monitoring violations.  
`serviceAccessApprover` |  `boolean` Optional. Allow partner to view access approval logs.  
`assuredWorkloadsMonitoring` |  `boolean` Optional. Allow partner to view violation alerts.  
`accessTransparencyLogsSupportCaseViewer` |  `boolean` Optional. Allow partner to view support case details for an AXT log  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
