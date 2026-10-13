---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:03.640898+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.

REST client for the DataTaxonomyService service.

DataTaxonomyService enables attribute-based governance. The resources currently offered include DataTaxonomy and DataAttribute.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dataplex::V1::DataTaxonomyService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the DataTaxonomyService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client-Configuration "Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all DataTaxonomyService clients
    ::Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the DataTaxonomyService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client#Google__Cloud__Dataplex__V1__DataTaxonomyService__Rest__Client_configure_class_ "Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client-Configuration "Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client-Configuration)) 



### #create_data_attribute
    
    
    def create_data_attribute(request, options = nil) -> ::Gapic::Operation
    def create_data_attribute(parent: nil, data_attribute_id: nil, data_attribute: nil, validate_only: nil) -> ::Gapic::Operation

Create a DataAttribute resource.

**Overloads**
    
    
    def create_data_attribute(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_data_attribute` via a request object, either of type [CreateDataAttributeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateDataAttributeRequest "Google::Cloud::Dataplex::V1::CreateDataAttributeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::CreateDataAttributeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateDataAttributeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_data_attribute(parent: nil, data_attribute_id: nil, data_attribute: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_data_attribute` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the parent data taxonomy projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id} 
  * **data_attribute_id** (::String) — 

Required. DataAttribute identifier.

    * Must contain only lowercase letters, numbers and hyphens.
    * Must start with a letter.
    * Must be between 1-63 characters.
    * Must end with a number or a letter.
    * Must be unique within the DataTaxonomy.
  * **data_attribute** ([::Google::Cloud::Dataplex::V1::DataAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttribute), ::Hash) — Required. DataAttribute resource. 
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::CreateDataAttributeRequest.new
    
    # Call the create_data_attribute method.
    result = client.create_data_attribute request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_data_attribute_binding
    
    
    def create_data_attribute_binding(request, options = nil) -> ::Gapic::Operation
    def create_data_attribute_binding(parent: nil, data_attribute_binding_id: nil, data_attribute_binding: nil, validate_only: nil) -> ::Gapic::Operation

Create a DataAttributeBinding resource.

