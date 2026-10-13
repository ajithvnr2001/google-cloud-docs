---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse/
title: Retail V2 API - Class Google::Cloud::Retail::V2::ConversationalSearchResponse (v2.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:32.291803+00:00
---

# Retail V2 API - Class Google::Cloud::Retail::V2::ConversationalSearchResponse (v2.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Retail V2 API - Class Google::Cloud::Retail::V2::ConversationalSearchResponse (v2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.0 (latest)  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.1  0.21.0  0.20.0  0.19.0  0.18.2  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Retail V2 API class Google::Cloud::Retail::V2::ConversationalSearchResponse.

Response message for [ConversationalSearchService.ConversationalSearch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchService-Client#Google__Cloud__Retail__V2__ConversationalSearchService__Client_conversational_search_instance_ "Google::Cloud::Retail::V2::ConversationalSearchService::Client#conversational_search \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #conversation_id
    
    
    def conversation_id() -> ::String

**Returns**

  * (::String) — Conversation UUID. This field will be stored in client side storage to maintain the conversation session with server and will be used for next search request's [ConversationalSearchRequest.conversation_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchRequest#Google__Cloud__Retail__V2__ConversationalSearchRequest_conversation_id_instance_ "Google::Cloud::Retail::V2::ConversationalSearchRequest#conversation_id \(method\)") to restore conversation state in server. 



### #conversation_id=
    
    
    def conversation_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Conversation UUID. This field will be stored in client side storage to maintain the conversation session with server and will be used for next search request's [ConversationalSearchRequest.conversation_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchRequest#Google__Cloud__Retail__V2__ConversationalSearchRequest_conversation_id_instance_ "Google::Cloud::Retail::V2::ConversationalSearchRequest#conversation_id \(method\)") to restore conversation state in server. 



**Returns**

  * (::String) — Conversation UUID. This field will be stored in client side storage to maintain the conversation session with server and will be used for next search request's [ConversationalSearchRequest.conversation_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchRequest#Google__Cloud__Retail__V2__ConversationalSearchRequest_conversation_id_instance_ "Google::Cloud::Retail::V2::ConversationalSearchRequest#conversation_id \(method\)") to restore conversation state in server. 



### #conversational_filtering_result
    
    
    def conversational_filtering_result() -> ::Google::Cloud::Retail::V2::ConversationalSearchResponse::ConversationalFilteringResult

**Returns**

  * ([::Google::Cloud::Retail::V2::ConversationalSearchResponse::ConversationalFilteringResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-ConversationalFilteringResult)) — This field specifies all related information that is needed on client side for UI rendering of conversational filtering search. 



### #conversational_filtering_result=
    
    
    def conversational_filtering_result=(value) -> ::Google::Cloud::Retail::V2::ConversationalSearchResponse::ConversationalFilteringResult

**Parameter**

  * **value** ([::Google::Cloud::Retail::V2::ConversationalSearchResponse::ConversationalFilteringResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-ConversationalFilteringResult)) — This field specifies all related information that is needed on client side for UI rendering of conversational filtering search. 



**Returns**

  * ([::Google::Cloud::Retail::V2::ConversationalSearchResponse::ConversationalFilteringResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-ConversationalFilteringResult)) — This field specifies all related information that is needed on client side for UI rendering of conversational filtering search. 



### #conversational_text_response
    
    
    def conversational_text_response() -> ::String

**Returns**

  * (::String) — The conversational answer-based text response generated by the Server. 



### #conversational_text_response=
    
    
    def conversational_text_response=(value) -> ::String

**Parameter**

  * **value** (::String) — The conversational answer-based text response generated by the Server. 



**Returns**

  * (::String) — The conversational answer-based text response generated by the Server. 



### #followup_question
    
    
    def followup_question() -> ::Google::Cloud::Retail::V2::ConversationalSearchResponse::FollowupQuestion

**Returns**

  * ([::Google::Cloud::Retail::V2::ConversationalSearchResponse::FollowupQuestion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-FollowupQuestion)) — The conversational followup question generated for Intent refinement. 



### #followup_question=
    
    
    def followup_question=(value) -> ::Google::Cloud::Retail::V2::ConversationalSearchResponse::FollowupQuestion

**Parameter**

  * **value** ([::Google::Cloud::Retail::V2::ConversationalSearchResponse::FollowupQuestion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-FollowupQuestion)) — The conversational followup question generated for Intent refinement. 



**Returns**

  * ([::Google::Cloud::Retail::V2::ConversationalSearchResponse::FollowupQuestion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-FollowupQuestion)) — The conversational followup question generated for Intent refinement. 



### #refined_search
    
    
    def refined_search() -> ::Array<::Google::Cloud::Retail::V2::ConversationalSearchResponse::RefinedSearch>

**Returns**

  * (::Array<[::Google::Cloud::Retail::V2::ConversationalSearchResponse::RefinedSearch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-RefinedSearch)>) — The proposed refined search queries. They can be used to fetch the relevant search results. When using CONVERSATIONAL_FILTER_ONLY mode, the refined_query from search response will be populated here. 



### #refined_search=
    
    
    def refined_search=(value) -> ::Array<::Google::Cloud::Retail::V2::ConversationalSearchResponse::RefinedSearch>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Retail::V2::ConversationalSearchResponse::RefinedSearch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-RefinedSearch)>) — The proposed refined search queries. They can be used to fetch the relevant search results. When using CONVERSATIONAL_FILTER_ONLY mode, the refined_query from search response will be populated here. 



