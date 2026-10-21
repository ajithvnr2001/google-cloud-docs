---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookExecutionJobs/list/
title: Method: notebookExecutionJobs.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:02:08.960999+00:00
---

# Method: notebookExecutionJobs.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookExecutionJobs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: notebookExecutionJobs.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.notebookExecutionJobs.list

Lists NotebookExecutionJobs in a Location.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/notebookExecutionJobs`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location from which to list the NotebookExecutionJobs. Format: `projects/{project}/locations/{location}`

### Query parameters

| `filter` `string` Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.

  * `notebookExecutionJob` supports = and !=. `notebookExecutionJob` represents the NotebookExecutionJob id.
  * `displayName` supports = and != and regex.
  * `schedule` supports = and != and regex.

Some examples: * `notebookExecutionJob="123"` * `notebookExecutionJob="my-execution-job"` * `displayName="myDisplayName"` and `displayName=~"myDisplayNameRegex"` | `pageSize` `integer` Optional. The standard list page size. | `pageToken` `string` Optional. The standard list page token. Typically obtained via `[ListNotebookExecutionJobsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookExecutionJobs/list#body.ListNotebookExecutionJobsResponse.FIELDS.next_page_token)` of the previous `[NotebookService.ListNotebookExecutionJobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookExecutionJobs/list#google.cloud.aiplatform.v1.NotebookService.ListNotebookExecutionJobs)` call. | `orderBy` `string` Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

  * `displayName`
  * `createTime`
  * `updateTime`

Example: `displayName, createTime desc`. | `view` `enum (`[NotebookExecutionJobView](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookExecutionJobView)`)` Optional. The NotebookExecutionJob view. Defaults to BASIC.

### Request body

The request body must be empty.

### Response body

Response message for [NotebookService.CreateNotebookExecutionJob] If successful, the response body contains data with the following structure: | Fields  
  
`notebookExecutionJobs[]` `object (`[NotebookExecutionJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookExecutionJobs#NotebookExecutionJob)`)` List of NotebookExecutionJobs in the requested page. | `nextPageToken` `string` A token to retrieve next page of results. Pass to `[ListNotebookExecutionJobsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookExecutionJobs/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "notebookExecutionJobs": [
        {
          object ([NotebookExecutionJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookExecutionJobs#NotebookExecutionJob))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
