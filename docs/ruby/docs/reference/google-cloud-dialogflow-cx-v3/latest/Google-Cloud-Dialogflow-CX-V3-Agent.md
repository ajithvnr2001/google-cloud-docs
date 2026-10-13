---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Agent (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:53.221637+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Agent (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Agent (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Agent.

Agents are best described as Natural Language Understanding (NLU) modules that transform user requests into actionable data. You can include agents in your app, product, or service to determine user intent and respond to the user in a natural way.

After you create an agent, you can add [Intents](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Intent "Google::Cloud::Dialogflow::CX::V3::Intent \(class\)"), [Entity Types][google.cloud.dialogflow.cx.v3.EntityType], [Flows](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow "Google::Cloud::Dialogflow::CX::V3::Flow \(class\)"), [Fulfillments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment "Google::Cloud::Dialogflow::CX::V3::Fulfillment \(class\)"), [Webhooks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Webhook "Google::Cloud::Dialogflow::CX::V3::Webhook \(class\)"), [TransitionRouteGroups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TransitionRouteGroup "Google::Cloud::Dialogflow::CX::V3::TransitionRouteGroup \(class\)") and so on to manage the conversation flows.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #advanced_settings
    
    
    def advanced_settings() -> ::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings)) — Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level. 



### #advanced_settings=
    
    
    def advanced_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings)) — Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings)) — Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level. 



### #answer_feedback_settings
    
    
    def answer_feedback_settings() -> ::Google::Cloud::Dialogflow::CX::V3::Agent::AnswerFeedbackSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::AnswerFeedbackSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-AnswerFeedbackSettings)) — Optional. Answer feedback collection settings. 



### #answer_feedback_settings=
    
    
    def answer_feedback_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::Agent::AnswerFeedbackSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::Agent::AnswerFeedbackSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-AnswerFeedbackSettings)) — Optional. Answer feedback collection settings. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::AnswerFeedbackSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-AnswerFeedbackSettings)) — Optional. Answer feedback collection settings. 



### #avatar_uri
    
    
    def avatar_uri() -> ::String

**Returns**

  * (::String) — The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. 



### #avatar_uri=
    
    
    def avatar_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. 



**Returns**

  * (::String) — The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. 



### #client_certificate_settings
    
    
    def client_certificate_settings() -> ::Google::Cloud::Dialogflow::CX::V3::Agent::ClientCertificateSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::ClientCertificateSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-ClientCertificateSettings)) — Optional. Settings for custom client certificates. 



### #client_certificate_settings=
    
    
    def client_certificate_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::Agent::ClientCertificateSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::Agent::ClientCertificateSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-ClientCertificateSettings)) — Optional. Settings for custom client certificates. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::ClientCertificateSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-ClientCertificateSettings)) — Optional. Settings for custom client certificates. 



### #default_language_code
    
    
    def default_language_code() -> ::String

