---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Rest-ServiceStub/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::AgentService::Rest::ServiceStub (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:30.563327+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::AgentService::Rest::ServiceStub (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::AgentService::Rest::ServiceStub (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::AgentService::Rest::ServiceStub.

REST service stub for the AgentService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #batch_delete_conversations
    
    
    def batch_delete_conversations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the batch_delete_conversations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::BatchDeleteConversationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-BatchDeleteConversationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_agent
    
    
    def create_agent(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Agent

Baseline implementation for the create_agent REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::CreateAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateAgentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_app
    
    
    def create_app(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_app REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::CreateAppRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateAppRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_app_version
    
    
    def create_app_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::AppVersion

Baseline implementation for the create_app_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::CreateAppVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateAppVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::AppVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AppVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::AppVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AppVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_deployment
    
    
    def create_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Deployment

Baseline implementation for the create_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::CreateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Deployment)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_example
    
    
    def create_example(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Example

Baseline implementation for the create_example REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::CreateExampleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateExampleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Example](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Example)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Example](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Example)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_guardrail
    
    
    def create_guardrail(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Guardrail

Baseline implementation for the create_guardrail REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::CreateGuardrailRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateGuardrailRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Guardrail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Guardrail)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Guardrail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Guardrail)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_tool
    
    
    def create_tool(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Tool

Baseline implementation for the create_tool REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::CreateToolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateToolRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Tool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Tool)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Tool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Tool)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_toolset
    
    
    def create_toolset(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Toolset

Baseline implementation for the create_toolset REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::CreateToolsetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-CreateToolsetRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Toolset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Toolset)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Toolset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Toolset)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_agent
    
    
    def delete_agent(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_agent REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteAgentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_app
    
    
    def delete_app(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_app REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteAppRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteAppRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_app_version
    
    
    def delete_app_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_app_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteAppVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteAppVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_conversation
    
    
    def delete_conversation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_conversation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteConversationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteConversationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_deployment
    
    
    def delete_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_example
    
    
    def delete_example(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_example REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteExampleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteExampleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_guardrail
    
    
    def delete_guardrail(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_guardrail REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteGuardrailRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteGuardrailRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_tool
    
    
    def delete_tool(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_tool REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteToolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteToolRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_toolset
    
    
    def delete_toolset(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_toolset REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::DeleteToolsetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-DeleteToolsetRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #export_app
    
    
    def export_app(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the export_app REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ExportAppRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ExportAppRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #generate_app_resource
    
    
    def generate_app_resource(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the generate_app_resource REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GenerateAppResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GenerateAppResourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_agent
    
    
    def get_agent(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Agent

Baseline implementation for the get_agent REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetAgentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_app
    
    
    def get_app(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::App

Baseline implementation for the get_app REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetAppRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetAppRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::App](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-App)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::App](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-App)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_app_version
    
    
    def get_app_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::AppVersion

Baseline implementation for the get_app_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetAppVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetAppVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::AppVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AppVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::AppVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AppVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_changelog
    
    
    def get_changelog(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Changelog

Baseline implementation for the get_changelog REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetChangelogRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetChangelogRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Changelog](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Changelog)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Changelog](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Changelog)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_conversation
    
    
    def get_conversation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Conversation

Baseline implementation for the get_conversation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetConversationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetConversationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Conversation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Conversation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_deployment
    
    
    def get_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Deployment

Baseline implementation for the get_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Deployment)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_example
    
    
    def get_example(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Example

Baseline implementation for the get_example REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetExampleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetExampleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Example](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Example)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Example](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Example)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_guardrail
    
    
    def get_guardrail(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Guardrail

Baseline implementation for the get_guardrail REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetGuardrailRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetGuardrailRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Guardrail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Guardrail)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Guardrail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Guardrail)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_security_settings
    
    
    def get_security_settings(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::SecuritySettings

Baseline implementation for the get_security_settings REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetSecuritySettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetSecuritySettingsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::SecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-SecuritySettings)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::SecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-SecuritySettings)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_tool
    
    
    def get_tool(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Tool

Baseline implementation for the get_tool REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetToolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetToolRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Tool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Tool)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Tool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Tool)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_toolset
    
    
    def get_toolset(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Toolset

Baseline implementation for the get_toolset REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::GetToolsetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GetToolsetRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Toolset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Toolset)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Toolset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Toolset)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #import_app
    
    
    def import_app(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the import_app REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ImportAppRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ImportAppRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_agents
    
    
    def list_agents(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListAgentsResponse

Baseline implementation for the list_agents REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListAgentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAgentsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListAgentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAgentsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListAgentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAgentsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_app_versions
    
    
    def list_app_versions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListAppVersionsResponse

Baseline implementation for the list_app_versions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListAppVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAppVersionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListAppVersionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAppVersionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListAppVersionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAppVersionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_apps
    
    
    def list_apps(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListAppsResponse

Baseline implementation for the list_apps REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListAppsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAppsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListAppsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAppsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListAppsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListAppsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_changelogs
    
    
    def list_changelogs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListChangelogsResponse

Baseline implementation for the list_changelogs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListChangelogsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListChangelogsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListChangelogsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListChangelogsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListChangelogsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListChangelogsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_conversations
    
    
    def list_conversations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListConversationsResponse

Baseline implementation for the list_conversations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListConversationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListConversationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListConversationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListConversationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListConversationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListConversationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_deployments
    
    
    def list_deployments(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListDeploymentsResponse

Baseline implementation for the list_deployments REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListDeploymentsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListDeploymentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListDeploymentsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListDeploymentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListDeploymentsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_examples
    
    
    def list_examples(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListExamplesResponse

Baseline implementation for the list_examples REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListExamplesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListExamplesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListExamplesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListExamplesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListExamplesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListExamplesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_guardrails
    
    
    def list_guardrails(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListGuardrailsResponse

Baseline implementation for the list_guardrails REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListGuardrailsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListGuardrailsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListGuardrailsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListGuardrailsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListGuardrailsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListGuardrailsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_tools
    
    
    def list_tools(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListToolsResponse

Baseline implementation for the list_tools REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListToolsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListToolsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListToolsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListToolsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListToolsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListToolsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_toolsets
    
    
    def list_toolsets(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::ListToolsetsResponse

Baseline implementation for the list_toolsets REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::ListToolsetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListToolsetsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::ListToolsetsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListToolsetsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ListToolsetsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListToolsetsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #restore_app_version
    
    
    def restore_app_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the restore_app_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::RestoreAppVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-RestoreAppVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_agent
    
    
    def update_agent(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Agent

Baseline implementation for the update_agent REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::UpdateAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-UpdateAgentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Agent)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_app
    
    
    def update_app(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::App

Baseline implementation for the update_app REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::UpdateAppRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-UpdateAppRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::App](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-App)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::App](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-App)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_deployment
    
    
    def update_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Deployment

Baseline implementation for the update_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::UpdateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-UpdateDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Deployment)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_example
    
    
    def update_example(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Example

Baseline implementation for the update_example REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::UpdateExampleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-UpdateExampleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Example](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Example)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Example](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Example)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_guardrail
    
    
    def update_guardrail(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Guardrail

Baseline implementation for the update_guardrail REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::UpdateGuardrailRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-UpdateGuardrailRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Guardrail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Guardrail)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Guardrail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Guardrail)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_security_settings
    
    
    def update_security_settings(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::SecuritySettings

Baseline implementation for the update_security_settings REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::UpdateSecuritySettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-UpdateSecuritySettingsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::SecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-SecuritySettings)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::SecuritySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-SecuritySettings)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_tool
    
    
    def update_tool(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Tool

Baseline implementation for the update_tool REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::UpdateToolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-UpdateToolRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Tool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Tool)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Tool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Tool)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_toolset
    
    
    def update_toolset(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Ces::V1beta::Toolset

Baseline implementation for the update_toolset REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Ces::V1beta::UpdateToolsetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-UpdateToolsetRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Ces::V1beta::Toolset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Toolset)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Toolset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Toolset)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
