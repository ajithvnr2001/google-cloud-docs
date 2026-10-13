---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:26.535706+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client.

Client for the DataA2AService service.

DataA2AService defines the Agent-to-Agent (A2A) protocol service for Gemini Data Analytics.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the DataA2AService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client-Configuration "Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all DataA2AService clients
    ::Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the DataA2AService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client#Google__Cloud__GeminiDataAnalytics__V1beta__DataA2AService__Client_configure_class_ "Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client-Configuration "Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client-Configuration)) 



### #get_agent_card
    
    
    def get_agent_card(request, options = nil) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard
    def get_agent_card(tenant: nil) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard

GetAgentCard returns the agent card for the agent.

**Overloads**
    
    
    def get_agent_card(request, options = nil) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard

Pass arguments to `get_agent_card` via a request object, either of type [GetAgentCardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-GetAgentCardRequest "Google::Cloud::GeminiDataAnalytics::V1beta::GetAgentCardRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GeminiDataAnalytics::V1beta::GetAgentCardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-GetAgentCardRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_agent_card(tenant: nil) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard

Pass arguments to `get_agent_card` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **tenant** (::String) — Optional. Optional tenant, provided as a path parameter. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCard)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentCard)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gemini_data_analytics/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GeminiDataAnalytics::V1beta::GetAgentCardRequest.new
    
    # Call the get_agent_card method.
    result = client.get_agent_card request
    
    # The returned object is of type Google::Cloud::GeminiDataAnalytics::V1beta::AgentCard.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new DataA2AService client object.

**Yields**

  * (config) — Configure the DataA2AService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataA2AService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client.new do |config|
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



### #send_message
    
    
    def send_message(request, options = nil) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageResponse
    def send_message(message: nil, configuration: nil, metadata: nil, tenant: nil) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageResponse

Send a message to the agent. This is a blocking call that will return the task once it is completed.

**Overloads**
    
    
    def send_message(request, options = nil) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageResponse

Pass arguments to `send_message` via a request object, either of type [SendMessageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageRequest "Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def send_message(message: nil, configuration: nil, metadata: nil, tenant: nil) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageResponse

Pass arguments to `send_message` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **message** ([::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage), ::Hash) — Required. The message to send to the agent. 
  * **configuration** ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageConfiguration), ::Hash) — Optional. Configuration for the send request. 
  * **metadata** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct), ::Hash) — Optional. Optional metadata for the request. 
  * **tenant** (::String) — Optional. Optional tenant, provided as a path parameter. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gemini_data_analytics/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest.new
    
    # Call the send_message method.
    result = client.send_message request
    
    # The returned object is of type Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageResponse.
    p result

### #send_streaming_message
    
    
    def send_streaming_message(request, options = nil) -> ::Enumerable<::Google::Cloud::GeminiDataAnalytics::V1beta::StreamResponse>
    def send_streaming_message(message: nil, configuration: nil, metadata: nil, tenant: nil) -> ::Enumerable<::Google::Cloud::GeminiDataAnalytics::V1beta::StreamResponse>

SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.

**Overloads**
    
    
    def send_streaming_message(request, options = nil) -> ::Enumerable<::Google::Cloud::GeminiDataAnalytics::V1beta::StreamResponse>

Pass arguments to `send_streaming_message` via a request object, either of type [SendMessageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageRequest "Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def send_streaming_message(message: nil, configuration: nil, metadata: nil, tenant: nil) -> ::Enumerable<::Google::Cloud::GeminiDataAnalytics::V1beta::StreamResponse>

Pass arguments to `send_streaming_message` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **message** ([::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage), ::Hash) — Required. The message to send to the agent. 
  * **configuration** ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageConfiguration), ::Hash) — Optional. Configuration for the send request. 
  * **metadata** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct), ::Hash) — Optional. Optional metadata for the request. 
  * **tenant** (::String) — Optional. Optional tenant, provided as a path parameter. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Enumerable<[::Google::Cloud::GeminiDataAnalytics::V1beta::StreamResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-StreamResponse)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Enumerable<[::Google::Cloud::GeminiDataAnalytics::V1beta::StreamResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-StreamResponse)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gemini_data_analytics/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GeminiDataAnalytics::V1beta::DataA2AService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest.new
    
    # Call the send_streaming_message method to start streaming.
    output = client.send_streaming_message request
    
    # The returned object is a streamed enumerable yielding elements of type
    # ::Google::Cloud::GeminiDataAnalytics::V1beta::StreamResponse
    output.each do |current_response|
      p current_response
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
