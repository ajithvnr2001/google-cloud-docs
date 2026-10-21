---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/patch/
title: Method: projects.dashboards.patch \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:44.033001+00:00
---

# Method: projects.dashboards.patch  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.dashboards.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Replaces an existing custom dashboard with a new definition.

This method requires the `monitoring.dashboards.update` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

### HTTP request

`PATCH https://monitoring.googleapis.com/v1/{dashboard.name}`

### Path parameters

Parameters  
---  
`dashboard.name` |  `string` Identifier. The resource name of the dashboard.  
  
### Query parameters

Parameters  
---  
`validateOnly` |  `boolean` If set, validate the request and preview the review, but do not actually save it.  
  
### Request body

The request body contains an instance of `[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dashboard)`.

### Response body

If successful, the response body contains an instance of `[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dashboard)`.

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
