---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:26.141788+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.

REST client for the GeneratorEvaluations service.

Service for managing generator evaluations.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the GeneratorEvaluations Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client-Configuration "Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all GeneratorEvaluations clients
    ::Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the GeneratorEvaluations Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client#Google__Cloud__Dialogflow__V2__GeneratorEvaluations__Rest__Client_configure_class_ "Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client-Configuration "Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client-Configuration)) 



### #create_generator_evaluation
    
    
    def create_generator_evaluation(request, options = nil) -> ::Gapic::Operation
    def create_generator_evaluation(parent: nil, generator_evaluation: nil) -> ::Gapic::Operation

Creates evaluation of a generator.

**Overloads**
    
    
    def create_generator_evaluation(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_generator_evaluation` via a request object, either of type [CreateGeneratorEvaluationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateGeneratorEvaluationRequest "Google::Cloud::Dialogflow::V2::CreateGeneratorEvaluationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::CreateGeneratorEvaluationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateGeneratorEvaluationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_generator_evaluation(parent: nil, generator_evaluation: nil) -> ::Gapic::Operation

Pass arguments to `create_generator_evaluation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The generator resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`
  * **generator_evaluation** ([::Google::Cloud::Dialogflow::V2::GeneratorEvaluation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluation), ::Hash) — Required. The generator evaluation to be created. 



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
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::CreateGeneratorEvaluationRequest.new
    
    # Call the create_generator_evaluation method.
    result = client.create_generator_evaluation request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_generator_evaluation
    
    
    def delete_generator_evaluation(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_generator_evaluation(name: nil) -> ::Google::Protobuf::Empty

Deletes an evaluation of generator.

**Overloads**
    
    
    def delete_generator_evaluation(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_generator_evaluation` via a request object, either of type [DeleteGeneratorEvaluationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteGeneratorEvaluationRequest "Google::Cloud::Dialogflow::V2::DeleteGeneratorEvaluationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::DeleteGeneratorEvaluationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteGeneratorEvaluationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_generator_evaluation(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_generator_evaluation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The generator evaluation resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/ evaluations/<Evaluation ID>`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::DeleteGeneratorEvaluationRequest.new
    
    # Call the delete_generator_evaluation method.
    result = client.delete_generator_evaluation request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_generator_evaluation
    
    
    def get_generator_evaluation(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::GeneratorEvaluation
    def get_generator_evaluation(name: nil) -> ::Google::Cloud::Dialogflow::V2::GeneratorEvaluation

Gets an evaluation of generator.

**Overloads**
    
    
    def get_generator_evaluation(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::GeneratorEvaluation

Pass arguments to `get_generator_evaluation` via a request object, either of type [Google::Cloud::Dialogflow::V2::GetGeneratorEvaluationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetGeneratorEvaluationRequest "Google::Cloud::Dialogflow::V2::GetGeneratorEvaluationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::GetGeneratorEvaluationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetGeneratorEvaluationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_generator_evaluation(name: nil) -> ::Google::Cloud::Dialogflow::V2::GeneratorEvaluation

Pass arguments to `get_generator_evaluation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The generator evaluation resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/evaluations/<Evaluation ID>`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::GeneratorEvaluation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::GeneratorEvaluation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluation)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::GetGeneratorEvaluationRequest.new
    
    # Call the get_generator_evaluation method.
    result = client.get_generator_evaluation request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::GeneratorEvaluation.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new GeneratorEvaluations REST client object.

**Yields**

  * (config) — Configure the GeneratorEvaluations client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_generator_evaluations
    
    
    def list_generator_evaluations(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::GeneratorEvaluation>
    def list_generator_evaluations(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::GeneratorEvaluation>

Lists evaluations of generator.

**Overloads**
    
    
    def list_generator_evaluations(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::GeneratorEvaluation>

Pass arguments to `list_generator_evaluations` via a request object, either of type [ListGeneratorEvaluationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListGeneratorEvaluationsRequest "Google::Cloud::Dialogflow::V2::ListGeneratorEvaluationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::ListGeneratorEvaluationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListGeneratorEvaluationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_generator_evaluations(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::GeneratorEvaluation>

Pass arguments to `list_generator_evaluations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The generator resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>` Wildcard value `-` is supported on generator_id to list evaluations across all generators under same project. 
  * **page_size** (::Integer) — Optional. Maximum number of evaluations to return in a single page. By default 100 and at most 1000. 
  * **page_token** (::String) — Optional. The next_page_token value returned from a previous list request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::GeneratorEvaluation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluation)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::GeneratorEvaluation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluation)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::ListGeneratorEvaluationsRequest.new
    
    # Call the list_generator_evaluations method.
    result = client.list_generator_evaluations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::V2::GeneratorEvaluation.
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
    
    
    def operations_client() -> ::Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::GeneratorEvaluations::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GeneratorEvaluations-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
