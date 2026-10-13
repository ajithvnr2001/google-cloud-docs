---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationProfiles-Rest-ServiceStub/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ConversationProfiles::Rest::ServiceStub (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:37.848809+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ConversationProfiles::Rest::ServiceStub (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationProfiles-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ConversationProfiles::Rest::ServiceStub (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::ConversationProfiles::Rest::ServiceStub.

REST service stub for the ConversationProfiles service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #clear_suggestion_feature_config
    
    
    def clear_suggestion_feature_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the clear_suggestion_feature_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ClearSuggestionFeatureConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_conversation_profile
    
    
    def create_conversation_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Dialogflow::V2::ConversationProfile

Baseline implementation for the create_conversation_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::CreateConversationProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateConversationProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::ConversationProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationProfile)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::ConversationProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationProfile)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_conversation_profile
    
    
    def delete_conversation_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_conversation_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::DeleteConversationProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteConversationProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_conversation_profile
    
    
    def get_conversation_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Dialogflow::V2::ConversationProfile

Baseline implementation for the get_conversation_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::GetConversationProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetConversationProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::ConversationProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationProfile)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::ConversationProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationProfile)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_conversation_profiles
    
    
    def list_conversation_profiles(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Dialogflow::V2::ListConversationProfilesResponse

Baseline implementation for the list_conversation_profiles REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::ListConversationProfilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListConversationProfilesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::ListConversationProfilesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListConversationProfilesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::ListConversationProfilesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListConversationProfilesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #set_suggestion_feature_config
    
    
    def set_suggestion_feature_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the set_suggestion_feature_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SetSuggestionFeatureConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_conversation_profile
    
    
    def update_conversation_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Dialogflow::V2::ConversationProfile

Baseline implementation for the update_conversation_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::UpdateConversationProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-UpdateConversationProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::ConversationProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationProfile)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::ConversationProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationProfile)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
