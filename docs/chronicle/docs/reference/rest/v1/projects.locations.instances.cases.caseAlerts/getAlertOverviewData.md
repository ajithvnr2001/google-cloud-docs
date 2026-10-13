---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/getAlertOverviewData/
title: Method: caseAlerts.getAlertOverviewData \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:09.963884+00:00
---

# Method: caseAlerts.getAlertOverviewData  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/getAlertOverviewData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: caseAlerts.getAlertOverviewData Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.caseAlerts.getAlertOverviewData

Retrieves a view of widgets for a specific alert. Use this method to get a high-level summary of the alert, potentially tailored to a specific playbook view.

### HTTP request

`GET https://{endpoint}/v1/{name}:alertOverviewData`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The alert to get overview for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts/{caseAlert}:getOverview  
  
### Query parameters

Parameters  
---  
`viewId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The view ID to get overview data for. If not provided, this will return the overview data according to the following criteria: 1. If one or more playbooks have been attached to the alert, the view for the most recent run of the first-attached playbook will be used. 2. If no playbook has been attached to the alert, default alert view will be used.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[OverviewData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/OverviewData)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.caseAlerts.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
