---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list/
title: Method: projects.notificationChannelDescriptors.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:13.078151+00:00
---

# Method: projects.notificationChannelDescriptors.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.notificationChannelDescriptors.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the descriptors for supported channel types. The use of descriptors makes it possible for new channel types to be dynamically added.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{name}/notificationChannelDescriptors`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The REST resource name of the parent from which to retrieve the notification channel descriptors. The expected syntax is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Note that this [names](https://cloud.google.com/monitoring/api/v3#project_name) the parent container in which to look for the descriptors; to retrieve a single descriptor by name, use the `[notificationChannelDescriptors.get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/get#google.monitoring.v3.NotificationChannelService.GetNotificationChannelDescriptor)` operation, instead. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannelDescriptors.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of results to return in a single response. If not set to a positive number, a reasonable value will be chosen by the service.  
`pageToken` |  `string` If non-empty, `pageToken` must contain a value returned as the `nextPageToken` in a previous response to request the next set of results.  
  
### Request body

The request body must be empty.

### Response body

The `notificationChannelDescriptors.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "channelDescriptors": [
        {
          object ([NotificationChannelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors#NotificationChannelDescriptor))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`channelDescriptors[]` |  `object (`[NotificationChannelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors#NotificationChannelDescriptor)`)` The monitored resource descriptors supported for the specified project, optionally filtered.  
`nextPageToken` |  `string` If not empty, indicates that there may be more results that match the request. Use the value in the `pageToken` field in a subsequent request to fetch the next set of results. If empty, all results have been returned.  
  
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
