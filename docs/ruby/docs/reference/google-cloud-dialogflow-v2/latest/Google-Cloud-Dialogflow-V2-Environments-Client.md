---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Environments::Client (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:33.278928+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Environments::Client (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Environments::Client (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::Environments::Client.

Client for the Environments service.

Service for managing [Environments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment "Google::Cloud::Dialogflow::V2::Environment \(class\)").

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::V2::Environments::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Environments Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client-Configuration "Google::Cloud::Dialogflow::V2::Environments::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Environments clients
    ::Google::Cloud::Dialogflow::V2::Environments::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Environments Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client#Google__Cloud__Dialogflow__V2__Environments__Client_configure_class_ "Google::Cloud::Dialogflow::V2::Environments::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client-Configuration "Google::Cloud::Dialogflow::V2::Environments::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client-Configuration)) 



### #create_environment
    
    
    def create_environment(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Environment
    def create_environment(parent: nil, environment: nil, environment_id: nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Creates an agent environment.

**Overloads**
    
    
    def create_environment(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Pass arguments to `create_environment` via a request object, either of type [CreateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateEnvironmentRequest "Google::Cloud::Dialogflow::V2::CreateEnvironmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::CreateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateEnvironmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_environment(parent: nil, environment: nil, environment_id: nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Pass arguments to `create_environment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The agent to create an environment for. Supported formats:

    * `projects/<Project ID>/agent`
    * `projects/<Project ID>/locations/<Location ID>/agent`
  * **environment** ([::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment), ::Hash) — Required. The environment to create. 
  * **environment_id** (::String) — Required. The unique id of the new environment. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::CreateEnvironmentRequest.new
    
    # Call the create_environment method.
    result = client.create_environment request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::Environment.
    p result

### #delete_environment
    
    
    def delete_environment(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_environment(name: nil) -> ::Google::Protobuf::Empty

Deletes the specified agent environment.

**Overloads**
    
    
    def delete_environment(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_environment` via a request object, either of type [DeleteEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteEnvironmentRequest "Google::Cloud::Dialogflow::V2::DeleteEnvironmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::DeleteEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteEnvironmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_environment(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_environment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the environment to delete. / Format:

    * `projects/<Project ID>/agent/environments/<Environment ID>`
    * `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`

The environment ID for the default environment is `-`. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::DeleteEnvironmentRequest.new
    
    # Call the delete_environment method.
    result = client.delete_environment request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_environment
    
    
    def get_environment(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Environment
    def get_environment(name: nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Retrieves the specified agent environment.

**Overloads**
    
    
    def get_environment(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Pass arguments to `get_environment` via a request object, either of type [GetEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetEnvironmentRequest "Google::Cloud::Dialogflow::V2::GetEnvironmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::GetEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetEnvironmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_environment(name: nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Pass arguments to `get_environment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the environment. Supported formats:

    * `projects/<Project ID>/agent/environments/<Environment ID>`
    * `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`

The environment ID for the default environment is `-`. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::GetEnvironmentRequest.new
    
    # Call the get_environment method.
    result = client.get_environment request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::Environment.
    p result

### #get_environment_history
    
    
    def get_environment_history(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::EnvironmentHistory::Entry>
    def get_environment_history(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::EnvironmentHistory::Entry>

Gets the history of the specified environment.

**Overloads**
    
    
    def get_environment_history(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::EnvironmentHistory::Entry>

Pass arguments to `get_environment_history` via a request object, either of type [GetEnvironmentHistoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetEnvironmentHistoryRequest "Google::Cloud::Dialogflow::V2::GetEnvironmentHistoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::GetEnvironmentHistoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetEnvironmentHistoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_environment_history(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::EnvironmentHistory::Entry>

Pass arguments to `get_environment_history` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the environment to retrieve history for. Supported formats:

    * `projects/<Project ID>/agent/environments/<Environment ID>`
    * `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`

The environment ID for the default environment is `-`. 

  * **page_size** (::Integer) — Optional. The maximum number of items to return in a single page. By default 100 and at most 1000. 
  * **page_token** (::String) — Optional. The next_page_token value returned from a previous list request. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::EnvironmentHistory::Entry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EnvironmentHistory-Entry)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::EnvironmentHistory::Entry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EnvironmentHistory-Entry)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::GetEnvironmentHistoryRequest.new
    
    # Call the get_environment_history method.
    result = client.get_environment_history request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::V2::EnvironmentHistory::Entry.
      p item
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Environments client object.

**Yields**

  * (config) — Configure the Environments client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environments-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::V2::Environments::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::V2::Environments::Client.new do |config|
      config.timeout = 10.0
    end

### #list_environments
    
    
    def list_environments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::Environment>
    def list_environments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::Environment>

Returns the list of all non-default environments of the specified agent.

**Overloads**
    
    
    def list_environments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::Environment>

Pass arguments to `list_environments` via a request object, either of type [ListEnvironmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListEnvironmentsRequest "Google::Cloud::Dialogflow::V2::ListEnvironmentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::ListEnvironmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListEnvironmentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_environments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dialogflow::V2::Environment>

Pass arguments to `list_environments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The agent to list all environments from. Format:

    * `projects/<Project ID>/agent`
    * `projects/<Project ID>/locations/<Location ID>/agent`
  * **page_size** (::Integer) — Optional. The maximum number of items to return in a single page. By default 100 and at most 1000. 
  * **page_token** (::String) — Optional. The next_page_token value returned from a previous list request. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::ListEnvironmentsRequest.new
    
    # Call the list_environments method.
    result = client.list_environments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::V2::Environment.
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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_environment
    
    
    def update_environment(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Environment
    def update_environment(environment: nil, update_mask: nil, allow_load_to_draft_and_discard_changes: nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Updates the specified agent environment.

This method allows you to deploy new agent versions into the environment. When an environment is pointed to a new agent version by setting `environment.agent_version`, the environment is temporarily set to the `LOADING` state. During that time, the environment continues serving the previous version of the agent. After the new agent version is done loading, the environment is set back to the `RUNNING` state. You can use "-" as Environment ID in environment name to update an agent version in the default environment. WARNING: this will negate all recent changes to the draft agent and can't be undone. You may want to save the draft agent to a version before calling this method.

**Overloads**
    
    
    def update_environment(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Pass arguments to `update_environment` via a request object, either of type [UpdateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-UpdateEnvironmentRequest "Google::Cloud::Dialogflow::V2::UpdateEnvironmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::UpdateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-UpdateEnvironmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_environment(environment: nil, update_mask: nil, allow_load_to_draft_and_discard_changes: nil) -> ::Google::Cloud::Dialogflow::V2::Environment

Pass arguments to `update_environment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **environment** ([::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment), ::Hash) — Required. The environment to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The mask to control which fields get updated. 
  * **allow_load_to_draft_and_discard_changes** (::Boolean) — Optional. This field is used to prevent accidental overwrite of the default environment, which is an operation that cannot be undone. To confirm that the caller desires this overwrite, this field must be explicitly set to true when updating the default environment (environment ID = `-`). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Environment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::UpdateEnvironmentRequest.new
    
    # Call the update_environment method.
    result = client.update_environment request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::Environment.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