**Returns**

  * (::String) — Required. Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the [Agents.UpdateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_update_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#update_agent \(method\)") method. 



### #default_language_code=
    
    
    def default_language_code=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the [Agents.UpdateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_update_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#update_agent \(method\)") method. 



**Returns**

  * (::String) — Required. Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the [Agents.UpdateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_update_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#update_agent \(method\)") method. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected. 



**Returns**

  * (::String) — The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. The human-readable name of the agent, unique within the location. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The human-readable name of the agent, unique within the location. 



**Returns**

  * (::String) — Required. The human-readable name of the agent, unique within the location. 



### #enable_multi_language_training
    
    
    def enable_multi_language_training() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Enable training multi-lingual models for this agent. These models will be trained on all the languages supported by the agent. 



### #enable_multi_language_training=
    
    
    def enable_multi_language_training=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Enable training multi-lingual models for this agent. These models will be trained on all the languages supported by the agent. 



**Returns**

  * (::Boolean) — Optional. Enable training multi-lingual models for this agent. These models will be trained on all the languages supported by the agent. 



### #enable_spell_correction
    
    
    def enable_spell_correction() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates if automatic spell correction is enabled in detect intent requests. 



### #enable_spell_correction=
    
    
    def enable_spell_correction=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates if automatic spell correction is enabled in detect intent requests. 



**Returns**

  * (::Boolean) — Indicates if automatic spell correction is enabled in detect intent requests. 



### #enable_stackdriver_logging
    
    
    def enable_stackdriver_logging() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates if stackdriver logging is enabled for the agent. Please use [agent.advanced_settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings-LoggingSettings "Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::LoggingSettings \(class\)") instead. 



### #enable_stackdriver_logging=
    
    
    def enable_stackdriver_logging=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates if stackdriver logging is enabled for the agent. Please use [agent.advanced_settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings-LoggingSettings "Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::LoggingSettings \(class\)") instead. 



**Returns**

  * (::Boolean) — Indicates if stackdriver logging is enabled for the agent. Please use [agent.advanced_settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings-LoggingSettings "Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::LoggingSettings \(class\)") instead. 



### #gen_app_builder_settings
    
    
    def gen_app_builder_settings() -> ::Google::Cloud::Dialogflow::CX::V3::Agent::GenAppBuilderSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::GenAppBuilderSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-GenAppBuilderSettings)) — Gen App Builder-related agent-level settings. 



### #gen_app_builder_settings=
    
    
    def gen_app_builder_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::Agent::GenAppBuilderSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::Agent::GenAppBuilderSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-GenAppBuilderSettings)) — Gen App Builder-related agent-level settings. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::GenAppBuilderSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-GenAppBuilderSettings)) — Gen App Builder-related agent-level settings. 



### #git_integration_settings
    
    
    def git_integration_settings() -> ::Google::Cloud::Dialogflow::CX::V3::Agent::GitIntegrationSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::GitIntegrationSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-GitIntegrationSettings)) — Git integration settings for this agent. 



### #git_integration_settings=
    
    
    def git_integration_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::Agent::GitIntegrationSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::Agent::GitIntegrationSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-GitIntegrationSettings)) — Git integration settings for this agent. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::GitIntegrationSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-GitIntegrationSettings)) — Git integration settings for this agent. 



### #locked
    
    
    def locked() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for [RestoreAgent][]. 



### #locked=
    
    
    def locked=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for [RestoreAgent][]. 



**Returns**

  * (::Boolean) — Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for [RestoreAgent][]. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The unique identifier of the agent. Required for the [Agents.UpdateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_update_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#update_agent \(method\)") method. [Agents.CreateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_create_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#create_agent \(method\)") populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The unique identifier of the agent. Required for the [Agents.UpdateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_update_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#update_agent \(method\)") method. [Agents.CreateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_create_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#create_agent \(method\)") populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



**Returns**

  * (::String) — The unique identifier of the agent. Required for the [Agents.UpdateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_update_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#update_agent \(method\)") method. [Agents.CreateAgent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_create_agent_instance_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client#create_agent \(method\)") populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



### #personalization_settings
    
    
    def personalization_settings() -> ::Google::Cloud::Dialogflow::CX::V3::Agent::PersonalizationSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::PersonalizationSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-PersonalizationSettings)) — Optional. Settings for end user personalization. 



### #personalization_settings=
    
    
    def personalization_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::Agent::PersonalizationSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::Agent::PersonalizationSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-PersonalizationSettings)) — Optional. Settings for end user personalization. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent::PersonalizationSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent-PersonalizationSettings)) — Optional. Settings for end user personalization. 



### #satisfies_pzi
    
    
    def satisfies_pzi() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Output only. A read only boolean field reflecting Zone Isolation status of the agent. 



### #satisfies_pzs
    
    
    def satisfies_pzs() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Output only. A read only boolean field reflecting Zone Separation status of the agent. 



