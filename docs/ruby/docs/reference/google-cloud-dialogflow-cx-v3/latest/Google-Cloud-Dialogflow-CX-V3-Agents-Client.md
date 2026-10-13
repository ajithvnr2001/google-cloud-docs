---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Agents::Client (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:56.157869+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Agents::Client (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Agents::Client (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Agents::Client.

Client for the Agents service.

Service for managing [Agents](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent "Google::Cloud::Dialogflow::CX::V3::Agent \(class\)").

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::CX::V3::Agents::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Agents Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client-Configuration "Google::Cloud::Dialogflow::CX::V3::Agents::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Agents clients
    ::Google::Cloud::Dialogflow::CX::V3::Agents::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Agents Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client#Google__Cloud__Dialogflow__CX__V3__Agents__Client_configure_class_ "Google::Cloud::Dialogflow::CX::V3::Agents::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client-Configuration "Google::Cloud::Dialogflow::CX::V3::Agents::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client-Configuration)) 



### #create_agent
    
    
    def create_agent(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent
    def create_agent(parent: nil, agent: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Overloads**
    
    
    def create_agent(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Pass arguments to `create_agent` via a request object, either of type [CreateAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-CreateAgentRequest "Google::Cloud::Dialogflow::CX::V3::CreateAgentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::CreateAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-CreateAgentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_agent(parent: nil, agent: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Pass arguments to `create_agent` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`. 
  * **agent** ([::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent), ::Hash) — Required. The agent to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::CreateAgentRequest.new
    
    # Call the create_agent method.
    result = client.create_agent request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Agent.
    p result

### #delete_agent
    
    
    def delete_agent(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_agent(name: nil) -> ::Google::Protobuf::Empty

Deletes the specified agent.

**Overloads**
    
    
    def delete_agent(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_agent` via a request object, either of type [DeleteAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeleteAgentRequest "Google::Cloud::Dialogflow::CX::V3::DeleteAgentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::DeleteAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeleteAgentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_agent(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_agent` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::DeleteAgentRequest.new
    
    # Call the delete_agent method.
    result = client.delete_agent request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #export_agent
    
    
    def export_agent(request, options = nil) -> ::Gapic::Operation
    def export_agent(name: nil, agent_uri: nil, data_format: nil, environment: nil, git_destination: nil, include_bigquery_export_settings: nil) -> ::Gapic::Operation

Exports the specified agent to a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentResponse "Google::Cloud::Dialogflow::CX::V3::ExportAgentResponse \(class\)")



**Overloads**
    
    
    def export_agent(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_agent` via a request object, either of type [ExportAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest "Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def export_agent(name: nil, agent_uri: nil, data_format: nil, environment: nil, git_destination: nil, include_bigquery_export_settings: nil) -> ::Gapic::Operation

Pass arguments to `export_agent` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the agent to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 
  * **agent_uri** (::String) — Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the agent to. The format of this URI must be `gs://<bucket-name>/<object-name>`. If left unspecified, the serialized agent is returned inline.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). 

  * **data_format** ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::DataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest-DataFormat)) — Optional. The data format of the exported agent. If not specified, `BLOB` is assumed. 
  * **environment** (::String) — Optional. Environment name. If not set, draft environment is assumed. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 
  * **git_destination** ([::Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest::GitDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportAgentRequest-GitDestination), ::Hash) — Optional. The Git branch to export the agent to. 
  * **include_bigquery_export_settings** (::Boolean) — Optional. Whether to include BigQuery Export setting. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ExportAgentRequest.new
    
    # Call the export_agent method.
    result = client.export_agent request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_agent
    
    
    def get_agent(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent
    def get_agent(name: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Retrieves the specified agent.

**Overloads**
    
    
    def get_agent(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Pass arguments to `get_agent` via a request object, either of type [GetAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetAgentRequest "Google::Cloud::Dialogflow::CX::V3::GetAgentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::GetAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetAgentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_agent(name: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Pass arguments to `get_agent` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::GetAgentRequest.new
    
    # Call the get_agent method.
    result = client.get_agent request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Agent.
    p result

### #get_agent_validation_result
    
    
    def get_agent_validation_result(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult
    def get_agent_validation_result(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Overloads**
    
    
    def get_agent_validation_result(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult

Pass arguments to `get_agent_validation_result` via a request object, either of type [GetAgentValidationResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetAgentValidationResultRequest "Google::Cloud::Dialogflow::CX::V3::GetAgentValidationResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::GetAgentValidationResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetAgentValidationResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_agent_validation_result(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult

Pass arguments to `get_agent_validation_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`. 
  * **language_code** (::String) — If not specified, the agent's default language is used. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AgentValidationResult)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AgentValidationResult)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::GetAgentValidationResultRequest.new
    
    # Call the get_agent_validation_result method.
    result = client.get_agent_validation_result request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::AgentValidationResult.
    p result

### #get_generative_settings
    
    
    def get_generative_settings(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings
    def get_generative_settings(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings

Gets the generative settings for the agent.

**Overloads**
    
    
    def get_generative_settings(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings

Pass arguments to `get_generative_settings` via a request object, either of type [GetGenerativeSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetGenerativeSettingsRequest "Google::Cloud::Dialogflow::CX::V3::GetGenerativeSettingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::GetGenerativeSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetGenerativeSettingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_generative_settings(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings

Pass arguments to `get_generative_settings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`. 
  * **language_code** (::String) — Required. Language code of the generative settings. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GenerativeSettings)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GenerativeSettings)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::GetGenerativeSettingsRequest.new
    
    # Call the get_generative_settings method.
    result = client.get_generative_settings request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::GenerativeSettings.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Agents client object.

**Yields**

  * (config) — Configure the Agents client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::CX::V3::Agents::Client.new do |config|
      config.timeout = 10.0
    end

### #list_agents
    
    
    def list_agents(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Agent>
    def list_agents(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Agent>

Returns the list of all agents in the specified location.

**Overloads**
    
    
    def list_agents(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Agent>

Pass arguments to `list_agents` via a request object, either of type [ListAgentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ListAgentsRequest "Google::Cloud::Dialogflow::CX::V3::ListAgentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ListAgentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ListAgentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_agents(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Agent>

Pass arguments to `list_agents` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location to list all agents for. Format: `projects/<ProjectID>/locations/<LocationID>`. 
  * **page_size** (::Integer) — The maximum number of items to return in a single page. By default 100 and at most 1000. 
  * **page_token** (::String) — The next_page_token value returned from a previous list request. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ListAgentsRequest.new
    
    # Call the list_agents method.
    result = client.list_agents request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::CX::V3::Agent.
      p item
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



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Dialogflow::CX::V3::Agents::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agents::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agents-Operations)) 



### #restore_agent
    
    
    def restore_agent(request, options = nil) -> ::Gapic::Operation
    def restore_agent(name: nil, agent_uri: nil, agent_content: nil, git_source: nil, restore_option: nil) -> ::Gapic::Operation

Restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Overloads**
    
    
    def restore_agent(request, options = nil) -> ::Gapic::Operation

Pass arguments to `restore_agent` via a request object, either of type [RestoreAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-RestoreAgentRequest "Google::Cloud::Dialogflow::CX::V3::RestoreAgentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::RestoreAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-RestoreAgentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def restore_agent(name: nil, agent_uri: nil, agent_content: nil, git_source: nil, restore_option: nil) -> ::Gapic::Operation

Pass arguments to `restore_agent` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the agent to restore into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 
  * **agent_uri** (::String) — The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to restore agent from. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

Note: The following parameters are mutually exclusive: `agent_uri`, `agent_content`, `git_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **agent_content** (::String) — Uncompressed raw byte content for agent.

Note: The following parameters are mutually exclusive: `agent_content`, `agent_uri`, `git_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **git_source** ([::Google::Cloud::Dialogflow::CX::V3::RestoreAgentRequest::GitSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-RestoreAgentRequest-GitSource), ::Hash) — Setting for restoring from a git branch

Note: The following parameters are mutually exclusive: `git_source`, `agent_uri`, `agent_content`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **restore_option** ([::Google::Cloud::Dialogflow::CX::V3::RestoreAgentRequest::RestoreOption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-RestoreAgentRequest-RestoreOption)) — Agent restore mode. If not specified, `KEEP` is assumed. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::RestoreAgentRequest.new
    
    # Call the restore_agent method.
    result = client.restore_agent request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_agent
    
    
    def update_agent(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent
    def update_agent(agent: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Overloads**
    
    
    def update_agent(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Pass arguments to `update_agent` via a request object, either of type [UpdateAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateAgentRequest "Google::Cloud::Dialogflow::CX::V3::UpdateAgentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::UpdateAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateAgentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_agent(agent: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Agent

Pass arguments to `update_agent` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **agent** ([::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent), ::Hash) — Required. The agent to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-FieldMask), ::Hash) — The mask to control which fields get updated. If the mask is not present, all fields will be updated. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::UpdateAgentRequest.new
    
    # Call the update_agent method.
    result = client.update_agent request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Agent.
    p result

### #update_generative_settings
    
    
    def update_generative_settings(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings
    def update_generative_settings(generative_settings: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings

Updates the generative settings for the agent.

**Overloads**
    
    
    def update_generative_settings(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings

Pass arguments to `update_generative_settings` via a request object, either of type [UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateGenerativeSettingsRequest "Google::Cloud::Dialogflow::CX::V3::UpdateGenerativeSettingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateGenerativeSettingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_generative_settings(generative_settings: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings

Pass arguments to `update_generative_settings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **generative_settings** ([::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GenerativeSettings), ::Hash) — Required. Generative settings to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The mask to control which fields get updated. If the mask is not present, all fields will be updated. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GenerativeSettings)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::GenerativeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GenerativeSettings)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::UpdateGenerativeSettingsRequest.new
    
    # Call the update_generative_settings method.
    result = client.update_generative_settings request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::GenerativeSettings.
    p result

### #validate_agent
    
    
    def validate_agent(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult
    def validate_agent(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult

Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results.

**Overloads**
    
    
    def validate_agent(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult

Pass arguments to `validate_agent` via a request object, either of type [ValidateAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ValidateAgentRequest "Google::Cloud::Dialogflow::CX::V3::ValidateAgentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ValidateAgentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ValidateAgentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def validate_agent(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult

Pass arguments to `validate_agent` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The agent to validate. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 
  * **language_code** (::String) — If not specified, the agent's default language is used. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AgentValidationResult)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AgentValidationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AgentValidationResult)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Agents::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ValidateAgentRequest.new
    
    # Call the validate_agent method.
    result = client.validate_agent request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::AgentValidationResult.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
