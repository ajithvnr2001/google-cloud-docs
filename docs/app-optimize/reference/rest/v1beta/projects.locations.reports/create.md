---
url: https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/create/
title: Method: projects.locations.reports.create \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:14.357722+00:00
---

# Method: projects.locations.reports.create  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  Method: projects.locations.reports.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `reports.read`.

### HTTP request

`POST https://appoptimize.googleapis.com/v1beta/{parent=projects/*/locations/*}/reports`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent Google Cloud project that will own the report.This value does not define the scope of the report data. See `Report.scope` for setting the data scope.Format: `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`reportId` |  `string` Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
  
### Request body

The request body contains an instance of `[Report](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports#Report)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/appoptimize`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `appoptimize.reports.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
