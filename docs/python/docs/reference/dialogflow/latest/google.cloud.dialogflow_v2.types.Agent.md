---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent
title: Class Agent (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:26.170747+00:00
---

# Class Agent (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Agent (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 
    
    
    Agent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Dialogflow agent is a virtual agent that handles conversations with your end-users. It is a natural language understanding module that understands the nuances of human language. Dialogflow translates end-user text or audio during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow agent to handle the types of conversations required for your system.

For more information about agents, see the `Agent guide <https://cloud.google.com/dialogflow/docs/agents-overview>`__.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The project of this agent. Format: `projects/`.   
`display_name` |  `str`   
Required. The name of this agent.   
`default_language_code` |  `str`   
Required. The default language of the agent as a language tag. See `Language Support   
`supported_language_codes` |  `MutableSequence[str]`   
Optional. The list of all languages supported by this agent (except for the `default_language_code`).   
`time_zone` |  `str`   
Required. The time zone of this agent from the `time zone database   
`description` |  `str`   
Optional. The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.   
`avatar_uri` |  `str`   
Optional. The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted `Web Demo   
`enable_logging` |  `bool`   
Optional. Determines whether this agent should log conversation queries.   
`match_mode` |  `[google.cloud.dialogflow_v2.types.Agent.MatchMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent.MatchMode)`   
Optional. Determines how intents are detected from user queries.   
`classification_threshold` |  `float`   
Optional. To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used.   
`api_version` |  `[google.cloud.dialogflow_v2.types.Agent.ApiVersion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent.ApiVersion)`   
Optional. API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query different service endpoints for different API versions. However, bots connectors and webhook calls will follow the specified API version.   
`tier` |  `[google.cloud.dialogflow_v2.types.Agent.Tier](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent.Tier)`   
Optional. The agent tier. If not specified, TIER_STANDARD is assumed.   
  
## Classes 

### ApiVersion
    
    
    ApiVersion(value)

API version for the agent.

### MatchMode
    
    
    MatchMode(value)

Match mode determines how intents are detected from user queries.

### Tier
    
    
    Tier(value)

Represents the agent tier.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
