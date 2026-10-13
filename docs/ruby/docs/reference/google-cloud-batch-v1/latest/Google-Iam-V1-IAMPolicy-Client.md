---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client/
title: Batch V1 API - Class Google::Iam::V1::IAMPolicy::Client (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:40.074757+00:00
---

# Batch V1 API - Class Google::Iam::V1::IAMPolicy::Client (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Batch V1 API - Class Google::Iam::V1::IAMPolicy::Client (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.2  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.21.0  0.20.1  0.19.2  0.18.3  0.17.4  0.16.2  0.15.1  0.14.0  0.13.1  0.12.0  0.11.1  0.10.5  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.3  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Batch V1 API class Google::Iam::V1::IAMPolicy::Client.

Client for the IAMPolicy service.

API Overview

Manages Identity and Access Management (IAM) policies.

Any implementation of an API that offers access control features implements the google.iam.v1.IAMPolicy interface.

### Data model

Access control is applied when a principal (user or service account), takes some action on a resource exposed by a service. Resources, identified by URI-like names, are the unit of access control specification. Service implementations can choose the granularity of access control and the supported permissions for their resources. For example one database service may allow access control to be specified only at the Table level, whereas another might allow access control to also be specified at the Column level.

### Policy Structure

See google.iam.v1.Policy

This is intentionally not a CRUD style API because access control policies are created and deleted implicitly with the resources to which they are attached.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the IAMPolicy Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client-Configuration "Google::Iam::V1::IAMPolicy::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all IAMPolicy clients
    ::Google::Iam::V1::IAMPolicy::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the IAMPolicy Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client#Google__Iam__V1__IAMPolicy__Client_configure_class_ "Google::Iam::V1::IAMPolicy::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client-Configuration "Google::Iam::V1::IAMPolicy::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client-Configuration)) 



### #get_iam_policy
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Overloads**
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via a request object, either of type [GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-GetIamPolicyRequest "Google::Iam::V1::GetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-GetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. 
  * **options** ([::Google::Iam::V1::GetPolicyOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-GetPolicyOptions), ::Hash) — OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/iam/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V1::IAMPolicy::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::GetIamPolicyRequest.new
    
    # Call the get_iam_policy method.
    result = client.get_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new IAMPolicy client object.

**Yields**

  * (config) — Configure the IAMPolicy client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-IAMPolicy-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Iam::V1::IAMPolicy::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Iam::V1::IAMPolicy::Client.new do |config|
      config.timeout = 10.0
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



### #set_iam_policy
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Overloads**
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via a request object, either of type [SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-SetIamPolicyRequest "Google::Iam::V1::SetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-SetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 
  * **policy** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-Policy), ::Hash) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Protobuf-FieldMask), ::Hash) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/iam/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V1::IAMPolicy::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::SetIamPolicyRequest.new
    
    # Call the set_iam_policy method.
    result = client.set_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-TestIamPermissionsRequest "Google::Iam::V1::TestIamPermissionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-TestIamPermissionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. 
  * **permissions** (::Array<::String>) — The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/iam/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Iam::V1::IAMPolicy::Client.new
    
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
