---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/update/
title: Method: projects.groups.update \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:12.437216+00:00
---

# Method: projects.groups.update  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.groups.update Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates an existing group. You can change any group attributes except `name`.

### HTTP request

`PUT https://monitoring.googleapis.com/v3/{group.name}`

### Path parameters

Parameters  
---  
`group.name` |  `string` Output only. The name of this group. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

When creating a group, this field is ignored and a new name is created consisting of the project specified in the call to `groups.create` and a unique `[GROUP_ID]` that is generated automatically.  
  
### Query parameters

Parameters  
---  
`validateOnly` |  `boolean` If true, validate this request but do not update the existing group.  
  
### Request body

The request body contains an instance of `[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group)`.

### Response body

If successful, the response body contains an instance of `[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
