---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryParameters/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::QueryParameters (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:34.046983+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::QueryParameters (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryParameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::QueryParameters (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::QueryParameters.

Represents the parameters of a conversational query.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #analyze_query_text_sentiment
    
    
    def analyze_query_text_sentiment() -> ::Boolean

**Returns**

  * (::Boolean) — Configures whether sentiment analysis should be performed. If not provided, sentiment analysis is not performed. 



### #analyze_query_text_sentiment=
    
    
    def analyze_query_text_sentiment=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Configures whether sentiment analysis should be performed. If not provided, sentiment analysis is not performed. 



**Returns**

  * (::Boolean) — Configures whether sentiment analysis should be performed. If not provided, sentiment analysis is not performed. 



### #channel
    
    
    def channel() -> ::String

**Returns**

  * (::String) — The channel which this query is for.

If specified, only the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") associated with the channel will be returned. If no [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") is associated with the channel, it falls back to the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") with unspecified channel.

If unspecified, the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") with unspecified channel will be returned. 




### #channel=
    
    
    def channel=(value) -> ::String

**Parameter**

  * **value** (::String) — The channel which this query is for.

If specified, only the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") associated with the channel will be returned. If no [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") is associated with the channel, it falls back to the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") with unspecified channel.

If unspecified, the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") with unspecified channel will be returned. 




**Returns**

  * (::String) — The channel which this query is for.

If specified, only the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") associated with the channel will be returned. If no [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") is associated with the channel, it falls back to the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") with unspecified channel.

If unspecified, the [ResponseMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ResponseMessage "Google::Cloud::Dialogflow::CX::V3::ResponseMessage \(class\)") with unspecified channel will be returned. 




### #current_page
    
    
    def current_page() -> ::String

**Returns**

  * (::String) — The unique identifier of the [page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Page "Google::Cloud::Dialogflow::CX::V3::Page \(class\)") to override the [current page][QueryResult.current_page] in the session. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

