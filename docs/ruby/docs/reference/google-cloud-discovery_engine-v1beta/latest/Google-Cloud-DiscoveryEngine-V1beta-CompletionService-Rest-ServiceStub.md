---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Rest-ServiceStub/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Rest::ServiceStub (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:51.295575+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Rest::ServiceStub (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompletionService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Rest::ServiceStub (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::CompletionService::Rest::ServiceStub.

REST service stub for the CompletionService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #advanced_complete_query
    
    
    def advanced_complete_query(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse

Baseline implementation for the advanced_complete_query REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::AdvancedCompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AdvancedCompleteQueryResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #complete_query
    
    
    def complete_query(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse

Baseline implementation for the complete_query REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CompleteQueryResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #import_completion_suggestions
    
    
    def import_completion_suggestions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the import_completion_suggestions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1beta::ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportCompletionSuggestionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #import_suggestion_deny_list_entries
    
    
    def import_suggestion_deny_list_entries(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the import_suggestion_deny_list_entries REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1beta::ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ImportSuggestionDenyListEntriesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #purge_completion_suggestions
    
    
    def purge_completion_suggestions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the purge_completion_suggestions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1beta::PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeCompletionSuggestionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #purge_suggestion_deny_list_entries
    
    
    def purge_suggestion_deny_list_entries(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the purge_suggestion_deny_list_entries REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1beta::PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-PurgeSuggestionDenyListEntriesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #remove_suggestion
    
    
    def remove_suggestion(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse

Baseline implementation for the remove_suggestion REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RemoveSuggestionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RemoveSuggestionResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::RemoveSuggestionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RemoveSuggestionResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
