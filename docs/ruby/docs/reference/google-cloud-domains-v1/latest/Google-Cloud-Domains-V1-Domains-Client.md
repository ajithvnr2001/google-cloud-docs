---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client/
title: Cloud Domains V1 API - Class Google::Cloud::Domains::V1::Domains::Client (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:00.664564+00:00
---

# Cloud Domains V1 API - Class Google::Cloud::Domains::V1::Domains::Client (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Domains V1 API - Class Google::Cloud::Domains::V1::Domains::Client (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Domains V1 API class Google::Cloud::Domains::V1::Domains::Client.

Client for the Domains service.

The Cloud Domains API enables management and configuration of domain names.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Domains::V1::Domains::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Domains Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client-Configuration "Google::Cloud::Domains::V1::Domains::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Domains clients
    ::Google::Cloud::Domains::V1::Domains::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Domains Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client#Google__Cloud__Domains__V1__Domains__Client_configure_class_ "Google::Cloud::Domains::V1::Domains::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client-Configuration "Google::Cloud::Domains::V1::Domains::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client-Configuration)) 



### #configure_contact_settings
    
    
    def configure_contact_settings(request, options = nil) -> ::Gapic::Operation
    def configure_contact_settings(registration: nil, contact_settings: nil, update_mask: nil, contact_notices: nil, validate_only: nil) -> ::Gapic::Operation

Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact .

**Overloads**
    
    
    def configure_contact_settings(request, options = nil) -> ::Gapic::Operation

Pass arguments to `configure_contact_settings` via a request object, either of type [ConfigureContactSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ConfigureContactSettingsRequest "Google::Cloud::Domains::V1::ConfigureContactSettingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::ConfigureContactSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ConfigureContactSettingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def configure_contact_settings(registration: nil, contact_settings: nil, update_mask: nil, contact_notices: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `configure_contact_settings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **registration** (::String) — Required. The name of the `Registration` whose contact settings are being updated, in the format `projects/*/locations/*/registrations/*`. 
  * **contact_settings** ([::Google::Cloud::Domains::V1::ContactSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ContactSettings), ::Hash) — Fields of the `ContactSettings` to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The field mask describing which fields to update as a comma-separated list. For example, if only the registrant contact is being updated, the `update_mask` is `"registrant_contact"`. 
  * **contact_notices** (::Array<[::Google::Cloud::Domains::V1::ContactNotice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ContactNotice)>) — The list of contact notices that the caller acknowledges. The notices needed here depend on the values specified in `contact_settings`. 
  * **validate_only** (::Boolean) — Validate the request without actually updating the contact settings. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::ConfigureContactSettingsRequest.new
    
    # Call the configure_contact_settings method.
    result = client.configure_contact_settings request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #configure_dns_settings
    
    
    def configure_dns_settings(request, options = nil) -> ::Gapic::Operation
    def configure_dns_settings(registration: nil, dns_settings: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Updates a `Registration`'s DNS settings.

**Overloads**
    
    
    def configure_dns_settings(request, options = nil) -> ::Gapic::Operation

Pass arguments to `configure_dns_settings` via a request object, either of type [ConfigureDnsSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ConfigureDnsSettingsRequest "Google::Cloud::Domains::V1::ConfigureDnsSettingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::ConfigureDnsSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ConfigureDnsSettingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def configure_dns_settings(registration: nil, dns_settings: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `configure_dns_settings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **registration** (::String) — Required. The name of the `Registration` whose DNS settings are being updated, in the format `projects/*/locations/*/registrations/*`. 
  * **dns_settings** ([::Google::Cloud::Domains::V1::DnsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-DnsSettings), ::Hash) — Fields of the `DnsSettings` to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The field mask describing which fields to update as a comma-separated list. For example, if only the name servers are being updated for an existing Custom DNS configuration, the `update_mask` is `"custom_dns.name_servers"`.

When changing the DNS provider from one type to another, pass the new provider's field name as part of the field mask. For example, when changing from a Google Domains DNS configuration to a Custom DNS configuration, the `update_mask` is `"custom_dns"`. // 

  * **validate_only** (::Boolean) — Validate the request without actually updating the DNS settings. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::ConfigureDnsSettingsRequest.new
    
    # Call the configure_dns_settings method.
    result = client.configure_dns_settings request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #configure_management_settings
    
    
    def configure_management_settings(request, options = nil) -> ::Gapic::Operation
    def configure_management_settings(registration: nil, management_settings: nil, update_mask: nil) -> ::Gapic::Operation

Updates a `Registration`'s management settings.

**Overloads**
    
    
    def configure_management_settings(request, options = nil) -> ::Gapic::Operation

Pass arguments to `configure_management_settings` via a request object, either of type [ConfigureManagementSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ConfigureManagementSettingsRequest "Google::Cloud::Domains::V1::ConfigureManagementSettingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::ConfigureManagementSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ConfigureManagementSettingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def configure_management_settings(registration: nil, management_settings: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `configure_management_settings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **registration** (::String) — Required. The name of the `Registration` whose management settings are being updated, in the format `projects/*/locations/*/registrations/*`. 
  * **management_settings** ([::Google::Cloud::Domains::V1::ManagementSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ManagementSettings), ::Hash) — Fields of the `ManagementSettings` to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The field mask describing which fields to update as a comma-separated list. For example, if only the transfer lock is being updated, the `update_mask` is `"transfer_lock_state"`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::ConfigureManagementSettingsRequest.new
    
    # Call the configure_management_settings method.
    result = client.configure_management_settings request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_registration
    
    
    def delete_registration(request, options = nil) -> ::Gapic::Operation
    def delete_registration(name: nil) -> ::Gapic::Operation

Deletes a `Registration` resource.

This method works on any `Registration` resource using [Subscription or Commitment billing](https://docs.cloud.google.com/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past.

For `Registration` resources using [Monthly billing](https://docs.cloud.google.com/domains/pricing#billing-models), this method works if:

  * `state` is `EXPORTED` with `expire_time` in the past
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED`



When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

**Overloads**
    
    
    def delete_registration(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_registration` via a request object, either of type [Google::Cloud::Domains::V1::DeleteRegistrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-DeleteRegistrationRequest "Google::Cloud::Domains::V1::DeleteRegistrationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::DeleteRegistrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-DeleteRegistrationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_registration(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_registration` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the `Registration` to delete, in the format `projects/*/locations/*/registrations/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::DeleteRegistrationRequest.new
    
    # Call the delete_registration method.
    result = client.delete_registration request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_registration
    
    
    def export_registration(request, options = nil) -> ::Gapic::Operation
    def export_registration(name: nil) -> ::Gapic::Operation

Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.

When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

**Overloads**
    
    
    def export_registration(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_registration` via a request object, either of type [ExportRegistrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ExportRegistrationRequest "Google::Cloud::Domains::V1::ExportRegistrationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::ExportRegistrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ExportRegistrationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def export_registration(name: nil) -> ::Gapic::Operation

Pass arguments to `export_registration` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the `Registration` to export, in the format `projects/*/locations/*/registrations/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::ExportRegistrationRequest.new
    
    # Call the export_registration method.
    result = client.export_registration request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_registration
    
    
    def get_registration(request, options = nil) -> ::Google::Cloud::Domains::V1::Registration
    def get_registration(name: nil) -> ::Google::Cloud::Domains::V1::Registration

Gets the details of a `Registration` resource.

**Overloads**
    
    
    def get_registration(request, options = nil) -> ::Google::Cloud::Domains::V1::Registration

Pass arguments to `get_registration` via a request object, either of type [GetRegistrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-GetRegistrationRequest "Google::Cloud::Domains::V1::GetRegistrationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::GetRegistrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-GetRegistrationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_registration(name: nil) -> ::Google::Cloud::Domains::V1::Registration

Pass arguments to `get_registration` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the `Registration` to get, in the format `projects/*/locations/*/registrations/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Domains::V1::Registration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Registration)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Domains::V1::Registration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Registration)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::GetRegistrationRequest.new
    
    # Call the get_registration method.
    result = client.get_registration request
    
    # The returned object is of type Google::Cloud::Domains::V1::Registration.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Domains client object.

**Yields**

  * (config) — Configure the Domains client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Domains::V1::Domains::Client.new do |config|
      config.timeout = 10.0
    end

### #list_registrations
    
    
    def list_registrations(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Domains::V1::Registration>
    def list_registrations(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Domains::V1::Registration>

Lists the `Registration` resources in a project.

**Overloads**
    
    
    def list_registrations(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Domains::V1::Registration>

Pass arguments to `list_registrations` via a request object, either of type [ListRegistrationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ListRegistrationsRequest "Google::Cloud::Domains::V1::ListRegistrationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::ListRegistrationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ListRegistrationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_registrations(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Domains::V1::Registration>

Pass arguments to `list_registrations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which to list `Registration`s, specified in the format `projects/*/locations/*`. 
  * **page_size** (::Integer) — Maximum number of results to return. 
  * **page_token** (::String) — When set to the `next_page_token` from a prior response, provides the next page of results. 
  * **filter** (::String) — Filter expression to restrict the `Registration`s returned.

The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, a boolean, or an enum value. The comparison operator should be one of =, !=, >, <, >=, <=, or : for prefix or wildcard matches.

For example, to filter to a specific domain name, use an expression like `domainName="example.com"`. You can also check for the existence of a field; for example, to find domains using custom DNS settings, use an expression like `dnsSettings.customDns:*`.

You can also create compound filters by combining expressions with the `AND` and `OR` operators. For example, to find domains that are suspended or have specific issues flagged, use an expression like `(state=SUSPENDED) OR (issue:*)`. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Domains::V1::Registration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Registration)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Domains::V1::Registration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Registration)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::ListRegistrationsRequest.new
    
    # Call the list_registrations method.
    result = client.list_registrations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Domains::V1::Registration.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Domains::V1::Domains::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Domains::V1::Domains::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Domains-Operations)) 



### #register_domain
    
    
    def register_domain(request, options = nil) -> ::Gapic::Operation
    def register_domain(parent: nil, registration: nil, domain_notices: nil, contact_notices: nil, yearly_price: nil, validate_only: nil) -> ::Gapic::Operation

Registers a new domain name and creates a corresponding `Registration` resource.

Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method.

A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.

**Overloads**
    
    
    def register_domain(request, options = nil) -> ::Gapic::Operation

Pass arguments to `register_domain` via a request object, either of type [RegisterDomainRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RegisterDomainRequest "Google::Cloud::Domains::V1::RegisterDomainRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::RegisterDomainRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RegisterDomainRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def register_domain(parent: nil, registration: nil, domain_notices: nil, contact_notices: nil, yearly_price: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `register_domain` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the `Registration`. Must be in the format `projects/*/locations/*`. 
  * **registration** ([::Google::Cloud::Domains::V1::Registration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Registration), ::Hash) — Required. The complete `Registration` resource to be created. 
  * **domain_notices** (::Array<[::Google::Cloud::Domains::V1::DomainNotice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-DomainNotice)>) — The list of domain notices that you acknowledge. Call `RetrieveRegisterParameters` to see the notices that need acknowledgement. 
  * **contact_notices** (::Array<[::Google::Cloud::Domains::V1::ContactNotice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ContactNotice)>) — The list of contact notices that the caller acknowledges. The notices needed here depend on the values specified in `registration.contact_settings`. 
  * **yearly_price** ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Type-Money), ::Hash) — Required. Yearly price to register or renew the domain. The value that should be put here can be obtained from RetrieveRegisterParameters or SearchDomains calls. 
  * **validate_only** (::Boolean) — When true, only validation is performed, without actually registering the domain. Follows: https://cloud.google.com/apis/design/design_patterns#request_validation 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::RegisterDomainRequest.new
    
    # Call the register_domain method.
    result = client.register_domain request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #reset_authorization_code
    
    
    def reset_authorization_code(request, options = nil) -> ::Google::Cloud::Domains::V1::AuthorizationCode
    def reset_authorization_code(registration: nil) -> ::Google::Cloud::Domains::V1::AuthorizationCode

Resets the authorization code of the `Registration` to a new random string.

You can call this method only after 60 days have elapsed since the initial domain registration.

**Overloads**
    
    
    def reset_authorization_code(request, options = nil) -> ::Google::Cloud::Domains::V1::AuthorizationCode

Pass arguments to `reset_authorization_code` via a request object, either of type [ResetAuthorizationCodeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ResetAuthorizationCodeRequest "Google::Cloud::Domains::V1::ResetAuthorizationCodeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::ResetAuthorizationCodeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ResetAuthorizationCodeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def reset_authorization_code(registration: nil) -> ::Google::Cloud::Domains::V1::AuthorizationCode

Pass arguments to `reset_authorization_code` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **registration** (::String) — Required. The name of the `Registration` whose authorization code is being reset, in the format `projects/*/locations/*/registrations/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Domains::V1::AuthorizationCode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-AuthorizationCode)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Domains::V1::AuthorizationCode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-AuthorizationCode)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::ResetAuthorizationCodeRequest.new
    
    # Call the reset_authorization_code method.
    result = client.reset_authorization_code request
    
    # The returned object is of type Google::Cloud::Domains::V1::AuthorizationCode.
    p result

### #retrieve_authorization_code
    
    
    def retrieve_authorization_code(request, options = nil) -> ::Google::Cloud::Domains::V1::AuthorizationCode
    def retrieve_authorization_code(registration: nil) -> ::Google::Cloud::Domains::V1::AuthorizationCode

Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.

You can call this method only after 60 days have elapsed since the initial domain registration.

**Overloads**
    
    
    def retrieve_authorization_code(request, options = nil) -> ::Google::Cloud::Domains::V1::AuthorizationCode

Pass arguments to `retrieve_authorization_code` via a request object, either of type [RetrieveAuthorizationCodeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveAuthorizationCodeRequest "Google::Cloud::Domains::V1::RetrieveAuthorizationCodeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::RetrieveAuthorizationCodeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveAuthorizationCodeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def retrieve_authorization_code(registration: nil) -> ::Google::Cloud::Domains::V1::AuthorizationCode

Pass arguments to `retrieve_authorization_code` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **registration** (::String) — Required. The name of the `Registration` whose authorization code is being retrieved, in the format `projects/*/locations/*/registrations/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Domains::V1::AuthorizationCode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-AuthorizationCode)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Domains::V1::AuthorizationCode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-AuthorizationCode)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::RetrieveAuthorizationCodeRequest.new
    
    # Call the retrieve_authorization_code method.
    result = client.retrieve_authorization_code request
    
    # The returned object is of type Google::Cloud::Domains::V1::AuthorizationCode.
    p result

### #retrieve_register_parameters
    
    
    def retrieve_register_parameters(request, options = nil) -> ::Google::Cloud::Domains::V1::RetrieveRegisterParametersResponse
    def retrieve_register_parameters(domain_name: nil, location: nil) -> ::Google::Cloud::Domains::V1::RetrieveRegisterParametersResponse

Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`.

**Overloads**
    
    
    def retrieve_register_parameters(request, options = nil) -> ::Google::Cloud::Domains::V1::RetrieveRegisterParametersResponse

Pass arguments to `retrieve_register_parameters` via a request object, either of type [RetrieveRegisterParametersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveRegisterParametersRequest "Google::Cloud::Domains::V1::RetrieveRegisterParametersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::RetrieveRegisterParametersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveRegisterParametersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def retrieve_register_parameters(domain_name: nil, location: nil) -> ::Google::Cloud::Domains::V1::RetrieveRegisterParametersResponse

Pass arguments to `retrieve_register_parameters` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **domain_name** (::String) — Required. The domain name. Unicode domain names must be expressed in Punycode format. 
  * **location** (::String) — Required. The location. Must be in the format `projects/*/locations/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Domains::V1::RetrieveRegisterParametersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveRegisterParametersResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Domains::V1::RetrieveRegisterParametersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveRegisterParametersResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::RetrieveRegisterParametersRequest.new
    
    # Call the retrieve_register_parameters method.
    result = client.retrieve_register_parameters request
    
    # The returned object is of type Google::Cloud::Domains::V1::RetrieveRegisterParametersResponse.
    p result

### #retrieve_transfer_parameters
    
    
    def retrieve_transfer_parameters(request, options = nil) -> ::Google::Cloud::Domains::V1::RetrieveTransferParametersResponse
    def retrieve_transfer_parameters(domain_name: nil, location: nil) -> ::Google::Cloud::Domains::V1::RetrieveTransferParametersResponse

Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Use the returned values to call `TransferDomain`.

**Overloads**
    
    
    def retrieve_transfer_parameters(request, options = nil) -> ::Google::Cloud::Domains::V1::RetrieveTransferParametersResponse

Pass arguments to `retrieve_transfer_parameters` via a request object, either of type [RetrieveTransferParametersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveTransferParametersRequest "Google::Cloud::Domains::V1::RetrieveTransferParametersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::RetrieveTransferParametersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveTransferParametersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def retrieve_transfer_parameters(domain_name: nil, location: nil) -> ::Google::Cloud::Domains::V1::RetrieveTransferParametersResponse

Pass arguments to `retrieve_transfer_parameters` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **domain_name** (::String) — Required. The domain name. Unicode domain names must be expressed in Punycode format. 
  * **location** (::String) — Required. The location. Must be in the format `projects/*/locations/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Domains::V1::RetrieveTransferParametersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveTransferParametersResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Domains::V1::RetrieveTransferParametersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-RetrieveTransferParametersResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::RetrieveTransferParametersRequest.new
    
    # Call the retrieve_transfer_parameters method.
    result = client.retrieve_transfer_parameters request
    
    # The returned object is of type Google::Cloud::Domains::V1::RetrieveTransferParametersResponse.
    p result

### #search_domains
    
    
    def search_domains(request, options = nil) -> ::Google::Cloud::Domains::V1::SearchDomainsResponse
    def search_domains(query: nil, location: nil) -> ::Google::Cloud::Domains::V1::SearchDomainsResponse

Searches for available domain names similar to the provided query.

Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability.

**Overloads**
    
    
    def search_domains(request, options = nil) -> ::Google::Cloud::Domains::V1::SearchDomainsResponse

Pass arguments to `search_domains` via a request object, either of type [SearchDomainsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-SearchDomainsRequest "Google::Cloud::Domains::V1::SearchDomainsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::SearchDomainsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-SearchDomainsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def search_domains(query: nil, location: nil) -> ::Google::Cloud::Domains::V1::SearchDomainsResponse

Pass arguments to `search_domains` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **query** (::String) — Required. String used to search for available domain names. 
  * **location** (::String) — Required. The location. Must be in the format `projects/*/locations/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Domains::V1::SearchDomainsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-SearchDomainsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Domains::V1::SearchDomainsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-SearchDomainsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::SearchDomainsRequest.new
    
    # Call the search_domains method.
    result = client.search_domains request
    
    # The returned object is of type Google::Cloud::Domains::V1::SearchDomainsResponse.
    p result

### #transfer_domain
    
    
    def transfer_domain(request, options = nil) -> ::Gapic::Operation
    def transfer_domain(parent: nil, registration: nil, contact_notices: nil, yearly_price: nil, authorization_code: nil, validate_only: nil) -> ::Gapic::Operation

Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method.

A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website.

A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer.

**Overloads**
    
    
    def transfer_domain(request, options = nil) -> ::Gapic::Operation

Pass arguments to `transfer_domain` via a request object, either of type [TransferDomainRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-TransferDomainRequest "Google::Cloud::Domains::V1::TransferDomainRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::TransferDomainRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-TransferDomainRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def transfer_domain(parent: nil, registration: nil, contact_notices: nil, yearly_price: nil, authorization_code: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `transfer_domain` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the `Registration`. Must be in the format `projects/*/locations/*`. 
  * **registration** ([::Google::Cloud::Domains::V1::Registration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Registration), ::Hash) — Required. The complete `Registration` resource to be created.

You can leave `registration.dns_settings` unset to import the domain's current DNS configuration from its current registrar. Use this option only if you are sure that the domain's current DNS service does not cease upon transfer, as is often the case for DNS services provided for free by the registrar. 

  * **contact_notices** (::Array<[::Google::Cloud::Domains::V1::ContactNotice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ContactNotice)>) — The list of contact notices that you acknowledge. The notices needed here depend on the values specified in `registration.contact_settings`. 
  * **yearly_price** ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Type-Money), ::Hash) — Required. Acknowledgement of the price to transfer or renew the domain for one year. Call `RetrieveTransferParameters` to obtain the price, which you must acknowledge. 
  * **authorization_code** ([::Google::Cloud::Domains::V1::AuthorizationCode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-AuthorizationCode), ::Hash) — The domain's transfer authorization code. You can obtain this from the domain's current registrar. 
  * **validate_only** (::Boolean) — Validate the request without actually transferring the domain. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::TransferDomainRequest.new
    
    # Call the transfer_domain method.
    result = client.transfer_domain request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_registration
    
    
    def update_registration(request, options = nil) -> ::Gapic::Operation
    def update_registration(registration: nil, update_mask: nil) -> ::Gapic::Operation

Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method:

  * To update management settings, see `ConfigureManagementSettings`
  * To update DNS configuration, see `ConfigureDnsSettings`
  * To update contact information, see `ConfigureContactSettings`



**Overloads**
    
    
    def update_registration(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_registration` via a request object, either of type [UpdateRegistrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-UpdateRegistrationRequest "Google::Cloud::Domains::V1::UpdateRegistrationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Domains::V1::UpdateRegistrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-UpdateRegistrationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_registration(registration: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_registration` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **registration** ([::Google::Cloud::Domains::V1::Registration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-Registration), ::Hash) — Fields of the `Registration` to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The field mask describing which fields to update as a comma-separated list. For example, if only the labels are being updated, the `update_mask` is `"labels"`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/domains/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Domains::V1::Domains::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Domains::V1::UpdateRegistrationRequest.new
    
    # Call the update_registration method.
    result = client.update_registration request
    
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
