---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/generateReport/
title: Method: cases.generateReport \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:00.932967+00:00
---

# Method: cases.generateReport  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/generateReport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: cases.generateReport Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * ReportType



**Full name** : projects.locations.instances.cases.generateReport

Generates a report for a Case in a specified format (e.g., PDF, HTML). Use this method to create a shareable summary of the case.

### HTTP request

`POST https://{endpoint}/v1/{name}:generateReport`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Case to generate Report for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "caseId": integer,
      "reportKind": enum ([ReportType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/generateReport#ReportType))
    }  
  
Fields  
---  
`caseId` |  `integer` Required. Case id to generate report for.  
`reportKind` |  `enum (`[ReportType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/generateReport#ReportType)`)` Required. Report kind.  
  
### Response body

Response message for cases.generateReport.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fileContents": string,
      "contentType": string
    }  
  
Fields  
---  
`fileContents` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The content of the report.A base64-encoded string.  
`contentType` |  `string` Output only. The content type of the report.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.cases.generateReport`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ReportType

Report type.

Enums  
---  
`REPORT_TYPE_UNSPECIFIED` | Unspecified report type.  
`PDF` | PDF report type.  
`RTF` | RTF report type.  
`DOC` | DOC report type.  
`DOCX` | DOCX report type.  
`HTML` | HTML report type.  
`XLSX` | XLSX report type.  
`CSV` | CSV report type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
