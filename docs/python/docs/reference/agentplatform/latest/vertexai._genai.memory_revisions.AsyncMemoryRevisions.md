---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.memory_revisions.AsyncMemoryRevisions
title: Class AsyncMemoryRevisions (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:48.117717+00:00
---

# Class AsyncMemoryRevisions (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.memory_revisions.AsyncMemoryRevisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncMemoryRevisions (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AsyncMemoryRevisions(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `AsyncMemoryRevisions` class.

## Methods 

### get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryRevisionConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryRevisionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.MemoryRevision

Gets an agent engine memory revision.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Agent Engine memory revision to get. Format: `projects/{project}/locations/{location}/reasoningEngines/{resource_id}/memories/{memory_id}/revisions/{revision_id}`.  
`config` |  `GetAgentEngineMemoryRevisionConfig`   
Optional. Additional configurations for getting the Agent Engine memory revision.  
**Returns**  
---  
**Type** | **Description**  
`AgentEngineMemoryRevision` | The requested Agent Engine memory revision.  
  
### list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineMemoryRevisionsConfig,
                vertexai._genai.types.common.ListAgentEngineMemoryRevisionsConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[vertexai._genai.types.common.MemoryRevision]

Lists Agent Engine memory revisions.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the Memory to list revisions for.  
`config` |  `ListAgentEngineMemoryRevisionsConfigOrDict`   
Optional. The configuration for the memories to list revisions.  
**Returns**  
---  
**Type** | **Description**  
`AsyncPager[MemoryRevision]` | An async pager of memory revisions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
