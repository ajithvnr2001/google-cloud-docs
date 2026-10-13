---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCard/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:14.224806+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard.

AgentCard conveys key information about an agent.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #additional_interfaces
    
    
    def additional_interfaces() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::AgentInterface>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentInterface)>) — Optional. Announcement of additional supported transports. 



### #additional_interfaces=
    
    
    def additional_interfaces=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::AgentInterface>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentInterface)>) — Optional. Announcement of additional supported transports. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentInterface)>) — Optional. Announcement of additional supported transports. 



### #capabilities
    
    
    def capabilities() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCapabilities

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCapabilities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCapabilities)) — Optional. A2A Capability set supported by the agent. 



### #capabilities=
    
    
    def capabilities=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCapabilities

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCapabilities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCapabilities)) — Optional. A2A Capability set supported by the agent. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCapabilities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCapabilities)) — Optional. A2A Capability set supported by the agent. 



### #default_input_modes
    
    
    def default_input_modes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The set of interaction modes that the agent supports across all skills. 



### #default_input_modes=
    
    
    def default_input_modes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The set of interaction modes that the agent supports across all skills. 



**Returns**

  * (::Array<::String>) — Optional. The set of interaction modes that the agent supports across all skills. 



### #default_output_modes
    
    
    def default_output_modes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The mime types supported as outputs from this agent. 



### #default_output_modes=
    
    
    def default_output_modes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The mime types supported as outputs from this agent. 



**Returns**

  * (::Array<::String>) — Optional. The mime types supported as outputs from this agent. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. A description of the agent's domain of action/solution space. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A description of the agent's domain of action/solution space. 



**Returns**

  * (::String) — Optional. A description of the agent's domain of action/solution space. 



### #documentation_url
    
    
    def documentation_url() -> ::String

**Returns**

  * (::String) — Optional. A url to provide additional documentation about the agent. 



### #documentation_url=
    
    
    def documentation_url=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A url to provide additional documentation about the agent. 



**Returns**

  * (::String) — Optional. A url to provide additional documentation about the agent. 



### #icon_url
    
    
    def icon_url() -> ::String

**Returns**

  * (::String) — Optional. An optional URL to an icon for the agent. 



### #icon_url=
    
    
    def icon_url=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional URL to an icon for the agent. 



**Returns**

  * (::String) — Optional. An optional URL to an icon for the agent. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Optional. A human readable name for the agent. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A human readable name for the agent. 



**Returns**

  * (::String) — Optional. A human readable name for the agent. 



### #preferred_transport
    
    
    def preferred_transport() -> ::String

**Returns**

  * (::String) — Optional. The transport of the preferred endpoint. If empty, defaults to JSONRPC. 



### #preferred_transport=
    
    
    def preferred_transport=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The transport of the preferred endpoint. If empty, defaults to JSONRPC. 



**Returns**

  * (::String) — Optional. The transport of the preferred endpoint. If empty, defaults to JSONRPC. 



### #protocol_version
    
    
    def protocol_version() -> ::String

**Returns**

  * (::String) — Optional. The version of the A2A protocol this agent supports. 



### #protocol_version=
    
    
    def protocol_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The version of the A2A protocol this agent supports. 



**Returns**

  * (::String) — Optional. The version of the A2A protocol this agent supports. 



### #provider
    
    
    def provider() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentProvider

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentProvider)) — Optional. The service provider of the agent. 



### #provider=
    
    
    def provider=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentProvider

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentProvider)) — Optional. The service provider of the agent. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentProvider)) — Optional. The service provider of the agent. 



### #security
    
    
    def security() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::Security>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Security](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Security)>) — Security requirements for contacting the agent. 



### #security=
    
    
    def security=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::Security>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Security](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Security)>) — Security requirements for contacting the agent. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Security](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Security)>) — Security requirements for contacting the agent. 



### #security_schemes
    
    
    def security_schemes() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::GeminiDataAnalytics::V1beta::SecurityScheme}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::GeminiDataAnalytics::V1beta::SecurityScheme}) — The security scheme details used for authenticating with this agent. 



### #security_schemes=
    
    
    def security_schemes=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::GeminiDataAnalytics::V1beta::SecurityScheme}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::GeminiDataAnalytics::V1beta::SecurityScheme}) — The security scheme details used for authenticating with this agent. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::GeminiDataAnalytics::V1beta::SecurityScheme}) — The security scheme details used for authenticating with this agent. 



### #signatures
    
    
    def signatures() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCardSignature>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCardSignature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCardSignature)>) — Optional. JSON Web Signatures computed for this AgentCard. 



### #signatures=
    
    
    def signatures=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCardSignature>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCardSignature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCardSignature)>) — Optional. JSON Web Signatures computed for this AgentCard. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCardSignature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCardSignature)>) — Optional. JSON Web Signatures computed for this AgentCard. 



### #skills
    
    
    def skills() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::AgentSkill>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentSkill](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentSkill)>) — Optional. Skills represent a unit of ability an agent can perform. 



### #skills=
    
    
    def skills=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::AgentSkill>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentSkill](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentSkill)>) — Optional. Skills represent a unit of ability an agent can perform. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::AgentSkill](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentSkill)>) — Optional. Skills represent a unit of ability an agent can perform. 



### #supports_authenticated_extended_card
    
    
    def supports_authenticated_extended_card() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether the agent supports providing an extended agent card when the user is authenticated. 



### #supports_authenticated_extended_card=
    
    
    def supports_authenticated_extended_card=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether the agent supports providing an extended agent card when the user is authenticated. 



**Returns**

  * (::Boolean) — Optional. Whether the agent supports providing an extended agent card when the user is authenticated. 



### #url
    
    
    def url() -> ::String

**Returns**

  * (::String) — Optional. A URL to the address the agent is hosted at. 



### #url=
    
    
    def url=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A URL to the address the agent is hosted at. 



**Returns**

  * (::String) — Optional. A URL to the address the agent is hosted at. 



### #version
    
    
    def version() -> ::String

**Returns**

  * (::String) — Optional. The version of the agent. 



### #version=
    
    
    def version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The version of the agent. 



**Returns**

  * (::String) — Optional. The version of the agent. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
