---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-EngineService-Rest-ServiceStub/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::EngineService::Rest::ServiceStub (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:04.500107+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::EngineService::Rest::ServiceStub (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-EngineService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::EngineService::Rest::ServiceStub (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::EngineService::Rest::ServiceStub.

REST service stub for the EngineService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_engine
    
    
    def create_engine(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_engine REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1::CreateEngineRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateEngineRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_engine
    
    
    def delete_engine(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_engine REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1::DeleteEngineRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DeleteEngineRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_engine
    
    
    def get_engine(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::DiscoveryEngine::V1::Engine

Baseline implementation for the get_engine REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1::GetEngineRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-GetEngineRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1::Engine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Engine)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::Engine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Engine)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_engines
    
    
    def list_engines(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::DiscoveryEngine::V1::ListEnginesResponse

Baseline implementation for the list_engines REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1::ListEnginesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListEnginesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1::ListEnginesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListEnginesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::ListEnginesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListEnginesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_engine
    
    
    def update_engine(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::DiscoveryEngine::V1::Engine

Baseline implementation for the update_engine REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::DiscoveryEngine::V1::UpdateEngineRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-UpdateEngineRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1::Engine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Engine)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::Engine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Engine)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
