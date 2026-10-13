---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.AgentEngines
title: Class AgentEngines (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:45.812530+00:00
---

# Class AgentEngines (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.AgentEngines

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AgentEngines (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AgentEngines(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `AgentEngines` class.

## Properties 

### a2a_tasks

API documentation for `a2a_tasks` property.

### memories

API documentation for `memories` property.

### runtimes

API documentation for `runtimes` property.

### sandboxes

API documentation for `sandboxes` property.

### sessions

API documentation for `sessions` property.

## Methods 

### append_session_event
    
    
    append_session_event(
        *,
        name: str,
        author: str,
        invocation_id: str,
        timestamp: datetime.datetime,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfig,
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AppendAgentEngineSessionEventResponse

Deprecated. Use agent_engines.sessions.events.append instead.

### cancel_query_job
    
    
    cancel_query_job(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CancelQueryJobAgentEngineConfig,
                vertexai._genai.types.common.CancelQueryJobAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.CancelQueryJobResult

Cancels a long-running query job on an Agent Engine.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The reasoning engine resource name.  
`config` |  `CancelQueryJobAgentEngineConfigOrDict`   
Optional. The configuration for the cancel_query_job.  
  
### check_query_job
    
    
    check_query_job(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CheckQueryJobAgentEngineConfig,
                vertexai._genai.types.common.CheckQueryJobAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.CheckQueryJobResult

Checks a query job on an agent engine and optionally returns the results.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. A fully-qualified resource name or ID.  
`config` |  `CheckQueryJobAgentEngineConfigOrDict`   
Optional. The configuration for the check_query_job. If not provided, the default configuration will be used. This can be used to specify the following fields: - retrieve_result: Whether to retrieve the results of the query job.  
  
### create
    
    
    create(
        *,
        agent_engine: typing.Optional[typing.Any] = None,
        agent: typing.Optional[typing.Any] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AgentEngineConfig,
                vertexai._genai.types.common.AgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngine

Creates an agent engine.

The Agent Engine will be an instance of the `agent_engine` that was passed in, running remotely on Vertex AI.

Sample `src_dir` contents (e.g. `./user_src_dir`):
    
    
    user_src_dir/
    |-- main.py
    |-- requirements.txt
    |-- user_code/
    |   |-- utils.py
    |   |-- ...
    |-- ...
    

To build an Agent Engine with the above files, run:
    
    
    client = <xref uid="vertexai.Client">vertexai.Client</xref>(
        project="your-project",
        location="us-central1",
    )
    remote_agent = client.agent_engines.create(
        agent=local_agent,
        config=dict(
            requirements=[
                # I.e. the PyPI dependencies listed in requirements.txt
                "google-cloud-aiplatform[agent_engines,adk]",
                ...
            ],
            extra_packages=[
                "./user_src_dir/main.py", # a single file
                "./user_src_dir/user_code", # a directory
                ...
            ],
        ),
    )
    

**Parameters**  
---  
**Name** | **Description**  
`agent` |  `Any`   
Optional. The Agent to be created. If not specified, this will correspond to a lightweight instance that cannot be queried (but can be updated to future instances that can be queried).  
`agent_engine` |  `Any`   
Optional. This is deprecated. Please use `agent` instead.  
`config` |  `AgentEngineConfig`   
Optional. The configurations to use for creating the Agent Engine.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the `project` was not set using `client.Client`.  
`ValueError` | If the `location` was not set using `client.Client`.  
`ValueError` | If `config.staging_bucket` was not set when `agent`  
`i` | specified.:  
`ValueError` | If `config.staging_bucket` does not start with "gs://".  
`ValueError` | If `config.extra_packages` is specified but `agent`  
`i` | None.:  
`ValueError` | If `config.requirements` is specified but `agent` is None.  
`ValueError` | If `config.env_vars` has a dictionary entry that does not  
`correspon` | to an environment variable value or a SecretRef.:  
`TypeError` | If `config.env_vars` is not a dictionary.  
`FileNotFoundError` | If `config.extra_packages` includes a file or  
`director` | that does not exist.:  
`IOError` | If `config.requirements` is a string that corresponds to a  
`nonexisten` | file.:  
**Returns**  
---  
**Type** | **Description**  
`AgentEngine` | The created Agent Engine instance.  
  
### create_memory
    
    
    create_memory(
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

Deprecated. Use agent_engines.memories.create instead.

### create_session
    
    
    create_session(
        *,
        name: str,
        user_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateAgentEngineSessionConfig,
                vertexai._genai.types.common.CreateAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineSessionOperation

Deprecated. Use agent_engines.sessions.create instead.

### delete
    
    
    delete(
        *,
        name: str,
        force: typing.Optional[bool] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineConfig,
                vertexai._genai.types.common.DeleteAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineOperation

Delete an Agent Engine resource.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Agent Engine to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{resource_id}` or `reasoningEngines/{resource_id}`.  
`force` |  `bool`   
Optional. If set to True, child resources will also be deleted. Otherwise, the request will fail with FAILED_PRECONDITION error when the Agent Engine has undeleted child resources. Defaults to False.  
`config` |  `DeleteAgentEngineConfig`   
Optional. Additional configurations for deleting the Agent Engine.  
  
### delete_memory
    
    
    delete_memory(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfig,
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineMemoryOperation

Deprecated. Use agent_engines.memories.delete instead.

### delete_session
    
    
    delete_session(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineSessionConfig,
                vertexai._genai.types.common.DeleteAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineSessionOperation

Deprecated. Use agent_engines.sessions.delete instead.

### generate_memories
    
    
    generate_memories(
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

Deprecated. Use agent_engines.memories.generate instead.

### get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineConfig,
                vertexai._genai.types.common.GetAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngine

Gets an agent engine.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. A fully-qualified resource name or ID such as "projects/123/locations/us-central1/reasoningEngines/456" or a shortened name such as "reasoningEngines/456".  
  
### get_memory
    
    
    get_memory(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Memory

Deprecated. Use agent_engines.memories.get instead.

### get_session
    
    
    get_session(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineSessionConfig,
                vertexai._genai.types.common.GetAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Session

Deprecated. Use agent_engines.sessions.get instead.

### list
    
    
    list(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineConfig,
                vertexai._genai.types.common.ListAgentEngineConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.AgentEngine]

List all instances of Agent Engine matching the filter.

Example Usage:
    
    
        import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    client = <xref uid="vertexai.Client">vertexai.Client</xref>(project="my_project", location="us-central1")
    for agent in client.[agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).list(
        config={"filter": "'display_name="My Custom Agent"'},
    ):
        print(agent.api_resource.name)
    

**Parameter**  
---  
**Name** | **Description**  
`config` |  `ListAgentEngineConfig`   
Optional. The config (e.g. filter) for the agents to be listed.  
**Returns**  
---  
**Type** | **Description**  
`Iterable[AgentEngine]` | An iterable of Agent Engines matching the filter.  
  
### list_memories
    
    
    list_memories(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineMemoryConfig,
                vertexai._genai.types.common.ListAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Memory]

Deprecated. Use agent_engines.memories.list instead.

### list_session_events
    
    
    list_session_events(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.SessionEvent]

Deprecated. Use agent_engines.sessions.events.list instead.

### list_sessions
    
    
    list_sessions(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Session]

Deprecated. Use agent_engines.sessions.list instead.

### retrieve_memories
    
    
    retrieve_memories(
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

Deprecated. Use agent_engines.memories.retrieve instead.

### run_query_job
    
    
    run_query_job(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RunQueryJobAgentEngineConfig,
                vertexai._genai.types.common.RunQueryJobAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.RunQueryJobResult

Launches a long-running query job on an Agent Engine

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. A fully-qualified resource name or ID.  
`config` |  `RunQueryJobAgentEngineConfigOrDict`   
Optional. The configuration for the async query. If not provided, the default configuration will be used. This can be used to specify the following fields: - query: The query to send to the agent engine. - output_gcs_uri: The GCS URI to use for the output.  
  
### update
    
    
    update(
        *,
        name: str,
        agent: typing.Optional[typing.Any] = None,
        agent_engine: typing.Optional[typing.Any] = None,
        config: typing.Union[
            vertexai._genai.types.common.AgentEngineConfig,
            vertexai._genai.types.common.AgentEngineConfigDict,
        ]
    ) -> vertexai._genai.types.common.AgentEngine

Updates an existing Agent Engine.

This method updates the configuration of an existing Agent Engine running remotely, which is identified by its name.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. A fully-qualified resource name or ID such as "projects/123/locations/us-central1/reasoningEngines/456" or a shortened name such as "reasoningEngines/456".  
`agent` |  `Any`   
Optional. The instance to be used as the updated Agent Engine. If it is not specified, the existing instance will be used.  
`agent_engine` |  `Any`   
Optional. This is deprecated. Please use `agent` instead.  
`config` |  `AgentEngineConfig`   
Optional. The configurations to use for updating the Agent Engine.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the `project` was not set using `client.Client`.  
`ValueError` | If the `location` was not set using `client.Client`.  
`ValueError` | If `config.staging_bucket` was not set when `agent_engine`  
`i` | specified.:  
`ValueError` | If `config.staging_bucket` does not start with "gs://".  
`ValueError` | If `config.extra_packages` is specified but `agent_engine`  
`i` | None.:  
`ValueError` | If `config.requirements` is specified but `agent_engine` is  
`None.` |   
`ValueError` | If `config.env_vars` has a dictionary entry that does not  
`correspon` | to an environment variable value or a SecretRef.:  
`TypeError` | If `config.env_vars` is not a dictionary.  
`FileNotFoundError` | If `config.extra_packages` includes a file or  
`director` | that does not exist.:  
`IOError` | If `config.requirements` is a string that corresponds to a  
`nonexisten` | file.:  
**Returns**  
---  
**Type** | **Description**  
`AgentEngine` | The updated Agent Engine.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
