---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/list/
title: Method: projects.alerts.list \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:37.883245+00:00
---

# Method: projects.alerts.list  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  Method: projects.alerts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Get a list of alerts that meet the filter criteria.

### HTTP request

`GET https://threatintelligence.googleapis.com/v1beta/{parent=projects/*}/alerts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent of the alerts. Format: projects/{project}  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. Filter criteria.Supported fields for filtering include:

  * `audit.create_time`
  * `audit.creator`
  * `audit.update_time`
  * `audit.updater`
  * `detail.data_leak.discovery_document_ids`
  * `detail.data_leak.severity`
  * `detail.detail_type`
  * `detail.initial_access_broker.discovery_document_ids`
  * `detail.initial_access_broker.severity`
  * `detail.insider_threat.discovery_document_ids`
  * `detail.insider_threat.severity`
  * `findingCount`
  * `priorityAnalysis.priority_level`
  * `relevanceAnalysis.confidence`
  * `relevanceAnalysis.relevance_level`
  * `relevanceAnalysis.relevant`
  * `severityAnalysis.severity_level`
  * `state`

Examples:

  * `detail.detail_type = "initial_access_broker"`
  * `detail.detail_type != "data_leak"`
  * `detail.insider_threat.severity = "HIGH"`
  * `audit.create_time >= "2026-04-03T00:00:00Z" AND audit.create_time < "2026-04-06T00:00:00Z"`
  * `state = "NEW" OR state = "TRIAGED"`
  * `severityAnalysis.severity_level = "SEVERITY_LEVEL_CRITICAL"`

  
`orderBy` |  `string` Optional. Order by criteria in the csv format: "field1, field2 desc" or "field1, field2" or "field1 asc, field2". If a field is specified without `asc` or `desc`, ascending order is used by default. Supported fields for ordering are identical to those supported for filtering.Examples:

  * `audit.create_time desc`
  * `audit.update_time asc`
  * `audit.create_time desc, severityAnalysis.severity_level desc`

  
`pageToken` |  `string` Optional. Page token to retrieve the next page of results.  
`pageSize` |  `integer` Optional. Page size. Default to 100 alerts per page. Maximum is 1000 alerts per page.  
  
### Request body

The request body must be empty.

### Response body

Response message for alerts.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "alerts": [
        {
          object ([Alert](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#Alert))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`alerts[]` |  `object (`[Alert](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#Alert)`)` List of alerts.  
`nextPageToken` |  `string` Page token.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `threatintelligence.alerts.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
