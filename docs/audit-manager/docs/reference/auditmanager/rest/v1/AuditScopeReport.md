---
url: https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/AuditScopeReport/
title: AuditScopeReport \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:33.044647+00:00
---

# AuditScopeReport  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/AuditScopeReport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest)



Send feedback 

#  AuditScopeReport Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Audit scope report.

JSON representation  
---  
      
    
    {
      "name": string,
    
      // Union field audit_report can be only one of the following:
      "scopeReportContents": string
      // End of list of possible types for union field audit_report.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name for the audit scope report, in one of the following formats:

  * `projects/{project}/locations/{location}/auditScopeReports/{audit_scope_report}`
  * `folders/{folder}/locations/{location}/auditScopeReports/{audit_scope_report}`
  * `organizations/{organization}/locations/{location}/auditScopeReports/{audit_scope_report}`

  
Union field `audit_report`. Specific format or delivery method for the exported audit scope report. `audit_report` can be only one of the following:  
`scopeReportContents` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Audit scope report content in byte format.A base64-encoded string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
