---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.memories/list/
title: Method: memories.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:21.037575+00:00
---

# Method: memories.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.memories/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: memories.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.reasoningEngines.memories.list

List Memories.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/memories`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the ReasoningEngine to list the Memories under. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`

### Query parameters

| `filter` `string` Optional. The standard list filter. More detail in [AIP-160](https://google.aip.dev/160).Supported fields: * `scope` (as a JSON string with equality match only) * `topics` (i.e. `topics.custom_memory_topic_label: "example topic" OR topics.managed_memory_topic: USER_PREFERENCES`) | `pageSize` `integer` Optional. The standard list page size. | `pageToken` `string` Optional. The standard list page token. | `orderBy` `string` Optional. The standard list order by string. If not specified, the default order is `createTime desc`. If specified, the default sorting order of provided fields is ascending.More detail in [AIP-132](https://google.aip.dev/132).Supported fields: * `createTime` * `updateTime`

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListMemoriesResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ListMemoriesResponse)`.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.memories.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs). Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
