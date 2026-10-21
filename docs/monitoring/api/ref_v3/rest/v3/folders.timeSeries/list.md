---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/folders.timeSeries/list/
title: Method: folders.timeSeries.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:11.324761+00:00
---

# Method: folders.timeSeries.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/folders.timeSeries/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: folders.timeSeries.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists time series that match a filter.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{name}/timeSeries`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name), organization or folder on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    organizations/[ORGANIZATION_ID]
    folders/[FOLDER_ID]
      
  
### Query parameters

Parameters  
---  
`filter` |  `string` Required. A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that specifies which time series should be returned. The filter must specify a single metric type, and can additionally specify metric labels and other information. For example:
    
    
    metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
        metric.labels.instance_name = "my-instance-name"
      
  
`interval` |  `object (`[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval)`)` Required. The time interval for which results should be returned. Only time series that contain data points in the specified interval are included in the response.  
`aggregation` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aggregation)`)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series across specified labels.By default (if no `aggregation` is explicitly specified), the raw time series data is returned.  
`secondaryAggregation` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aggregation)`)` Apply a second aggregation after `aggregation` is applied. May only be specified if `aggregation` is specified.  
`orderBy` |  `string` Unsupported: must be left blank. The points in each time series are currently returned in reverse time order (most recent to oldest).  
`view` |  `enum (`[TimeSeriesView](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeriesView)`)` Required. Specifies which information is returned about the time series.  
`pageSize` |  `integer` A positive number that is the maximum number of results to return. If `pageSize` is empty or more than 100,000 results, the effective `pageSize` is 100,000 results. If `view` is set to `FULL`, this is the maximum number of `Points` returned. If `view` is set to `HEADERS`, this is the maximum number of `TimeSeries` returned.  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListTimeSeriesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/ListTimeSeriesResponse)`.

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
