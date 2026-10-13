---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App/
title: Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::App (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:39.095451+00:00
---

# Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::App (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::App (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1 API class Google::Cloud::Ces::V1::App.

An app serves as a top-level container for a group of agents, including the root agent and its sub-agents, along with their associated configurations. These agents work together to achieve specific goals within the app's context.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #audio_processing_config
    
    
    def audio_processing_config() -> ::Google::Cloud::Ces::V1::AudioProcessingConfig

**Returns**

  * ([::Google::Cloud::Ces::V1::AudioProcessingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-AudioProcessingConfig)) — Optional. Audio processing configuration of the app. 



### #audio_processing_config=
    
    
    def audio_processing_config=(value) -> ::Google::Cloud::Ces::V1::AudioProcessingConfig

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::AudioProcessingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-AudioProcessingConfig)) — Optional. Audio processing configuration of the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::AudioProcessingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-AudioProcessingConfig)) — Optional. Audio processing configuration of the app. 



### #client_certificate_settings
    
    
    def client_certificate_settings() -> ::Google::Cloud::Ces::V1::ClientCertificateSettings

**Returns**

  * ([::Google::Cloud::Ces::V1::ClientCertificateSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ClientCertificateSettings)) — Optional. The default client certificate settings for the app. 



### #client_certificate_settings=
    
    
    def client_certificate_settings=(value) -> ::Google::Cloud::Ces::V1::ClientCertificateSettings

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::ClientCertificateSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ClientCertificateSettings)) — Optional. The default client certificate settings for the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::ClientCertificateSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ClientCertificateSettings)) — Optional. The default client certificate settings for the app. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the app was created. 



### #data_store_settings
    
    
    def data_store_settings() -> ::Google::Cloud::Ces::V1::DataStoreSettings

**Returns**

  * ([::Google::Cloud::Ces::V1::DataStoreSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-DataStoreSettings)) — Optional. The data store settings for the app. 



### #data_store_settings=
    
    
    def data_store_settings=(value) -> ::Google::Cloud::Ces::V1::DataStoreSettings

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::DataStoreSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-DataStoreSettings)) — Optional. The data store settings for the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::DataStoreSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-DataStoreSettings)) — Optional. The data store settings for the app. 



### #default_channel_profile
    
    
    def default_channel_profile() -> ::Google::Cloud::Ces::V1::ChannelProfile

**Returns**

  * ([::Google::Cloud::Ces::V1::ChannelProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ChannelProfile)) — Optional. The default channel profile used by the app. 



### #default_channel_profile=
    
    
    def default_channel_profile=(value) -> ::Google::Cloud::Ces::V1::ChannelProfile

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::ChannelProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ChannelProfile)) — Optional. The default channel profile used by the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::ChannelProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ChannelProfile)) — Optional. The default channel profile used by the app. 



### #deployment_count
    
    
    def deployment_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of deployments in the app. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Human-readable description of the app. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Human-readable description of the app. 



**Returns**

  * (::String) — Optional. Human-readable description of the app. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. Display name of the app. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Display name of the app. 



**Returns**

  * (::String) — Required. Display name of the app. 



### #error_handling_settings
    
    
    def error_handling_settings() -> ::Google::Cloud::Ces::V1::ErrorHandlingSettings

**Returns**

  * ([::Google::Cloud::Ces::V1::ErrorHandlingSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ErrorHandlingSettings)) — Optional. Error handling settings of the app. 



### #error_handling_settings=
    
    
    def error_handling_settings=(value) -> ::Google::Cloud::Ces::V1::ErrorHandlingSettings

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::ErrorHandlingSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ErrorHandlingSettings)) — Optional. Error handling settings of the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::ErrorHandlingSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ErrorHandlingSettings)) — Optional. Error handling settings of the app. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes. 



### #evaluation_metrics_thresholds
    
    
    def evaluation_metrics_thresholds() -> ::Google::Cloud::Ces::V1::EvaluationMetricsThresholds

**Returns**

  * ([::Google::Cloud::Ces::V1::EvaluationMetricsThresholds](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EvaluationMetricsThresholds)) — Optional. The evaluation thresholds for the app. 



### #evaluation_metrics_thresholds=
    
    
    def evaluation_metrics_thresholds=(value) -> ::Google::Cloud::Ces::V1::EvaluationMetricsThresholds

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::EvaluationMetricsThresholds](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EvaluationMetricsThresholds)) — Optional. The evaluation thresholds for the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::EvaluationMetricsThresholds](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-EvaluationMetricsThresholds)) — Optional. The evaluation thresholds for the app. 



### #global_instruction
    
    
    def global_instruction() -> ::String

**Returns**

  * (::String) — Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents. 



### #global_instruction=
    
    
    def global_instruction=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents. 



**Returns**

  * (::String) — Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents. 



### #guardrails
    
    
    def guardrails() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`



### #guardrails=
    
    
    def guardrails=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`



