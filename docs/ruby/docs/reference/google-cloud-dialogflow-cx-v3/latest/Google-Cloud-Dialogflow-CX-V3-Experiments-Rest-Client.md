---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:55.217211+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.

REST client for the Experiments service.

Service for managing [Experiments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment "Google::Cloud::Dialogflow::CX::V3::Experiment \(class\)").

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::CX::V3::Experiments::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Experiments Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client-Configuration "Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Experiments clients
    ::Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Experiments Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client#Google__Cloud__Dialogflow__CX__V3__Experiments__Rest__Client_configure_class_ "Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client-Configuration "Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client-Configuration)) 



### #create_experiment
    
    
    def create_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment
    def create_experiment(parent: nil, experiment: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Creates an [Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment "Google::Cloud::Dialogflow::CX::V3::Experiment \(class\)") in the specified [Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environment "Google::Cloud::Dialogflow::CX::V3::Environment \(class\)").

**Overloads**
    
    
    def create_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `create_experiment` via a request object, either of type [CreateExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-CreateExperimentRequest "Google::Cloud::Dialogflow::CX::V3::CreateExperimentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::CreateExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-CreateExperimentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_experiment(parent: nil, experiment: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `create_experiment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The [Agent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Agent "Google::Cloud::Dialogflow::CX::V3::Agent \(class\)") to create an [Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environment "Google::Cloud::Dialogflow::CX::V3::Environment \(class\)") for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 
  * **experiment** ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment), ::Hash) — Required. The experiment to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::CreateExperimentRequest.new
    
    # Call the create_experiment method.
    result = client.create_experiment request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Experiment.
    p result

### #delete_experiment
    
    
    def delete_experiment(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_experiment(name: nil) -> ::Google::Protobuf::Empty

Deletes the specified [Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment "Google::Cloud::Dialogflow::CX::V3::Experiment \(class\)").

**Overloads**
    
    
    def delete_experiment(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_experiment` via a request object, either of type [DeleteExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeleteExperimentRequest "Google::Cloud::Dialogflow::CX::V3::DeleteExperimentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::DeleteExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeleteExperimentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_experiment(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_experiment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the [Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environment "Google::Cloud::Dialogflow::CX::V3::Environment \(class\)") to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>`. 



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
    client = Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::DeleteExperimentRequest.new
    
    # Call the delete_experiment method.
    result = client.delete_experiment request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_experiment
    
    
    def get_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment
    def get_experiment(name: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Retrieves the specified [Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment "Google::Cloud::Dialogflow::CX::V3::Experiment \(class\)").

**Overloads**
    
    
    def get_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `get_experiment` via a request object, either of type [GetExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetExperimentRequest "Google::Cloud::Dialogflow::CX::V3::GetExperimentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::GetExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetExperimentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_experiment(name: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `get_experiment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the [Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environment "Google::Cloud::Dialogflow::CX::V3::Environment \(class\)"). Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::GetExperimentRequest.new
    
    # Call the get_experiment method.
    result = client.get_experiment request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Experiment.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Experiments REST client object.

**Yields**

  * (config) — Configure the Experiments client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiments-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_experiments
    
    
    def list_experiments(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Experiment>
    def list_experiments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Experiment>

Returns the list of all experiments in the specified [Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environment "Google::Cloud::Dialogflow::CX::V3::Environment \(class\)").

**Overloads**
    
    
    def list_experiments(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Experiment>

Pass arguments to `list_experiments` via a request object, either of type [ListExperimentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ListExperimentsRequest "Google::Cloud::Dialogflow::CX::V3::ListExperimentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ListExperimentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ListExperimentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_experiments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Experiment>

Pass arguments to `list_experiments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The [Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environment "Google::Cloud::Dialogflow::CX::V3::Environment \(class\)") to list all environments for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. 
  * **page_size** (::Integer) — The maximum number of items to return in a single page. By default 20 and at most 100. 
  * **page_token** (::String) — The next_page_token value returned from a previous list request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ListExperimentsRequest.new
    
    # Call the list_experiments method.
    result = client.list_experiments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::CX::V3::Experiment.
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



### #start_experiment
    
    
    def start_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment
    def start_experiment(name: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Starts the specified [Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment "Google::Cloud::Dialogflow::CX::V3::Experiment \(class\)"). This rpc only changes the state of experiment from PENDING to RUNNING.

**Overloads**
    
    
    def start_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `start_experiment` via a request object, either of type [StartExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-StartExperimentRequest "Google::Cloud::Dialogflow::CX::V3::StartExperimentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::StartExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-StartExperimentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def start_experiment(name: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `start_experiment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the experiment to start. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::StartExperimentRequest.new
    
    # Call the start_experiment method.
    result = client.start_experiment request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Experiment.
    p result

### #stop_experiment
    
    
    def stop_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment
    def stop_experiment(name: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Stops the specified [Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment "Google::Cloud::Dialogflow::CX::V3::Experiment \(class\)"). This rpc only changes the state of experiment from RUNNING to DONE.

**Overloads**
    
    
    def stop_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `stop_experiment` via a request object, either of type [StopExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-StopExperimentRequest "Google::Cloud::Dialogflow::CX::V3::StopExperimentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::StopExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-StopExperimentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def stop_experiment(name: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `stop_experiment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the experiment to stop. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::StopExperimentRequest.new
    
    # Call the stop_experiment method.
    result = client.stop_experiment request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Experiment.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_experiment
    
    
    def update_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment
    def update_experiment(experiment: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Updates the specified [Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment "Google::Cloud::Dialogflow::CX::V3::Experiment \(class\)").

**Overloads**
    
    
    def update_experiment(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `update_experiment` via a request object, either of type [UpdateExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateExperimentRequest "Google::Cloud::Dialogflow::CX::V3::UpdateExperimentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::UpdateExperimentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateExperimentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_experiment(experiment: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Experiment

Pass arguments to `update_experiment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **experiment** ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment), ::Hash) — Required. The experiment to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The mask to control which fields get updated. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Experiment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Experiment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Experiments::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::UpdateExperimentRequest.new
    
    # Call the update_experiment method.
    result = client.update_experiment request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Experiment.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
