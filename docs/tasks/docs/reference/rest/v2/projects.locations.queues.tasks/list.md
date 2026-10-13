---
url: https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list/
title: Method: projects.locations.queues.tasks.list \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:10.338188+00:00
---

# Method: projects.locations.queues.tasks.list  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/tasks/docs/apis)



Send feedback 

#  Method: projects.locations.queues.tasks.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the tasks in a queue.

By default, only the `[BASIC](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#View.ENUM_VALUES.BASIC)` view is retrieved due to performance considerations; `[responseView](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list#body.QUERY_PARAMETERS.response_view)` controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

### HTTP request

`GET https://cloudtasks.googleapis.com/v2/{parent=projects/*/locations/*/queues/*}/tasks`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudtasks.tasks.list`

  
  
### Query parameters

Parameters  
---  
`responseView` |  `enum (`[View](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#View)`)` The responseView specifies which subset of the `[Task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#Task)` will be returned.By default responseView is `[BASIC](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#View.ENUM_VALUES.BASIC)`; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains.Authorization for `[FULL](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#View.ENUM_VALUES.FULL)` requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the `[Task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#Task)` resource.  
`pageSize` |  `integer` Maximum page size.Fewer tasks than requested might be returned, even if more tasks exist; use `[nextPageToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list#body.ListTasksResponse.FIELDS.next_page_token)` in the response to determine if more tasks exist.The maximum page size is 1000. If unspecified, the page size will be the maximum.  
`pageToken` |  `string` A token identifying the page of results to return.To request the first page results, pageToken must be empty. To request the next page of results, pageToken must be the value of `[nextPageToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list#body.ListTasksResponse.FIELDS.next_page_token)` returned from the previous call to `[tasks.list](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list#google.cloud.tasks.v2.CloudTasks.ListTasks)` method.The page token is valid for only 2 hours.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing tasks using `[tasks.list](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list#google.cloud.tasks.v2.CloudTasks.ListTasks)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#Task))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#Task)`)` The list of tasks.  
`nextPageToken` |  `string` A token to retrieve next page of results.To return the next page of results, call `[tasks.list](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list#google.cloud.tasks.v2.CloudTasks.ListTasks)` with this value as the `[pageToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list#body.QUERY_PARAMETERS.page_token)`.If the nextPageToken is empty, there are no more results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-tasks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
