---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/list/
title: Method: customJobs.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:03.098488+00:00
---

# Method: customJobs.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: customJobs.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.customJobs.list

Lists CustomJobs in a Location.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/customJobs`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location to list the CustomJobs from. Format: `projects/{project}/locations/{location}`

### Query parameters

| `filter` `string` The standard list filter.Supported fields:

  * `displayName` supports `=`, `!=` comparisons, and `:` wildcard.
  * `state` supports `=`, `!=` comparisons.
  * `createTime` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `createTime` must be in RFC 3339 format.
  * `labels` supports general map functions that is: `labels.key=value` \- key:value equality `labels.key:* - key existence

Some examples of using the filter are:

  * `state="JOB_STATE_SUCCEEDED" AND displayName:"my_job_*"`
  * `state!="JOB_STATE_FAILED" OR displayName="my_job"`
  * `NOT displayName="my_job"`
  * `createTime>"2021-05-18T00:00:00Z"`
  * `labels.keyA=valueA`
  * `labels.keyB:*`

| `pageSize` `integer` The standard list page size. | `pageToken` `string` The standard list page token. Typically obtained via `[ListCustomJobsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/list#body.ListCustomJobsResponse.FIELDS.next_page_token)` of the previous `[JobService.ListCustomJobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/list#google.cloud.aiplatform.v1.JobService.ListCustomJobs)` call. | `readMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Mask specifying which fields to read.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.

### Request body

The request body must be empty.

### Response body

Response message for `[JobService.ListCustomJobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/list#google.cloud.aiplatform.v1.JobService.ListCustomJobs)` If successful, the response body contains data with the following structure: | Fields  
  
`customJobs[]` `object (`[CustomJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs#CustomJob)`)` List of CustomJobs in the requested page. | `nextPageToken` `string` A token to retrieve the next page of results. Pass to `[ListCustomJobsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "customJobs": [
        {
          object ([CustomJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs#CustomJob))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
