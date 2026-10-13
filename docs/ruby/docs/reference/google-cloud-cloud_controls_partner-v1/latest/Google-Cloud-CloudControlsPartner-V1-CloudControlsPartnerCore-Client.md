---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client/
title: Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client (v2.4.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:29.829768+00:00
---

# Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client (v2.4.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client (v2.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.1 (latest)  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.1.1 

Reference documentation and code samples for the Cloud Controls Partner V1 API class Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.

Client for the CloudControlsPartnerCore service.

Service describing handlers for resources

## Inherits

  * Object 



## Includes

  * [Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CloudControlsPartnerCore Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client-Configuration "Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CloudControlsPartnerCore clients
    ::Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the CloudControlsPartnerCore Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client#Google__Cloud__CloudControlsPartner__V1__CloudControlsPartnerCore__Client_configure_class_ "Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client-Configuration "Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client-Configuration)) 



### #create_customer
    
    
    def create_customer(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer
    def create_customer(parent: nil, customer: nil, customer_id: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Creates a new customer.

**Overloads**
    
    
    def create_customer(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Pass arguments to `create_customer` via a request object, either of type [Google::Cloud::CloudControlsPartner::V1::CreateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CreateCustomerRequest "Google::Cloud::CloudControlsPartner::V1::CreateCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::CreateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CreateCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_customer(parent: nil, customer: nil, customer_id: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Pass arguments to `create_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource Format: `organizations/{organization}/locations/{location}`
  * **customer** ([::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer), ::Hash) — Required. The customer to create. 
  * **customer_id** (::String) — Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::CreateCustomerRequest.new
    
    # Call the create_customer method.
    result = client.create_customer request
    
    # The returned object is of type Google::Cloud::CloudControlsPartner::V1::Customer.
    p result

### #delete_customer
    
    
    def delete_customer(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_customer(name: nil) -> ::Google::Protobuf::Empty

Delete details of a single customer

**Overloads**
    
    
    def delete_customer(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_customer` via a request object, either of type [DeleteCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-DeleteCustomerRequest "Google::Cloud::CloudControlsPartner::V1::DeleteCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::DeleteCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-DeleteCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_customer(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. name of the resource to be deleted format: name=organizations/_/locations/_ /customers/* 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::DeleteCustomerRequest.new
    
    # Call the delete_customer method.
    result = client.delete_customer request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_customer
    
    
    def get_customer(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer
    def get_customer(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Gets details of a single customer

**Overloads**
    
    
    def get_customer(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Pass arguments to `get_customer` via a request object, either of type [GetCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetCustomerRequest "Google::Cloud::CloudControlsPartner::V1::GetCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::GetCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_customer(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Pass arguments to `get_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::GetCustomerRequest.new
    
    # Call the get_customer method.
    result = client.get_customer request
    
    # The returned object is of type Google::Cloud::CloudControlsPartner::V1::Customer.
    p result

### #get_ekm_connections
    
    
    def get_ekm_connections(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::EkmConnections
    def get_ekm_connections(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::EkmConnections

Gets the EKM connections associated with a workload

**Overloads**
    
    
    def get_ekm_connections(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::EkmConnections

Pass arguments to `get_ekm_connections` via a request object, either of type [GetEkmConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetEkmConnectionsRequest "Google::Cloud::CloudControlsPartner::V1::GetEkmConnectionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::GetEkmConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetEkmConnectionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_ekm_connections(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::EkmConnections

Pass arguments to `get_ekm_connections` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudControlsPartner::V1::EkmConnections](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-EkmConnections)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::EkmConnections](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-EkmConnections)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::GetEkmConnectionsRequest.new
    
    # Call the get_ekm_connections method.
    result = client.get_ekm_connections request
    
    # The returned object is of type Google::Cloud::CloudControlsPartner::V1::EkmConnections.
    p result

### #get_partner
    
    
    def get_partner(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Partner
    def get_partner(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Partner

Get details of a Partner.

**Overloads**
    
    
    def get_partner(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Partner

Pass arguments to `get_partner` via a request object, either of type [GetPartnerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetPartnerRequest "Google::Cloud::CloudControlsPartner::V1::GetPartnerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::GetPartnerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetPartnerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_partner(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Partner

Pass arguments to `get_partner` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Format: `organizations/{organization}/locations/{location}/partner`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudControlsPartner::V1::Partner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Partner)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::Partner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Partner)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::GetPartnerRequest.new
    
    # Call the get_partner method.
    result = client.get_partner request
    
    # The returned object is of type Google::Cloud::CloudControlsPartner::V1::Partner.
    p result

### #get_partner_permissions
    
    
    def get_partner_permissions(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::PartnerPermissions
    def get_partner_permissions(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::PartnerPermissions

Gets the partner permissions granted for a workload

**Overloads**
    
    
    def get_partner_permissions(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::PartnerPermissions

Pass arguments to `get_partner_permissions` via a request object, either of type [GetPartnerPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetPartnerPermissionsRequest "Google::Cloud::CloudControlsPartner::V1::GetPartnerPermissionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::GetPartnerPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetPartnerPermissionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_partner_permissions(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::PartnerPermissions

Pass arguments to `get_partner_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource to get in the format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudControlsPartner::V1::PartnerPermissions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-PartnerPermissions)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::PartnerPermissions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-PartnerPermissions)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::GetPartnerPermissionsRequest.new
    
    # Call the get_partner_permissions method.
    result = client.get_partner_permissions request
    
    # The returned object is of type Google::Cloud::CloudControlsPartner::V1::PartnerPermissions.
    p result

### #get_workload
    
    
    def get_workload(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Workload
    def get_workload(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Workload

Gets details of a single workload

**Overloads**
    
    
    def get_workload(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Workload

Pass arguments to `get_workload` via a request object, either of type [GetWorkloadRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetWorkloadRequest "Google::Cloud::CloudControlsPartner::V1::GetWorkloadRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::GetWorkloadRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetWorkloadRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_workload(name: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Workload

Pass arguments to `get_workload` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudControlsPartner::V1::Workload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Workload)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::Workload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Workload)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::GetWorkloadRequest.new
    
    # Call the get_workload method.
    result = client.get_workload request
    
    # The returned object is of type Google::Cloud::CloudControlsPartner::V1::Workload.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CloudControlsPartnerCore client object.

**Yields**

  * (config) — Configure the CloudControlsPartnerCore client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerCore-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new do |config|
      config.timeout = 10.0
    end

### #list_access_approval_requests
    
    
    def list_access_approval_requests(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::AccessApprovalRequest>
    def list_access_approval_requests(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::AccessApprovalRequest>

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

**Overloads**
    
    
    def list_access_approval_requests(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::AccessApprovalRequest>

Pass arguments to `list_access_approval_requests` via a request object, either of type [ListAccessApprovalRequestsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListAccessApprovalRequestsRequest "Google::Cloud::CloudControlsPartner::V1::ListAccessApprovalRequestsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::ListAccessApprovalRequestsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListAccessApprovalRequestsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_access_approval_requests(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::AccessApprovalRequest>

Pass arguments to `list_access_approval_requests` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`
  * **page_size** (::Integer) — Optional. The maximum number of access requests to return. The service may return fewer than this value. If unspecified, at most 500 access requests will be returned. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListAccessApprovalRequests` call. Provide this to retrieve the subsequent page. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Hint for how to order the results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudControlsPartner::V1::AccessApprovalRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-AccessApprovalRequest)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudControlsPartner::V1::AccessApprovalRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-AccessApprovalRequest)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::ListAccessApprovalRequestsRequest.new
    
    # Call the list_access_approval_requests method.
    result = client.list_access_approval_requests request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudControlsPartner::V1::AccessApprovalRequest.
      p item
    end

### #list_customers
    
    
    def list_customers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::Customer>
    def list_customers(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::Customer>

Lists customers of a partner identified by its Google Cloud organization ID

**Overloads**
    
    
    def list_customers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::Customer>

Pass arguments to `list_customers` via a request object, either of type [ListCustomersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListCustomersRequest "Google::Cloud::CloudControlsPartner::V1::ListCustomersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::ListCustomersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListCustomersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_customers(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::Customer>

Pass arguments to `list_customers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource Format: `organizations/{organization}/locations/{location}`
  * **page_size** (::Integer) — The maximum number of Customers to return. The service may return fewer than this value. If unspecified, at most 500 Customers will be returned. 
  * **page_token** (::String) — A page token, received from a previous `ListCustomers` call. Provide this to retrieve the subsequent page. 
  * **filter** (::String) — Optional. Filtering results 
  * **order_by** (::String) — Optional. Hint for how to order the results 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::ListCustomersRequest.new
    
    # Call the list_customers method.
    result = client.list_customers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudControlsPartner::V1::Customer.
      p item
    end

### #list_workloads
    
    
    def list_workloads(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::Workload>
    def list_workloads(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::Workload>

Lists customer workloads for a given customer org id

**Overloads**
    
    
    def list_workloads(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::Workload>

Pass arguments to `list_workloads` via a request object, either of type [ListWorkloadsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListWorkloadsRequest "Google::Cloud::CloudControlsPartner::V1::ListWorkloadsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::ListWorkloadsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListWorkloadsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_workloads(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudControlsPartner::V1::Workload>

Pass arguments to `list_workloads` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}`
  * **page_size** (::Integer) — The maximum number of workloads to return. The service may return fewer than this value. If unspecified, at most 500 workloads will be returned. 
  * **page_token** (::String) — A page token, received from a previous `ListWorkloads` call. Provide this to retrieve the subsequent page. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Hint for how to order the results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudControlsPartner::V1::Workload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Workload)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudControlsPartner::V1::Workload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Workload)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::ListWorkloadsRequest.new
    
    # Call the list_workloads method.
    result = client.list_workloads request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudControlsPartner::V1::Workload.
      p item
    end

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



### #update_customer
    
    
    def update_customer(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer
    def update_customer(customer: nil, update_mask: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Update details of a single customer

**Overloads**
    
    
    def update_customer(request, options = nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Pass arguments to `update_customer` via a request object, either of type [UpdateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-UpdateCustomerRequest "Google::Cloud::CloudControlsPartner::V1::UpdateCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudControlsPartner::V1::UpdateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-UpdateCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_customer(customer: nil, update_mask: nil) -> ::Google::Cloud::CloudControlsPartner::V1::Customer

Pass arguments to `update_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **customer** ([::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer), ::Hash) — Required. The customer to update Format: `organizations/{organization}/locations/{location}/customers/{customer}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The list of fields to update 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Customer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_controls_partner/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerCore::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudControlsPartner::V1::UpdateCustomerRequest.new
    
    # Call the update_customer method.
    result = client.update_customer request
    
    # The returned object is of type Google::Cloud::CloudControlsPartner::V1::Customer.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
