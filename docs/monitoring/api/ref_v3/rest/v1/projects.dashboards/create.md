---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create/
title: Method: projects.dashboards.create \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:36:23.780684+00:00
---

# Method: projects.dashboards.create  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.dashboards.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see [Managing dashboards by API](https://cloud.google.com/monitoring/dashboards/api-dashboard). This method requires the `monitoring.dashboards.create` permission on the specified project. For more information about permissions, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

### HTTP request

`POST https://monitoring.googleapis.com/v1/{parent}/dashboards`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

The `[PROJECT_ID_OR_NUMBER]` must match the dashboard resource name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `monitoring.dashboards.create`

  
  
### Query parameters

Parameters  
---  
`validateOnly` |  `boolean` If set, validate the request and preview the review, but do not actually save it.  
  
### Request body

The request body contains an instance of `[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dashboard)`.

### Response body

If successful, the response body contains a newly created instance of `[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dashboard)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
