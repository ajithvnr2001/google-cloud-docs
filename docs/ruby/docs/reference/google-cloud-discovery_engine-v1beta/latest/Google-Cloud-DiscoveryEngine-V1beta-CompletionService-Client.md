---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:03.907102+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.

Client for the CompletionService service.

Service for Auto-Completion.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CompletionService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client-Configuration "Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CompletionService clients
    ::Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.configure do |config|
      config.timeout = 10.0
    end

### #advanced_complete_query
    
    
    def advanced_complete_query(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse
    def advanced_complete_query(completion_config: nil, query: nil, query_model: nil, user_pseudo_id: nil, user_info: nil, include_tail_suggestions: nil, boost_spec: nil, suggestion_types: nil, suggestion_type_specs: nil, experiment_ids: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse

Completes the user input with advanced keyword suggestions.

**Overloads**
    
    
    def advanced_complete_query(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse

Pass arguments to `advanced_complete_query` via a request object, either of type [AdvancedCompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest "Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def advanced_complete_query(completion_config: nil, query: nil, query_model: nil, user_pseudo_id: nil, user_info: nil, include_tail_suggestions: nil, boost_spec: nil, suggestion_types: nil, suggestion_type_specs: nil, experiment_ids: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse

Pass arguments to `advanced_complete_query` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **completion_config** (::String) — Required. The completion_config of the parent dataStore or engine resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/*/completionConfig` `projects/*/locations/global/collections/default_collection/engines/*/completionConfig`. 
  * **query** (::String) — Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters.

The query can not be empty for most of the suggestion types. If it is empty, an `INVALID_ARGUMENT` error is returned. The exception is when the suggestion_types contains only the type `RECENT_SEARCH`, the query can be an empty string. The is called "zero prefix" feature, which returns user's recently searched queries given the empty query. 

  * **query_model** (::String) — 

Specifies the autocomplete query model, which only applies to the QUERY SuggestionType. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

    * `document` \- Using suggestions generated from user-imported documents.
    * `search-history` \- Using suggestions generated from the past history of [SearchService.Search](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__SearchService__Client_search_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search \(method\)") API calls. Do not use it when there is no traffic for Search API.
    * `user-event` \- Using suggestions generated from user-imported search events.
    * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

Default values:

    * `document` is the default model for regular dataStores.
    * `search-history` is the default model for site search dataStores.
  * **user_pseudo_id** (::String) — Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128 

  * **user_info** ([::Google::Cloud::DiscoveryEngine::V1beta::UserInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserInfo), ::Hash) — Optional. Information about the end user.

This should be the same identifier information as [UserEvent.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_info \(method\)") and [SearchRequest.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_info \(method\)"). 

  * **include_tail_suggestions** (::Boolean) — Indicates if tail suggestions should be returned if there are no suggestions that match the full query. Even if set to true, if there are suggestions that match the full query, those are returned and no tail suggestions are returned. 
  * **boost_spec** ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::BoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-BoostSpec), ::Hash) — Optional. Specification to boost suggestions matching the condition. 
  * **suggestion_types** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-SuggestionType)>) — Optional. Suggestion types to return. If empty or unspecified, query suggestions are returned. Only one suggestion type is supported at the moment. 
  * **suggestion_type_specs** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest::SuggestionTypeSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest-SuggestionTypeSpec), ::Hash>) — Optional. Specification of each suggestion type. 
  * **experiment_ids** (::Array<::String>) — Optional. Experiment ids for this request. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest.new
    
    # Call the advanced_complete_query method.
    result = client.advanced_complete_query request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse.
    p result

### #complete_query
    
    
    def complete_query(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse
    def complete_query(data_store: nil, query: nil, query_model: nil, user_pseudo_id: nil, include_tail_suggestions: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse

Completes the specified user input with keyword suggestions.

**Overloads**
    
    
    def complete_query(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse

Pass arguments to `complete_query` via a request object, either of type [Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryRequest "Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def complete_query(data_store: nil, query: nil, query_model: nil, user_pseudo_id: nil, include_tail_suggestions: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse

Pass arguments to `complete_query` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **data_store** (::String) — Required. The parent data store resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store`. 
  * **query** (::String) — Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters. 
  * **query_model** (::String) — 

Specifies the autocomplete data model. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

    * `document` \- Using suggestions generated from user-imported documents.
    * `search-history` \- Using suggestions generated from the past history of [SearchService.Search](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__SearchService__Client_search_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search \(method\)") API calls. Do not use it when there is no traffic for Search API.
    * `user-event` \- Using suggestions generated from user-imported search events.
    * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

Default values:

    * `document` is the default model for regular dataStores.
    * `search-history` is the default model for site search dataStores.
  * **user_pseudo_id** (::String) — Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned. 

  * **include_tail_suggestions** (::Boolean) — Indicates if tail suggestions should be returned if there are no suggestions that match the full query. Even if set to true, if there are suggestions that match the full query, those are returned and no tail suggestions are returned. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest.new
    
    # Call the complete_query method.
    result = client.complete_query request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the CompletionService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client#Google__Cloud__DiscoveryEngine__V1beta__CompletionService__Client_configure_class_ "Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client-Configuration "Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client-Configuration)) 



### #import_completion_suggestions
    
    
    def import_completion_suggestions(request, options = nil) -> ::Gapic::Operation
    def import_completion_suggestions(inline_source: nil, gcs_source: nil, bigquery_source: nil, parent: nil, error_config: nil) -> ::Gapic::Operation

Imports {::Google::Cloud::DiscoveryEngine::V1beta::CompletionSuggestion CompletionSuggestion}s for a DataStore.

**Overloads**
    
    
    def import_completion_suggestions(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_completion_suggestions` via a request object, either of type [ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportCompletionSuggestionsRequest "Google::Cloud::DiscoveryEngine::V1beta::ImportCompletionSuggestionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportCompletionSuggestionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def import_completion_suggestions(inline_source: nil, gcs_source: nil, bigquery_source: nil, parent: nil, error_config: nil) -> ::Gapic::Operation

Pass arguments to `import_completion_suggestions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **inline_source** ([::Google::Cloud::DiscoveryEngine::V1beta::ImportCompletionSuggestionsRequest::InlineSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportCompletionSuggestionsRequest-InlineSource), ::Hash) — The Inline source for suggestion entries.

Note: The following parameters are mutually exclusive: `inline_source`, `gcs_source`, `bigquery_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **gcs_source** ([::Google::Cloud::DiscoveryEngine::V1beta::GcsSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GcsSource), ::Hash) — Cloud Storage location for the input content.

Note: The following parameters are mutually exclusive: `gcs_source`, `inline_source`, `bigquery_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **bigquery_source** ([::Google::Cloud::DiscoveryEngine::V1beta::BigQuerySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-BigQuerySource), ::Hash) — BigQuery input source.

Note: The following parameters are mutually exclusive: `bigquery_source`, `inline_source`, `gcs_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **parent** (::String) — Required. The parent data store resource name for which to import customer autocomplete suggestions.

Follows pattern `projects/*/locations/*/collections/*/dataStores/*`

  * **error_config** ([::Google::Cloud::DiscoveryEngine::V1beta::ImportErrorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportErrorConfig), ::Hash) — The desired location of errors incurred during the Import. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::ImportCompletionSuggestionsRequest.new
    
    # Call the import_completion_suggestions method.
    result = client.import_completion_suggestions request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #import_suggestion_deny_list_entries
    
    
    def import_suggestion_deny_list_entries(request, options = nil) -> ::Gapic::Operation
    def import_suggestion_deny_list_entries(inline_source: nil, gcs_source: nil, parent: nil) -> ::Gapic::Operation

Imports all [SuggestionDenyListEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SuggestionDenyListEntry "Google::Cloud::DiscoveryEngine::V1beta::SuggestionDenyListEntry \(class\)") for a DataStore.

**Overloads**
    
    
    def import_suggestion_deny_list_entries(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_suggestion_deny_list_entries` via a request object, either of type [ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportSuggestionDenyListEntriesRequest "Google::Cloud::DiscoveryEngine::V1beta::ImportSuggestionDenyListEntriesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportSuggestionDenyListEntriesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def import_suggestion_deny_list_entries(inline_source: nil, gcs_source: nil, parent: nil) -> ::Gapic::Operation

Pass arguments to `import_suggestion_deny_list_entries` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **inline_source** ([::Google::Cloud::DiscoveryEngine::V1beta::ImportSuggestionDenyListEntriesRequest::InlineSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportSuggestionDenyListEntriesRequest-InlineSource), ::Hash) — The Inline source for the input content for suggestion deny list entries.

Note: The following parameters are mutually exclusive: `inline_source`, `gcs_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **gcs_source** ([::Google::Cloud::DiscoveryEngine::V1beta::GcsSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GcsSource), ::Hash) — Cloud Storage location for the input content.

Only 1 file can be specified that contains all entries to import. Supported values `gcs_source.schema` for autocomplete suggestion deny list entry imports:

    * `suggestion_deny_list` (default): One JSON [SuggestionDenyListEntry] per line.

Note: The following parameters are mutually exclusive: `gcs_source`, `inline_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **parent** (::String) — Required. The parent data store resource name for which to import denylist entries. Follows pattern projects/_/locations/_ /collections/_/dataStores/_. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::ImportSuggestionDenyListEntriesRequest.new
    
    # Call the import_suggestion_deny_list_entries method.
    result = client.import_suggestion_deny_list_entries request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CompletionService client object.

**Yields**

  * (config) — Configure the CompletionService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new do |config|
      config.timeout = 10.0
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Operations)) 



### #purge_completion_suggestions
    
    
    def purge_completion_suggestions(request, options = nil) -> ::Gapic::Operation
    def purge_completion_suggestions(parent: nil) -> ::Gapic::Operation

Permanently deletes all {::Google::Cloud::DiscoveryEngine::V1beta::CompletionSuggestion CompletionSuggestion}s for a DataStore.

**Overloads**
    
    
    def purge_completion_suggestions(request, options = nil) -> ::Gapic::Operation

Pass arguments to `purge_completion_suggestions` via a request object, either of type [PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeCompletionSuggestionsRequest "Google::Cloud::DiscoveryEngine::V1beta::PurgeCompletionSuggestionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeCompletionSuggestionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def purge_completion_suggestions(parent: nil) -> ::Gapic::Operation

Pass arguments to `purge_completion_suggestions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **parent** (::String) — Required. The parent data store resource name for which to purge completion suggestions. Follows pattern projects/_/locations/_ /collections/_/dataStores/_. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::PurgeCompletionSuggestionsRequest.new
    
    # Call the purge_completion_suggestions method.
    result = client.purge_completion_suggestions request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #purge_suggestion_deny_list_entries
    
    
    def purge_suggestion_deny_list_entries(request, options = nil) -> ::Gapic::Operation
    def purge_suggestion_deny_list_entries(parent: nil) -> ::Gapic::Operation

Permanently deletes all [SuggestionDenyListEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SuggestionDenyListEntry "Google::Cloud::DiscoveryEngine::V1beta::SuggestionDenyListEntry \(class\)") for a DataStore.

**Overloads**
    
    
    def purge_suggestion_deny_list_entries(request, options = nil) -> ::Gapic::Operation

Pass arguments to `purge_suggestion_deny_list_entries` via a request object, either of type [PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeSuggestionDenyListEntriesRequest "Google::Cloud::DiscoveryEngine::V1beta::PurgeSuggestionDenyListEntriesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeSuggestionDenyListEntriesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def purge_suggestion_deny_list_entries(parent: nil) -> ::Gapic::Operation

Pass arguments to `purge_suggestion_deny_list_entries` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **parent** (::String) — Required. The parent data store resource name for which to import denylist entries. Follows pattern projects/_/locations/_ /collections/_/dataStores/_. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::PurgeSuggestionDenyListEntriesRequest.new
    
    # Call the purge_suggestion_deny_list_entries method.
    result = client.purge_suggestion_deny_list_entries request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #remove_suggestion
    
    
    def remove_suggestion(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse
    def remove_suggestion(search_history_suggestion: nil, remove_all_search_history_suggestions: nil, completion_config: nil, user_pseudo_id: nil, user_info: nil, remove_time: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse

Removes the search history suggestion in an engine for a user. This will remove the suggestion from being returned in the [AdvancedCompleteQueryResponse.recent_search_suggestions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryResponse#Google__Cloud__DiscoveryEngine__V1beta__AdvancedCompleteQueryResponse_recent_search_suggestions_instance_ "Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse#recent_search_suggestions \(method\)") for this user. If the user searches the same suggestion again, the new history will override and suggest this suggestion again.

**Overloads**
    
    
    def remove_suggestion(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse

Pass arguments to `remove_suggestion` via a request object, either of type [RemoveSuggestionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RemoveSuggestionRequest "Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RemoveSuggestionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def remove_suggestion(search_history_suggestion: nil, remove_all_search_history_suggestions: nil, completion_config: nil, user_pseudo_id: nil, user_info: nil, remove_time: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse

Pass arguments to `remove_suggestion` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **search_history_suggestion** (::String) — The search history suggestion to be removed.

Note: The following parameters are mutually exclusive: `search_history_suggestion`, `remove_all_search_history_suggestions`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **remove_all_search_history_suggestions** (::Boolean) — Remove all search history suggestions for the user.

Note: The following parameters are mutually exclusive: `remove_all_search_history_suggestions`, `search_history_suggestion`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **completion_config** (::String) — Required. The completion_config of the parent engine resource name for which the search history suggestion is to be removed, such as `projects/*/locations/global/collections/default_collection/engines/*/completionConfig`. 
  * **user_pseudo_id** (::String) — Required. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128. 

  * **user_info** ([::Google::Cloud::DiscoveryEngine::V1beta::UserInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserInfo), ::Hash) — Optional. Information about the end user.

This should be the same identifier information as [UserEvent.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_info \(method\)") and [SearchRequest.user_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_info_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_info \(method\)"). 

  * **remove_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-Timestamp), ::Hash) — Required. Time at which the suggestion was removed. If not set, the current time will be used. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RemoveSuggestionResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RemoveSuggestionResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionRequest.new
    
    # Call the remove_suggestion method.
    result = client.remove_suggestion request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
