---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:38.603860+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.

REST client for the ConversationDatasets service.

Conversation datasets.

Conversation datasets contain raw conversation files and their customizable metadata that can be used for model training.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::V2::ConversationDatasets::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ConversationDatasets Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client-Configuration "Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ConversationDatasets clients
    ::Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ConversationDatasets Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client#Google__Cloud__Dialogflow__V2__ConversationDatasets__Rest__Client_configure_class_ "Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client-Configuration "Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client-Configuration)) 



### #create_conversation_dataset
    
    
    def create_conversation_dataset(request, options = nil) -> ::Gapic::Operation
    def create_conversation_dataset(parent: nil, conversation_dataset: nil) -> ::Gapic::Operation

Creates a new conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [CreateConversationDatasetOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateConversationDatasetOperationMetadata "Google::Cloud::Dialogflow::V2::CreateConversationDatasetOperationMetadata \(class\)")
  * `response`: [ConversationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDataset "Google::Cloud::Dialogflow::V2::ConversationDataset \(class\)")



**Overloads**
    
    
    def create_conversation_dataset(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_conversation_dataset` via a request object, either of type [Google::Cloud::Dialogflow::V2::CreateConversationDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateConversationDatasetRequest "Google::Cloud::Dialogflow::V2::CreateConversationDatasetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::CreateConversationDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateConversationDatasetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_conversation_dataset(parent: nil, conversation_dataset: nil) -> ::Gapic::Operation

Pass arguments to `create_conversation_dataset` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project to create conversation dataset for. Format: `projects/<Project ID>/locations/<Location ID>`
  * **conversation_dataset** ([::Google::Cloud::Dialogflow::V2::ConversationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDataset), ::Hash) — Required. The conversation dataset to create. 



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
    client = Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::CreateConversationDatasetRequest.new
    
    # Call the create_conversation_dataset method.
    result = client.create_conversation_dataset request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_conversation_dataset
    
    
    def delete_conversation_dataset(request, options = nil) -> ::Gapic::Operation
    def delete_conversation_dataset(name: nil) -> ::Gapic::Operation

Deletes the specified conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [DeleteConversationDatasetOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteConversationDatasetOperationMetadata "Google::Cloud::Dialogflow::V2::DeleteConversationDatasetOperationMetadata \(class\)")
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



**Overloads**
    
    
    def delete_conversation_dataset(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_conversation_dataset` via a request object, either of type [DeleteConversationDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteConversationDatasetRequest "Google::Cloud::Dialogflow::V2::DeleteConversationDatasetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::DeleteConversationDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteConversationDatasetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_conversation_dataset(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_conversation_dataset` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The conversation dataset to delete. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>`



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
    client = Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::DeleteConversationDatasetRequest.new
    
    # Call the delete_conversation_dataset method.
    result = client.delete_conversation_dataset request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_conversation_dataset
    
    
    def get_conversation_dataset(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::ConversationDataset
    def get_conversation_dataset(name: nil) -> ::Google::Cloud::Dialogflow::V2::ConversationDataset

Retrieves the specified conversation dataset.

**Overloads**
    
    
    def get_conversation_dataset(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::ConversationDataset

Pass arguments to `get_conversation_dataset` via a request object, either of type [GetConversationDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetConversationDatasetRequest "Google::Cloud::Dialogflow::V2::GetConversationDatasetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::GetConversationDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetConversationDatasetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_conversation_dataset(name: nil) -> ::Google::Cloud::Dialogflow::V2::ConversationDataset

Pass arguments to `get_conversation_dataset` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The conversation dataset to retrieve. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::ConversationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDataset)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::ConversationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDataset)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::GetConversationDatasetRequest.new
    
    # Call the get_conversation_dataset method.
    result = client.get_conversation_dataset request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::ConversationDataset.
    p result

### #import_conversation_data
    
    
    def import_conversation_data(request, options = nil) -> ::Gapic::Operation
    def import_conversation_data(name: nil, input_config: nil) -> ::Gapic::Operation

Import data into the specified conversation dataset. Note that it is not allowed to import data to a conversation dataset that already has data in it.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [ImportConversationDataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ImportConversationDataOperationMetadata "Google::Cloud::Dialogflow::V2::ImportConversationDataOperationMetadata \(class\)")
  * `response`: [ImportConversationDataOperationResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ImportConversationDataOperationResponse "Google::Cloud::Dialogflow::V2::ImportConversationDataOperationResponse \(class\)")



**Overloads**
    
    
    def import_conversation_data(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_conversation_data` via a request object, either of type [ImportConversationDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ImportConversationDataRequest "Google::Cloud::Dialogflow::V2::ImportConversationDataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::ImportConversationDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ImportConversationDataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def import_conversation_data(name: nil, input_config: nil) -> ::Gapic::Operation

Pass arguments to `import_conversation_data` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Dataset resource name. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>`
  * **input_config** ([::Google::Cloud::Dialogflow::V2::InputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-InputConfig), ::Hash) — Required. Configuration describing where to import data from. 



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
    client = Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::ImportConversationDataRequest.new
    
    # Call the import_conversation_data method.
    result = client.import_conversation_data request
    
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

Create a new ConversationDatasets REST client object.

**Yields**

  * (config) — Configure the ConversationDatasets client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_conversation_datasets
    
    
    def list_conversation_datasets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::ConversationDataset>
    def list_conversation_datasets(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::ConversationDataset>

Returns the list of all conversation datasets in the specified project and location.

**Overloads**
    
    
    def list_conversation_datasets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::ConversationDataset>

Pass arguments to `list_conversation_datasets` via a request object, either of type [ListConversationDatasetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListConversationDatasetsRequest "Google::Cloud::Dialogflow::V2::ListConversationDatasetsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::ListConversationDatasetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListConversationDatasetsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_conversation_datasets(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::ConversationDataset>

Pass arguments to `list_conversation_datasets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location name to list all conversation datasets for. Format: `projects/<Project ID>/locations/<Location ID>`
  * **page_size** (::Integer) — Optional. Maximum number of conversation datasets to return in a single page. By default 100 and at most 1000. 
  * **page_token** (::String) — Optional. The next_page_token value returned from a previous list request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::ConversationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDataset)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::ConversationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDataset)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::ListConversationDatasetsRequest.new
    
    # Call the list_conversation_datasets method.
    result = client.list_conversation_datasets request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::V2::ConversationDataset.
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
    
    
    def operations_client() -> ::Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::ConversationDatasets::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ConversationDatasets-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
