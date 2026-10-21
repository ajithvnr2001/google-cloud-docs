---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/list/
title: Method: projects.locations.apps.evaluations.results.list \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:49:21.362351+00:00
---

# Method: projects.locations.apps.evaluations.results.list  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.evaluations.results.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists all evaluation results for a given evaluation.

### HTTP request

`GET https://ces.googleapis.com/v1beta/{parent=projects/*/locations/*/apps/*/evaluations/*}/results`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the evaluation to list evaluation results from. To filter by evaluation run, use `-` as the evaluation ID and specify the evaluation run ID in the filter. For example: `projects/{project}/locations/{location}/apps/{app}/evaluations/-`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. The `[nextPageToken](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/list#body.ListEvaluationResultsResponse.FIELDS.next_page_token)` value returned from a previous list `[EvaluationService.ListEvaluationResults](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/list#google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the evaluation results. See <https://google.aip.dev/160> for more details.  
`orderBy` |  `string` Optional. Field to sort by. Only "name" and "createTime", and "updateTime" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "updateTime" will be the default. See <https://google.aip.dev/132#ordering> for more details.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[EvaluationService.ListEvaluationResults](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/list#google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "evaluationResults": [
        {
          object ([EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`evaluationResults[]` |  `object (`[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results#EvaluationResult)`)` The list of evaluation results.  
`nextPageToken` |  `string` A token that can be sent as `[ListEvaluationResultsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluations.results/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluationResults.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
