---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:19.581815+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.

REST client for the Generators service.

Service for managing [Generators](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator "Google::Cloud::Dialogflow::CX::V3::Generator \(class\)")

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::CX::V3::Generators::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Generators Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client-Configuration "Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Generators clients
    ::Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Generators Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client#Google__Cloud__Dialogflow__CX__V3__Generators__Rest__Client_configure_class_ "Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client-Configuration "Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client-Configuration)) 



### #create_generator
    
    
    def create_generator(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator
    def create_generator(parent: nil, generator: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Creates a generator in the specified agent.

**Overloads**
    
    
    def create_generator(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Pass arguments to `create_generator` via a request object, either of type [CreateGeneratorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-CreateGeneratorRequest "Google::Cloud::Dialogflow::CX::V3::CreateGeneratorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::CreateGeneratorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-CreateGeneratorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_generator(parent: nil, generator: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Pass arguments to `create_generator` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The agent to create a generator for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 
  * **generator** ([::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator), ::Hash) — Required. The generator to create. 
  * **language_code** (::String) — 

The language to create generators for the following fields:

    * `Generator.prompt_text.text` If not specified, the agent's default language is used.



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::CreateGeneratorRequest.new
    
    # Call the create_generator method.
    result = client.create_generator request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Generator.
    p result

### #delete_generator
    
    
    def delete_generator(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_generator(name: nil, force: nil) -> ::Google::Protobuf::Empty

Deletes the specified generators.

**Overloads**
    
    
    def delete_generator(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_generator` via a request object, either of type [DeleteGeneratorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeleteGeneratorRequest "Google::Cloud::Dialogflow::CX::V3::DeleteGeneratorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::DeleteGeneratorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DeleteGeneratorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_generator(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_generator` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the generator to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generators/<GeneratorID>`. 
  * **force** (::Boolean) — 

This field has no effect for generators not being used. For generators that are used by pages/flows/transition route groups:

    * If `force` is set to false, an error will be returned with message indicating the referenced resources.
    * If `force` is set to true, Dialogflow will remove the generator, as well as any references to the generator (i.e. [Generator][Fulfillment.generator]) in fulfillments.



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
    client = Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::DeleteGeneratorRequest.new
    
    # Call the delete_generator method.
    result = client.delete_generator request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_generator
    
    
    def get_generator(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator
    def get_generator(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Retrieves the specified generator.

**Overloads**
    
    
    def get_generator(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Pass arguments to `get_generator` via a request object, either of type [Google::Cloud::Dialogflow::CX::V3::GetGeneratorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetGeneratorRequest "Google::Cloud::Dialogflow::CX::V3::GetGeneratorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::GetGeneratorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-GetGeneratorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_generator(name: nil, language_code: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Pass arguments to `get_generator` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the generator. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generators/<GeneratorID>`. 
  * **language_code** (::String) — The language to list generators for. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::GetGeneratorRequest.new
    
    # Call the get_generator method.
    result = client.get_generator request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Generator.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Generators REST client object.

**Yields**

  * (config) — Configure the Generators client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generators-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_generators
    
    
    def list_generators(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Generator>
    def list_generators(parent: nil, language_code: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Generator>

Returns the list of all generators in the specified agent.

**Overloads**
    
    
    def list_generators(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Generator>

Pass arguments to `list_generators` via a request object, either of type [ListGeneratorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ListGeneratorsRequest "Google::Cloud::Dialogflow::CX::V3::ListGeneratorsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::ListGeneratorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ListGeneratorsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_generators(parent: nil, language_code: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::CX::V3::Generator>

Pass arguments to `list_generators` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The agent to list all generators for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 
  * **language_code** (::String) — The language to list generators for. 
  * **page_size** (::Integer) — The maximum number of items to return in a single page. By default 100 and at most 1000. 
  * **page_token** (::String) — The next_page_token value returned from a previous list request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::ListGeneratorsRequest.new
    
    # Call the list_generators method.
    result = client.list_generators request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::CX::V3::Generator.
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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_generator
    
    
    def update_generator(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator
    def update_generator(generator: nil, language_code: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Update the specified generator.

**Overloads**
    
    
    def update_generator(request, options = nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Pass arguments to `update_generator` via a request object, either of type [UpdateGeneratorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateGeneratorRequest "Google::Cloud::Dialogflow::CX::V3::UpdateGeneratorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::CX::V3::UpdateGeneratorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UpdateGeneratorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_generator(generator: nil, language_code: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::CX::V3::Generator

Pass arguments to `update_generator` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **generator** ([::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator), ::Hash) — Required. The generator to update. 
  * **language_code** (::String) — The language to list generators for. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-FieldMask), ::Hash) — The mask to control which fields get updated. If the mask is not present, all fields will be updated. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Generator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Generator)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/cx/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::CX::V3::Generators::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::CX::V3::UpdateGeneratorRequest.new
    
    # Call the update_generator method.
    result = client.update_generator request
    
    # The returned object is of type Google::Cloud::Dialogflow::CX::V3::Generator.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
