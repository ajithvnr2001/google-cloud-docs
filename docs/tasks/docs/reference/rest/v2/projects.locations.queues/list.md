---
url: https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list/
title: Method: projects.locations.queues.list \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:18.903393+00:00
---

# Method: projects.locations.queues.list  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/tasks/docs/apis)



Send feedback 

#  Method: projects.locations.queues.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists queues.

Queues are returned in lexicographical order.

### HTTP request

`GET https://cloudtasks.googleapis.com/v2/{parent=projects/*/locations/*}/queues`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The location name. For example: `projects/PROJECT_ID/locations/LOCATION_ID` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudtasks.queues.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` `filter` can be used to specify a subset of queues. Any `[Queue](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#Queue)` field can be used as a filter and several operators as supported. For example: `<=, <, >=, >, !=, =, :`. The filter syntax is the same as described in [Stackdriver's Advanced Logs Filters](https://cloud.google.com/logging/docs/view/advanced_filters).Sample filter "state: PAUSED".Note that using filters might cause fewer queues than the requested pageSize to be returned.  
`pageSize` |  `integer` Requested page size.The maximum page size is 9800. If unspecified, the page size will be the maximum. Fewer queues than requested might be returned, even if more queues exist; use the `[nextPageToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list#body.ListQueuesResponse.FIELDS.next_page_token)` in the response to determine if more queues exist.  
`pageToken` |  `string` A token identifying the page of results to return.To request the first page results, pageToken must be empty. To request the next page of results, pageToken must be the value of `[nextPageToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list#body.ListQueuesResponse.FIELDS.next_page_token)` returned from the previous call to `[queues.list](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list#google.cloud.tasks.v2.CloudTasks.ListQueues)` method. It is an error to switch the value of the `[filter](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list#body.QUERY_PARAMETERS.filter)` while iterating through pages.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[queues.list](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list#google.cloud.tasks.v2.CloudTasks.ListQueues)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "queues": [
        {
          object ([Queue](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#Queue))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`queues[]` |  `object (`[Queue](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#Queue)`)` The list of queues.  
`nextPageToken` |  `string` A token to retrieve next page of results.To return the next page of results, call `[queues.list](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list#google.cloud.tasks.v2.CloudTasks.ListQueues)` with this value as the `[pageToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list#body.QUERY_PARAMETERS.page_token)`.If the nextPageToken is empty, there are no more results.The page token is valid for only 2 hours.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-tasks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
