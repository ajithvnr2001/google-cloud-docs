---
url: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.frameworkAudits/create/
title: Method: folders.locations.frameworkAudits.create \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:53.680560+00:00
---

# Method: folders.locations.frameworkAudits.create  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.frameworkAudits/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: folders.locations.frameworkAudits.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Creates a framework audit.

### HTTP request

`POST https://cloudsecuritycompliance.googleapis.com/v1/{parent=folders/*/locations/*}/frameworkAudits`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this framework audit is created.Supported formats are the following:

  * `organizations/{organization_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `projects/{projectId}/locations/{location}`

  
  
### Query parameters

Parameters  
---  
`frameworkAuditId` |  `string` Optional. The ID to use for the framework audit. The ID becomes the final component of the framework audit's full resource name.The ID must be between 4 and 63 characters and can contain lowercase letters, numbers, and hyphens.  
  
### Request body

The request body contains an instance of `[FrameworkAudit](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.frameworkAudits#FrameworkAudit)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.operationDetails#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `cloudsecuritycompliance.frameworkAudits.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-07 UTC."],[],[]] 
