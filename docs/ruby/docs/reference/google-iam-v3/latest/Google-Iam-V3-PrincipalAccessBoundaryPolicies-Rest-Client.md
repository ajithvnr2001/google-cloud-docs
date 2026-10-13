---
url: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client/
title: Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client (v0.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:53.171521+00:00
---

# Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client (v0.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client (v0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.5.0  0.4.1  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Identity and Access Management (IAM) V3 API class Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.

REST client for the PrincipalAccessBoundaryPolicies service.

Manages Identity and Access Management (IAM) principal access boundary policies.

## Inherits

  * Object 



## Includes

  * [Google::Iam::V3::PrincipalAccessBoundaryPolicies::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the PrincipalAccessBoundaryPolicies Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client-Configuration "Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all PrincipalAccessBoundaryPolicies clients
    ::Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the PrincipalAccessBoundaryPolicies Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client#Google__Iam__V3__PrincipalAccessBoundaryPolicies__Rest__Client_configure_class_ "Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client-Configuration "Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client-Configuration)) 



### #create_principal_access_boundary_policy
    
    
    def create_principal_access_boundary_policy(request, options = nil) -> ::Gapic::Operation
    def create_principal_access_boundary_policy(parent: nil, principal_access_boundary_policy_id: nil, principal_access_boundary_policy: nil, validate_only: nil) -> ::Gapic::Operation

Creates a principal access boundary policy, and returns a long running operation.

**Overloads**
    
    
    def create_principal_access_boundary_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_principal_access_boundary_policy` via a request object, either of type [CreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-CreatePrincipalAccessBoundaryPolicyRequest "Google::Iam::V3::CreatePrincipalAccessBoundaryPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V3::CreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-CreatePrincipalAccessBoundaryPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_principal_access_boundary_policy(parent: nil, principal_access_boundary_policy_id: nil, principal_access_boundary_policy: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_principal_access_boundary_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported.

Format: `organizations/{organization_id}/locations/{location}`

  * **principal_access_boundary_policy_id** (::String) — Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name.

This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/. 

  * **principal_access_boundary_policy** ([::Google::Iam::V3::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicy), ::Hash) — Required. The principal access boundary policy to create. 
  * **validate_only** (::Boolean) — Optional. If set, validate the request and preview the creation, but do not actually post it. 



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
    
    
    require "google/iam/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V3::CreatePrincipalAccessBoundaryPolicyRequest.new
    
    # Call the create_principal_access_boundary_policy method.
    result = client.create_principal_access_boundary_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_principal_access_boundary_policy
    
    
    def delete_principal_access_boundary_policy(request, options = nil) -> ::Gapic::Operation
    def delete_principal_access_boundary_policy(name: nil, etag: nil, validate_only: nil, force: nil) -> ::Gapic::Operation

Deletes a principal access boundary policy.

**Overloads**
    
    
    def delete_principal_access_boundary_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_principal_access_boundary_policy` via a request object, either of type [DeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-DeletePrincipalAccessBoundaryPolicyRequest "Google::Iam::V3::DeletePrincipalAccessBoundaryPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V3::DeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-DeletePrincipalAccessBoundaryPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_principal_access_boundary_policy(name: nil, etag: nil, validate_only: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_principal_access_boundary_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the principal access boundary policy to delete.

Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`

  * **etag** (::String) — Optional. The etag of the principal access boundary policy. If this is provided, it must match the server's etag. 
  * **validate_only** (::Boolean) — Optional. If set, validate the request and preview the deletion, but do not actually post it. 
  * **force** (::Boolean) — Optional. If set to true, the request will force the deletion of the policy even if the policy is referenced in policy bindings. 



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
    
    
    require "google/iam/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V3::DeletePrincipalAccessBoundaryPolicyRequest.new
    
    # Call the delete_principal_access_boundary_policy method.
    result = client.delete_principal_access_boundary_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_principal_access_boundary_policy
    
    
    def get_principal_access_boundary_policy(request, options = nil) -> ::Google::Iam::V3::PrincipalAccessBoundaryPolicy
    def get_principal_access_boundary_policy(name: nil) -> ::Google::Iam::V3::PrincipalAccessBoundaryPolicy

Gets a principal access boundary policy.

**Overloads**
    
    
    def get_principal_access_boundary_policy(request, options = nil) -> ::Google::Iam::V3::PrincipalAccessBoundaryPolicy

Pass arguments to `get_principal_access_boundary_policy` via a request object, either of type [GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-GetPrincipalAccessBoundaryPolicyRequest "Google::Iam::V3::GetPrincipalAccessBoundaryPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V3::GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-GetPrincipalAccessBoundaryPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_principal_access_boundary_policy(name: nil) -> ::Google::Iam::V3::PrincipalAccessBoundaryPolicy

Pass arguments to `get_principal_access_boundary_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the principal access boundary policy to retrieve.

Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V3::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V3::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/iam/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V3::GetPrincipalAccessBoundaryPolicyRequest.new
    
    # Call the get_principal_access_boundary_policy method.
    result = client.get_principal_access_boundary_policy request
    
    # The returned object is of type Google::Iam::V3::PrincipalAccessBoundaryPolicy.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new PrincipalAccessBoundaryPolicies REST client object.

**Yields**

  * (config) — Configure the PrincipalAccessBoundaryPolicies client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_principal_access_boundary_policies
    
    
    def list_principal_access_boundary_policies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Iam::V3::PrincipalAccessBoundaryPolicy>
    def list_principal_access_boundary_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Iam::V3::PrincipalAccessBoundaryPolicy>

Lists principal access boundary policies.

**Overloads**
    
    
    def list_principal_access_boundary_policies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Iam::V3::PrincipalAccessBoundaryPolicy>

Pass arguments to `list_principal_access_boundary_policies` via a request object, either of type [ListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-ListPrincipalAccessBoundaryPoliciesRequest "Google::Iam::V3::ListPrincipalAccessBoundaryPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V3::ListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-ListPrincipalAccessBoundaryPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_principal_access_boundary_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Iam::V3::PrincipalAccessBoundaryPolicy>

Pass arguments to `list_principal_access_boundary_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource, which owns the collection of principal access boundary policies.

Format: `organizations/{organization_id}/locations/{location}`

  * **page_size** (::Integer) — Optional. The maximum number of principal access boundary policies to return. The service may return fewer than this value.

If unspecified, at most 50 principal access boundary policies will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000\. 

  * **page_token** (::String) — Optional. A page token, received from a previous `ListPrincipalAccessBoundaryPolicies` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPrincipalAccessBoundaryPolicies` must match the call that provided the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Iam::V3::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicy)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Iam::V3::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/iam/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V3::ListPrincipalAccessBoundaryPoliciesRequest.new
    
    # Call the list_principal_access_boundary_policies method.
    result = client.list_principal_access_boundary_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Iam::V3::PrincipalAccessBoundaryPolicy.
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
    
    
    def operations_client() -> ::Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Rest-Operations)) 



### #search_principal_access_boundary_policy_bindings
    
    
    def search_principal_access_boundary_policy_bindings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Iam::V3::PolicyBinding>
    def search_principal_access_boundary_policy_bindings(name: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Iam::V3::PolicyBinding>

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

**Overloads**
    
    
    def search_principal_access_boundary_policy_bindings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Iam::V3::PolicyBinding>

Pass arguments to `search_principal_access_boundary_policy_bindings` via a request object, either of type [SearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-SearchPrincipalAccessBoundaryPolicyBindingsRequest "Google::Iam::V3::SearchPrincipalAccessBoundaryPolicyBindingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V3::SearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-SearchPrincipalAccessBoundaryPolicyBindingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def search_principal_access_boundary_policy_bindings(name: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Iam::V3::PolicyBinding>

Pass arguments to `search_principal_access_boundary_policy_bindings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the principal access boundary policy. Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`
  * **page_size** (::Integer) — Optional. The maximum number of policy bindings to return. The service may return fewer than this value.

If unspecified, at most 50 policy bindings will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 

  * **page_token** (::String) — Optional. A page token, received from a previous `SearchPrincipalAccessBoundaryPolicyBindingsRequest` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `SearchPrincipalAccessBoundaryPolicyBindingsRequest` must match the call that provided the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Iam::V3::PolicyBinding](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PolicyBinding)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Iam::V3::PolicyBinding](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PolicyBinding)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/iam/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V3::SearchPrincipalAccessBoundaryPolicyBindingsRequest.new
    
    # Call the search_principal_access_boundary_policy_bindings method.
    result = client.search_principal_access_boundary_policy_bindings request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Iam::V3::PolicyBinding.
      p item
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_principal_access_boundary_policy
    
    
    def update_principal_access_boundary_policy(request, options = nil) -> ::Gapic::Operation
    def update_principal_access_boundary_policy(principal_access_boundary_policy: nil, validate_only: nil, update_mask: nil) -> ::Gapic::Operation

Updates a principal access boundary policy.

**Overloads**
    
    
    def update_principal_access_boundary_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_principal_access_boundary_policy` via a request object, either of type [UpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-UpdatePrincipalAccessBoundaryPolicyRequest "Google::Iam::V3::UpdatePrincipalAccessBoundaryPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V3::UpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-UpdatePrincipalAccessBoundaryPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_principal_access_boundary_policy(principal_access_boundary_policy: nil, validate_only: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_principal_access_boundary_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **principal_access_boundary_policy** ([::Google::Iam::V3::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicy), ::Hash) — Required. The principal access boundary policy to update.

The principal access boundary policy's `name` field is used to identify the policy to update. 

  * **validate_only** (::Boolean) — Optional. If set, validate the request and preview the update, but do not actually post it. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The list of fields to update 



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
    
    
    require "google/iam/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V3::PrincipalAccessBoundaryPolicies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V3::UpdatePrincipalAccessBoundaryPolicyRequest.new
    
    # Call the update_principal_access_boundary_policy method.
    result = client.update_principal_access_boundary_policy request
    
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
