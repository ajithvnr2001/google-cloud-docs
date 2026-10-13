---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.executions/list/
title: Method: projects.locations.executions.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:58.005221+00:00
---

# Method: projects.locations.executions.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.executions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.executions.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists executions in a given project and location

### HTTP request

`GET https://notebooks.googleapis.com/v1/{parent}/executions`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Format: `parent=projects/{projectId}/locations/{location}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `notebooks.executions.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum return size of the list call.  
`pageToken` |  `string` A previous returned page token that can be used to continue listing from the last result.  
`filter` |  `string` Filter applied to resulting executions. Currently only supports filtering executions by a specified `scheduleId`. Format: `scheduleId=<Schedule_ID>`  
`orderBy` |  `string` Sort by field.  
  
### Request body

The request body must be empty.

### Response body

Response for listing scheduled notebook executions

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "executions": [
        {
          object ([Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.executions#Execution))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`executions[]` |  `object (`[Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.executions#Execution)`)` A list of returned instances.  
`nextPageToken` |  `string` Page token that can be used to continue listing from the last result in the next list call.  
`unreachable[]` |  `string` Executions IDs that could not be reached. For example:
    
    
    ['projects/{projectId}/location/{location}/executions/imagenet_test1',
     'projects/{projectId}/location/{location}/executions/classifier_train1']
      
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/notebooks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