**Returns**

  * (::Array<[::Google::Cloud::Retail::V2::ConversationalSearchResponse::RefinedSearch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-RefinedSearch)>) — The proposed refined search queries. They can be used to fetch the relevant search results. When using CONVERSATIONAL_FILTER_ONLY mode, the refined_query from search response will be populated here. 



### #state
    
    
    def state() -> ::Google::Cloud::Retail::V2::ConversationalSearchResponse::State

**Returns**

  * ([::Google::Cloud::Retail::V2::ConversationalSearchResponse::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-ConversationalSearchResponse-State)) — Output only. The state of the response generation. 



### #user_query_types
    
    
    def user_query_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — 

The types Retail classifies the search query as.

Supported values are:

    * "ORDER_SUPPORT"
    * "SIMPLE_PRODUCT_SEARCH"
    * "INTENT_REFINEMENT"
    * "PRODUCT_DETAILS"
    * "PRODUCT_COMPARISON"
    * "DEALS_AND_COUPONS"
    * "STORE_RELEVANT"
    * "BLOCKLISTED"
    * "BEST_PRODUCT"
    * "RETAIL_SUPPORT"
    * "DISABLED"



### #user_query_types=
    
    
    def user_query_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — 

The types Retail classifies the search query as.

Supported values are:

    * "ORDER_SUPPORT"
    * "SIMPLE_PRODUCT_SEARCH"
    * "INTENT_REFINEMENT"
    * "PRODUCT_DETAILS"
    * "PRODUCT_COMPARISON"
    * "DEALS_AND_COUPONS"
    * "STORE_RELEVANT"
    * "BLOCKLISTED"
    * "BEST_PRODUCT"
    * "RETAIL_SUPPORT"
    * "DISABLED"



**Returns**

  * (::Array<::String>) — 

The types Retail classifies the search query as.

Supported values are:

    * "ORDER_SUPPORT"
    * "SIMPLE_PRODUCT_SEARCH"
    * "INTENT_REFINEMENT"
    * "PRODUCT_DETAILS"
    * "PRODUCT_COMPARISON"
    * "DEALS_AND_COUPONS"
    * "STORE_RELEVANT"
    * "BLOCKLISTED"
    * "BEST_PRODUCT"
    * "RETAIL_SUPPORT"
    * "DISABLED"



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
