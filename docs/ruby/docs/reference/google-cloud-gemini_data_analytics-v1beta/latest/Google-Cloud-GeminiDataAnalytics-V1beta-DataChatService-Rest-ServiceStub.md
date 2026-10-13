---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataChatService-Rest-ServiceStub/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataChatService::Rest::ServiceStub (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:57.117126+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataChatService::Rest::ServiceStub (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataChatService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataChatService::Rest::ServiceStub (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::DataChatService::Rest::ServiceStub.

REST service stub for the DataChatService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #chat
    
    
    def chat(request_pb, options = nil) { |chunk| ... } -> ::Gapic::Rest::TransportOperation

Baseline implementation for the chat REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::GeminiDataAnalytics::V1beta::ChatRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-ChatRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yield Parameter**

  * **chunk** (::String) — The chunk of data received during server streaming. 



**Returns**

  * (::Gapic::Rest::TransportOperation) 



**Raises**

  * (::ArgumentError) 



### #create_conversation
    
    
    def create_conversation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation

Baseline implementation for the create_conversation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::GeminiDataAnalytics::V1beta::CreateConversationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-CreateConversationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Conversation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Conversation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_conversation
    
    
    def delete_conversation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_conversation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::GeminiDataAnalytics::V1beta::DeleteConversationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DeleteConversationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_conversation
    
    
    def get_conversation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation

Baseline implementation for the get_conversation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::GeminiDataAnalytics::V1beta::GetConversationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-GetConversationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Conversation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Conversation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_conversations
    
    
    def list_conversations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::GeminiDataAnalytics::V1beta::ListConversationsResponse

Baseline implementation for the list_conversations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::GeminiDataAnalytics::V1beta::ListConversationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-ListConversationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GeminiDataAnalytics::V1beta::ListConversationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-ListConversationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::ListConversationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-ListConversationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_messages
    
    
    def list_messages(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::GeminiDataAnalytics::V1beta::ListMessagesResponse

Baseline implementation for the list_messages REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::GeminiDataAnalytics::V1beta::ListMessagesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-ListMessagesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GeminiDataAnalytics::V1beta::ListMessagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-ListMessagesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::ListMessagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-ListMessagesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #query_data
    
    
    def query_data(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::GeminiDataAnalytics::V1beta::QueryDataResponse

Baseline implementation for the query_data REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::GeminiDataAnalytics::V1beta::QueryDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-QueryDataRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GeminiDataAnalytics::V1beta::QueryDataResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-QueryDataResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::QueryDataResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-QueryDataResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_conversation
    
    
    def update_conversation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation

Baseline implementation for the update_conversation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::GeminiDataAnalytics::V1beta::UpdateConversationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-UpdateConversationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Conversation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Conversation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