**Returns**

  * (::Array<::String>) — Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`



### #language_settings
    
    
    def language_settings() -> ::Google::Cloud::Ces::V1::LanguageSettings

**Returns**

  * ([::Google::Cloud::Ces::V1::LanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-LanguageSettings)) — Optional. Language settings of the app. 



### #language_settings=
    
    
    def language_settings=(value) -> ::Google::Cloud::Ces::V1::LanguageSettings

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::LanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-LanguageSettings)) — Optional. Language settings of the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::LanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-LanguageSettings)) — Optional. Language settings of the app. 



### #locked
    
    
    def locked() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected. 



### #locked=
    
    
    def locked=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected. 



**Returns**

  * (::Boolean) — Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected. 



### #logging_settings
    
    
    def logging_settings() -> ::Google::Cloud::Ces::V1::LoggingSettings

**Returns**

  * ([::Google::Cloud::Ces::V1::LoggingSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-LoggingSettings)) — Optional. Logging settings of the app. 



### #logging_settings=
    
    
    def logging_settings=(value) -> ::Google::Cloud::Ces::V1::LoggingSettings

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::LoggingSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-LoggingSettings)) — Optional. Logging settings of the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::LoggingSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-LoggingSettings)) — Optional. Logging settings of the app. 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages. 



### #model_settings
    
    
    def model_settings() -> ::Google::Cloud::Ces::V1::ModelSettings

**Returns**

  * ([::Google::Cloud::Ces::V1::ModelSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ModelSettings)) — Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed. 



### #model_settings=
    
    
    def model_settings=(value) -> ::Google::Cloud::Ces::V1::ModelSettings

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::ModelSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ModelSettings)) — Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed. 



**Returns**

  * ([::Google::Cloud::Ces::V1::ModelSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ModelSettings)) — Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The unique identifier of the app. Format: `projects/{project}/locations/{location}/apps/{app}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The unique identifier of the app. Format: `projects/{project}/locations/{location}/apps/{app}`



**Returns**

  * (::String) — Identifier. The unique identifier of the app. Format: `projects/{project}/locations/{location}/apps/{app}`



### #pinned
    
    
    def pinned() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether the app is pinned in the app list. 



### #pinned=
    
    
    def pinned=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether the app is pinned in the app list. 



**Returns**

  * (::Boolean) — Optional. Whether the app is pinned in the app list. 



### #predefined_variable_declarations
    
    
    def predefined_variable_declarations() -> ::Array<::Google::Cloud::Ces::V1::App::VariableDeclaration>

**Returns**

  * (::Array<[::Google::Cloud::Ces::V1::App::VariableDeclaration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App-VariableDeclaration)>) — Output only. The declarations of predefined variables for the app. 



### #root_agent
    
    
    def root_agent() -> ::String

**Returns**

  * (::String) — Optional. The root agent is the entry point of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`



### #root_agent=
    
    
    def root_agent=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The root agent is the entry point of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`



**Returns**

  * (::String) — Optional. The root agent is the entry point of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`



### #time_zone_settings
    
    
    def time_zone_settings() -> ::Google::Cloud::Ces::V1::TimeZoneSettings

**Returns**

  * ([::Google::Cloud::Ces::V1::TimeZoneSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TimeZoneSettings)) — Optional. TimeZone settings of the app. 



### #time_zone_settings=
    
    
    def time_zone_settings=(value) -> ::Google::Cloud::Ces::V1::TimeZoneSettings

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::TimeZoneSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TimeZoneSettings)) — Optional. TimeZone settings of the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::TimeZoneSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TimeZoneSettings)) — Optional. TimeZone settings of the app. 



### #tool_execution_mode
    
    
    def tool_execution_mode() -> ::Google::Cloud::Ces::V1::App::ToolExecutionMode

**Returns**

  * ([::Google::Cloud::Ces::V1::App::ToolExecutionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App-ToolExecutionMode)) — Optional. The tool execution mode for the app. If not provided, will default to PARALLEL. 



### #tool_execution_mode=
    
    
    def tool_execution_mode=(value) -> ::Google::Cloud::Ces::V1::App::ToolExecutionMode

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::App::ToolExecutionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App-ToolExecutionMode)) — Optional. The tool execution mode for the app. If not provided, will default to PARALLEL. 



**Returns**

  * ([::Google::Cloud::Ces::V1::App::ToolExecutionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App-ToolExecutionMode)) — Optional. The tool execution mode for the app. If not provided, will default to PARALLEL. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the app was last updated. 



### #validation_errors
    
    
    def validation_errors() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. Misconfigurations or warnings in the app. 



### #variable_declarations
    
    
    def variable_declarations() -> ::Array<::Google::Cloud::Ces::V1::App::VariableDeclaration>

**Returns**

  * (::Array<[::Google::Cloud::Ces::V1::App::VariableDeclaration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App-VariableDeclaration)>) — Optional. The declarations of the variables. 



### #variable_declarations=
    
    
    def variable_declarations=(value) -> ::Array<::Google::Cloud::Ces::V1::App::VariableDeclaration>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Ces::V1::App::VariableDeclaration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App-VariableDeclaration)>) — Optional. The declarations of the variables. 



**Returns**

  * (::Array<[::Google::Cloud::Ces::V1::App::VariableDeclaration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-App-VariableDeclaration)>) — Optional. The declarations of the variables. 



### #vpc_sc_settings
    
    
    def vpc_sc_settings() -> ::Google::Cloud::Ces::V1::VpcScSettings

**Returns**

  * ([::Google::Cloud::Ces::V1::VpcScSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-VpcScSettings)) — Optional. VPC-SC settings for the app. 



### #vpc_sc_settings=
    
    
    def vpc_sc_settings=(value) -> ::Google::Cloud::Ces::V1::VpcScSettings

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::VpcScSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-VpcScSettings)) — Optional. VPC-SC settings for the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1::VpcScSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-VpcScSettings)) — Optional. VPC-SC settings for the app. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
