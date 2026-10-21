---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.studies/list/
title: Method: studies.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:34:34.018100+00:00
---

# Method: studies.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.studies/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: studies.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.studies.list

Lists all the studies in a region for an associated project.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/studies`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location to list the Study from. Format: `projects/{project}/locations/{location}`

### Query parameters

| `pageToken` `string` Optional. A page token to request the next page of results. If unspecified, there are no subsequent pages. | `pageSize` `integer` Optional. The maximum number of studies to return per "page" of results. If unspecified, service will pick an appropriate default.

### Request body

The request body must be empty.

### Response body

Response message for `[VizierService.ListStudies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.studies/list#google.cloud.aiplatform.v1beta1.VizierService.ListStudies)`. If successful, the response body contains data with the following structure: | Fields  
  
`studies[]` `object (`[Study](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.studies#Study)`)` The studies associated with the project. | `nextPageToken` `string` Passes this token as the `pageToken` field of the request for a subsequent call. If this field is omitted, there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "studies": [
        {
          object ([Study](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.studies#Study))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
