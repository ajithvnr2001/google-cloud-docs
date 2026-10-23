---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.runtimeRevisions/list/
title: Method: runtimeRevisions.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:57:13.745571+00:00
---

# Method: runtimeRevisions.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.runtimeRevisions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: runtimeRevisions.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.reasoningEngines.runtimeRevisions.list

Lists runtime revisions in a reasoning engine.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/runtimeRevisions`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the ReasoningEngine to list the ReasoningEngineRuntimeRevisions from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`

### Query parameters

| `filter` `string` Optional. The standard list filter. More detail in [AIP-160](https://google.aip.dev/160). | `pageSize` `integer` Optional. The maximum number of ReasoningEngineRuntimeRevisions to return. The service may return fewer than this value.If unspecified, at most 50 revisions will be returned.The maximum value is 100; values above 100 will be coerced to 100. | `pageToken` `string` Optional. The standard list page token.

### Request body

The request body must be empty.

### Response body

Response message for `[ReasoningEngineRuntimeRevisionService.ListReasoningEngineRuntimeRevisions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.runtimeRevisions/list#google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionService.ListReasoningEngineRuntimeRevisions)` If successful, the response body contains data with the following structure: | Fields  
  
`reasoningEngineRuntimeRevisions[]` `object (`[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.runtimeRevisions#ReasoningEngineRuntimeRevision)`)` List of ReasoningEngineRuntimeRevisions in the requested page. | `nextPageToken` `string` A token to retrieve the next page of results. Pass to `[ListReasoningEngineRuntimeRevisionsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.runtimeRevisions/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "reasoningEngineRuntimeRevisions": [
        {
          object ([ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.runtimeRevisions#ReasoningEngineRuntimeRevision))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.reasoningEngineRuntimeRevisions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
