---
url: https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/ReportGenerationProgress/
title: ReportGenerationProgress \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:12.672298+00:00
---

# ReportGenerationProgress  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/ReportGenerationProgress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest)



Send feedback 

#  ReportGenerationProgress Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Details about the current status of the report-generation process.

JSON representation  
---  
      
    
    {
      "state": enum ([OperationState](https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/OperationState)),
      "failureReason": string,
      "evaluationPercentComplete": number,
      "reportGenerationPercentComplete": number,
      "reportUploadingPercentComplete": number,
      "destinationGcsBucket": string,
      "auditReport": string
    }  
  
Fields  
---  
`state` |  `enum (`[OperationState](https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/OperationState)`)` Output only. Current state of execution for report generation.  
`failureReason` |  `string` Output only. Reason for failure during the audit report generation process. This field is set only if the `OperationState` attribute is `OPERATION_STATE_FAILED`.  
`evaluationPercentComplete` |  `number` Progress of the evaluation process. The progress is defined in terms of percentage complete.  
`reportGenerationPercentComplete` |  `number` Report generation progress, defined in terms of percentage complete. Until evaluation is complete, this value is always `0`.  
`reportUploadingPercentComplete` |  `number` Report uploading progress, defined in terms of percentage complete. Until evaluation and report generation are complete, this value is always `0`.  
`destinationGcsBucket` |  `string` Output only. Cloud Storage bucket where the audit report is uploaded to after the evaluation process is completed.  
`auditReport` |  `string` Output only. Name of the audit report.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
