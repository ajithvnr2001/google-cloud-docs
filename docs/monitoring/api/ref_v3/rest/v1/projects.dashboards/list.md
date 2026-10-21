---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/list/
title: Method: projects.dashboards.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:02:40.621422+00:00
---

# Method: projects.dashboards.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.dashboards.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the existing dashboards.

This method requires the `monitoring.dashboards.list` permission on the specified project. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

### HTTP request

`GET https://monitoring.googleapis.com/v1/{parent}/dashboards`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The scope of the dashboards to list. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `monitoring.dashboards.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` A positive number that is the maximum number of results to return. If unspecified, a default of 1000 is used.  
`pageToken` |  `string` Optional. If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
### Request body

The request body must be empty.

### Response body

The `dashboards.list` request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dashboards": [
        {
          object ([Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dashboard))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dashboards[]` |  `object (`[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dashboard)`)` The list of requested dashboards.  
`nextPageToken` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `pageToken` in the next call to this method.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
