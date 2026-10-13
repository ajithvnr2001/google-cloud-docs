---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/CreateWorkloadOperationMetadata/
title: CreateWorkloadOperationMetadata \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:31.185344+00:00
---

# CreateWorkloadOperationMetadata  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/CreateWorkloadOperationMetadata/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  CreateWorkloadOperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Operation metadata to give request details of CreateWorkload.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "displayName": string,
      "parent": string,
      "complianceRegime": enum ([ComplianceRegime](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime))
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Time when the operation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Optional. The display name of the workload.  
`parent` |  `string` Optional. The parent of the workload.  
`complianceRegime` |  `enum (`[ComplianceRegime](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime)`)` Optional. Compliance controls that should be applied to the resources managed by the workload.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-27 UTC."],[],[]] 
