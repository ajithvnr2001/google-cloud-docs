---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations
title: REST Resource: projects.locations.global.domains.sqlIntegrations \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:43:07.588666+00:00
---

# REST Resource: projects.locations.global.domains.sqlIntegrations  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  REST Resource: projects.locations.global.domains.sqlIntegrations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SqlIntegration
    * JSON representation
  * State
  * Methods



## Resource: SqlIntegration

Represents the SQL instance integrated with Managed AD.

JSON representation  
---  
      
    
    {
      "name": string,
      "sqlInstance": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations#State))
    }  
  
Fields  
---  
`name` |  `string` The unique name of the SQL integration in the form of `projects/{projectId}/locations/global/domains/{domainName}/sqlIntegrations/{sqlIntegration}`  
`sqlInstance` |  `string` The full resource name of an integrated SQL instance  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time the SQL integration was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time the SQL integration was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations#State)`)` Output only. The current state of the SQL integration.  
  
## State

Represents the different states of a SQL integration.

Enums  
---  
`STATE_UNSPECIFIED` | Not Set  
`CREATING` | The SQL integration is being created.  
`DELETING` | The SQL integration is being deleted.  
`READY` | The SQL integration is ready.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations/get)`

|  Gets details of a single sqlIntegration.  
  
### `[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations/list)`

|  Lists SqlIntegrations in a given domain.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
