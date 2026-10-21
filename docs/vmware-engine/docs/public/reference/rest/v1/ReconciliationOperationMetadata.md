---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/ReconciliationOperationMetadata/
title: ReconciliationOperationMetadata \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:24.496817+00:00
---

# ReconciliationOperationMetadata  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/ReconciliationOperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  ReconciliationOperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Operation metadata returned by the CLH during resource state reconciliation.

JSON representation  
---  
      
    
    {
      "deleteResource": boolean,
      "exclusiveAction": enum ([ExclusiveRepairActionFlag](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/ExclusiveRepairActionFlag))
    }  
  
Fields  
---  
`deleteResource  
**(deprecated)**` |  `boolean` This item is deprecated!DEPRECATED. Use exclusiveAction instead.  
`exclusiveAction` |  `enum (`[ExclusiveRepairActionFlag](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/ExclusiveRepairActionFlag)`)` Excluisive action returned by the CLH.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
