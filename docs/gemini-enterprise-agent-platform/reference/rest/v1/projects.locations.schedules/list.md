---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.schedules/list/
title: Method: schedules.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:40.823084+00:00
---

# Method: schedules.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.schedules/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: schedules.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.schedules.list

Lists Schedules in a Location.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/schedules`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location to list the Schedules from. Format: `projects/{project}/locations/{location}`

### Query parameters

| `filter` `string` Lists the Schedules that match the filter expression. The following fields are supported:

  * `displayName`: Supports `=`, `!=` comparisons, and `:` wildcard.
  * `state`: Supports `=` and `!=` comparisons.
  * `request`: Supports existence of the  check. (e.g. `createPipelineJobRequest:*` \--> Schedule has createPipelineJobRequest).
  * `createTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `startTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `endTime`: Supports `=`, `!=`, `<`, `>`, `<=`, `>=` comparisons and `:*` existence check. Values must be in RFC 3339 format.
  * `nextRunTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.

Filter expressions can be combined together using logical operators (`NOT`, `AND` & `OR`). The syntax to define filter expression is based on <https://google.aip.dev/160>.Examples:

  * `state="ACTIVE" AND displayName:"my_schedule_*"`
  * `NOT displayName="my_schedule"`
  * `createTime>"2021-05-18T00:00:00Z"`
  * `endTime>"2021-05-18T00:00:00Z" OR NOT endTime:*`
  * `createPipelineJobRequest:*`

| `pageSize` `integer` The standard list page size. Default to 100 if not specified. | `pageToken` `string` The standard list page token. Typically obtained via `[ListSchedulesResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.schedules/list#body.ListSchedulesResponse.FIELDS.next_page_token)` of the previous `[ScheduleService.ListSchedules](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.schedules/list#google.cloud.aiplatform.v1.ScheduleService.ListSchedules)` call. | `orderBy` `string` A comma-separated list of fields to order by. The default sort order is in ascending order. Use "desc" after a field name for descending. You can have multiple orderBy fields provided.For example, using "createTime desc, endTime" will order results by create time in descending order, and if there are multiple schedules having the same create time, order them by the end time in ascending order.If orderBy is not specified, it will order by default with createTime in descending order.Supported fields:

  * `createTime`
  * `startTime`
  * `endTime`
  * `nextRunTime`



### Request body

The request body must be empty.

### Response body

Response message for `[ScheduleService.ListSchedules](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.schedules/list#google.cloud.aiplatform.v1.ScheduleService.ListSchedules)` If successful, the response body contains data with the following structure: | Fields  
  
`schedules[]` `object (`[Schedule](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.schedules#Schedule)`)` List of Schedules in the requested page. | `nextPageToken` `string` A token to retrieve the next page of results. Pass to `[ListSchedulesRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.schedules/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "schedules": [
        {
          object ([Schedule](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.schedules#Schedule))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.schedules.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
