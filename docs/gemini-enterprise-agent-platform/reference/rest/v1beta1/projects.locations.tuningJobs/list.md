---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs/list/
title: Method: tuningJobs.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:13.608572+00:00
---

# Method: tuningJobs.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: tuningJobs.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.tuningJobs.list

Lists tuning jobs in a location.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/tuningJobs`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the location to list the tuning jobs from. Format: `projects/{project}/locations/{location}`

### Query parameters

| `filter` `string` Optional. The standard list filter. | `pageSize` `integer` Optional. The standard list page size. | `pageToken` `string` Optional. The standard list page token.Typically obtained from `[ListTuningJobsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs/list#body.ListTuningJobsResponse.FIELDS.next_page_token)` of the previous `[GenAiTuningService.ListTuningJobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs/list#google.cloud.aiplatform.v1beta1.GenAiTuningService.ListTuningJobs)` call.

### Request body

The request body must be empty.

### Response body

Response message for `[GenAiTuningService.ListTuningJobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs/list#google.cloud.aiplatform.v1beta1.GenAiTuningService.ListTuningJobs)` If successful, the response body contains data with the following structure: | Fields  
  
`tuningJobs[]` `object (`[TuningJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs#TuningJob)`)` The tuning jobs that match the request. | `nextPageToken` `string` A token to retrieve the next page of results.Pass this token in a subsequent [GenAiTuningService.ListTuningJobs] call to retrieve the next page of results. | JSON representation  
---  
      
    
    {
      "tuningJobs": [
        {
          object ([TuningJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs#TuningJob))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.tuningJobs.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
