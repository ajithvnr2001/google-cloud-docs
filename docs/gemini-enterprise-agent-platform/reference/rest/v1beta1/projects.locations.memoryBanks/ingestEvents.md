---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.memoryBanks/ingestEvents/
title: Method: memoryBanks.ingestEvents \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:46:51.935201+00:00
---

# Method: memoryBanks.ingestEvents  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.memoryBanks/ingestEvents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: memoryBanks.ingestEvents Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.memoryBanks.ingestEvents

Ingests events for a Memory Bank.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}:ingestEvents`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the ReasoningEngine to ingest events to. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`

### Request body

The request body contains data with the following structure: | Fields  
  
`streamId` `string` Optional. The id of the stream to ingest events into. If not provided, a new one will be created. | `generationTriggerConfig` `object (`[MemoryGenerationTriggerConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines#MemoryGenerationTriggerConfig)`)` Optional. Configuration for triggering memory generation from this ingestion. If not set, then the stream will be force flushed immediately. | `scope` `map (key: string, value: string)` Required. The scope of the memories that should be generated from the stream. Memories will be consolidated across memories with the same scope. scope values cannot contain the wildcard character '*'. | `forceFlush` `boolean` Optional. Forces a flush of all pending events in the stream and triggers memory generation immediately bypassing any conditions configured in the `generationTriggerConfig`. | `source` `Union type`  
  
Source of the events to ingest. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`directContentsSource` `object (`[IngestionDirectContentsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/IngestionDirectContentsSource)`)` Ingest events directly from the request. End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-09-01 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
