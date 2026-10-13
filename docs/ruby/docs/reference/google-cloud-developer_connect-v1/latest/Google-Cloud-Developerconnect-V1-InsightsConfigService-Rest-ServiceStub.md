---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-InsightsConfigService-Rest-ServiceStub/
title: Developer Connect V1 API - Class Google::Cloud::Developerconnect::V1::InsightsConfigService::Rest::ServiceStub (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:12.551827+00:00
---

# Developer Connect V1 API - Class Google::Cloud::Developerconnect::V1::InsightsConfigService::Rest::ServiceStub (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-InsightsConfigService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Developer Connect V1 API - Class Google::Cloud::Developerconnect::V1::InsightsConfigService::Rest::ServiceStub (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Developer Connect V1 API class Google::Cloud::Developerconnect::V1::InsightsConfigService::Rest::ServiceStub.

REST service stub for the InsightsConfigService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_insights_config
    
    
    def create_insights_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_insights_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Developerconnect::V1::CreateInsightsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-CreateInsightsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_insights_config
    
    
    def delete_insights_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_insights_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Developerconnect::V1::DeleteInsightsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-DeleteInsightsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_deployment_event
    
    
    def get_deployment_event(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Developerconnect::V1::DeploymentEvent

Baseline implementation for the get_deployment_event REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Developerconnect::V1::GetDeploymentEventRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-GetDeploymentEventRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Developerconnect::V1::DeploymentEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-DeploymentEvent)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Developerconnect::V1::DeploymentEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-DeploymentEvent)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_insights_config
    
    
    def get_insights_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Developerconnect::V1::InsightsConfig

Baseline implementation for the get_insights_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Developerconnect::V1::GetInsightsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-GetInsightsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Developerconnect::V1::InsightsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-InsightsConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Developerconnect::V1::InsightsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-InsightsConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_deployment_events
    
    
    def list_deployment_events(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Developerconnect::V1::ListDeploymentEventsResponse

Baseline implementation for the list_deployment_events REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Developerconnect::V1::ListDeploymentEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-ListDeploymentEventsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Developerconnect::V1::ListDeploymentEventsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-ListDeploymentEventsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Developerconnect::V1::ListDeploymentEventsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-ListDeploymentEventsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_insights_configs
    
    
    def list_insights_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Developerconnect::V1::ListInsightsConfigsResponse

Baseline implementation for the list_insights_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Developerconnect::V1::ListInsightsConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-ListInsightsConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Developerconnect::V1::ListInsightsConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-ListInsightsConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Developerconnect::V1::ListInsightsConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-ListInsightsConfigsResponse)) — A result object deserialized from the server's reply 



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



### #update_insights_config
    
    
    def update_insights_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_insights_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Developerconnect::V1::UpdateInsightsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-Developerconnect-V1-UpdateInsightsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
