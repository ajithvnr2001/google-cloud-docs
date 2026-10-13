---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines
title: Class AsyncAgentEngines (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:46.110646+00:00
---

# Class AsyncAgentEngines (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncAgentEngines (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AsyncAgentEngines(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `AsyncAgentEngines` class.

## Properties 

### a2a_tasks

API documentation for `a2a_tasks` property.

### memories

API documentation for `memories` property.

### runtimes

API documentation for `runtimes` property.

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
