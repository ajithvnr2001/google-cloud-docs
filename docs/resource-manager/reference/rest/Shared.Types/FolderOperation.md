---
url: https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/FolderOperation/
title: FolderOperation \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:19:27.151576+00:00
---

# FolderOperation  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/FolderOperation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)



Send feedback 

#  FolderOperation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata describing a long running folder operation

JSON representation  
---  
      
    
    {
      "displayName": string,
      "operationType": enum ([OperationType](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/OperationType)),
      "sourceParent": string,
      "destinationParent": string
    }  
  
Fields  
---  
`displayName` |  `string` The display name of the folder.  
`operationType` |  `enum (`[OperationType](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/OperationType)`)` The type of this operation.  
`sourceParent` |  `string` The resource name of the folder's parent. Only applicable when the operationType is MOVE.  
`destinationParent` |  `string` The resource name of the folder or organization we are either creating the folder under or moving the folder to.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
