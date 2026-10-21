---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/list/
title: Method: projects.locations.apps.scheduledEvaluationRuns.list \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:38:55.189543+00:00
---

# Method: projects.locations.apps.scheduledEvaluationRuns.list  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.scheduledEvaluationRuns.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists all scheduled evaluation runs in the given app.

### HTTP request

`GET https://ces.googleapis.com/v1beta/{parent=projects/*/locations/*/apps/*}/scheduledEvaluationRuns`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the app to list scheduled evaluation runs from.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. The `[nextPageToken](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/list#body.ListScheduledEvaluationRunsResponse.FIELDS.next_page_token)` value returned from a previous list `[EvaluationService.ListScheduledEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/list#google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the scheduled evaluation runs. See <https://google.aip.dev/160> for more details. Currently supports filtering by: * request.evaluations:evaluationId * request.evaluation_dataset:evaluationDatasetId  
`orderBy` |  `string` Optional. Field to sort by. Supported fields are: "name" (ascending), "createTime" (descending), "updateTime" (descending), "next_scheduled_execution" (ascending), and "lastCompletedRun.create_time" (descending). If not included, "updateTime" will be the default. See <https://google.aip.dev/132#ordering> for more details.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[EvaluationService.ListScheduledEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/list#google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "scheduledEvaluationRuns": [
        {
          object ([ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns#ScheduledEvaluationRun))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`scheduledEvaluationRuns[]` |  `object (`[ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns#ScheduledEvaluationRun)`)` The list of scheduled evaluation runs.  
`nextPageToken` |  `string` A token that can be sent as `[ListScheduledEvaluationRunsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.scheduledEvaluationRuns/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
