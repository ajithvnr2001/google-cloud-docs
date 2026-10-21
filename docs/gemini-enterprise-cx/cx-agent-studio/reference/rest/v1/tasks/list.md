---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks/list/
title: Method: tasks.list \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:38.837199+00:00
---

# Method: tasks.list  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: tasks.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists tasks that match the specified filter.

### HTTP request

`GET https://ces.googleapis.com/tasks`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`contextId` |  `string` Filter tasks by context ID to get tasks from a specific conversation or session.  
`status` |  `enum (`[TaskState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#TaskState)`)` Filter tasks by their current status state.  
`pageToken` |  `string` A page token, received from a previous `tasks.list` call. `ListTasksResponse.next_page_token`. Provide this to retrieve the subsequent page.  
`statusTimestampAfter` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Filter tasks which have a status updated after the provided timestamp in ISO 8601 format (e.g., "2023-10-27T10:00:00Z"). Only tasks with a status timestamp time greater than or equal to this value will be returned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`pageSize` |  `integer` The maximum number of tasks to return. The service may return fewer than this value. If unspecified, at most 50 tasks will be returned. The minimum value is 1. The maximum value is 100.  
`historyLength` |  `integer` The maximum number of messages to include in each task's history.  
`includeArtifacts` |  `boolean` Whether to include artifacts in the returned tasks. Defaults to false to reduce payload size.  
  
### Request body

The request body must be empty.

### Response body

Result object for `tasks.list` method containing an array of tasks and pagination information.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#Task))
        }
      ],
      "nextPageToken": string,
      "pageSize": integer,
      "totalSize": integer
    }  
  
Fields  
---  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#Task)`)` Required. Array of tasks matching the specified criteria.  
`nextPageToken` |  `string` Required. A token to retrieve the next page of results, or empty if there are no more results in the list.  
`pageSize` |  `integer` Required. The page size used for this response.  
`totalSize` |  `integer` Required. Total number of tasks available (before pagination).  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-23 UTC."],[],[]] 
