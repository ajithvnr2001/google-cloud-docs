---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryRequest/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:34.739175+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest.

Request message for [CompletionService.CompleteQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Client#Google__Cloud__DiscoveryEngine__V1beta__CompletionService__Client_complete_query_instance_ "Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Client#complete_query \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #data_store
    
    
    def data_store() -> ::String

**Returns**

  * (::String) — Required. The parent data store resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store`. 



### #data_store=
    
    
    def data_store=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent data store resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store`. 



**Returns**

  * (::String) — Required. The parent data store resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store`. 



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



### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters. 



**Returns**

  * (::String) — Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters. 



### #query_model
    
    
    def query_model() -> ::String

**Returns**

  * (::String) — 

Specifies the autocomplete data model. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

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

Specifies the autocomplete data model. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

    * `document` \- Using suggestions generated from user-imported documents.
    * `search-history` \- Using suggestions generated from the past history of [SearchService.Search](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__SearchService__Client_search_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search \(method\)") API calls. Do not use it when there is no traffic for Search API.
    * `user-event` \- Using suggestions generated from user-imported search events.
    * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

Default values:

    * `document` is the default model for regular dataStores.
    * `search-history` is the default model for site search dataStores.



**Returns**

  * (::String) — 

Specifies the autocomplete data model. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

    * `document` \- Using suggestions generated from user-imported documents.
    * `search-history` \- Using suggestions generated from the past history of [SearchService.Search](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__SearchService__Client_search_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search \(method\)") API calls. Do not use it when there is no traffic for Search API.
    * `user-event` \- Using suggestions generated from user-imported search events.
    * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

Default values:

    * `document` is the default model for regular dataStores.
    * `search-history` is the default model for site search dataStores.



### #user_pseudo_id
    
    
    def user_pseudo_id() -> ::String

**Returns**

  * (::String) — Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned. 




### #user_pseudo_id=
    
    
    def user_pseudo_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned. 




**Returns**

  * (::String) — Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent#Google__Cloud__DiscoveryEngine__V1beta__UserEvent_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UserEvent#user_pseudo_id \(method\)") and [SearchRequest.user_pseudo_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_user_pseudo_id_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#user_pseudo_id \(method\)").

The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
