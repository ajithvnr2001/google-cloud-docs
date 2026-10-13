---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client/
title: Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:48.822509+00:00
---

# Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.1  2.2.2  2.1.1  2.0.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.2  0.20.1  0.19.0  0.18.1  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1 

Reference documentation and code samples for the Data Catalog V1 API class Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.

REST client for the PolicyTagManager service.

Policy Tag Manager API service allows you to manage your policy tags and taxonomies.

Policy tags are used to tag BigQuery columns and apply additional access control policies. A taxonomy is a hierarchical grouping of policy tags that classify data along a common axis.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::DataCatalog::V1::PolicyTagManager::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the PolicyTagManager Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client-Configuration "Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all PolicyTagManager clients
    ::Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the PolicyTagManager Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client#Google__Cloud__DataCatalog__V1__PolicyTagManager__Rest__Client_configure_class_ "Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client-Configuration "Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client-Configuration)) 



### #create_policy_tag
    
    
    def create_policy_tag(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag
    def create_policy_tag(parent: nil, policy_tag: nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Creates a policy tag in a taxonomy.

**Overloads**
    
    
    def create_policy_tag(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Pass arguments to `create_policy_tag` via a request object, either of type [CreatePolicyTagRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-CreatePolicyTagRequest "Google::Cloud::DataCatalog::V1::CreatePolicyTagRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::CreatePolicyTagRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-CreatePolicyTagRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_policy_tag(parent: nil, policy_tag: nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Pass arguments to `create_policy_tag` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource name of the taxonomy that the policy tag will belong to. 
  * **policy_tag** ([::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag), ::Hash) — The policy tag to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::CreatePolicyTagRequest.new
    
    # Call the create_policy_tag method.
    result = client.create_policy_tag request
    
    # The returned object is of type Google::Cloud::DataCatalog::V1::PolicyTag.
    p result

### #create_taxonomy
    
    
    def create_taxonomy(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy
    def create_taxonomy(parent: nil, taxonomy: nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Creates a taxonomy in a specified project.

The taxonomy is initially empty, that is, it doesn't contain policy tags.

**Overloads**
    
    
    def create_taxonomy(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Pass arguments to `create_taxonomy` via a request object, either of type [CreateTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-CreateTaxonomyRequest "Google::Cloud::DataCatalog::V1::CreateTaxonomyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::CreateTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-CreateTaxonomyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_taxonomy(parent: nil, taxonomy: nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Pass arguments to `create_taxonomy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource name of the project that the taxonomy will belong to. 
  * **taxonomy** ([::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy), ::Hash) — The taxonomy to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::CreateTaxonomyRequest.new
    
    # Call the create_taxonomy method.
    result = client.create_taxonomy request
    
    # The returned object is of type Google::Cloud::DataCatalog::V1::Taxonomy.
    p result

### #delete_policy_tag
    
    
    def delete_policy_tag(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_policy_tag(name: nil) -> ::Google::Protobuf::Empty

Deletes a policy tag together with the following:

  * All of its descendant policy tags, if any
  * Policies associated with the policy tag and its descendants
  * References from BigQuery table schema of the policy tag and its descendants



**Overloads**
    
    
    def delete_policy_tag(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_policy_tag` via a request object, either of type [DeletePolicyTagRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DeletePolicyTagRequest "Google::Cloud::DataCatalog::V1::DeletePolicyTagRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::DeletePolicyTagRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DeletePolicyTagRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_policy_tag(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_policy_tag` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the policy tag to delete.

Note: All of its descendant policy tags are also deleted. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::DeletePolicyTagRequest.new
    
    # Call the delete_policy_tag method.
    result = client.delete_policy_tag request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_taxonomy
    
    
    def delete_taxonomy(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_taxonomy(name: nil) -> ::Google::Protobuf::Empty

Deletes a taxonomy, including all policy tags in this taxonomy, their associated policies, and the policy tags references from BigQuery columns.

**Overloads**
    
    
    def delete_taxonomy(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_taxonomy` via a request object, either of type [DeleteTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DeleteTaxonomyRequest "Google::Cloud::DataCatalog::V1::DeleteTaxonomyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::DeleteTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DeleteTaxonomyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_taxonomy(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_taxonomy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the taxonomy to delete.

Note: All policy tags in this taxonomy are also deleted. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::DeleteTaxonomyRequest.new
    
    # Call the delete_taxonomy method.
    result = client.delete_taxonomy request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_iam_policy
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Gets the IAM policy for a policy tag or a taxonomy.

**Overloads**
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via a request object, either of type Iam::V1::GetIamPolicyRequest or an equivalent Hash. 

**Parameters**

  * **request** (::Google::Iam::V1::GetIamPolicyRequest, ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. 
  * **options** (::Google::Iam::V1::GetPolicyOptions, ::Hash) — OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Google::Iam::V1::Policy) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Google::Iam::V1::Policy) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::GetIamPolicyRequest.new
    
    # Call the get_iam_policy method.
    result = client.get_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #get_policy_tag
    
    
    def get_policy_tag(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag
    def get_policy_tag(name: nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Gets a policy tag.

**Overloads**
    
    
    def get_policy_tag(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Pass arguments to `get_policy_tag` via a request object, either of type [GetPolicyTagRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-GetPolicyTagRequest "Google::Cloud::DataCatalog::V1::GetPolicyTagRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::GetPolicyTagRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-GetPolicyTagRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_policy_tag(name: nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Pass arguments to `get_policy_tag` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the policy tag. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::GetPolicyTagRequest.new
    
    # Call the get_policy_tag method.
    result = client.get_policy_tag request
    
    # The returned object is of type Google::Cloud::DataCatalog::V1::PolicyTag.
    p result

### #get_taxonomy
    
    
    def get_taxonomy(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy
    def get_taxonomy(name: nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Gets a taxonomy.

**Overloads**
    
    
    def get_taxonomy(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Pass arguments to `get_taxonomy` via a request object, either of type [GetTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-GetTaxonomyRequest "Google::Cloud::DataCatalog::V1::GetTaxonomyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::GetTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-GetTaxonomyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_taxonomy(name: nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Pass arguments to `get_taxonomy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the taxonomy to get. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::GetTaxonomyRequest.new
    
    # Call the get_taxonomy method.
    result = client.get_taxonomy request
    
    # The returned object is of type Google::Cloud::DataCatalog::V1::Taxonomy.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new PolicyTagManager REST client object.

**Yields**

  * (config) — Configure the PolicyTagManager client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTagManager-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_policy_tags
    
    
    def list_policy_tags(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DataCatalog::V1::PolicyTag>
    def list_policy_tags(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DataCatalog::V1::PolicyTag>

Lists all policy tags in a taxonomy.

**Overloads**
    
    
    def list_policy_tags(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DataCatalog::V1::PolicyTag>

Pass arguments to `list_policy_tags` via a request object, either of type [ListPolicyTagsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-ListPolicyTagsRequest "Google::Cloud::DataCatalog::V1::ListPolicyTagsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::ListPolicyTagsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-ListPolicyTagsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_policy_tags(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DataCatalog::V1::PolicyTag>

Pass arguments to `list_policy_tags` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource name of the taxonomy to list the policy tags of. 
  * **page_size** (::Integer) — The maximum number of items to return. Must be a value between 1 and 1000 inclusively. If not set, defaults to 50. 
  * **page_token** (::String) — The pagination token of the next results page. If not set, returns the first page.

The token is returned in the response to a previous list request. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::ListPolicyTagsRequest.new
    
    # Call the list_policy_tags method.
    result = client.list_policy_tags request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::DataCatalog::V1::PolicyTag.
      p item
    end

### #list_taxonomies
    
    
    def list_taxonomies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DataCatalog::V1::Taxonomy>
    def list_taxonomies(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DataCatalog::V1::Taxonomy>

Lists all taxonomies in a project in a particular location that you have a permission to view.

**Overloads**
    
    
    def list_taxonomies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DataCatalog::V1::Taxonomy>

Pass arguments to `list_taxonomies` via a request object, either of type [ListTaxonomiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-ListTaxonomiesRequest "Google::Cloud::DataCatalog::V1::ListTaxonomiesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::ListTaxonomiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-ListTaxonomiesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_taxonomies(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DataCatalog::V1::Taxonomy>

Pass arguments to `list_taxonomies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource name of the project to list the taxonomies of. 
  * **page_size** (::Integer) — The maximum number of items to return. Must be a value between 1 and 1000 inclusively. If not set, defaults to 50. 
  * **page_token** (::String) — The pagination token of the next results page. If not set, the first page is returned.

The token is returned in the response to a previous list request. 

  * **filter** (::String) — Supported field for filter is 'service' and value is 'dataplex'. Eg: service=dataplex. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::ListTaxonomiesRequest.new
    
    # Call the list_taxonomies method.
    result = client.list_taxonomies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::DataCatalog::V1::Taxonomy.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #set_iam_policy
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Sets the IAM policy for a policy tag or a taxonomy.

**Overloads**
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via a request object, either of type Iam::V1::SetIamPolicyRequest or an equivalent Hash. 

**Parameters**

  * **request** (::Google::Iam::V1::SetIamPolicyRequest, ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 
  * **policy** (::Google::Iam::V1::Policy, ::Hash) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-FieldMask), ::Hash) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Google::Iam::V1::Policy) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Google::Iam::V1::Policy) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::SetIamPolicyRequest.new
    
    # Call the set_iam_policy method.
    result = client.set_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Returns your permissions on a specified policy tag or taxonomy.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type Iam::V1::TestIamPermissionsRequest or an equivalent Hash. 

**Parameters**

  * **request** (::Google::Iam::V1::TestIamPermissionsRequest, ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. 
  * **permissions** (::Array<::String>) — The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions). 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Google::Iam::V1::TestIamPermissionsResponse) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Google::Iam::V1::TestIamPermissionsResponse) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::TestIamPermissionsRequest.new
    
    # Call the test_iam_permissions method.
    result = client.test_iam_permissions request
    
    # The returned object is of type Google::Iam::V1::TestIamPermissionsResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_policy_tag
    
    
    def update_policy_tag(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag
    def update_policy_tag(policy_tag: nil, update_mask: nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Updates a policy tag, including its display name, description, and parent policy tag.

**Overloads**
    
    
    def update_policy_tag(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Pass arguments to `update_policy_tag` via a request object, either of type [UpdatePolicyTagRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-UpdatePolicyTagRequest "Google::Cloud::DataCatalog::V1::UpdatePolicyTagRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::UpdatePolicyTagRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-UpdatePolicyTagRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_policy_tag(policy_tag: nil, update_mask: nil) -> ::Google::Cloud::DataCatalog::V1::PolicyTag

Pass arguments to `update_policy_tag` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **policy_tag** ([::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag), ::Hash) — The policy tag to update. You can update only its description, display name, and parent policy tag fields. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Specifies the fields to update.

You can update only display name, description, and parent policy tag. If not set, defaults to all updatable fields. For more information, see [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DataCatalog::V1::PolicyTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-PolicyTag)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::UpdatePolicyTagRequest.new
    
    # Call the update_policy_tag method.
    result = client.update_policy_tag request
    
    # The returned object is of type Google::Cloud::DataCatalog::V1::PolicyTag.
    p result

### #update_taxonomy
    
    
    def update_taxonomy(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy
    def update_taxonomy(taxonomy: nil, update_mask: nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Updates a taxonomy, including its display name, description, and activated policy types.

**Overloads**
    
    
    def update_taxonomy(request, options = nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Pass arguments to `update_taxonomy` via a request object, either of type [UpdateTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-UpdateTaxonomyRequest "Google::Cloud::DataCatalog::V1::UpdateTaxonomyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DataCatalog::V1::UpdateTaxonomyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-UpdateTaxonomyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_taxonomy(taxonomy: nil, update_mask: nil) -> ::Google::Cloud::DataCatalog::V1::Taxonomy

Pass arguments to `update_taxonomy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **taxonomy** ([::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy), ::Hash) — The taxonomy to update. You can update only its description, display name, and activated policy types. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Specifies fields to update. If not set, defaults to all fields you can update.

For more information, see [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DataCatalog::V1::Taxonomy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-Taxonomy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/data_catalog/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DataCatalog::V1::PolicyTagManager::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DataCatalog::V1::UpdateTaxonomyRequest.new
    
    # Call the update_taxonomy method.
    result = client.update_taxonomy request
    
    # The returned object is of type Google::Cloud::DataCatalog::V1::Taxonomy.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
