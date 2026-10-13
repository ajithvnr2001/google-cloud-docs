---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:09.144035+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.

REST client for the KnowledgeBases service.

Service for managing [KnowledgeBases](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase "Google::Cloud::Dialogflow::V2::KnowledgeBase \(class\)").

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dialogflow::V2::KnowledgeBases::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the KnowledgeBases Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client-Configuration "Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all KnowledgeBases clients
    ::Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the KnowledgeBases Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client#Google__Cloud__Dialogflow__V2__KnowledgeBases__Rest__Client_configure_class_ "Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client-Configuration "Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client-Configuration)) 



### #create_knowledge_base
    
    
    def create_knowledge_base(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase
    def create_knowledge_base(parent: nil, knowledge_base: nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Creates a knowledge base.

**Overloads**
    
    
    def create_knowledge_base(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Pass arguments to `create_knowledge_base` via a request object, either of type [CreateKnowledgeBaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateKnowledgeBaseRequest "Google::Cloud::Dialogflow::V2::CreateKnowledgeBaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::CreateKnowledgeBaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateKnowledgeBaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_knowledge_base(parent: nil, knowledge_base: nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Pass arguments to `create_knowledge_base` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project to create a knowledge base for. Format: `projects/<Project ID>/locations/<Location ID>`. 
  * **knowledge_base** ([::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase), ::Hash) — Required. The knowledge base to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::CreateKnowledgeBaseRequest.new
    
    # Call the create_knowledge_base method.
    result = client.create_knowledge_base request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::KnowledgeBase.
    p result

### #delete_knowledge_base
    
    
    def delete_knowledge_base(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_knowledge_base(name: nil, force: nil) -> ::Google::Protobuf::Empty

Deletes the specified knowledge base.

**Overloads**
    
    
    def delete_knowledge_base(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_knowledge_base` via a request object, either of type [DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteKnowledgeBaseRequest "Google::Cloud::Dialogflow::V2::DeleteKnowledgeBaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteKnowledgeBaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_knowledge_base(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_knowledge_base` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the knowledge base to delete. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`. 
  * **force** (::Boolean) — Optional. Force deletes the knowledge base. When set to true, any documents in the knowledge base are also deleted. 



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
    client = Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::DeleteKnowledgeBaseRequest.new
    
    # Call the delete_knowledge_base method.
    result = client.delete_knowledge_base request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_knowledge_base
    
    
    def get_knowledge_base(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase
    def get_knowledge_base(name: nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Retrieves the specified knowledge base.

**Overloads**
    
    
    def get_knowledge_base(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Pass arguments to `get_knowledge_base` via a request object, either of type [GetKnowledgeBaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetKnowledgeBaseRequest "Google::Cloud::Dialogflow::V2::GetKnowledgeBaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::GetKnowledgeBaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetKnowledgeBaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_knowledge_base(name: nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Pass arguments to `get_knowledge_base` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the knowledge base to retrieve. Format `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::GetKnowledgeBaseRequest.new
    
    # Call the get_knowledge_base method.
    result = client.get_knowledge_base request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::KnowledgeBase.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new KnowledgeBases REST client object.

**Yields**

  * (config) — Configure the KnowledgeBases client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBases-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_knowledge_bases
    
    
    def list_knowledge_bases(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::KnowledgeBase>
    def list_knowledge_bases(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::KnowledgeBase>

Returns the list of all knowledge bases of the specified agent.

**Overloads**
    
    
    def list_knowledge_bases(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::KnowledgeBase>

Pass arguments to `list_knowledge_bases` via a request object, either of type [ListKnowledgeBasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListKnowledgeBasesRequest "Google::Cloud::Dialogflow::V2::ListKnowledgeBasesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::ListKnowledgeBasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListKnowledgeBasesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_knowledge_bases(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dialogflow::V2::KnowledgeBase>

Pass arguments to `list_knowledge_bases` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project to list of knowledge bases for. Format: `projects/<Project ID>/locations/<Location ID>`. 
  * **page_size** (::Integer) — The maximum number of items to return in a single page. By default 10 and at most 100. 
  * **page_token** (::String) — The next_page_token value returned from a previous list request. 
  * **filter** (::String) — The filter expression used to filter knowledge bases returned by the list method. The expression has the following syntax:

The following fields and operators are supported:

    * display_name with has(:) operator
    * language_code with equals(=) operator

Examples:

    * 'language_code=en-us' matches knowledge bases with en-us language code.
    * 'display_name:articles' matches knowledge bases whose display name contains "articles".
    * 'display_name:"Best Articles"' matches knowledge bases whose display name contains "Best Articles".
    * 'language_code=en-gb AND display_name=articles' matches all knowledge bases whose display name contains "articles" and whose language code is "en-gb".

Note: An empty filter string (i.e. "") is a no-op and will result in no filtering.

For more information about filtering, see [API Filtering](https://aip.dev/160). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::ListKnowledgeBasesRequest.new
    
    # Call the list_knowledge_bases method.
    result = client.list_knowledge_bases request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dialogflow::V2::KnowledgeBase.
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



### #update_knowledge_base
    
    
    def update_knowledge_base(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase
    def update_knowledge_base(knowledge_base: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Updates the specified knowledge base.

**Overloads**
    
    
    def update_knowledge_base(request, options = nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Pass arguments to `update_knowledge_base` via a request object, either of type [UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-UpdateKnowledgeBaseRequest "Google::Cloud::Dialogflow::V2::UpdateKnowledgeBaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dialogflow::V2::UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-UpdateKnowledgeBaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_knowledge_base(knowledge_base: nil, update_mask: nil) -> ::Google::Cloud::Dialogflow::V2::KnowledgeBase

Pass arguments to `update_knowledge_base` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **knowledge_base** ([::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase), ::Hash) — Required. The knowledge base to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Not specified means `update all`. Currently, only `display_name` can be updated, an InvalidArgument will be returned for attempting to update other fields. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::KnowledgeBase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-KnowledgeBase)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dialogflow/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dialogflow::V2::KnowledgeBases::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dialogflow::V2::UpdateKnowledgeBaseRequest.new
    
    # Call the update_knowledge_base method.
    result = client.update_knowledge_base request
    
    # The returned object is of type Google::Cloud::Dialogflow::V2::KnowledgeBase.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