**Overloads**
    
    
    def create_data_attribute_binding(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_data_attribute_binding` via a request object, either of type [CreateDataAttributeBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateDataAttributeBindingRequest "Google::Cloud::Dataplex::V1::CreateDataAttributeBindingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::CreateDataAttributeBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateDataAttributeBindingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_data_attribute_binding(parent: nil, data_attribute_binding_id: nil, data_attribute_binding: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_data_attribute_binding` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the parent data taxonomy projects/{project_number}/locations/{location_id} 
  * **data_attribute_binding_id** (::String) — 

Required. DataAttributeBinding identifier.

    * Must contain only lowercase letters, numbers and hyphens.
    * Must start with a letter.
    * Must be between 1-63 characters.
    * Must end with a number or a letter.
    * Must be unique within the Location.
  * **data_attribute_binding** ([::Google::Cloud::Dataplex::V1::DataAttributeBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttributeBinding), ::Hash) — Required. DataAttributeBinding resource. 
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::CreateDataAttributeBindingRequest.new
    
    # Call the create_data_attribute_binding method.
    result = client.create_data_attribute_binding request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_data_taxonomy
    
    
    def create_data_taxonomy(request, options = nil) -> ::Gapic::Operation
    def create_data_taxonomy(parent: nil, data_taxonomy_id: nil, data_taxonomy: nil, validate_only: nil) -> ::Gapic::Operation

Create a DataTaxonomy resource.

**Overloads**
    
    
    def create_data_taxonomy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_data_taxonomy` via a request object, either of type [CreateDataTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateDataTaxonomyRequest "Google::Cloud::Dataplex::V1::CreateDataTaxonomyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::CreateDataTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateDataTaxonomyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_data_taxonomy(parent: nil, data_taxonomy_id: nil, data_taxonomy: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_data_taxonomy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) 
  * **data_taxonomy_id** (::String) — 

Required. DataTaxonomy identifier.

    * Must contain only lowercase letters, numbers and hyphens.
    * Must start with a letter.
    * Must be between 1-63 characters.
    * Must end with a number or a letter.
    * Must be unique within the Project.
  * **data_taxonomy** ([::Google::Cloud::Dataplex::V1::DataTaxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomy), ::Hash) — Required. DataTaxonomy resource. 
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::CreateDataTaxonomyRequest.new
    
    # Call the create_data_taxonomy method.
    result = client.create_data_taxonomy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_data_attribute
    
    
    def delete_data_attribute(request, options = nil) -> ::Gapic::Operation
    def delete_data_attribute(name: nil, etag: nil) -> ::Gapic::Operation

Deletes a Data Attribute resource.

**Overloads**
    
    
    def delete_data_attribute(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_data_attribute` via a request object, either of type [Google::Cloud::Dataplex::V1::DeleteDataAttributeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteDataAttributeRequest "Google::Cloud::Dataplex::V1::DeleteDataAttributeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::DeleteDataAttributeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteDataAttributeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_data_attribute(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_data_attribute` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the DataAttribute: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id} 
  * **etag** (::String) — Optional. If the client provided etag value does not match the current etag value, the DeleteDataAttribute method returns an ABORTED error response. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::DeleteDataAttributeRequest.new
    
    # Call the delete_data_attribute method.
    result = client.delete_data_attribute request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_data_attribute_binding
    
    
    def delete_data_attribute_binding(request, options = nil) -> ::Gapic::Operation
    def delete_data_attribute_binding(name: nil, etag: nil) -> ::Gapic::Operation

Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted.

**Overloads**
    
    
    def delete_data_attribute_binding(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_data_attribute_binding` via a request object, either of type [Google::Cloud::Dataplex::V1::DeleteDataAttributeBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteDataAttributeBindingRequest "Google::Cloud::Dataplex::V1::DeleteDataAttributeBindingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::DeleteDataAttributeBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteDataAttributeBindingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_data_attribute_binding(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_data_attribute_binding` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the DataAttributeBinding: projects/{project_number}/locations/{location_id}/dataAttributeBindings/{data_attribute_binding_id} 
  * **etag** (::String) — Required. If the client provided etag value does not match the current etag value, the DeleteDataAttributeBindingRequest method returns an ABORTED error response. Etags must be used when calling the DeleteDataAttributeBinding. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::DeleteDataAttributeBindingRequest.new
    
    # Call the delete_data_attribute_binding method.
    result = client.delete_data_attribute_binding request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_data_taxonomy
    
    
    def delete_data_taxonomy(request, options = nil) -> ::Gapic::Operation
    def delete_data_taxonomy(name: nil, etag: nil) -> ::Gapic::Operation

Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted.

**Overloads**
    
    
    def delete_data_taxonomy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_data_taxonomy` via a request object, either of type [Google::Cloud::Dataplex::V1::DeleteDataTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteDataTaxonomyRequest "Google::Cloud::Dataplex::V1::DeleteDataTaxonomyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::DeleteDataTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteDataTaxonomyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_data_taxonomy(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_data_taxonomy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the DataTaxonomy: projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id} 
  * **etag** (::String) — Optional. If the client provided etag value does not match the current etag value,the DeleteDataTaxonomy method returns an ABORTED error. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::DeleteDataTaxonomyRequest.new
    
    # Call the delete_data_taxonomy method.
    result = client.delete_data_taxonomy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_data_attribute
    
    
    def get_data_attribute(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataAttribute
    def get_data_attribute(name: nil) -> ::Google::Cloud::Dataplex::V1::DataAttribute

Retrieves a Data Attribute resource.

**Overloads**
    
    
    def get_data_attribute(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataAttribute

Pass arguments to `get_data_attribute` via a request object, either of type [GetDataAttributeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataAttributeRequest "Google::Cloud::Dataplex::V1::GetDataAttributeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GetDataAttributeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataAttributeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_data_attribute(name: nil) -> ::Google::Cloud::Dataplex::V1::DataAttribute

Pass arguments to `get_data_attribute` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the dataAttribute: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::DataAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttribute)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::DataAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttribute)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GetDataAttributeRequest.new
    
    # Call the get_data_attribute method.
    result = client.get_data_attribute request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::DataAttribute.
    p result

### #get_data_attribute_binding
    
    
    def get_data_attribute_binding(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataAttributeBinding
    def get_data_attribute_binding(name: nil) -> ::Google::Cloud::Dataplex::V1::DataAttributeBinding

Retrieves a DataAttributeBinding resource.

**Overloads**
    
    
    def get_data_attribute_binding(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataAttributeBinding

Pass arguments to `get_data_attribute_binding` via a request object, either of type [GetDataAttributeBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataAttributeBindingRequest "Google::Cloud::Dataplex::V1::GetDataAttributeBindingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GetDataAttributeBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataAttributeBindingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_data_attribute_binding(name: nil) -> ::Google::Cloud::Dataplex::V1::DataAttributeBinding

Pass arguments to `get_data_attribute_binding` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the DataAttributeBinding: projects/{project_number}/locations/{location_id}/dataAttributeBindings/{data_attribute_binding_id} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::DataAttributeBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttributeBinding)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::DataAttributeBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttributeBinding)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GetDataAttributeBindingRequest.new
    
    # Call the get_data_attribute_binding method.
    result = client.get_data_attribute_binding request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::DataAttributeBinding.
    p result

### #get_data_taxonomy
    
    
    def get_data_taxonomy(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataTaxonomy
    def get_data_taxonomy(name: nil) -> ::Google::Cloud::Dataplex::V1::DataTaxonomy

Retrieves a DataTaxonomy resource.

**Overloads**
    
    
    def get_data_taxonomy(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataTaxonomy

Pass arguments to `get_data_taxonomy` via a request object, either of type [GetDataTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataTaxonomyRequest "Google::Cloud::Dataplex::V1::GetDataTaxonomyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GetDataTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataTaxonomyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_data_taxonomy(name: nil) -> ::Google::Cloud::Dataplex::V1::DataTaxonomy

Pass arguments to `get_data_taxonomy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::DataTaxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::DataTaxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GetDataTaxonomyRequest.new
    
    # Call the get_data_taxonomy method.
    result = client.get_data_taxonomy request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::DataTaxonomy.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new DataTaxonomyService REST client object.

**Yields**

  * (config) — Configure the DataTaxonomyService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_data_attribute_bindings
    
    
    def list_data_attribute_bindings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataAttributeBinding>
    def list_data_attribute_bindings(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataAttributeBinding>

Lists DataAttributeBinding resources in a project and location.

**Overloads**
    
    
    def list_data_attribute_bindings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataAttributeBinding>

Pass arguments to `list_data_attribute_bindings` via a request object, either of type [ListDataAttributeBindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataAttributeBindingsRequest "Google::Cloud::Dataplex::V1::ListDataAttributeBindingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::ListDataAttributeBindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataAttributeBindingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_data_attribute_bindings(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataAttributeBinding>

Pass arguments to `list_data_attribute_bindings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location: projects/{project_number}/locations/{location_id} 
  * **page_size** (::Integer) — Optional. Maximum number of DataAttributeBindings to return. The service may return fewer than this value. If unspecified, at most 10 DataAttributeBindings will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. Page token received from a previous `ListDataAttributeBindings` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataAttributeBindings` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Filter request. Filter using resource: filter=resource:"resource-name" Filter using attribute: filter=attributes:"attribute-name" Filter using attribute in paths list: filter=paths.attributes:"attribute-name" 
  * **order_by** (::String) — Optional. Order by fields for the result. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataAttributeBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttributeBinding)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataAttributeBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttributeBinding)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::ListDataAttributeBindingsRequest.new
    
    # Call the list_data_attribute_bindings method.
    result = client.list_data_attribute_bindings request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataplex::V1::DataAttributeBinding.
      p item
    end

### #list_data_attributes
    
    
    def list_data_attributes(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataAttribute>
    def list_data_attributes(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataAttribute>

Lists Data Attribute resources in a DataTaxonomy.

**Overloads**
    
    
    def list_data_attributes(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataAttribute>

Pass arguments to `list_data_attributes` via a request object, either of type [ListDataAttributesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataAttributesRequest "Google::Cloud::Dataplex::V1::ListDataAttributesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::ListDataAttributesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataAttributesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_data_attributes(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataAttribute>

Pass arguments to `list_data_attributes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the DataTaxonomy: projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id} 
  * **page_size** (::Integer) — Optional. Maximum number of DataAttributes to return. The service may return fewer than this value. If unspecified, at most 10 dataAttributes will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. Page token received from a previous `ListDataAttributes` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataAttributes` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Filter request. 
  * **order_by** (::String) — Optional. Order by fields for the result. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttribute)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttribute)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::ListDataAttributesRequest.new
    
    # Call the list_data_attributes method.
    result = client.list_data_attributes request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataplex::V1::DataAttribute.
      p item
    end

### #list_data_taxonomies
    
    
    def list_data_taxonomies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataTaxonomy>
    def list_data_taxonomies(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataTaxonomy>

Lists DataTaxonomy resources in a project and location.

**Overloads**
    
    
    def list_data_taxonomies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataTaxonomy>

Pass arguments to `list_data_taxonomies` via a request object, either of type [ListDataTaxonomiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataTaxonomiesRequest "Google::Cloud::Dataplex::V1::ListDataTaxonomiesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::ListDataTaxonomiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataTaxonomiesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_data_taxonomies(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataTaxonomy>

Pass arguments to `list_data_taxonomies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the DataTaxonomy location, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region. 
  * **page_size** (::Integer) — Optional. Maximum number of DataTaxonomies to return. The service may return fewer than this value. If unspecified, at most 10 DataTaxonomies will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. Page token received from a previous `ListDataTaxonomies` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataTaxonomies` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Filter request. 
  * **order_by** (::String) — Optional. Order by fields for the result. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataTaxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomy)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataTaxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::ListDataTaxonomiesRequest.new
    
    # Call the list_data_taxonomies method.
    result = client.list_data_taxonomies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataplex::V1::DataTaxonomy.
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
    
    
    def operations_client() -> ::Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomyService-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_data_attribute
    
    
    def update_data_attribute(request, options = nil) -> ::Gapic::Operation
    def update_data_attribute(update_mask: nil, data_attribute: nil, validate_only: nil) -> ::Gapic::Operation

Updates a DataAttribute resource.

**Overloads**
    
    
    def update_data_attribute(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_data_attribute` via a request object, either of type [UpdateDataAttributeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateDataAttributeRequest "Google::Cloud::Dataplex::V1::UpdateDataAttributeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::UpdateDataAttributeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateDataAttributeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_data_attribute(update_mask: nil, data_attribute: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `update_data_attribute` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Mask of fields to update. 
  * **data_attribute** ([::Google::Cloud::Dataplex::V1::DataAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttribute), ::Hash) — Required. Only fields specified in `update_mask` are updated. 
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::UpdateDataAttributeRequest.new
    
    # Call the update_data_attribute method.
    result = client.update_data_attribute request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_data_attribute_binding
    
    
    def update_data_attribute_binding(request, options = nil) -> ::Gapic::Operation
    def update_data_attribute_binding(update_mask: nil, data_attribute_binding: nil, validate_only: nil) -> ::Gapic::Operation

Updates a DataAttributeBinding resource.

**Overloads**
    
    
    def update_data_attribute_binding(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_data_attribute_binding` via a request object, either of type [UpdateDataAttributeBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateDataAttributeBindingRequest "Google::Cloud::Dataplex::V1::UpdateDataAttributeBindingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::UpdateDataAttributeBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateDataAttributeBindingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_data_attribute_binding(update_mask: nil, data_attribute_binding: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `update_data_attribute_binding` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Mask of fields to update. 
  * **data_attribute_binding** ([::Google::Cloud::Dataplex::V1::DataAttributeBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataAttributeBinding), ::Hash) — Required. Only fields specified in `update_mask` are updated. 
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::UpdateDataAttributeBindingRequest.new
    
    # Call the update_data_attribute_binding method.
    result = client.update_data_attribute_binding request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_data_taxonomy
    
    
    def update_data_taxonomy(request, options = nil) -> ::Gapic::Operation
    def update_data_taxonomy(update_mask: nil, data_taxonomy: nil, validate_only: nil) -> ::Gapic::Operation

Updates a DataTaxonomy resource.

**Overloads**
    
    
    def update_data_taxonomy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_data_taxonomy` via a request object, either of type [UpdateDataTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateDataTaxonomyRequest "Google::Cloud::Dataplex::V1::UpdateDataTaxonomyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::UpdateDataTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateDataTaxonomyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_data_taxonomy(update_mask: nil, data_taxonomy: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `update_data_taxonomy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Mask of fields to update. 
  * **data_taxonomy** ([::Google::Cloud::Dataplex::V1::DataTaxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataTaxonomy), ::Hash) — Required. Only fields specified in `update_mask` are updated. 
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



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
    client = Google::Cloud::Dataplex::V1::DataTaxonomyService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::UpdateDataTaxonomyRequest.new
    
    # Call the update_data_taxonomy method.
    result = client.update_data_taxonomy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
