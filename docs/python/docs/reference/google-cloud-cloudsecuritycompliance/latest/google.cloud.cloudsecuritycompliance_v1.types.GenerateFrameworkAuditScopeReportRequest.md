---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.GenerateFrameworkAuditScopeReportRequest
title: Class GenerateFrameworkAuditScopeReportRequest (0.8.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:07.135501+00:00
---

# Class GenerateFrameworkAuditScopeReportRequest (0.8.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.GenerateFrameworkAuditScopeReportRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenerateFrameworkAuditScopeReportRequest (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    GenerateFrameworkAuditScopeReportRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The request message for [GenerateFrameworkAuditScopeReport][].

## Attributes  
  
---  
**Name** | **Description**  
`scope` |  `str`   
Required. The organization, folder or project for the audit report. Supported formats are the following: \- `projects/{project_id}/locations/{location}` \- `folders/{folder_id}/locations/{location}` \- `organizations/{organization_id}/locations/{location}`  
`report_format` |  `[google.cloud.cloudsecuritycompliance_v1.types.GenerateFrameworkAuditScopeReportRequest.Format](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.GenerateFrameworkAuditScopeReportRequest.Format)`   
Required. The format that the scope report bytes is returned in.   
`compliance_framework` |  `str`   
Required. The compliance framework that the scope report is generated for.   
  
## Classes 

### Format
    
    
    Format(value)

The set of options for the audit scope report format.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
