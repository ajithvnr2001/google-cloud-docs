---
url: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.AsyncAgentEngines
title: Class AsyncAgentEngines (1.153.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:58.686388+00:00
---

# Class AsyncAgentEngines (1.153.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.AsyncAgentEngines

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncAgentEngines (1.153.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.153.1 (latest)  1.153.0  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0 
    
    
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

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
