---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.memories/retrieve/
title: Method: memories.retrieve \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:57:31.354753+00:00
---

# Method: memories.retrieve  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.memories/retrieve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: memories.retrieve Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.reasoningEngines.memories.retrieve

Retrieve memories.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}/memories:retrieve`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the ReasoningEngine to retrieve memories from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`

### Request body

The request body contains data with the following structure: | Fields  
  
`scope` `map (key: string, value: string)` Required. The scope of the memories to retrieve. A memory must have exactly the same scope (`Memory.scope`) as the scope provided here to be retrieved (same keys and values). Order does not matter, but it is case-sensitive. | `filter` `string` Optional. The standard list filter that will be applied to the retrieved memories. More detail in [AIP-160](https://google.aip.dev/160).Supported fields: * `fact` * `createTime` * `updateTime` * `topics` (i.e. `topics.custom_memory_topic_label: "example topic" OR topics.managed_memory_topic: USER_PREFERENCES`) | `memoryTypes[]` `enum (`[MemoryType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/MemoryType)`)` Optional. Specifies the types of memories to retrieve. If this field is empty or not provided, the request will default to retrieving only memories of type `NATURAL_LANGUAGE_COLLECTION`. If populated, the request will retrieve memories matching any of the specified `MemoryType` values. | `retrieval_params` `Union type`  
  
Parameters for retrieval. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`similaritySearchParams` `object (`[SimilaritySearchParams](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SimilaritySearchParams)`)` Parameters for semantic similarity search based retrieval. | `simpleRetrievalParams` `object (`[SimpleRetrievalParams](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SimpleRetrievalParams)`)` Parameters for simple (non-similarity search) retrieval. End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[RetrieveMemoriesResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RetrieveMemoriesResponse)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-09-01 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
