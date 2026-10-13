---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ChatRequest
title: Class ChatRequest (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:49.066421+00:00
---

# Class ChatRequest (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ChatRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ChatRequest (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ChatRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for Chat.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`inline_context` |  `[google.cloud.geminidataanalytics_v1.types.Context](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context)`   
Optional. Inline context for the chat request. Use this to chat statelessly (without managed conversation persistence and without an Agent) by passing all context inline. This field is a member of `oneof`_ `context_provider`.   
`conversation_reference` |  `[google.cloud.geminidataanalytics_v1.types.ConversationReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ConversationReference)`   
Optional. Reference to a persisted conversation and agent context. Use this to chat with an Agent using managed conversation persistence. This field is a member of `oneof`_ `context_provider`.   
`data_agent_context` |  `[google.cloud.geminidataanalytics_v1.types.DataAgentContext](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DataAgentContext)`   
Optional. Context for the chat request. Use this to chat with an Agent statelessly, without managed conversation persistence. This field is a member of `oneof`_ `context_provider`.   
`client_managed_resource_context` |  `[google.cloud.geminidataanalytics_v1.types.ClientManagedResourceContext](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ClientManagedResourceContext)`   
Optional. Context with client managed resources. Some clients may not use GDA managed resources including conversations and agents, instead they create and manage their own conversations and agents resources. This field is a member of `oneof`_ `context_provider`.   
`looker_settings` |  `[google.cloud.geminidataanalytics_v1.types.LookerSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.LookerSettings)`   
Optional. Looker specific settings. This field is a member of `oneof`_ `datasource_settings`.   
`parent` |  `str`   
Required. The parent value for chat request. Pattern: `projects/{project}/locations/{location}`  
`messages` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.Message](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Message)]`   
Required. Content of current conversation.   
`credentials` |  `[google.cloud.geminidataanalytics_v1.types.Credentials](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Credentials)`   
Optional. The credentials to use when calling the data source(s) specified in the context. This field can be used to provide credentials for various data sources. For example, when connecting to Looker, it currently supports both OAuth token and API key-based credentials, as described in `Authentication with an SDK   
`thinking_mode` |  `[google.cloud.geminidataanalytics_v1.types.ChatRequest.ThinkingMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ChatRequest.ThinkingMode)`   
Optional. The thinking mode to use for the agent loop. Defaults to THINKING_MODE_UNSPECIFIED if not specified.   
`model` |  `[google.cloud.geminidataanalytics_v1.types.ChatRequest.Model](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ChatRequest.Model)`   
Optional. The model to use for the agent loop when processing the request. This setting only has an effect when context.options.model is not set.   
  
## Classes 

### Model
    
    
    Model(value)

Model selection for the agent for BigQuery users.

### ThinkingMode
    
    
    ThinkingMode(value)

Mode of thinking for the agent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
