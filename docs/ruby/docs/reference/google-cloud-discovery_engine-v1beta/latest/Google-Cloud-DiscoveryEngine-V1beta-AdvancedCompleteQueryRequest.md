---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:59:06.764201+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest.

Request message for [CompletionService.AdvancedCompleteQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client#Google__Cloud__DiscoveryEngine__V1beta__CompletionService__Client_advanced_complete_query_instance_ "Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client#advanced_complete_query \(method\)") method. .

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #boost_spec
    
    
    def boost_spec() -> ::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::BoostSpec

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-BoostSpec)) — Optional. Specification to boost suggestions matching the condition. 



### #boost_spec=
    
    
    def boost_spec=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::BoostSpec

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-BoostSpec)) — Optional. Specification to boost suggestions matching the condition. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-BoostSpec)) — Optional. Specification to boost suggestions matching the condition. 



### #completion_config
    
    
    def completion_config() -> ::String

**Returns**

  * (::String) — Required. The completion_config of the parent dataStore or engine resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/*/completionConfig` `projects/*/locations/global/collections/default_collection/engines/*/completionConfig`. 



### #completion_config=
    
    
    def completion_config=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The completion_config of the parent dataStore or engine resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/*/completionConfig` `projects/*/locations/global/collections/default_collection/engines/*/completionConfig`. 



**Returns**

  * (::String) — Required. The completion_config of the parent dataStore or engine resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/*/completionConfig` `projects/*/locations/global/collections/default_collection/engines/*/completionConfig`. 



### #experiment_ids
    
    
    def experiment_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Experiment ids for this request. 



### #experiment_ids=
    
    
    def experiment_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Experiment ids for this request. 



**Returns**

  * (::Array<::String>) — Optional. Experiment ids for this request. 



### #include_tail_suggestions
    
    
    def include_tail_suggestions() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates if tail suggestions should be returned if there are no suggestions that match the full query. Even if set to true, if there are suggestions that match the full query, those are returned and no tail suggestions are returned. 



### #include_tail_suggestions=
    
    
    def include_tail_suggestions=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates if tail suggestions should be returned if there are no suggestions that match the full query. Even if set to true, if there are suggestions that match the full query, those are returned and no tail suggestions are returned. 



**Returns**

  * (::Boolean) — Indicates if tail suggestions should be returned if there are no suggestions that match the full query. Even if set to true, if there are suggestions that match the full query, those are returned and no tail suggestions are returned. 



### #query
    
    
    def query() -> ::String

**Returns**

  * (::String) — Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters.

The query can not be empty for most of the suggestion types. If it is empty, an `INVALID_ARGUMENT` error is returned. The exception is when the suggestion_types contains only the type `RECENT_SEARCH`, the query can be an empty string. The is called "zero prefix" feature, which returns user's recently searched queries given the empty query. 




### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters.

The query can not be empty for most of the suggestion types. If it is empty, an `INVALID_ARGUMENT` error is returned. The exception is when the suggestion_types contains only the type `RECENT_SEARCH`, the query can be an empty string. The is called "zero prefix" feature, which returns user's recently searched queries given the empty query. 




**Returns**

  * (::String) — Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters.

The query can not be empty for most of the suggestion types. If it is empty, an `INVALID_ARGUMENT` error is returned. The exception is when the suggestion_types contains only the type `RECENT_SEARCH`, the query can be an empty string. The is called "zero prefix" feature, which returns user's recently searched queries given the empty query. 




### #query_model
    
    
    def query_model() -> ::String

**Returns**

  * (::String) — 

Specifies the autocomplete query model, which only applies to the QUERY SuggestionType. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

    * `document` \- Using suggestions generated from user-imported documents.
    * `search-history` \- Using suggestions generated from the past history of [SearchService.Search](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__SearchService__Client_search_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search \(method\)") API calls. Do not use it when there is no traffic for Search API.
    * `user-event` \- Using suggestions generated from user-imported search events.
    * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

Default values:

    * `document` is the default model for regular dataStores.
    * `search-history` is the default model for site search dataStores.



### #query_model=
    
    
    def query_model=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Specifies the autocomplete query model, which only applies to the QUERY SuggestionType. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

    * `document` \- Using suggestions generated from user-imported documents.
    * `search-history` \- Using suggestions generated from the past history of [SearchService.Search](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__SearchService__Client_search_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search \(method\)") API calls. Do not use it when there is no traffic for Search API.
    * `user-event` \- Using suggestions generated from user-imported search events.
    * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

Default values:

    * `document` is the default model for regular dataStores.
    * `search-history` is the default model for site search dataStores.



**Returns**

  * (::String) — 

Specifies the autocomplete query model, which only applies to the QUERY SuggestionType. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

    * `document` \- Using suggestions generated from user-imported documents.
    * `search-history` \- Using suggestions generated from the past history of [SearchService.Search](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__SearchService__Client_search_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search \(method\)") API calls. Do not use it when there is no traffic for Search API.
    * `user-event` \- Using suggestions generated from user-imported search events.
    * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

Default values:

    * `document` is the default model for regular dataStores.
    * `search-history` is the default model for site search dataStores.



### #suggestion_type_specs
    
    
    def suggestion_type_specs() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionTypeSpec>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionTypeSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-SuggestionTypeSpec)>) — Optional. Specification of each suggestion type. 



### #suggestion_type_specs=
    
    
    def suggestion_type_specs=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionTypeSpec>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionTypeSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-SuggestionTypeSpec)>) — Optional. Specification of each suggestion type. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionTypeSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-SuggestionTypeSpec)>) — Optional. Specification of each suggestion type. 



### #suggestion_types
    
    
    def suggestion_types() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionType>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-SuggestionType)>) — Optional. Suggestion types to return. If empty or unspecified, query suggestions are returned. Only one suggestion type is supported at the moment. 



### #suggestion_types=
    
    
    def suggestion_types=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionType>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-SuggestionType)>) — Optional. Suggestion types to return. If empty or unspecified, query suggestions are returned. Only one suggestion type is supported at the moment. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-SuggestionType)>) — Optional. Suggestion types to return. If empty or unspecified, query suggestions are returned. Only one suggestion type is supported at the moment. 



### #user_info
    
    
    def user_info() -> ::Google::Cloud::DiscoveryEngine::V1beta::UserInfo

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::UserInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserInfo)) — Optional. Information about the end user.

This should be the same identifier information as [UserEvent.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_info \(method\)") and [SearchRequest.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_info \(method\)"). 




### #user_info=
    
    
    def user_info=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::UserInfo

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::UserInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserInfo)) — Optional. Information about the end user.

This should be the same identifier information as [UserEvent.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_info \(method\)") and [SearchRequest.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_info \(method\)"). 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::UserInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserInfo)) — Optional. Information about the end user.

This should be the same identifier information as [UserEvent.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_info \(method\)") and [SearchRequest.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_info \(method\)"). 




### #user_pseudo_id
    
    
    def user_pseudo_id() -> ::String

**Returns**

  * (::String) — Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128 




### #user_pseudo_id=
    
    
    def user_pseudo_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128 




**Returns**

  * (::String) — Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
