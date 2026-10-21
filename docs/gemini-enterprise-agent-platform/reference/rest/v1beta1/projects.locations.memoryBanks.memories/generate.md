---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.memoryBanks.memories/generate/
title: Method: memories.generate \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:03:48.316754+00:00
---

# Method: memories.generate  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.memoryBanks.memories/generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: memories.generate Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.memoryBanks.memories.generate

Generate memories.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}/memories:generate`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the ReasoningEngine to generate memories for. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`

### Request body

The request body contains data with the following structure: | Fields  
  
`disableConsolidation` `boolean` Optional. If true, generated memories will not be consolidated with existing memories; all generated memories will be added as new memories regardless of whether they are duplicates of or contradictory to existing memories. By default, memory consolidation is enabled. | `scope` `map (key: string, value: string)` Optional. The scope of the memories that should be generated. Memories will be consolidated across memories with the same scope. Must be provided unless the scope is defined in the source content. If `scope` is provided, it will override the scope defined in the source content. scope values cannot contain the wildcard character '*'. | `source` `Union type`  
  
Source content used to generate memories. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`vertexSessionSource` `object (`[VertexSessionSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/VertexSessionSource)`)` Defines a Vertex Session as the source content from which to generate memories. | `directContentsSource` `object (`[DirectContentsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DirectContentsSource)`)` Defines a direct source of content as the source content from which to generate memories. | `directMemoriesSource` `object (`[DirectMemoriesSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DirectMemoriesSource)`)` Defines a direct source of memories that should be uploaded to Memory Bank. This is similar to `memories.create`, but it allows for consolidation between these new memories and existing memories for the same scope. End of mutually exclusive fields. | `revision_expiration` `Union type`  
  
The expiration of the Memory Revisions created as a result of this request. If not set, Memory Bank will defer to `MemoryBankConfig.memory_revision_default_ttl` or the global default, 365 days. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`revisionExpireTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. timestamp of when the revision is considered expired. If not set, the memory revision will be kept until manually deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `revisionTtl` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The TTL for the revision. The expiration time is computed: now + TTL.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-09-01 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
