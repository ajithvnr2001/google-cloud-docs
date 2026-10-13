---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudtasks/v2/projects.locations.queues.tasks/list/
title: Method: googleapis.cloudtasks.v2.projects.locations.queues.tasks.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:30.516239+00:00
---

# Method: googleapis.cloudtasks.v2.projects.locations.queues.tasks.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudtasks/v2/projects.locations.queues.tasks/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudtasks.v2.projects.locations.queues.tasks.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists the tasks in a queue. By default, only the BASIC view is retrieved due to performance considerations; response_view controls the subset of information which is returned. The tasks may be returned in any order. The ordering may change at any time.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Maximum page size. Fewer tasks than requested might be returned, even if more tasks exist; use next_page_token in the response to determine if more tasks exist. The maximum page size is 1000. If unspecified, the page size will be the maximum.  
`pageToken` |  `string` A token identifying the page of results to return. To request the first page results, page_token must be empty. To request the next page of results, page_token must be the value of next_page_token returned from the previous call to ListTasks method. The page token is valid for only 2 hours.  
`responseView` |  `enum` The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Task resource.  
Enum type. Can be one of the following:  
`VIEW_UNSPECIFIED` | Unspecified. Defaults to BASIC.  
`BASIC` | The basic view omits fields which can be large or can contain sensitive data. This view does not include the body in AppEngineHttpRequest. Bodies are desirable to return only when needed, because they can be large and because of the sensitivity of the data that you choose to store in it.  
`FULL` | All information is returned. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Queue resource.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`ListTasksResponse`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudtasks/v2/Overview#ListTasksResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list).

### YAML
    
    
    - list:
        call: googleapis.cloudtasks.v2.projects.locations.queues.tasks.list
        args:
            parent: ...
            pageSize: ...
            pageToken: ...
            responseView: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.cloudtasks.v2.projects.locations.queues.tasks.list",
          "args": {
            "parent": "...",
            "pageSize": "...",
            "pageToken": "...",
            "responseView": "..."
          },
          "result": "listResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
