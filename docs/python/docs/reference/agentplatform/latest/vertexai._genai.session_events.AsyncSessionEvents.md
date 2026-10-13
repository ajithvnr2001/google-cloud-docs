---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.session_events.AsyncSessionEvents
title: Class AsyncSessionEvents (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:51.623138+00:00
---

# Class AsyncSessionEvents (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.session_events.AsyncSessionEvents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncSessionEvents (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AsyncSessionEvents(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `AsyncSessionEvents` class.

## Methods 

### append
    
    
    append(
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

Appends Agent Engine session event.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Agent Engine session to append the event to. Format: `projects/{project}/locations/{location}/reasoningEngines/{resource_id}/sessions/{session_id}`.  
`author` |  `str`   
Required. The author of the Agent Engine session event.  
`invocation_id` |  `str`   
Required. The invocation ID of the Agent Engine session event.  
`timestamp` |  `datetime.datetime`   
Required. The timestamp of the Agent Engine session event.  
`config` |  `AppendAgentEngineSessionEventConfig`   
Optional. Additional configurations for appending the Agent Engine session event.  
**Returns**  
---  
**Type** | **Description**  
`AppendAgentEngineSessionEventResponse` | The requested Agent Engine session event.  
  
### list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[vertexai._genai.types.common.SessionEvent]

Lists Agent Engine session events.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine to list session events for.  
`config` |  `ListAgentEngineSessionEventsConfig`   
Optional. The configuration for the session events to list. Currently, the `filter` field in `config` only supports filtering by `timestamp`. The timestamp value must be enclosed in double quotes and include the time zone information. For example: `config={'filter': 'timestamp>="2025-08-07T19:44:38.4Z"'}`.  
**Returns**  
---  
**Type** | **Description**  
`AsyncPager[SessionEvent]` | An async pager of session events.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