If `current_page` is specified, the previous state of the session will be ignored by Dialogflow, including the [previous page][QueryResult.current_page] and the [previous session parameters][QueryResult.parameters]. In most cases, [current_page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryParameters#Google__Cloud__Dialogflow__CX__V3__QueryParameters_current_page_instance_ "Google::Cloud::Dialogflow::CX::V3::QueryParameters#current_page \(method\)") and [parameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryParameters#Google__Cloud__Dialogflow__CX__V3__QueryParameters_parameters_instance_ "Google::Cloud::Dialogflow::CX::V3::QueryParameters#parameters \(method\)") should be configured together to direct a session to a specific state. 




### #current_page=
    
    
    def current_page=(value) -> ::String

**Parameter**

  * **value** (::String) — The unique identifier of the [page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Page "Google::Cloud::Dialogflow::CX::V3::Page \(class\)") to override the [current page][QueryResult.current_page] in the session. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

If `current_page` is specified, the previous state of the session will be ignored by Dialogflow, including the [previous page][QueryResult.current_page] and the [previous session parameters][QueryResult.parameters]. In most cases, [current_page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryParameters#Google__Cloud__Dialogflow__CX__V3__QueryParameters_current_page_instance_ "Google::Cloud::Dialogflow::CX::V3::QueryParameters#current_page \(method\)") and [parameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryParameters#Google__Cloud__Dialogflow__CX__V3__QueryParameters_parameters_instance_ "Google::Cloud::Dialogflow::CX::V3::QueryParameters#parameters \(method\)") should be configured together to direct a session to a specific state. 




**Returns**

  * (::String) — The unique identifier of the [page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Page "Google::Cloud::Dialogflow::CX::V3::Page \(class\)") to override the [current page][QueryResult.current_page] in the session. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

If `current_page` is specified, the previous state of the session will be ignored by Dialogflow, including the [previous page][QueryResult.current_page] and the [previous session parameters][QueryResult.parameters]. In most cases, [current_page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryParameters#Google__Cloud__Dialogflow__CX__V3__QueryParameters_current_page_instance_ "Google::Cloud::Dialogflow::CX::V3::QueryParameters#current_page \(method\)") and [parameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryParameters#Google__Cloud__Dialogflow__CX__V3__QueryParameters_parameters_instance_ "Google::Cloud::Dialogflow::CX::V3::QueryParameters#parameters \(method\)") should be configured together to direct a session to a specific state. 




### #current_playbook
    
    
    def current_playbook() -> ::String

**Returns**

  * (::String) — Optional. The unique identifier of the [playbook](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Playbook "Google::Cloud::Dialogflow::CX::V3::Playbook \(class\)") to start or continue the session with. If `current_playbook` is specified, the previous state of the session will be ignored by Dialogflow.

Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`. 




### #current_playbook=
    
    
    def current_playbook=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The unique identifier of the [playbook](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Playbook "Google::Cloud::Dialogflow::CX::V3::Playbook \(class\)") to start or continue the session with. If `current_playbook` is specified, the previous state of the session will be ignored by Dialogflow.

Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`. 




**Returns**

  * (::String) — Optional. The unique identifier of the [playbook](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Playbook "Google::Cloud::Dialogflow::CX::V3::Playbook \(class\)") to start or continue the session with. If `current_playbook` is specified, the previous state of the session will be ignored by Dialogflow.

Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`. 




### #disable_webhook
    
    
    def disable_webhook() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to disable webhook calls for this request. 



### #disable_webhook=
    
    
    def disable_webhook=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to disable webhook calls for this request. 



**Returns**

  * (::Boolean) — Whether to disable webhook calls for this request. 



### #end_user_metadata
    
    
    def end_user_metadata() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. Information about the end-user to improve the relevance and accuracy of generative answers.

This will be interpreted and used by a language model, so, for good results, the data should be self-descriptive, and in a simple structure.

Example:

`json { "subscription plan": "Business Premium Plus", "devices owned": [ \\{"model": "Google Pixel 7"}, \\{"model": "Google Pixel Tablet"} ] } `




### #end_user_metadata=
    
    
    def end_user_metadata=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. Information about the end-user to improve the relevance and accuracy of generative answers.

This will be interpreted and used by a language model, so, for good results, the data should be self-descriptive, and in a simple structure.

Example:

`json { "subscription plan": "Business Premium Plus", "devices owned": [ \\{"model": "Google Pixel 7"}, \\{"model": "Google Pixel Tablet"} ] } `




**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — Optional. Information about the end-user to improve the relevance and accuracy of generative answers.

This will be interpreted and used by a language model, so, for good results, the data should be self-descriptive, and in a simple structure.

Example:

`json { "subscription plan": "Business Premium Plus", "devices owned": [ \\{"model": "Google Pixel 7"}, \\{"model": "Google Pixel Tablet"} ] } `




### #flow_versions
    
    
    def flow_versions() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of flow versions to override for the request. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>`.

If version 1 of flow X is included in this list, the traffic of flow X will go through version 1 regardless of the version configuration in the environment. Each flow can have at most one version specified in this list. 




### #flow_versions=
    
    
    def flow_versions=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of flow versions to override for the request. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>`.

If version 1 of flow X is included in this list, the traffic of flow X will go through version 1 regardless of the version configuration in the environment. Each flow can have at most one version specified in this list. 




**Returns**

  * (::Array<::String>) — A list of flow versions to override for the request. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>`.

If version 1 of flow X is included in this list, the traffic of flow X will go through version 1 regardless of the version configuration in the environment. Each flow can have at most one version specified in this list. 




### #geo_location
    
    
    def geo_location() -> ::Google::Type::LatLng

**Returns**

  * ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Type-LatLng)) — The geo location of this conversational query. 



### #geo_location=
    
    
    def geo_location=(value) -> ::Google::Type::LatLng

**Parameter**

  * **value** ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Type-LatLng)) — The geo location of this conversational query. 



**Returns**

  * ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Type-LatLng)) — The geo location of this conversational query. 



### #llm_model_settings
    
    
    def llm_model_settings() -> ::Google::Cloud::Dialogflow::CX::V3::LlmModelSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::LlmModelSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-LlmModelSettings)) — Optional. Use the specified LLM model settings for processing the request. 



