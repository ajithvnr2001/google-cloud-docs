---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.pipelineJobs/list/
title: Method: pipelineJobs.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:57:40.697636+00:00
---

# Method: pipelineJobs.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.pipelineJobs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: pipelineJobs.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.pipelineJobs.list

Lists PipelineJobs in a Location.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/pipelineJobs`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location to list the PipelineJobs from. Format: `projects/{project}/locations/{location}`

### Query parameters

| `filter` `string` Lists the PipelineJobs that match the filter expression. The following fields are supported:

  * `pipelineName`: Supports `=` and `!=` comparisons.
  * `displayName`: Supports `=`, `!=` comparisons, and `:` wildcard.
  * `pipelineJobUserId`: Supports `=`, `!=` comparisons, and `:` wildcard. for example, can check if pipeline's displayName contains _step_ by doing displayName:"*step*"
  * `state`: Supports `=` and `!=` comparisons.
  * `createTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `updateTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `endTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `labels`: Supports key-value equality and key presence.
  * `templateUri`: Supports `=`, `!=` comparisons, and `:` wildcard.
  * `templateMetadata.version`: Supports `=`, `!=` comparisons, and `:` wildcard.

Filter expressions can be combined together using logical operators (`AND` & `OR`). For example: `pipelineName="test" AND createTime>"2020-05-18T13:30:00Z"`.The syntax to define filter expression is based on <https://google.aip.dev/160>.Examples:

  * `createTime>"2021-05-18T00:00:00Z" OR updateTime>"2020-05-18T00:00:00Z"` PipelineJobs created or updated after 2020-05-18 00:00:00 UTC.
  * `labels.env = "prod"` PipelineJobs with label "env" set to "prod".

| `pageSize` `integer` The standard list page size. | `pageToken` `string` The standard list page token. Typically obtained via `[ListPipelineJobsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.pipelineJobs/list#body.ListPipelineJobsResponse.FIELDS.next_page_token)` of the previous `[PipelineService.ListPipelineJobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.pipelineJobs/list#google.cloud.aiplatform.v1beta1.PipelineService.ListPipelineJobs)` call. | `orderBy` `string` A comma-separated list of fields to order by. The default sort order is in ascending order. Use "desc" after a field name for descending. You can have multiple orderBy fields provided e.g. "createTime desc, endTime", "endTime, startTime, updateTime" For example, using "createTime desc, endTime" will order results by create time in descending order, and if there are multiple jobs having the same create time, order them by the end time in ascending order. if orderBy is not specified, it will order by default order is create time in descending order. Supported fields:

  * `createTime`
  * `updateTime`
  * `endTime`
  * `startTime`

| `readMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Mask specifying which fields to read.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.

### Request body

The request body must be empty.

### Response body

Response message for `[PipelineService.ListPipelineJobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.pipelineJobs/list#google.cloud.aiplatform.v1beta1.PipelineService.ListPipelineJobs)` If successful, the response body contains data with the following structure: | Fields  
  
`pipelineJobs[]` `object (`[PipelineJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.pipelineJobs#PipelineJob)`)` List of PipelineJobs in the requested page. | `nextPageToken` `string` A token to retrieve the next page of results. Pass to `[ListPipelineJobsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.pipelineJobs/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "pipelineJobs": [
        {
          object ([PipelineJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.pipelineJobs#PipelineJob))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
