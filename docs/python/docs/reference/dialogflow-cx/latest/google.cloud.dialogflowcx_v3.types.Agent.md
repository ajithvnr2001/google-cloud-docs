---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Agent
title: Class Agent (2.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:00.194972+00:00
---

# Class Agent (2.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Agent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Agent (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.1.0  2.0.0  1.43.0  1.42.0  1.41.1  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.1  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.5  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.2  1.2.0  1.1.1  1.0.0  0.8.2  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    Agent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Agents are best described as Natural Language Understanding (NLU) modules that transform user requests into actionable data. You can include agents in your app, product, or service to determine user intent and respond to the user in a natural way.

After you create an agent, you can add Intents, [Entity Types][google.cloud.dialogflow.cx.v3.EntityType], Flows, Fulfillments, Webhooks, TransitionRouteGroups and so on to manage the conversation flows.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects/`.   
`display_name` |  `str`   
Required. The human-readable name of the agent, unique within the location.   
`default_language_code` |  `str`   
Required. Immutable. The default language of the agent as a language tag. See `Language Support   
`supported_language_codes` |  `MutableSequence[str]`   
The list of all languages supported by the agent (except for the `default_language_code`).   
`time_zone` |  `str`   
Required. The time zone of the agent from the `time zone database   
`description` |  `str`   
The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected.   
`avatar_uri` |  `str`   
The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted `Web Demo   
`speech_to_text_settings` |  `[google.cloud.dialogflowcx_v3.types.SpeechToTextSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SpeechToTextSettings)`   
Speech recognition related settings.   
`start_flow` |  `str`   
Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/`. Currently only the default start flow with id "00000000-0000-0000-0000-000000000000" is allowed. This field is a member of `oneof`_ `session_entry_resource`.   
`start_playbook` |  `str`   
Name of the start playbook in this agent. A start playbook will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/`. Currently only the default playbook with id "00000000-0000-0000-0000-000000000000" is allowed. This field is a member of `oneof`_ `session_entry_resource`.   
`security_settings` |  `str`   
Name of the SecuritySettings reference for the agent. Format: `projects/`.   
`enable_stackdriver_logging` |  `bool`   
Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead.   
`enable_spell_correction` |  `bool`   
Indicates if automatic spell correction is enabled in detect intent requests.   
`enable_multi_language_training` |  `bool`   
Optional. Enable training multi-lingual models for this agent. These models will be trained on all the languages supported by the agent.   
`locked` |  `bool`   
Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for [RestoreAgent][].   
`advanced_settings` |  `[google.cloud.dialogflowcx_v3.types.AdvancedSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AdvancedSettings)`   
Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level.   
`git_integration_settings` |  `[google.cloud.dialogflowcx_v3.types.Agent.GitIntegrationSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Agent.GitIntegrationSettings)`   
Git integration settings for this agent.   
`text_to_speech_settings` |  `[google.cloud.dialogflowcx_v3.types.TextToSpeechSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TextToSpeechSettings)`   
Settings on instructing the speech synthesizer on how to generate the output audio content.   
`gen_app_builder_settings` |  `[google.cloud.dialogflowcx_v3.types.Agent.GenAppBuilderSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Agent.GenAppBuilderSettings)`   
Gen App Builder-related agent-level settings. This field is a member of `oneof`_ `_gen_app_builder_settings`.   
`answer_feedback_settings` |  `[google.cloud.dialogflowcx_v3.types.Agent.AnswerFeedbackSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Agent.AnswerFeedbackSettings)`   
Optional. Answer feedback collection settings.   
`personalization_settings` |  `[google.cloud.dialogflowcx_v3.types.Agent.PersonalizationSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Agent.PersonalizationSettings)`   
Optional. Settings for end user personalization.   
`client_certificate_settings` |  `[google.cloud.dialogflowcx_v3.types.Agent.ClientCertificateSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Agent.ClientCertificateSettings)`   
Optional. Settings for custom client certificates.   
`satisfies_pzs` |  `bool`   
Optional. Output only. A read only boolean field reflecting Zone Separation status of the agent. This field is a member of `oneof`_ `_satisfies_pzs`.   
`satisfies_pzi` |  `bool`   
Optional. Output only. A read only boolean field reflecting Zone Isolation status of the agent. This field is a member of `oneof`_ `_satisfies_pzi`.   
  
## Classes 

### AnswerFeedbackSettings
    
    
    AnswerFeedbackSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Settings for answer feedback collection.

### ClientCertificateSettings
    
    
    ClientCertificateSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Settings for custom client certificates.

### GenAppBuilderSettings
    
    
    GenAppBuilderSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Settings for Gen App Builder.

### GitIntegrationSettings
    
    
    GitIntegrationSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Settings for connecting to Git repository for an agent.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### PersonalizationSettings
    
    
    PersonalizationSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Settings for end user personalization.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
