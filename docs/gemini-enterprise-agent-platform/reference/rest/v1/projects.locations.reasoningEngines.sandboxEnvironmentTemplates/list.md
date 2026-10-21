---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentTemplates/list/
title: Method: sandboxEnvironmentTemplates.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:44:38.022492+00:00
---

# Method: sandboxEnvironmentTemplates.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentTemplates/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: sandboxEnvironmentTemplates.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.reasoningEngines.sandboxEnvironmentTemplates.list

Lists `[SandboxEnvironmentTemplate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentTemplates#SandboxEnvironmentTemplate)`s in a given reasoning engine.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/sandboxEnvironmentTemplates`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the reasoning engine to list sandbox environment templates from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`

### Query parameters

| `filter` `string` Optional. The standard list filter. More detail in [AIP-160](https://google.aip.dev/160). | `pageSize` `integer` Optional. The maximum number of SandboxEnvironmentTemplates to return. The service may return fewer than this value. If unspecified, at most 100 SandboxEnvironmentTemplates will be returned. | `pageToken` `string` Optional. The standard list page token, received from a previous `sandboxEnvironmentTemplates.list` call. Provide this to retrieve the subsequent page.

### Request body

The request body must be empty.

### Response body

Response message for `[SandboxEnvironmentService.ListSandboxEnvironmentTemplates](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentTemplates/list#google.cloud.aiplatform.v1.SandboxEnvironmentService.ListSandboxEnvironmentTemplates)`. If successful, the response body contains data with the following structure: | Fields  
  
`sandboxEnvironmentTemplates[]` `object (`[SandboxEnvironmentTemplate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentTemplates#SandboxEnvironmentTemplate)`)` The SandboxEnvironmentTemplates matching the request. | `nextPageToken` `string` A token, which can be sent as `[ListSandboxEnvironmentTemplatesRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentTemplates/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "sandboxEnvironmentTemplates": [
        {
          object ([SandboxEnvironmentTemplate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentTemplates#SandboxEnvironmentTemplate))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