### #llm_model_settings=
    
    
    def llm_model_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::LlmModelSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::LlmModelSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-LlmModelSettings)) — Optional. Use the specified LLM model settings for processing the request. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::LlmModelSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-LlmModelSettings)) — Optional. Use the specified LLM model settings for processing the request. 



### #parameter_scope
    
    
    def parameter_scope() -> ::String

**Returns**

  * (::String) — Scope for the parameters. If not specified, parameters will be treated as session parameters. Parameters with custom scope will not be put into [session parameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SessionInfo#Google__Cloud__Dialogflow__CX__V3__SessionInfo_parameters_instance_ "Google::Cloud::Dialogflow::CX::V3::SessionInfo#parameters \(method\)").

You can reference the parameters with custom scope in the agent with the following format: $parameter-scope.params.parameter-id. 




### #parameter_scope=
    
    
    def parameter_scope=(value) -> ::String

**Parameter**

  * **value** (::String) — Scope for the parameters. If not specified, parameters will be treated as session parameters. Parameters with custom scope will not be put into [session parameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SessionInfo#Google__Cloud__Dialogflow__CX__V3__SessionInfo_parameters_instance_ "Google::Cloud::Dialogflow::CX::V3::SessionInfo#parameters \(method\)").

You can reference the parameters with custom scope in the agent with the following format: $parameter-scope.params.parameter-id. 




**Returns**

  * (::String) — Scope for the parameters. If not specified, parameters will be treated as session parameters. Parameters with custom scope will not be put into [session parameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SessionInfo#Google__Cloud__Dialogflow__CX__V3__SessionInfo_parameters_instance_ "Google::Cloud::Dialogflow::CX::V3::SessionInfo#parameters \(method\)").

You can reference the parameters with custom scope in the agent with the following format: $parameter-scope.params.parameter-id. 




### #parameters
    
    
    def parameters() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — 

Additional parameters to be put into [session parameters][SessionInfo.parameters]. To remove a parameter from the session, clients should explicitly set the parameter value to null.

You can reference the session parameters in the agent with the following format: $session.params.parameter-id.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

    * MapKey type: string
    * MapKey value: parameter name
    * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
    * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



### #parameters=
    
    
    def parameters=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — 

Additional parameters to be put into [session parameters][SessionInfo.parameters]. To remove a parameter from the session, clients should explicitly set the parameter value to null.

You can reference the session parameters in the agent with the following format: $session.params.parameter-id.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

    * MapKey type: string
    * MapKey value: parameter name
    * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
    * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — 

Additional parameters to be put into [session parameters][SessionInfo.parameters]. To remove a parameter from the session, clients should explicitly set the parameter value to null.

You can reference the session parameters in the agent with the following format: $session.params.parameter-id.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

    * MapKey type: string
    * MapKey value: parameter name
    * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
    * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



### #payload
    
    
    def payload() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — This field can be used to pass custom data into the webhook associated with the agent. Arbitrary JSON objects are supported. Some integrations that query a Dialogflow agent may provide additional information in the payload. In particular, for the Dialogflow Phone Gateway integration, this field has the form: ` { "telephony": { "caller_id": "+18558363987" } } `



### #payload=
    
    
    def payload=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — This field can be used to pass custom data into the webhook associated with the agent. Arbitrary JSON objects are supported. Some integrations that query a Dialogflow agent may provide additional information in the payload. In particular, for the Dialogflow Phone Gateway integration, this field has the form: ` { "telephony": { "caller_id": "+18558363987" } } `



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Struct)) — This field can be used to pass custom data into the webhook associated with the agent. Arbitrary JSON objects are supported. Some integrations that query a Dialogflow agent may provide additional information in the payload. In particular, for the Dialogflow Phone Gateway integration, this field has the form: ` { "telephony": { "caller_id": "+18558363987" } } `



### #populate_data_store_connection_signals
    
    
    def populate_data_store_connection_signals() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true and data stores are involved in serving the request then DetectIntentResponse.query_result.data_store_connection_signals will be filled with data that can help evaluations. 



### #populate_data_store_connection_signals=
    
    
    def populate_data_store_connection_signals=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true and data stores are involved in serving the request then DetectIntentResponse.query_result.data_store_connection_signals will be filled with data that can help evaluations. 



**Returns**

  * (::Boolean) — Optional. If set to true and data stores are involved in serving the request then DetectIntentResponse.query_result.data_store_connection_signals will be filled with data that can help evaluations. 



### #search_config
    
    
    def search_config() -> ::Google::Cloud::Dialogflow::CX::V3::SearchConfig

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SearchConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SearchConfig)) — Optional. Search configuration for UCS search queries. 



