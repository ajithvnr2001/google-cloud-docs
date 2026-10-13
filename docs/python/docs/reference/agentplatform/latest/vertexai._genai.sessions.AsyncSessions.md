---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.sessions.AsyncSessions
title: Class AsyncSessions (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:51.383050+00:00
---

# Class AsyncSessions (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.sessions.AsyncSessions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncSessions (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AsyncSessions(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `AsyncSessions` class.

## Properties 

### events

API documentation for `events` property.

## Methods 

### create
    
    
    create(
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

Creates a new session in the Agent Engine.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine to create the session for.  
`user_id` |  `str`   
Required. The user ID of the session.  
`config` |  `CreateAgentEngineSessionConfig`   
Optional. The configuration for the session to create.  
**Returns**  
---  
**Type** | **Description**  
`AgentEngineSessionOperation` | The operation for creating the session.  
  
### delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineSessionConfig,
                vertexai._genai.types.common.DeleteAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineSessionOperation

Delete an Agent Engine session.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Agent Engine session to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{resource_id}/sessions/{session_id}`.  
`config` |  `DeleteAgentEngineSessionConfig`   
Optional. Additional configurations for deleting the Agent Engine session.  
**Returns**  
---  
**Type** | **Description**  
`DeleteAgentEngineSessionOperation` | The operation for deleting the Agent Engine session.  
  
### get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineSessionConfig,
                vertexai._genai.types.common.GetAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Session

Gets an agent engine session.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Agent Engine session to get. Format: `projects/{project}/locations/{location}/reasoningEngines/{resource_id}/sessions/{session_id}`.  
`config` |  `GetAgentEngineSessionConfig`   
Optional. Additional configurations for getting the Agent Engine session.  
**Returns**  
---  
**Type** | **Description**  
`AgentEngineSession` | The requested Agent Engine session.  
  
### list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionsConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[vertexai._genai.types.common.Session]

Lists Agent Engine sessions.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine to list sessions for.  
`config` |  `ListAgentEngineSessionConfig`   
Optional. The configuration for the sessions to list.  
**Returns**  
---  
**Type** | **Description**  
`AsyncPager[Session]` | An async pager of sessions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
