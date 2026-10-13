---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ConverseConversationRequest/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ConverseConversationRequest (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:35.356801+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ConverseConversationRequest (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ConverseConversationRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ConverseConversationRequest (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::ConverseConversationRequest.

Request message for [ConversationalSearchService.ConverseConversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ConversationalSearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__ConversationalSearchService__Client_converse_conversation_instance_ "Google::Cloud::DiscoveryEngine::V1beta::ConversationalSearchService::Client#converse_conversation \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #boost_spec
    
    
    def boost_spec() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::BoostSpec

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-BoostSpec)) — Boost specification to boost certain documents in search results which may affect the converse response. For more information on boosting, see [Boosting](https://cloud.google.com/retail/docs/boosting#boost)



### #boost_spec=
    
    
    def boost_spec=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::BoostSpec

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-BoostSpec)) — Boost specification to boost certain documents in search results which may affect the converse response. For more information on boosting, see [Boosting](https://cloud.google.com/retail/docs/boosting#boost)



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-BoostSpec)) — Boost specification to boost certain documents in search results which may affect the converse response. For more information on boosting, see [Boosting](https://cloud.google.com/retail/docs/boosting#boost)



### #conversation
    
    
    def conversation() -> ::Google::Cloud::DiscoveryEngine::V1beta::Conversation

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Conversation)) — The conversation to be used by auto session only. The name field will be ignored as we automatically assign new name for the conversation in auto session. 



### #conversation=
    
    
    def conversation=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::Conversation

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Conversation)) — The conversation to be used by auto session only. The name field will be ignored as we automatically assign new name for the conversation in auto session. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Conversation)) — The conversation to be used by auto session only. The name field will be ignored as we automatically assign new name for the conversation in auto session. 



### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive. This will be used to filter search results which may affect the summary response.

If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.

Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'

For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive. This will be used to filter search results which may affect the summary response.

If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.

Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'

For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)




**Returns**

  * (::String) — The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive. This will be used to filter search results which may affect the summary response.

If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.

Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'

For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a ConverseConversation session. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a ConverseConversation session. 



**Returns**

  * (::String) — Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a ConverseConversation session. 



### #query
    
    
    def query() -> ::Google::Cloud::DiscoveryEngine::V1beta::TextInput

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-TextInput)) — Required. Current user input. 



### #query=
    
    
    def query=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::TextInput

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-TextInput)) — Required. Current user input. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-TextInput)) — Required. Current user input. 



### #safe_search
    
    
    def safe_search() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to turn on safe search. 



### #safe_search=
    
    
    def safe_search=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to turn on safe search. 



**Returns**

  * (::Boolean) — Whether to turn on safe search. 



### #serving_config
    
    
    def serving_config() -> ::String

**Returns**

  * (::String) — The resource name of the Serving Config to use. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/servingConfigs/{serving_config_id}` If this is not set, the default serving config will be used. 



### #serving_config=
    
    
    def serving_config=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource name of the Serving Config to use. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/servingConfigs/{serving_config_id}` If this is not set, the default serving config will be used. 



**Returns**

  * (::String) — The resource name of the Serving Config to use. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/servingConfigs/{serving_config_id}` If this is not set, the default serving config will be used. 



### #summary_spec
    
    
    def summary_spec() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::ContentSearchSpec::SummarySpec

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::ContentSearchSpec::SummarySpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-ContentSearchSpec-SummarySpec)) — A specification for configuring the summary returned in the response. 



### #summary_spec=
    
    
    def summary_spec=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::ContentSearchSpec::SummarySpec

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::ContentSearchSpec::SummarySpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-ContentSearchSpec-SummarySpec)) — A specification for configuring the summary returned in the response. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::ContentSearchSpec::SummarySpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-ContentSearchSpec-SummarySpec)) — A specification for configuring the summary returned in the response. 



### #user_labels
    
    
    def user_labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The user labels applied to a resource must meet the following requirements:

    * Each resource can have multiple labels, up to a maximum of 64.
    * Each label must be a key-value pair.
    * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
    * The key portion of a label must be unique. However, you can use the same key with multiple resources.
    * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details. 




### #user_labels=
    
    
    def user_labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The user labels applied to a resource must meet the following requirements:

    * Each resource can have multiple labels, up to a maximum of 64.
    * Each label must be a key-value pair.
    * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
    * The key portion of a label must be unique. However, you can use the same key with multiple resources.
    * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The user labels applied to a resource must meet the following requirements:

    * Each resource can have multiple labels, up to a maximum of 64.
    * Each label must be a key-value pair.
    * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
    * The key portion of a label must be unique. However, you can use the same key with multiple resources.
    * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