### #security_settings
    
    
    def security_settings() -> ::String

**Returns**

  * (::String) — Name of the [SecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SecuritySettings "Google::Cloud::Dialogflow::CX::V3::SecuritySettings \(class\)") reference for the agent. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<SecuritySettingsID>`. 



### #security_settings=
    
    
    def security_settings=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the [SecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SecuritySettings "Google::Cloud::Dialogflow::CX::V3::SecuritySettings \(class\)") reference for the agent. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<SecuritySettingsID>`. 



**Returns**

  * (::String) — Name of the [SecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SecuritySettings "Google::Cloud::Dialogflow::CX::V3::SecuritySettings \(class\)") reference for the agent. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<SecuritySettingsID>`. 



### #speech_to_text_settings
    
    
    def speech_to_text_settings() -> ::Google::Cloud::Dialogflow::CX::V3::SpeechToTextSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SpeechToTextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SpeechToTextSettings)) — Speech recognition related settings. 



### #speech_to_text_settings=
    
    
    def speech_to_text_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::SpeechToTextSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::SpeechToTextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SpeechToTextSettings)) — Speech recognition related settings. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SpeechToTextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SpeechToTextSettings)) — Speech recognition related settings. 



### #start_flow
    
    
    def start_flow() -> ::String

**Returns**

  * (::String) — Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. Currently only the default start flow with id "00000000-0000-0000-0000-000000000000" is allowed.

Note: The following fields are mutually exclusive: `start_flow`, `start_playbook`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #start_flow=
    
    
    def start_flow=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. Currently only the default start flow with id "00000000-0000-0000-0000-000000000000" is allowed.

Note: The following fields are mutually exclusive: `start_flow`, `start_playbook`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. Currently only the default start flow with id "00000000-0000-0000-0000-000000000000" is allowed.

Note: The following fields are mutually exclusive: `start_flow`, `start_playbook`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #start_playbook
    
    
    def start_playbook() -> ::String

**Returns**

  * (::String) — Name of the start playbook in this agent. A start playbook will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`. Currently only the default playbook with id "00000000-0000-0000-0000-000000000000" is allowed.

Note: The following fields are mutually exclusive: `start_playbook`, `start_flow`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #start_playbook=
    
    
    def start_playbook=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the start playbook in this agent. A start playbook will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`. Currently only the default playbook with id "00000000-0000-0000-0000-000000000000" is allowed.

Note: The following fields are mutually exclusive: `start_playbook`, `start_flow`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Name of the start playbook in this agent. A start playbook will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`. Currently only the default playbook with id "00000000-0000-0000-0000-000000000000" is allowed.

Note: The following fields are mutually exclusive: `start_playbook`, `start_flow`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #supported_language_codes
    
    
    def supported_language_codes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The list of all languages supported by the agent (except for the `default_language_code`). 



### #supported_language_codes=
    
    
    def supported_language_codes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The list of all languages supported by the agent (except for the `default_language_code`). 



**Returns**

  * (::Array<::String>) — The list of all languages supported by the agent (except for the `default_language_code`). 



### #text_to_speech_settings
    
    
    def text_to_speech_settings() -> ::Google::Cloud::Dialogflow::CX::V3::TextToSpeechSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::TextToSpeechSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TextToSpeechSettings)) — Settings on instructing the speech synthesizer on how to generate the output audio content. 



### #text_to_speech_settings=
    
    
    def text_to_speech_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::TextToSpeechSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::TextToSpeechSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TextToSpeechSettings)) — Settings on instructing the speech synthesizer on how to generate the output audio content. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::TextToSpeechSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TextToSpeechSettings)) — Settings on instructing the speech synthesizer on how to generate the output audio content. 



### #time_zone
    
    
    def time_zone() -> ::String

**Returns**

  * (::String) — Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. 



### #time_zone=
    
    
    def time_zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. 



**Returns**

  * (::String) — Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
