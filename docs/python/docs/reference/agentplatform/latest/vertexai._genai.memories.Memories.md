---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.memories.Memories
title: Class Memories (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:47.562114+00:00
---

# Class Memories (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.memories.Memories

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Memories (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    Memories(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `Memories` class.

## Properties 

### revisions

API documentation for `revisions` property.

## Methods 

### create
    
    
    create(
        *,
        name: str,
        fact: str,
        scope: dict[str, str],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AgentEngineMemoryConfig,
                vertexai._genai.types.common.AgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineMemoryOperation

Creates a new memory in the Agent Engine.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the memory to create.  
`fact` |  `str`   
Required. The fact to be stored in the memory.  
`scope` |  `dict[str, str]`   
Required. The scope of the memory. For example, {"user_id": "123"}.  
`config` |  `AgentEngineMemoryConfigOrDict`   
Optional. The configuration for the memory.  
**Returns**  
---  
**Type** | **Description**  
`AgentEngineMemoryOperation` | The operation for creating the memory.  
  
### delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfig,
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineMemoryOperation

Delete an Agent Engine memory.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Agent Engine memory to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{resource_id}/memories/{memory}`.  
`config` |  `DeleteAgentEngineMemoryConfig`   
Optional. Additional configurations for deleting the Agent Engine.  
  
### generate
    
    
    generate(
        *,
        name: str,
        vertex_session_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestVertexSessionSource,
                vertexai._genai.types.common.GenerateMemoriesRequestVertexSessionSourceDict,
            ]
        ] = None,
        direct_contents_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestDirectContentsSource,
                vertexai._genai.types.common.GenerateMemoriesRequestDirectContentsSourceDict,
            ]
        ] = None,
        direct_memories_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestDirectMemoriesSource,
                vertexai._genai.types.common.GenerateMemoriesRequestDirectMemoriesSourceDict,
            ]
        ] = None,
        scope: typing.Optional[dict[str, str]] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateAgentEngineMemoriesConfig,
                vertexai._genai.types.common.GenerateAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineGenerateMemoriesOperation

Generates memories for the agent engine.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine to generate memories for.  
`vertex_session_source` |  `GenerateMemoriesRequestVertexSessionSource`   
Optional. The vertex session source to use for generating memories. Only one of vertex_session_source, direct_contents_source, or direct_memories_source can be specified.  
`direct_contents_source` |  `GenerateMemoriesRequestDirectContentsSource`   
Optional. The direct contents source to use for generating memories. Only one of vertex_session_source, direct_contents_source, or direct_memories_source can be specified.  
`direct_memories_source` |  `GenerateMemoriesRequestDirectMemoriesSource`   
Optional. The direct memories source to use for generating memories. Only one of vertex_session_source, direct_contents_source, or direct_memories_source can be specified.  
`scope` |  `dict[str, str]`   
Optional. The scope of the memories to generate. This is optional if vertex_session_source is used, otherwise it must be specified.  
`config` |  `GenerateMemoriesConfig`   
Optional. The configuration for the memories to generate.  
**Returns**  
---  
**Type** | **Description**  
`AgentEngineGenerateMemoriesOperation` | The operation for generating the memories.  
  
### get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Memory

Gets an agent engine memory.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. A fully-qualified resource name or ID such as "projects/123/locations/us-central1/reasoningEngines/456/memories/789" or a shortened name such as "reasoningEngines/456/memories/789".  
  
### ingest_events
    
    
    ingest_events(
        *,
        name: str,
        scope: dict[str, str],
        stream_id: str = "",
        direct_contents_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.IngestionDirectContentsSource,
                vertexai._genai.types.common.IngestionDirectContentsSourceDict,
            ]
        ] = None,
        generation_trigger_config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.MemoryGenerationTriggerConfig,
                vertexai._genai.types.common.MemoryGenerationTriggerConfigDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.IngestEventsConfig,
                vertexai._genai.types.common.IngestEventsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.MemoryBankIngestEventsOperation

Ingests events into an Agent Engine.

Example usage:
    
    
    client.agent_engines.memories.ingest_events(
        name="projects/test-project/locations/us-central1/reasoningEngines/test-agent-engine",
        scope={"user_id": "test-user-id"},
        direct_contents_source={
            "events": [
                {
                    "content": {
                        "role": "user",
                        "parts": [
                            {"text": "I am a software engineer."}
                        ],
                    }
                }
            ]
        },
        generation_trigger_config={
            "generation_rule": {
                "idle_duration": "60s"
            }
        }
    )
    

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Agent Engine to ingest events into.  
`scope` |  `dict[str, str]`   
Required. The scope of the events to ingest. For example, {"user_id": "123"}.  
`stream_id` |  `str`   
Optional. The ID of the stream to ingest events into. If not specified, the events will be ingested into the default stream.  
`direct_contents_source` |  `IngestionDirectContentsSource`   
The direct contents source, containing the events to ingest.  
`generation_trigger_config` |  `MemoryGenerationTriggerConfig`   
Optional. The configuration for the generation trigger config.  
`config` |  `IngestEventsConfig`   
Optional. The configuration for the ingest events operation.  
**Returns**  
---  
**Type** | **Description**  
`AgentEngineIngestEventsOperation` | The operation for ingesting the events.  
  
### list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineMemoryConfig,
                vertexai._genai.types.common.ListAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Memory]

Lists Agent Engine memories.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine to list memories for.  
`config` |  `ListAgentEngineMemoryConfig`   
Optional. The configuration for the memories to list.  
**Returns**  
---  
**Type** | **Description**  
`Iterable[Memory]` | An iterable of memories.  
  
### purge
    
    
    purge(
        *,
        name: str,
        filter: typing.Optional[str] = None,
        filter_groups: typing.Optional[
            typing.List[vertexai._genai.types.common.MemoryConjunctionFilter]
        ] = None,
        force: bool = False,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.PurgeAgentEngineMemoriesConfig,
                vertexai._genai.types.common.PurgeAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEnginePurgeMemoriesOperation

Purges memories from an Agent Engine.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Agent Engine to purge memories from.  
`filter` |  `str`   
Optional. The standard list filter to determine which memories to purge.  
`filter_groups` |  `list[MemoryConjunctionFilter]`   
Optional. Metadata filters that will be applied to the memories' `metadata` using OR logic. Filters are defined using disjunctive normal form (OR of ANDs).  
`force` |  `bool`   
Optional. Whether to force the purge operation. If false, the operation will be staged but not executed.  
`config` |  `PurgeAgentEngineMemoriesConfig`   
Optional. The configuration for the purge operation.  
**Returns**  
---  
**Type** | **Description**  
`AgentEnginePurgeMemoriesOperation` | The operation for purging the memories.  
  
### retrieve
    
    
    retrieve(
        *,
        name: str,
        scope: dict[str, str],
        similarity_search_params: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoriesRequestSimilaritySearchParams,
                vertexai._genai.types.common.RetrieveMemoriesRequestSimilaritySearchParamsDict,
            ]
        ] = None,
        simple_retrieval_params: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoriesRequestSimpleRetrievalParams,
                vertexai._genai.types.common.RetrieveMemoriesRequestSimpleRetrievalParamsDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveAgentEngineMemoriesConfig,
                vertexai._genai.types.common.RetrieveAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[
        vertexai._genai.types.common.RetrieveMemoriesResponseRetrievedMemory
    ]

Retrieves memories for the agent.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine to retrieve memories for.  
`scope` |  `dict[str, str]`   
Required. The scope of the memories to retrieve. For example, {"user_id": "123"}.  
`similarity_search_params` |  `RetrieveMemoriesRequestSimilaritySearchParams`   
Optional. The similarity search parameters to use for retrieving memories.  
`simple_retrieval_params` |  `RetrieveMemoriesRequestSimpleRetrievalParams`   
Optional. The simple retrieval parameters to use for retrieving memories.  
`config` |  `RetrieveAgentEngineMemoriesConfig`   
Optional. The configuration for the memories to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`Iterator[RetrieveMemoriesResponseRetrievedMemory]` | An iterable of retrieved memories.  
  
### retrieve_profiles
    
    
    retrieve_profiles(
        *,
        name: str,
        scope: dict[str, str],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoryProfilesConfig,
                vertexai._genai.types.common.RetrieveMemoryProfilesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.RetrieveProfilesResponse

Retrieves memory profiles for an Agent Engine.

For example, you can use the following code to retrieve all memory profiles for scope `{'user_id': '123'}`:
    
    
    result = client.agent_engines.memories.retrieve_profiles(
        name="projects/123/locations/us-central1/reasoningEngines/456",
        scope={"user_id": "123"}
    )
    
    for profile in result.profiles.values():
      # Each profile is a dictionary corresponding to the relevant schema.
      print(profile.profile)
    

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. A fully-qualified resource name or ID such as "projects/123/locations/us-central1/reasoningEngines/456".  
`scope` |  `dict[str, str]`   
Required. The scope of the memories to retrieve. A memory must have exactly the same scope as the scope provided here to be retrieved (i.e. same keys and values). Order does not matter, but it is case-sensitive.  
**Returns**  
---  
**Type** | **Description**  
`RetrieveProfilesResponse` | The retrieved memory profiles.  
  
### rollback
    
    
    rollback(
        *,
        name: str,
        target_revision_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RollbackAgentEngineMemoryConfig,
                vertexai._genai.types.common.RollbackAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineRollbackMemoryOperation

Rolls back a memory to a previous revision.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the memory to rollback.  
`target_revision_id` |  `str`   
Required. The revision ID to roll back to  
`config` |  `RollbackAgentEngineMemoryConfig`   
Optional. The configuration for the rollback.  
**Returns**  
---  
**Type** | **Description**  
`AgentEngineRollbackMemoryOperation` | The operation for rolling back the memory.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
