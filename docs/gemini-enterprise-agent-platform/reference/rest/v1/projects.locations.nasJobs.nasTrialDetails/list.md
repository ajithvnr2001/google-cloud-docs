---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails/list/
title: Method: nasTrialDetails.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:57:50.093426+00:00
---

# Method: nasTrialDetails.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: nasTrialDetails.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.nasJobs.nasTrialDetails.list

List top NasTrialDetails of a NasJob.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/nasTrialDetails`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The name of the NasJob resource. Format: `projects/{project}/locations/{location}/nasJobs/{nasJob}`

### Query parameters

| `pageSize` `integer` The standard list page size. | `pageToken` `string` The standard list page token. Typically obtained via `[ListNasTrialDetailsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails/list#body.ListNasTrialDetailsResponse.FIELDS.next_page_token)` of the previous `[JobService.ListNasTrialDetails](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails/list#google.cloud.aiplatform.v1.JobService.ListNasTrialDetails)` call.

### Request body

The request body must be empty.

### Response body

Response message for `[JobService.ListNasTrialDetails](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails/list#google.cloud.aiplatform.v1.JobService.ListNasTrialDetails)` If successful, the response body contains data with the following structure: | Fields  
  
`nasTrialDetails[]` `object (`[NasTrialDetail](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails#NasTrialDetail)`)` List of top NasTrials in the requested page. | `nextPageToken` `string` A token to retrieve the next page of results. Pass to `[ListNasTrialDetailsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "nasTrialDetails": [
        {
          object ([NasTrialDetail](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails#NasTrialDetail))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.nasTrialDetails.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
