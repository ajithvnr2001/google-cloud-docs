---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubPlugin-Rest-ServiceStub/
title: API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubPlugin::Rest::ServiceStub (v1.0.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:18.694582+00:00
---

# API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubPlugin::Rest::ServiceStub (v1.0.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubPlugin-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubPlugin::Rest::ServiceStub (v1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.2  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the API hub V1 API class Google::Cloud::ApiHub::V1::ApiHubPlugin::Rest::ServiceStub.

REST service stub for the ApiHubPlugin service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_plugin
    
    
    def create_plugin(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ApiHub::V1::Plugin

Baseline implementation for the create_plugin REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::CreatePluginRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-CreatePluginRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::Plugin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Plugin)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::Plugin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Plugin)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_plugin_instance
    
    
    def create_plugin_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_plugin_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::CreatePluginInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-CreatePluginInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_plugin
    
    
    def delete_plugin(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_plugin REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::DeletePluginRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-DeletePluginRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_plugin_instance
    
    
    def delete_plugin_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_plugin_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::DeletePluginInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-DeletePluginInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #disable_plugin
    
    
    def disable_plugin(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ApiHub::V1::Plugin

Baseline implementation for the disable_plugin REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::DisablePluginRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-DisablePluginRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::Plugin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Plugin)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::Plugin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Plugin)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #disable_plugin_instance_action
    
    
    def disable_plugin_instance_action(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the disable_plugin_instance_action REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::DisablePluginInstanceActionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-DisablePluginInstanceActionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #enable_plugin
    
    
    def enable_plugin(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ApiHub::V1::Plugin

Baseline implementation for the enable_plugin REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::EnablePluginRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-EnablePluginRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::Plugin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Plugin)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::Plugin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Plugin)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #enable_plugin_instance_action
    
    
    def enable_plugin_instance_action(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the enable_plugin_instance_action REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::EnablePluginInstanceActionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-EnablePluginInstanceActionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #execute_plugin_instance_action
    
    
    def execute_plugin_instance_action(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the execute_plugin_instance_action REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ExecutePluginInstanceActionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_plugin
    
    
    def get_plugin(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ApiHub::V1::Plugin

Baseline implementation for the get_plugin REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::GetPluginRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-GetPluginRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::Plugin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Plugin)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::Plugin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Plugin)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_plugin_instance
    
    
    def get_plugin_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ApiHub::V1::PluginInstance

Baseline implementation for the get_plugin_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::GetPluginInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-GetPluginInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::PluginInstance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::PluginInstance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstance)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_plugin_instances
    
    
    def list_plugin_instances(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ApiHub::V1::ListPluginInstancesResponse

Baseline implementation for the list_plugin_instances REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::ListPluginInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ListPluginInstancesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::ListPluginInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ListPluginInstancesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::ListPluginInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ListPluginInstancesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_plugins
    
    
    def list_plugins(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ApiHub::V1::ListPluginsResponse

Baseline implementation for the list_plugins REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::ListPluginsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ListPluginsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::ListPluginsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ListPluginsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::ListPluginsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ListPluginsResponse)) — A result object deserialized from the server's reply 



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



### #update_plugin_instance
    
    
    def update_plugin_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ApiHub::V1::PluginInstance

Baseline implementation for the update_plugin_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ApiHub::V1::UpdatePluginInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-UpdatePluginInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::PluginInstance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::PluginInstance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstance)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
