---
url: https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions.tasks/list/
title: Method: projects.locations.jobs.executions.tasks.list \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:10.402812+00:00
---

# Method: projects.locations.jobs.executions.tasks.list  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions.tasks/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Reference ](https://docs.cloud.google.com/run/docs/apis)



Send feedback 

#  Method: projects.locations.jobs.executions.tasks.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists Tasks from an Execution of a Job.

### HTTP request

`GET https://run.googleapis.com/v2/{parent}/tasks`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The Execution from which the Tasks should be listed. To list all Tasks across Executions of a Job, use "-" instead of Execution name. To list all Tasks across Jobs, use "-" instead of Job name. Format: projects/{project}/locations/{location}/jobs/{job}/executions/{execution} It takes the form `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `run.tasks.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of Tasks to return in this call.  
`pageToken` |  `string` A page token received from a previous call to tasks.list. All other parameters must match.  
`showDeleted` |  `boolean` If true, returns deleted (but unexpired) resources along with active ones.  
  
### Request body

The request body must be empty.

### Response body

Response message containing a list of Tasks.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions.tasks#Task))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions.tasks#Task)`)` The resulting list of Tasks.  
`nextPageToken` |  `string` A token indicating there are more items than pageSize. Use it in the next tasks.list request to continue.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
