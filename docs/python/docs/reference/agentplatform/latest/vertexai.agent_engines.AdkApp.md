---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AdkApp
title: Class AdkApp (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:04.224670+00:00
---

# Class AdkApp (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AdkApp

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AdkApp (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AdkApp(
        *,
        app: App = None,
        agent: BaseAgent = None,
        app_name: typing.Optional[str] = None,
        plugins: typing.Optional[typing.List[BasePlugin]] = None,
        enable_tracing: typing.Optional[bool] = None,
        session_service_builder: typing.Optional[
            typing.Callable[[...], BaseSessionService]
        ] = None,
        artifact_service_builder: typing.Optional[
            typing.Callable[[...], BaseArtifactService]
        ] = None,
        memory_service_builder: typing.Optional[
            typing.Callable[[...], BaseMemoryService]
        ] = None,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

An ADK Application.

## Methods 

### AdkApp
    
    
    AdkApp(
        *,
        app: App = None,
        agent: BaseAgent = None,
        app_name: typing.Optional[str] = None,
        plugins: typing.Optional[typing.List[BasePlugin]] = None,
        enable_tracing: typing.Optional[bool] = None,
        session_service_builder: typing.Optional[
            typing.Callable[[...], BaseSessionService]
        ] = None,
        artifact_service_builder: typing.Optional[
            typing.Callable[[...], BaseArtifactService]
        ] = None,
        memory_service_builder: typing.Optional[
            typing.Callable[[...], BaseMemoryService]
        ] = None,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

An ADK Application.

See <https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/develop/adk> for details on how to develop ADK applications on Agent Engine.

**Parameters**  
---  
**Name** | **Description**  
`agent` |  `google.adk.agents.BaseAgent`   
Required. The ADK agent to run.  
`app_name` |  `str`   
Optional. The name of the ADK application. Defaults to "default-app-name" when running locally, and to the corresponding agent engine ID when deployed on Agent Engine.  
`plugins` |  `List[BasePlugin]`   
Optional. The plugins to use for the ADK application. Defaults to an empty list.  
`enable_tracing` |  `bool`   
Optional. Whether to enable tracing in Cloud Trace. Defaults to False.  
`session_service_builder` |  `Callable[..., BaseSessionService]`   
Optional. A callable that returns an ADK session service. Defaults to a callable that returns InMemorySessionService when running locally and VertexAiSessionService when running on Agent Engine.  
`artifact_service_builder` |  `Callable[..., BaseArtifactService]`   
Optional. A callable that returns an ADK artifact service. Defaults to a callable that returns InMemoryArtifactService.  
`memory_service_builder` |  `Callable[..., BaseMemoryService]`   
Optional. A callable that returns an ADK memory service. Defaults to a callable that returns InMemoryMemoryService when running locally and VertexAiMemoryBankService when running on Agent Engine.  
`instrumentor_builder` |  `Callable[..., Any]`   
Optional. Callable that returns a new instrumentor. This can be used for customizing the instrumentation logic of the Agent. If not provided, a default instrumentor builder will be used. This parameter is ignored if `enable_tracing` is False.  
  
### async_add_session_to_memory
    
    
    async_add_session_to_memory(*, session: typing.Dict[str, typing.Any])

Generates memories.

**Parameter**  
---  
**Name** | **Description**  
`session` |  `Dict[str, Any]`   
Required. The session to use for generating memories. It should be a dictionary representing an ADK Session object, e.g. session.model_dump(mode="json").  
  
### async_create_session
    
    
    async_create_session(
        *,
        user_id: str,
        session_id: typing.Optional[str] = None,
        state: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Creates a new session.

**Parameters**  
---  
**Name** | **Description**  
`user_id` |  `str`   
Required. The ID of the user.  
`session_id` |  `str`   
Optional. The ID of the session. If not provided, an ID will be be generated for the session.  
`state` |  `dict[str, Any]`   
Optional. The initial state of the session.  
`ttl` |  `str`   
Optional. The time-to-live for the session.  
`expire_time` |  `str`   
Optional. The expiration time for the session.  
`\*\*kwargs` |  `dict[str, Any]`   
Optional. Additional keyword arguments to pass to the session service.  
**Returns**  
---  
**Type** | **Description**  
`Session` | The newly created session instance.  
  
### async_delete_session
    
    
    async_delete_session(*, user_id: str, session_id: str, **kwargs)

Deletes a session for the given user.

**Parameters**  
---  
**Name** | **Description**  
`user_id` |  `str`   
Required. The ID of the user.  
`session_id` |  `str`   
Required. The ID of the session.  
`\*\*kwargs` |  `dict[str, Any]`   
Optional. Additional keyword arguments to pass to the session service.  
  
### async_get_session
    
    
    async_get_session(*, user_id: str, session_id: str, **kwargs)

Get a session for the given user.

**Parameters**  
---  
**Name** | **Description**  
`user_id` |  `str`   
Required. The ID of the user.  
`session_id` |  `str`   
Required. The ID of the session.  
`\*\*kwargs` |  `dict[str, Any]`   
Optional. Additional keyword arguments to pass to the session service.  
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If the session is not found.  
**Returns**  
---  
**Type** | **Description**  
`Session` | The session instance (if any). It returns None if the session is not found.  
  
### async_list_sessions
    
    
    async_list_sessions(*, user_id: str, **kwargs)

List sessions for the given user.

**Parameters**  
---  
**Name** | **Description**  
`user_id` |  `str`   
Required. The ID of the user.  
`\*\*kwargs` |  `dict[str, Any]`   
Optional. Additional keyword arguments to pass to the session service.  
**Returns**  
---  
**Type** | **Description**  
`ListSessionsResponse` | The list of sessions.  
  
### async_search_memory
    
    
    async_search_memory(*, user_id: str, query: str)

Searches memories for the given user.

### async_stream_query
    
    
    async_stream_query(
        *,
        message: typing.Union[str, typing.Dict[str, typing.Any]],
        user_id: str,
        session_id: typing.Optional[str] = None,
        session_events: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None,
        run_config: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    ) -> typing.AsyncIterable[typing.Dict[str, typing.Any]]

Streams responses asynchronously from the ADK application.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `str`   
Required. The message to stream responses for.  
`user_id` |  `str`   
Required. The ID of the user.  
`session_id` |  `str`   
Optional. The ID of the session. If not provided, a new session will be created for the user. If this is specified, then `session_events` will be ignored.  
`session_events` |  `Optional[List[Dict[str, Any]]]`   
Optional. The session events to use for the query. This will be used to initialize the session if `session_id` is not provided. That session exists only for this query and is deleted once the stream ends.  
`run_config` |  `Optional[Dict[str, Any]]`   
Optional. The run config to use for the query. If you want to pass in a `run_config` pydantic object, you can pass in a dict representing it as `run_config.model_dump(mode="json")`.  
`\*\*kwargs` |  `dict[str, Any] :Yields: Event dictionaries asynchronously.`   
Optional. Additional keyword arguments to pass to the runner.  
**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If message is not a string or a dictionary representing  
`` | Content object.:  
`ValueError` | If both session_id and session_events are specified.  
  
### clone
    
    
    clone()

Returns a clone of the ADK application.

### create_session
    
    
    create_session(
        *,
        user_id: str,
        session_id: typing.Optional[str] = None,
        state: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Deprecated. Use async_create_session instead.

Creates a new session.

### delete_session
    
    
    delete_session(*, user_id: str, session_id: str, **kwargs)

Deprecated. Use async_delete_session instead.

Deletes a session for the given user.

### get_session
    
    
    get_session(*, user_id: str, session_id: str, **kwargs)

Deprecated. Use async_get_session instead.

Get a session for the given user.

### list_sessions
    
    
    list_sessions(*, user_id: str, **kwargs)

Deprecated. Use async_list_sessions instead.

List sessions for the given user.

### register_operations
    
    
    register_operations() -> typing.Dict[str, typing.List[str]]

Registers the operations of the ADK application.

### set_up
    
    
    set_up()

Sets up the ADK application.

### stream_query
    
    
    stream_query(
        *,
        message: typing.Union[str, typing.Dict[str, typing.Any]],
        user_id: str,
        session_id: typing.Optional[str] = None,
        run_config: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Deprecated. Use async_stream_query instead.

Streams responses from the ADK application in response to a message.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `Union[str, Dict[str, Any]]`   
Required. The message to stream responses for.  
`user_id` |  `str`   
Required. The ID of the user.  
`session_id` |  `str`   
Optional. The ID of the session. If not provided, a new session will be created for the user.  
`run_config` |  `Optional[Dict[str, Any]]`   
Optional. The run config to use for the query. If you want to pass in a `run_config` pydantic object, you can pass in a dict representing it as `run_config.model_dump(mode="json")`.  
`\*\*kwargs` |  `dict[str, Any] :Yields: The output of querying the ADK application.`   
Optional. Additional keyword arguments to pass to the runner.  
  
### streaming_agent_run_with_events
    
    
    streaming_agent_run_with_events(request_json: str)

Streams responses asynchronously from the ADK application.

In general, you should use `async_stream_query` instead, as it has a more structured API and works with the respective ADK services that you have defined for the AdkApp. This method is primarily meant for invocation from AgentSpace.

**Parameter**  
---  
**Name** | **Description**  
`request_json` |  `str`   
Required. The request to stream responses for.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
