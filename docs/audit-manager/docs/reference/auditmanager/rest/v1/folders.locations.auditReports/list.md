---
url: https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/folders.locations.auditReports/list/
title: Method: folders.locations.auditReports.list \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:59.181646+00:00
---

# Method: folders.locations.auditReports.list  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/folders.locations.auditReports/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest)



Send feedback 

#  Method: folders.locations.auditReports.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Lists the audit reports for the organization, folder, or project that you specify as the parent scope.

### HTTP request

`GET https://auditmanager.googleapis.com/v1/{parent=folders/*/locations/*}/auditReports`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent organization, folder, or project to list reports for, in one of the following formats:

  * `projects/{project}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of items to return in a single page. The service might return fewer items than this value. If unspecified, the service picks an appropriate default. The maximum value is 100; values above 100 are reduced to 100.  
`pageToken` |  `string` Optional. A page token, received from a previous call, to retrieve the next page of results.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListAuditReportsResponse](https://docs.cloud.google.com/audit-manager/docs/reference/auditmanager/rest/v1/ListAuditReportsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `auditmanager.auditReports.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
