---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts/list/
title: Method: projects.alerts.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:11.786405+00:00
---

# Method: projects.alerts.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.alerts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the existing alerts for the metrics scope of the project.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{parent}/alerts`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the project to list alerts for.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. An alert is returned if there is a match on any fields belonging to the alert or its subfields.  
`orderBy` |  `string` Optional. A comma-separated list of fields in `Alert` to use for sorting. The default sort direction is ascending. To specify descending order for a field, add a `desc` modifier. The following fields are supported:

  * `openTime`
  * `closeTime`

For example, `closeTime desc, openTime` will return the alerts closed most recently, with ties broken in the order of older alerts listed first.If the field is not set, the results are sorted by `openTime desc`.  
`pageSize` |  `integer` Optional. The maximum number of results to return in a single response. If not set to a positive number, at most 50 alerts will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. If non-empty, `pageToken` must contain a value returned as the `nextPageToken` in a previous response to request the next set of results.  
  
### Request body

The request body must be empty.

### Response body

The `alerts.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "alerts": [
        {
          object ([Alert](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Alert))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`alerts[]` |  `object (`[Alert](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Alert)`)` The list of alerts.  
`nextPageToken` |  `string` If not empty, indicates that there may be more results that match the request. Use the value in the `pageToken` field in a subsequent request to fetch the next set of results. The token is encrypted and only guaranteed to return correct results for 72 hours after it is created. If empty, all results have been returned.  
`totalSize` |  `integer` The estimated total number of matching results for this query.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
