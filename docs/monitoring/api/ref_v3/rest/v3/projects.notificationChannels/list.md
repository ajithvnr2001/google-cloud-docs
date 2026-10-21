---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list/
title: Method: projects.notificationChannels.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:13.016694+00:00
---

# Method: projects.notificationChannels.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.notificationChannels.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the notification channels that have been created for the project. To list the types of notification channels that are supported, use the `notificationChannelDescriptors.list` method.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{name}/notificationChannels`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

This names the container in which to look for the notification channels; it does not name a specific channel. To query a specific channel by REST resource name, use the `[`notificationChannels.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/get#google.monitoring.v3.NotificationChannelService.GetNotificationChannel)` operation. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. If provided, this field specifies the criteria that must be met by notification channels to be included in the response.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`orderBy` |  `string` Optional. A comma-separated list of fields by which to sort the result. Supports the same set of fields as in `filter`. Entries can be prefixed with a minus sign to sort in descending rather than ascending order.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`pageSize` |  `integer` Optional. The maximum number of results to return in a single response. If not set to a positive number, a reasonable value will be chosen by the service.  
`pageToken` |  `string` Optional. If non-empty, `pageToken` must contain a value returned as the `nextPageToken` in a previous response to request the next set of results.  
  
### Request body

The request body must be empty.

### Response body

The `notificationChannels.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "notificationChannels": [
        {
          object ([NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels#NotificationChannel))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`notificationChannels[]` |  `object (`[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels#NotificationChannel)`)` The notification channels defined for the specified project.  
`nextPageToken` |  `string` If not empty, indicates that there may be more results that match the request. Use the value in the `pageToken` field in a subsequent request to fetch the next set of results. If empty, all results have been returned.  
`totalSize` |  `integer` The total number of notification channels in all pages. This number is only an estimate, and may change in subsequent pages. <https://aip.dev/158>  
  
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
