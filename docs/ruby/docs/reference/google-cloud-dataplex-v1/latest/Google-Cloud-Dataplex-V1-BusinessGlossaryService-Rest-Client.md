---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:57.800605+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.

REST client for the BusinessGlossaryService service.

BusinessGlossaryService provides APIs for managing business glossary resources for enterprise customers. The resources currently supported in Business Glossary are:

  1. Glossary
  2. GlossaryCategory
  3. GlossaryTerm



## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dataplex::V1::BusinessGlossaryService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the BusinessGlossaryService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client-Configuration "Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all BusinessGlossaryService clients
    ::Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the BusinessGlossaryService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client#Google__Cloud__Dataplex__V1__BusinessGlossaryService__Rest__Client_configure_class_ "Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client-Configuration "Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client-Configuration)) 



### #create_glossary
    
    
    def create_glossary(request, options = nil) -> ::Gapic::Operation
    def create_glossary(parent: nil, glossary_id: nil, glossary: nil, validate_only: nil) -> ::Gapic::Operation

Creates a new Glossary resource.

**Overloads**
    
    
    def create_glossary(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_glossary` via a request object, either of type [CreateGlossaryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateGlossaryRequest "Google::Cloud::Dataplex::V1::CreateGlossaryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::CreateGlossaryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateGlossaryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_glossary(parent: nil, glossary_id: nil, glossary: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_glossary` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this Glossary will be created. Format: projects/{project_id_or_number}/locations/{location_id} where `location_id` refers to a Google Cloud region. 
  * **glossary_id** (::String) — Required. Glossary ID: Glossary identifier. 
  * **glossary** ([::Google::Cloud::Dataplex::V1::Glossary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Glossary), ::Hash) — Required. The Glossary to create. 
  * **validate_only** (::Boolean) — Optional. Validates the request without actually creating the Glossary. Default: false. 



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
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::CreateGlossaryRequest.new
    
    # Call the create_glossary method.
    result = client.create_glossary request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_glossary_category
    
    
    def create_glossary_category(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory
    def create_glossary_category(parent: nil, category_id: nil, category: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Creates a new GlossaryCategory resource.

**Overloads**
    
    
    def create_glossary_category(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Pass arguments to `create_glossary_category` via a request object, either of type [CreateGlossaryCategoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateGlossaryCategoryRequest "Google::Cloud::Dataplex::V1::CreateGlossaryCategoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::CreateGlossaryCategoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateGlossaryCategoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_glossary_category(parent: nil, category_id: nil, category: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Pass arguments to `create_glossary_category` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this GlossaryCategory will be created. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `locationId` refers to a Google Cloud region. 
  * **category_id** (::String) — Required. GlossaryCategory identifier. 
  * **category** ([::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory), ::Hash) — Required. The GlossaryCategory to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::CreateGlossaryCategoryRequest.new
    
    # Call the create_glossary_category method.
    result = client.create_glossary_category request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::GlossaryCategory.
    p result

### #create_glossary_term
    
    
    def create_glossary_term(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm
    def create_glossary_term(parent: nil, term_id: nil, term: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Creates a new GlossaryTerm resource.

**Overloads**
    
    
    def create_glossary_term(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Pass arguments to `create_glossary_term` via a request object, either of type [CreateGlossaryTermRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateGlossaryTermRequest "Google::Cloud::Dataplex::V1::CreateGlossaryTermRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::CreateGlossaryTermRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateGlossaryTermRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_glossary_term(parent: nil, term_id: nil, term: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Pass arguments to `create_glossary_term` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where the GlossaryTerm will be created. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `location_id` refers to a Google Cloud region. 
  * **term_id** (::String) — Required. GlossaryTerm identifier. 
  * **term** ([::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm), ::Hash) — Required. The GlossaryTerm to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::CreateGlossaryTermRequest.new
    
    # Call the create_glossary_term method.
    result = client.create_glossary_term request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::GlossaryTerm.
    p result

### #delete_glossary
    
    
    def delete_glossary(request, options = nil) -> ::Gapic::Operation
    def delete_glossary(name: nil, etag: nil) -> ::Gapic::Operation

Deletes a Glossary resource. All the categories and terms within the Glossary must be deleted before the Glossary can be deleted.

**Overloads**
    
    
    def delete_glossary(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_glossary` via a request object, either of type [DeleteGlossaryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteGlossaryRequest "Google::Cloud::Dataplex::V1::DeleteGlossaryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::DeleteGlossaryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteGlossaryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_glossary(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_glossary` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the Glossary to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} 
  * **etag** (::String) — Optional. The etag of the Glossary. If this is provided, it must match the server's etag. If the etag is provided and does not match the server-computed etag, the request must fail with a ABORTED error code. 



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
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::DeleteGlossaryRequest.new
    
    # Call the delete_glossary method.
    result = client.delete_glossary request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_glossary_category
    
    
    def delete_glossary_category(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_glossary_category(name: nil) -> ::Google::Protobuf::Empty

Deletes a GlossaryCategory resource. All the GlossaryCategories and GlossaryTerms nested directly under the specified GlossaryCategory will be moved one level up to the parent in the hierarchy.

**Overloads**
    
    
    def delete_glossary_category(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_glossary_category` via a request object, either of type [DeleteGlossaryCategoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteGlossaryCategoryRequest "Google::Cloud::Dataplex::V1::DeleteGlossaryCategoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::DeleteGlossaryCategoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteGlossaryCategoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_glossary_category(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_glossary_category` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the GlossaryCategory to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::DeleteGlossaryCategoryRequest.new
    
    # Call the delete_glossary_category method.
    result = client.delete_glossary_category request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_glossary_term
    
    
    def delete_glossary_term(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_glossary_term(name: nil) -> ::Google::Protobuf::Empty

Deletes a GlossaryTerm resource.

**Overloads**
    
    
    def delete_glossary_term(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_glossary_term` via a request object, either of type [DeleteGlossaryTermRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteGlossaryTermRequest "Google::Cloud::Dataplex::V1::DeleteGlossaryTermRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::DeleteGlossaryTermRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteGlossaryTermRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_glossary_term(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_glossary_term` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the GlossaryTerm to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::DeleteGlossaryTermRequest.new
    
    # Call the delete_glossary_term method.
    result = client.delete_glossary_term request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_glossary
    
    
    def get_glossary(request, options = nil) -> ::Google::Cloud::Dataplex::V1::Glossary
    def get_glossary(name: nil) -> ::Google::Cloud::Dataplex::V1::Glossary

Gets a Glossary resource.

**Overloads**
    
    
    def get_glossary(request, options = nil) -> ::Google::Cloud::Dataplex::V1::Glossary

Pass arguments to `get_glossary` via a request object, either of type [GetGlossaryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetGlossaryRequest "Google::Cloud::Dataplex::V1::GetGlossaryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GetGlossaryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetGlossaryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_glossary(name: nil) -> ::Google::Cloud::Dataplex::V1::Glossary

Pass arguments to `get_glossary` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Glossary to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::Glossary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Glossary)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::Glossary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Glossary)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GetGlossaryRequest.new
    
    # Call the get_glossary method.
    result = client.get_glossary request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::Glossary.
    p result

### #get_glossary_category
    
    
    def get_glossary_category(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory
    def get_glossary_category(name: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Gets a GlossaryCategory resource.

**Overloads**
    
    
    def get_glossary_category(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Pass arguments to `get_glossary_category` via a request object, either of type [GetGlossaryCategoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetGlossaryCategoryRequest "Google::Cloud::Dataplex::V1::GetGlossaryCategoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GetGlossaryCategoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetGlossaryCategoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_glossary_category(name: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Pass arguments to `get_glossary_category` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the GlossaryCategory to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GetGlossaryCategoryRequest.new
    
    # Call the get_glossary_category method.
    result = client.get_glossary_category request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::GlossaryCategory.
    p result

### #get_glossary_term
    
    
    def get_glossary_term(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm
    def get_glossary_term(name: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Gets a GlossaryTerm resource.

**Overloads**
    
    
    def get_glossary_term(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Pass arguments to `get_glossary_term` via a request object, either of type [GetGlossaryTermRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetGlossaryTermRequest "Google::Cloud::Dataplex::V1::GetGlossaryTermRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GetGlossaryTermRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetGlossaryTermRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_glossary_term(name: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Pass arguments to `get_glossary_term` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the GlossaryTerm to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GetGlossaryTermRequest.new
    
    # Call the get_glossary_term method.
    result = client.get_glossary_term request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::GlossaryTerm.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new BusinessGlossaryService REST client object.

**Yields**

  * (config) — Configure the BusinessGlossaryService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_glossaries
    
    
    def list_glossaries(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::Glossary>
    def list_glossaries(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::Glossary>

Lists Glossary resources in a project and location.

**Overloads**
    
    
    def list_glossaries(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::Glossary>

Pass arguments to `list_glossaries` via a request object, either of type [ListGlossariesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListGlossariesRequest "Google::Cloud::Dataplex::V1::ListGlossariesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::ListGlossariesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListGlossariesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_glossaries(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::Glossary>

Pass arguments to `list_glossaries` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which has this collection of Glossaries. Format: projects/{project_id_or_number}/locations/{location_id} where `location_id` refers to a Google Cloud region. 
  * **page_size** (::Integer) — Optional. The maximum number of Glossaries to return. The service may return fewer than this value. If unspecified, at most 50 Glossaries will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000\. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListGlossaries` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListGlossaries` must match the call that provided the page token. 
  * **filter** (::String) — 

Optional. Filter expression that filters Glossaries listed in the response. Filters on proto fields of Glossary are supported. Examples of using a filter are:

    * `display_name="my-glossary"`
    * `categoryCount=1`
    * `termCount=0`
  * **order_by** (::String) — Optional. Order by expression that orders Glossaries listed in the response. Order by fields are: `name` or `create_time` for the result. If not specified, the ordering is undefined. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::Glossary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Glossary)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::Glossary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Glossary)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::ListGlossariesRequest.new
    
    # Call the list_glossaries method.
    result = client.list_glossaries request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataplex::V1::Glossary.
      p item
    end

### #list_glossary_categories
    
    
    def list_glossary_categories(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::GlossaryCategory>
    def list_glossary_categories(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::GlossaryCategory>

Lists GlossaryCategory resources in a Glossary.

**Overloads**
    
    
    def list_glossary_categories(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::GlossaryCategory>

Pass arguments to `list_glossary_categories` via a request object, either of type [ListGlossaryCategoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListGlossaryCategoriesRequest "Google::Cloud::Dataplex::V1::ListGlossaryCategoriesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::ListGlossaryCategoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListGlossaryCategoriesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_glossary_categories(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::GlossaryCategory>

Pass arguments to `list_glossary_categories` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which has this collection of GlossaryCategories. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} Location is the Google Cloud region. 
  * **page_size** (::Integer) — Optional. The maximum number of GlossaryCategories to return. The service may return fewer than this value. If unspecified, at most 50 GlossaryCategories will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListGlossaryCategories` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListGlossaryCategories` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Filter expression that filters GlossaryCategories listed in the response. Filters are supported on the following fields:

    * immediate_parent

Examples of using a filter are: \- `immediate_parent="projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}"` \- `immediate_parent="projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}"`

This will only return the GlossaryCategories that are directly nested under the specified parent. 

  * **order_by** (::String) — Optional. Order by expression that orders GlossaryCategories listed in the response. Order by fields are: `name` or `create_time` for the result. If not specified, the ordering is undefined. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::ListGlossaryCategoriesRequest.new
    
    # Call the list_glossary_categories method.
    result = client.list_glossary_categories request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataplex::V1::GlossaryCategory.
      p item
    end

### #list_glossary_terms
    
    
    def list_glossary_terms(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::GlossaryTerm>
    def list_glossary_terms(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::GlossaryTerm>

Lists GlossaryTerm resources in a Glossary.

**Overloads**
    
    
    def list_glossary_terms(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::GlossaryTerm>

Pass arguments to `list_glossary_terms` via a request object, either of type [ListGlossaryTermsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListGlossaryTermsRequest "Google::Cloud::Dataplex::V1::ListGlossaryTermsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::ListGlossaryTermsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListGlossaryTermsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_glossary_terms(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::GlossaryTerm>

Pass arguments to `list_glossary_terms` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which has this collection of GlossaryTerms. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `location_id` refers to a Google Cloud region. 
  * **page_size** (::Integer) — Optional. The maximum number of GlossaryTerms to return. The service may return fewer than this value. If unspecified, at most 50 GlossaryTerms will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListGlossaryTerms` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListGlossaryTerms` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Filter expression that filters GlossaryTerms listed in the response. Filters are supported on the following fields:

    * immediate_parent

Examples of using a filter are: \- `immediate_parent="projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}"` \- `immediate_parent="projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}"`

This will only return the GlossaryTerms that are directly nested under the specified parent. 

  * **order_by** (::String) — Optional. Order by expression that orders GlossaryTerms listed in the response. Order by fields are: `name` or `create_time` for the result. If not specified, the ordering is undefined. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::ListGlossaryTermsRequest.new
    
    # Call the list_glossary_terms method.
    result = client.list_glossary_terms request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataplex::V1::GlossaryTerm.
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
    
    
    def operations_client() -> ::Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_glossary
    
    
    def update_glossary(request, options = nil) -> ::Gapic::Operation
    def update_glossary(glossary: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Updates a Glossary resource.

**Overloads**
    
    
    def update_glossary(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_glossary` via a request object, either of type [UpdateGlossaryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateGlossaryRequest "Google::Cloud::Dataplex::V1::UpdateGlossaryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::UpdateGlossaryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateGlossaryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_glossary(glossary: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `update_glossary` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **glossary** ([::Google::Cloud::Dataplex::V1::Glossary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Glossary), ::Hash) — Required. The Glossary to update. The Glossary's `name` field is used to identify the Glossary to update. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. 
  * **validate_only** (::Boolean) — Optional. Validates the request without actually updating the Glossary. Default: false. 



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
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::UpdateGlossaryRequest.new
    
    # Call the update_glossary method.
    result = client.update_glossary request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_glossary_category
    
    
    def update_glossary_category(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory
    def update_glossary_category(category: nil, update_mask: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Updates a GlossaryCategory resource.

**Overloads**
    
    
    def update_glossary_category(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Pass arguments to `update_glossary_category` via a request object, either of type [UpdateGlossaryCategoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateGlossaryCategoryRequest "Google::Cloud::Dataplex::V1::UpdateGlossaryCategoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::UpdateGlossaryCategoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateGlossaryCategoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_glossary_category(category: nil, update_mask: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryCategory

Pass arguments to `update_glossary_category` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **category** ([::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory), ::Hash) — Required. The GlossaryCategory to update. The GlossaryCategory's `name` field is used to identify the GlossaryCategory to update. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id} 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::GlossaryCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryCategory)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::UpdateGlossaryCategoryRequest.new
    
    # Call the update_glossary_category method.
    result = client.update_glossary_category request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::GlossaryCategory.
    p result

### #update_glossary_term
    
    
    def update_glossary_term(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm
    def update_glossary_term(term: nil, update_mask: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Updates a GlossaryTerm resource.

**Overloads**
    
    
    def update_glossary_term(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Pass arguments to `update_glossary_term` via a request object, either of type [UpdateGlossaryTermRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateGlossaryTermRequest "Google::Cloud::Dataplex::V1::UpdateGlossaryTermRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::UpdateGlossaryTermRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateGlossaryTermRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_glossary_term(term: nil, update_mask: nil) -> ::Google::Cloud::Dataplex::V1::GlossaryTerm

Pass arguments to `update_glossary_term` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **term** ([::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm), ::Hash) — Required. The GlossaryTerm to update. The GlossaryTerm's `name` field is used to identify the GlossaryTerm to update. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id} 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GlossaryTerm)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::UpdateGlossaryTermRequest.new
    
    # Call the update_glossary_term method.
    result = client.update_glossary_term request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::GlossaryTerm.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