### #search_config=
    
    
    def search_config=(value) -> ::Google::Cloud::Dialogflow::CX::V3::SearchConfig

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::SearchConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SearchConfig)) — Optional. Search configuration for UCS search queries. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::SearchConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SearchConfig)) — Optional. Search configuration for UCS search queries. 



### #session_entity_types
    
    
    def session_entity_types() -> ::Array<::Google::Cloud::Dialogflow::CX::V3::SessionEntityType>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::SessionEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SessionEntityType)>) — Additional session entity types to replace or extend developer entity types with. The entity synonyms apply to all languages and persist for the session of this query. 



### #session_entity_types=
    
    
    def session_entity_types=(value) -> ::Array<::Google::Cloud::Dialogflow::CX::V3::SessionEntityType>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::CX::V3::SessionEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SessionEntityType)>) — Additional session entity types to replace or extend developer entity types with. The entity synonyms apply to all languages and persist for the session of this query. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::SessionEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-SessionEntityType)>) — Additional session entity types to replace or extend developer entity types with. The entity synonyms apply to all languages and persist for the session of this query. 



### #session_ttl
    
    
    def session_ttl() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Optional. Configure lifetime of the Dialogflow session. By default, a Dialogflow session remains active and its data is stored for 30 minutes after the last request is sent for the session. This value should be no longer than 1 day. 



### #session_ttl=
    
    
    def session_ttl=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Optional. Configure lifetime of the Dialogflow session. By default, a Dialogflow session remains active and its data is stored for 30 minutes after the last request is sent for the session. This value should be no longer than 1 day. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Optional. Configure lifetime of the Dialogflow session. By default, a Dialogflow session remains active and its data is stored for 30 minutes after the last request is sent for the session. This value should be no longer than 1 day. 



### #time_zone
    
    
    def time_zone() -> ::String

**Returns**

  * (::String) — The time zone of this conversational query from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. If not provided, the time zone specified in the agent is used. 



### #time_zone=
    
    
    def time_zone=(value) -> ::String

**Parameter**

  * **value** (::String) — The time zone of this conversational query from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. If not provided, the time zone specified in the agent is used. 



**Returns**

  * (::String) — The time zone of this conversational query from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. If not provided, the time zone specified in the agent is used. 



### #webhook_headers
    
    
    def webhook_headers() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — This field can be used to pass HTTP headers for a webhook call. These headers will be sent to webhook along with the headers that have been configured through Dialogflow web console. The headers defined within this field will overwrite the headers configured through Dialogflow console if there is a conflict. Header names are case-insensitive. Google's specified headers are not allowed. Including: "Host", "Content-Length", "Connection", "From", "User-Agent", "Accept-Encoding", "If-Modified-Since", "If-None-Match", "X-Forwarded-For", etc. 



### #webhook_headers=
    
    
    def webhook_headers=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — This field can be used to pass HTTP headers for a webhook call. These headers will be sent to webhook along with the headers that have been configured through Dialogflow web console. The headers defined within this field will overwrite the headers configured through Dialogflow console if there is a conflict. Header names are case-insensitive. Google's specified headers are not allowed. Including: "Host", "Content-Length", "Connection", "From", "User-Agent", "Accept-Encoding", "If-Modified-Since", "If-None-Match", "X-Forwarded-For", etc. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — This field can be used to pass HTTP headers for a webhook call. These headers will be sent to webhook along with the headers that have been configured through Dialogflow web console. The headers defined within this field will overwrite the headers configured through Dialogflow console if there is a conflict. Header names are case-insensitive. Google's specified headers are not allowed. Including: "Host", "Content-Length", "Connection", "From", "User-Agent", "Accept-Encoding", "If-Modified-Since", "If-None-Match", "X-Forwarded-For", etc. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
