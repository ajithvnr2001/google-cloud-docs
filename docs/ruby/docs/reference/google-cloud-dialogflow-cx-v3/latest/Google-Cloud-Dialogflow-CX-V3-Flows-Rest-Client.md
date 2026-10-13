---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:43.026140+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.

REST client for the Flows service.

Service for managing [Flows](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow "Google::Cloud::Dialogflow::CX::V3::Flow \(class\)").

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::CX::V3::Flows::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Flows Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client-Configuration "Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Flows clients
    ::Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Flows Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client#Google__Cloud__Dialogflow__CX__V3__Flows__Rest__Client_configure_class_ "Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client-Configuration "Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client-Configuration)) 



### #create_flow
    
    
    def create_flow(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow
    def create_flow(parent: nil, flow: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Creates a flow in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Overloads**
    
    
    def create_flow(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Pass arguments to `create_flow` via a request object, either of type [CreateFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-CreateFlowRequest "Google::Cloud::Dialogflow::CX::V3::CreateFlowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::CreateFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-CreateFlowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_flow(parent: nil, flow: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Pass arguments to `create_flow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The agent to create a flow for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 
  * **flow** ([::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow), ::Hash) — Required. The flow to create. 
  * **language_code** (::String) — The language of the following fields in `flow`:

    * `Flow.event_handlers.trigger_fulfillment.messages`
    * `Flow.event_handlers.trigger_fulfillment.conditional_cases`
    * `Flow.transition_routes.trigger_fulfillment.messages`
    * `Flow.transition_routes.trigger_fulfillment.conditional_cases`

If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::CreateFlowRequest.new
    
    # Call the create_flow method.
    result = client.create_flow request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Flow.
    p result

### #delete_flow
    
    
    def delete_flow(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_flow(name: nil, force: nil) -> ::Google::Protobuf::Empty

Deletes a specified flow.

**Overloads**
    
    
    def delete_flow(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_flow` via a request object, either of type [DeleteFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeleteFlowRequest "Google::Cloud::Dialogflow::CX::V3::DeleteFlowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::DeleteFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeleteFlowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_flow(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_flow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the flow to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. 
  * **force** (::Boolean) — 

This field has no effect for flows with no incoming transitions. For flows with incoming transitions:

    * If `force` is set to false, an error will be returned with message indicating the incoming transitions.
    * If `force` is set to true, Dialogflow will remove the flow, as well as any transitions to the flow (i.e. [Target flow][EventHandler.target_flow] in event handlers or [Target flow][TransitionRoute.target_flow] in transition routes that point to this flow will be cleared).



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::DeleteFlowRequest.new
    
    # Call the delete_flow method.
    result = client.delete_flow request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #export_flow
    
    
    def export_flow(request, options = nil) -> ::Gapic::Operation
    def export_flow(name: nil, flow_uri: nil, include_referenced_flows: nil) -> ::Gapic::Operation

Exports the specified flow to a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportFlowResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportFlowResponse "Google::Cloud::Dialogflow::CX::V3::ExportFlowResponse \(class\)")



Note that resources (e.g. intents, entities, webhooks) that the flow references will also be exported.

**Overloads**
    
    
    def export_flow(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_flow` via a request object, either of type [ExportFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportFlowRequest "Google::Cloud::Dialogflow::CX::V3::ExportFlowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ExportFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportFlowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_flow(name: nil, flow_uri: nil, include_referenced_flows: nil) -> ::Gapic::Operation

Pass arguments to `export_flow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the flow to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. 
  * **flow_uri** (::String) — Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the flow to. The format of this URI must be `gs://<bucket-name>/<object-name>`. If left unspecified, the serialized flow is returned inline.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). 

  * **include_referenced_flows** (::Boolean) — Optional. Whether to export flows referenced by the specified flow. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ExportFlowRequest.new
    
    # Call the export_flow method.
    result = client.export_flow request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_flow
    
    
    def get_flow(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow
    def get_flow(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Retrieves the specified flow.

**Overloads**
    
    
    def get_flow(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Pass arguments to `get_flow` via a request object, either of type [GetFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetFlowRequest "Google::Cloud::Dialogflow::CX::V3::GetFlowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::GetFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetFlowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_flow(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Pass arguments to `get_flow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the flow to get. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. 
  * **language_code** (::String) — The language to retrieve the flow for. The following fields are language dependent:

    * `Flow.event_handlers.trigger_fulfillment.messages`
    * `Flow.event_handlers.trigger_fulfillment.conditional_cases`
    * `Flow.transition_routes.trigger_fulfillment.messages`
    * `Flow.transition_routes.trigger_fulfillment.conditional_cases`

If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::GetFlowRequest.new
    
    # Call the get_flow method.
    result = client.get_flow request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Flow.
    p result

### #get_flow_validation_result
    
    
    def get_flow_validation_result(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult
    def get_flow_validation_result(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult

Gets the latest flow validation result. Flow validation is performed when ValidateFlow is called.

**Overloads**
    
    
    def get_flow_validation_result(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult

Pass arguments to `get_flow_validation_result` via a request object, either of type [GetFlowValidationResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetFlowValidationResultRequest "Google::Cloud::Dialogflow::CX::V3::GetFlowValidationResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::GetFlowValidationResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetFlowValidationResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_flow_validation_result(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult

Pass arguments to `get_flow_validation_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The flow name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/validationResult`. 
  * **language_code** (::String) — If not specified, the agent's default language is used. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowValidationResult)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowValidationResult)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::GetFlowValidationResultRequest.new
    
    # Call the get_flow_validation_result method.
    result = client.get_flow_validation_result request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::FlowValidationResult.
    p result

### #import_flow
    
    
    def import_flow(request, options = nil) -> ::Gapic::Operation
    def import_flow(parent: nil, flow_uri: nil, flow_content: nil, import_option: nil, flow_import_strategy: nil) -> ::Gapic::Operation

Imports the specified flow to the specified agent from a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ImportFlowResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ImportFlowResponse "Google::Cloud::Dialogflow::CX::V3::ImportFlowResponse \(class\)")



Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Overloads**
    
    
    def import_flow(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_flow` via a request object, either of type [ImportFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ImportFlowRequest "Google::Cloud::Dialogflow::CX::V3::ImportFlowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ImportFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ImportFlowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def import_flow(parent: nil, flow_uri: nil, flow_content: nil, import_option: nil, flow_import_strategy: nil) -> ::Gapic::Operation

Pass arguments to `import_flow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The agent to import the flow into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 
  * **flow_uri** (::String) — The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import flow from. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

Note: The following parameters are mutually exclusive: `flow_uri`, `flow_content`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **flow_content** (::String) — Uncompressed raw byte content for flow.

Note: The following parameters are mutually exclusive: `flow_content`, `flow_uri`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **import_option** ([::Google::Cloud::Dialogflow::CX::V3::ImportFlowRequest::ImportOption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ImportFlowRequest-ImportOption)) — Flow import mode. If not specified, `KEEP` is assumed. 
  * **flow_import_strategy** ([::Google::Cloud::Dialogflow::CX::V3::FlowImportStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowImportStrategy), ::Hash) — Optional. Specifies the import strategy used when resolving resource conflicts. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ImportFlowRequest.new
    
    # Call the import_flow method.
    result = client.import_flow request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Flows REST client object.

**Yields**

  * (config) — Configure the Flows client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_flows
    
    
    def list_flows(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Flow>
    def list_flows(parent: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Flow>

Returns the list of all flows in the specified agent.

**Overloads**
    
    
    def list_flows(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Flow>

Pass arguments to `list_flows` via a request object, either of type [ListFlowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ListFlowsRequest "Google::Cloud::Dialogflow::CX::V3::ListFlowsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ListFlowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ListFlowsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_flows(parent: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Flow>

Pass arguments to `list_flows` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The agent containing the flows. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 
  * **page_size** (::Integer) — The maximum number of items to return in a single page. By default 100 and at most 1000. 
  * **page_token** (::String) — The next_page_token value returned from a previous list request. 
  * **language_code** (::String) — The language to list flows for. The following fields are language dependent:

    * `Flow.event_handlers.trigger_fulfillment.messages`
    * `Flow.event_handlers.trigger_fulfillment.conditional_cases`
    * `Flow.transition_routes.trigger_fulfillment.messages`
    * `Flow.transition_routes.trigger_fulfillment.conditional_cases`

If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ListFlowsRequest.new
    
    # Call the list_flows method.
    result = client.list_flows request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::CX::V3::Flow.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Rest::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Rest::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flows-Rest-Operations)) 



### #train_flow
    
    
    def train_flow(request, options = nil) -> ::Gapic::Operation
    def train_flow(name: nil) -> ::Gapic::Operation

Trains the specified flow. Note that only the flow in 'draft' environment is trained.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Overloads**
    
    
    def train_flow(request, options = nil) -> ::Gapic::Operation

Pass arguments to `train_flow` via a request object, either of type [TrainFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TrainFlowRequest "Google::Cloud::Dialogflow::CX::V3::TrainFlowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::TrainFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TrainFlowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def train_flow(name: nil) -> ::Gapic::Operation

Pass arguments to `train_flow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The flow to train. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::TrainFlowRequest.new
    
    # Call the train_flow method.
    result = client.train_flow request
    
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



### #update_flow
    
    
    def update_flow(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow
    def update_flow(flow: nil, update_mask: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Updates the specified flow.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Overloads**
    
    
    def update_flow(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Pass arguments to `update_flow` via a request object, either of type [UpdateFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateFlowRequest "Google::Cloud::Dialogflow::CX::V3::UpdateFlowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::UpdateFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateFlowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_flow(flow: nil, update_mask: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Flow

Pass arguments to `update_flow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **flow** ([::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow), ::Hash) — Required. The flow to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-FieldMask), ::Hash) — The mask to control which fields get updated. If the mask is not present, all fields will be updated. 
  * **language_code** (::String) — The language of the following fields in `flow`:

    * `Flow.event_handlers.trigger_fulfillment.messages`
    * `Flow.event_handlers.trigger_fulfillment.conditional_cases`
    * `Flow.transition_routes.trigger_fulfillment.messages`
    * `Flow.transition_routes.trigger_fulfillment.conditional_cases`

If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Flow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Flow)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::UpdateFlowRequest.new
    
    # Call the update_flow method.
    result = client.update_flow request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Flow.
    p result

### #validate_flow
    
    
    def validate_flow(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult
    def validate_flow(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult

Validates the specified flow and creates or updates validation results. Please call this API after the training is completed to get the complete validation results.

**Overloads**
    
    
    def validate_flow(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult

Pass arguments to `validate_flow` via a request object, either of type [ValidateFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ValidateFlowRequest "Google::Cloud::Dialogflow::CX::V3::ValidateFlowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ValidateFlowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ValidateFlowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def validate_flow(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult

Pass arguments to `validate_flow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The flow to validate. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. 
  * **language_code** (::String) — If not specified, the agent's default language is used. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowValidationResult)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::FlowValidationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowValidationResult)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Flows::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ValidateFlowRequest.new
    
    # Call the validate_flow method.
    result = client.validate_flow request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::FlowValidationResult.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
