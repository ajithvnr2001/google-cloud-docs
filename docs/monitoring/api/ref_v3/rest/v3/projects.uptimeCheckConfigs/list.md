---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list/
title: Method: projects.uptimeCheckConfigs.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:16.119128+00:00
---

# Method: projects.uptimeCheckConfigs.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.uptimeCheckConfigs.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the existing valid Uptime check configurations for the project (leaving out any invalid configurations).

### HTTP request

`GET https://monitoring.googleapis.com/v3/{parent}/uptimeCheckConfigs`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose Uptime check configurations are listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `monitoring.uptimeCheckConfigs.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` If provided, this field specifies the criteria that must be met by uptime checks to be included in the response.For more details, see [Filtering syntax](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering#filter_syntax).  
`pageSize` |  `integer` The maximum number of results to return in a single response. The server may further constrain the maximum number of results returned in a single page. If the pageSize is <=0, the server will decide the number of results to be returned.  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return more results from the previous method call.  
  
### Request body

The request body must be empty.

### Response body

The protocol for the `uptimeCheckConfigs.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "uptimeCheckConfigs": [
        {
          object ([UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`uptimeCheckConfigs[]` |  `object (`[UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig)`)` The returned Uptime check configurations.  
`nextPageToken` |  `string` This field represents the pagination token to retrieve the next page of results. If the value is empty, it means no further results for the request. To retrieve the next page of results, the value of the nextPageToken is passed to the subsequent List method call (in the request message's pageToken field).  
`totalSize` |  `integer` The total number of Uptime check configurations for the project, irrespective of any pagination.  
  
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
