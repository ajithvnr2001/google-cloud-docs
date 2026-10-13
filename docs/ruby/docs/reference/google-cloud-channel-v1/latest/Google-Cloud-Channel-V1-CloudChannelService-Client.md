---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Client (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:13.096564+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Client (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Client (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::CloudChannelService::Client.

Client for the CloudChannelService service.

CloudChannelService lets Google cloud resellers and distributors manage their customers, channel partners, entitlements, and reports.

Using this service:

  1. Resellers and distributors can manage a customer entity.
  2. Distributors can register an authorized reseller in their channel and provide them with delegated admin access.
  3. Resellers and distributors can manage customer entitlements.



CloudChannelService exposes the following resources:

  * [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)")s: An entity-usually an enterprise-managed by a reseller or distributor.

  * [Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement "Google::Cloud::Channel::V1::Entitlement \(class\)")s: An entity that provides a customer with the means to use a service. Entitlements are created or updated as a result of a successful fulfillment.

  * [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)")s: An entity that identifies links between distributors and their indirect resellers in a channel.




## Inherits

  * Object 



## Includes

  * [Google::Cloud::Channel::V1::CloudChannelService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CloudChannelService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client-Configuration "Google::Cloud::Channel::V1::CloudChannelService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CloudChannelService clients
    ::Google::Cloud::Channel::V1::CloudChannelService::Client.configure do |config|
      config.timeout = 10.0
    end

### #activate_entitlement
    
    
    def activate_entitlement(request, options = nil) -> ::Gapic::Operation
    def activate_entitlement(name: nil, request_id: nil) -> ::Gapic::Operation

Activates a previously suspended entitlement. Entitlements suspended for pending ToS acceptance can't be activated using this method.

An entitlement activation is a long-running operation and it updates the state of the customer entitlement.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * SUSPENSION_NOT_RESELLER_INITIATED: Can only activate reseller-initiated suspensions and entitlements that have accepted the TOS.
  * NOT_SUSPENDED: Can only activate suspended entitlements not in an ACTIVE state.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def activate_entitlement(request, options = nil) -> ::Gapic::Operation

Pass arguments to `activate_entitlement` via a request object, either of type [ActivateEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ActivateEntitlementRequest "Google::Cloud::Channel::V1::ActivateEntitlementRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ActivateEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ActivateEntitlementRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def activate_entitlement(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `activate_entitlement` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the entitlement to activate. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ActivateEntitlementRequest.new
    
    # Call the activate_entitlement method.
    result = client.activate_entitlement request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #cancel_entitlement
    
    
    def cancel_entitlement(request, options = nil) -> ::Gapic::Operation
    def cancel_entitlement(name: nil, request_id: nil) -> ::Gapic::Operation

Cancels a previously fulfilled entitlement.

An entitlement cancellation is a long-running operation.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * FAILED_PRECONDITION: There are Google Cloud projects linked to the Google Cloud entitlement's Cloud Billing subaccount.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google Workspace add-ons, or entitlements for Google Cloud's development platform.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def cancel_entitlement(request, options = nil) -> ::Gapic::Operation

Pass arguments to `cancel_entitlement` via a request object, either of type [Google::Cloud::Channel::V1::CancelEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CancelEntitlementRequest "Google::Cloud::Channel::V1::CancelEntitlementRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::CancelEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CancelEntitlementRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def cancel_entitlement(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `cancel_entitlement` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the entitlement to cancel. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::CancelEntitlementRequest.new
    
    # Call the cancel_entitlement method.
    result = client.cancel_entitlement request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #change_offer
    
    
    def change_offer(request, options = nil) -> ::Gapic::Operation
    def change_offer(name: nil, offer: nil, parameters: nil, purchase_order_id: nil, request_id: nil, billing_account: nil, price_reference_id: nil) -> ::Gapic::Operation

Updates the Offer for an existing customer entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Offer or Entitlement resource not found.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def change_offer(request, options = nil) -> ::Gapic::Operation

Pass arguments to `change_offer` via a request object, either of type [Google::Cloud::Channel::V1::ChangeOfferRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeOfferRequest "Google::Cloud::Channel::V1::ChangeOfferRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ChangeOfferRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeOfferRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def change_offer(name: nil, offer: nil, parameters: nil, purchase_order_id: nil, request_id: nil, billing_account: nil, price_reference_id: nil) -> ::Gapic::Operation

Pass arguments to `change_offer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 
  * **offer** (::String) — Required. New Offer. Format: accounts/{account_id}/offers/{offer_id}. 
  * **parameters** (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter), ::Hash>) — Optional. Parameters needed to purchase the Offer. To view the available Parameters refer to the [Offer.parameter_definitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer#Google__Cloud__Channel__V1__Offer_parameter_definitions_instance_ "Google::Cloud::Channel::V1::Offer#parameter_definitions \(method\)") from the desired offer. 
  * **purchase_order_id** (::String) — Optional. Purchase order id provided by the reseller. 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 

  * **billing_account** (::String) — Optional. The billing account resource name that is used to pay for this entitlement when setting up billing on a trial subscription.

This field is only relevant for multi-currency accounts. It should be left empty for single currency accounts. 

  * **price_reference_id** (::String) — Optional. Price reference ID for the offer. Only for offers that require additional price information. Used to guarantee that the pricing is consistent between quoting the offer and placing the order. 



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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ChangeOfferRequest.new
    
    # Call the change_offer method.
    result = client.change_offer request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #change_parameters
    
    
    def change_parameters(request, options = nil) -> ::Gapic::Operation
    def change_parameters(name: nil, parameters: nil, request_id: nil, purchase_order_id: nil) -> ::Gapic::Operation

Change parameters of the entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. For example, the number of seats being changed is greater than the allowed number of max seats, or decreasing seats for a commitment based plan.
  * NOT_FOUND: Entitlement resource not found.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def change_parameters(request, options = nil) -> ::Gapic::Operation

Pass arguments to `change_parameters` via a request object, either of type [Google::Cloud::Channel::V1::ChangeParametersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeParametersRequest "Google::Cloud::Channel::V1::ChangeParametersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ChangeParametersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeParametersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def change_parameters(name: nil, parameters: nil, request_id: nil, purchase_order_id: nil) -> ::Gapic::Operation

Pass arguments to `change_parameters` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 
  * **parameters** (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter), ::Hash>) — Required. Entitlement parameters to update. You can only change editable parameters.

To view the available Parameters for a request, refer to the [Offer.parameter_definitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer#Google__Cloud__Channel__V1__Offer_parameter_definitions_instance_ "Google::Cloud::Channel::V1::Offer#parameter_definitions \(method\)") from the desired offer. 

  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 

  * **purchase_order_id** (::String) — Optional. Purchase order ID provided by the reseller. 



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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ChangeParametersRequest.new
    
    # Call the change_parameters method.
    result = client.change_parameters request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #change_renewal_settings
    
    
    def change_renewal_settings(request, options = nil) -> ::Gapic::Operation
    def change_renewal_settings(name: nil, renewal_settings: nil, request_id: nil) -> ::Gapic::Operation

Updates the renewal settings for an existing customer entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for a commitment plan. Can't enable or disable renewals for non-commitment plans.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def change_renewal_settings(request, options = nil) -> ::Gapic::Operation

Pass arguments to `change_renewal_settings` via a request object, either of type [Google::Cloud::Channel::V1::ChangeRenewalSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeRenewalSettingsRequest "Google::Cloud::Channel::V1::ChangeRenewalSettingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ChangeRenewalSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeRenewalSettingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def change_renewal_settings(name: nil, renewal_settings: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `change_renewal_settings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 
  * **renewal_settings** ([::Google::Cloud::Channel::V1::RenewalSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RenewalSettings), ::Hash) — Required. New renewal settings. 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ChangeRenewalSettingsRequest.new
    
    # Call the change_renewal_settings method.
    result = client.change_renewal_settings request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #check_cloud_identity_accounts_exist
    
    
    def check_cloud_identity_accounts_exist(request, options = nil) -> ::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse
    def check_cloud_identity_accounts_exist(parent: nil, domain: nil, primary_admin_email: nil) -> ::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse

Confirms the existence of Cloud Identity accounts based on the domain and if the Cloud Identity accounts are owned by the reseller.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * INVALID_VALUE: Invalid domain value in the request.



Return value: A list of [CloudIdentityCustomerAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityCustomerAccount "Google::Cloud::Channel::V1::CloudIdentityCustomerAccount \(class\)") resources for the domain (may be empty)

Note: in the v1alpha1 version of the API, a NOT_FOUND error returns if no [CloudIdentityCustomerAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityCustomerAccount "Google::Cloud::Channel::V1::CloudIdentityCustomerAccount \(class\)") resources match the domain.

**Overloads**
    
    
    def check_cloud_identity_accounts_exist(request, options = nil) -> ::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse

Pass arguments to `check_cloud_identity_accounts_exist` via a request object, either of type [Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistRequest "Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def check_cloud_identity_accounts_exist(parent: nil, domain: nil, primary_admin_email: nil) -> ::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse

Pass arguments to `check_cloud_identity_accounts_exist` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The reseller account's resource name. Parent uses the format: accounts/{account_id} 
  * **domain** (::String) — Required. Domain to fetch for Cloud Identity account customers, including domain and team customers. For team customers, please use the domain for their emails. 
  * **primary_admin_email** (::String) — Optional. Primary admin email to fetch for Cloud Identity account team customer. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest.new
    
    # Call the check_cloud_identity_accounts_exist method.
    result = client.check_cloud_identity_accounts_exist request
    
    # The returned object is of type Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the CloudChannelService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_configure_class_ "Google::Cloud::Channel::V1::CloudChannelService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client-Configuration "Google::Cloud::Channel::V1::CloudChannelService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client-Configuration)) 



### #create_channel_partner_link
    
    
    def create_channel_partner_link(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink
    def create_channel_partner_link(parent: nil, channel_partner_link: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel. Invited partners need to follow the invite_link_uri provided in the response to accept. After accepting the invitation, a link is set up between the two parties. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already exists.
  * NOT_FOUND: No Cloud Identity customer exists for provided domain.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The new [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)") resource.

**Overloads**
    
    
    def create_channel_partner_link(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Pass arguments to `create_channel_partner_link` via a request object, either of type [Google::Cloud::Channel::V1::CreateChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateChannelPartnerLinkRequest "Google::Cloud::Channel::V1::CreateChannelPartnerLinkRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::CreateChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateChannelPartnerLinkRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_channel_partner_link(parent: nil, channel_partner_link: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Pass arguments to `create_channel_partner_link` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Create a channel partner link for the provided reseller account's resource name. Parent uses the format: accounts/{account_id} 
  * **channel_partner_link** ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink), ::Hash) — Required. The channel partner link to create. Either channel_partner_link.reseller_cloud_identity_id or domain can be used to create a link. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::CreateChannelPartnerLinkRequest.new
    
    # Call the create_channel_partner_link method.
    result = client.create_channel_partner_link request
    
    # The returned object is of type Google::Cloud::Channel::V1::ChannelPartnerLink.
    p result

### #create_channel_partner_repricing_config
    
    
    def create_channel_partner_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig
    def create_channel_partner_repricing_config(parent: nil, channel_partner_repricing_config: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Creates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. You can only create configs if the [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)") is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)").

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases.
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours.
  * There is a limit of ten configs for any ChannelPartner or [RepricingConfig.EntitlementGranularity.entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig-EntitlementGranularity#Google__Cloud__Channel__V1__RepricingConfig__EntitlementGranularity_entitlement_instance_ "Google::Cloud::Channel::V1::RepricingConfig::EntitlementGranularity#entitlement \(method\)"), for any [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)").
  * The contained [ChannelPartnerRepricingConfig.repricing_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig#Google__Cloud__Channel__V1__ChannelPartnerRepricingConfig_repricing_config_instance_ "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig#repricing_config \(method\)") value must be different from the value used in the current config for a ChannelPartner.



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months.
  * NOT_FOUND: The [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the updated [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") resource, otherwise returns an error.

**Overloads**
    
    
    def create_channel_partner_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Pass arguments to `create_channel_partner_repricing_config` via a request object, either of type [Google::Cloud::Channel::V1::CreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateChannelPartnerRepricingConfigRequest "Google::Cloud::Channel::V1::CreateChannelPartnerRepricingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::CreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateChannelPartnerRepricingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_channel_partner_repricing_config(parent: nil, channel_partner_repricing_config: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Pass arguments to `create_channel_partner_repricing_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the ChannelPartner that will receive the repricing config. Parent uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id} 
  * **channel_partner_repricing_config** ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig), ::Hash) — Required. The ChannelPartnerRepricingConfig object to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::CreateChannelPartnerRepricingConfigRequest.new
    
    # Call the create_channel_partner_repricing_config method.
    result = client.create_channel_partner_repricing_config request
    
    # The returned object is of type Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig.
    p result

### #create_customer
    
    
    def create_customer(request, options = nil) -> ::Google::Cloud::Channel::V1::Customer
    def create_customer(parent: nil, customer: nil) -> ::Google::Cloud::Channel::V1::Customer

Creates a new [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") resource under the reseller or distributor account.

Possible error codes:

  * PERMISSION_DENIED: 
    * The reseller account making the request is different from the reseller account in the API request.
    * You are not authorized to create a customer. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: 
    * Required request parameters are missing or invalid.
    * Domain field value doesn't match the primary email domain.



Return value: The newly created [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") resource.

**Overloads**
    
    
    def create_customer(request, options = nil) -> ::Google::Cloud::Channel::V1::Customer

Pass arguments to `create_customer` via a request object, either of type [Google::Cloud::Channel::V1::CreateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateCustomerRequest "Google::Cloud::Channel::V1::CreateCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::CreateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_customer(parent: nil, customer: nil) -> ::Google::Cloud::Channel::V1::Customer

Pass arguments to `create_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of reseller account in which to create the customer. Parent uses the format: accounts/{account_id} 
  * **customer** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer), ::Hash) — Required. The customer to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::CreateCustomerRequest.new
    
    # Call the create_customer method.
    result = client.create_customer request
    
    # The returned object is of type Google::Cloud::Channel::V1::Customer.
    p result

### #create_customer_repricing_config
    
    
    def create_customer_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig
    def create_customer_repricing_config(parent: nil, customer_repricing_config: nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Creates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. You can only create configs if the [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)") is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)").

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases.
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours.
  * There is a limit of ten configs for any [RepricingConfig.EntitlementGranularity.entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig-EntitlementGranularity#Google__Cloud__Channel__V1__RepricingConfig__EntitlementGranularity_entitlement_instance_ "Google::Cloud::Channel::V1::RepricingConfig::EntitlementGranularity#entitlement \(method\)"), for any [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)").
  * The contained [CustomerRepricingConfig.repricing_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig#Google__Cloud__Channel__V1__CustomerRepricingConfig_repricing_config_instance_ "Google::Cloud::Channel::V1::CustomerRepricingConfig#repricing_config \(method\)") value must be different from the value used in the current config for a [RepricingConfig.EntitlementGranularity.entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig-EntitlementGranularity#Google__Cloud__Channel__V1__RepricingConfig__EntitlementGranularity_entitlement_instance_ "Google::Cloud::Channel::V1::RepricingConfig::EntitlementGranularity#entitlement \(method\)").



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months.
  * NOT_FOUND: The [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the updated [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") resource, otherwise returns an error.

**Overloads**
    
    
    def create_customer_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Pass arguments to `create_customer_repricing_config` via a request object, either of type [Google::Cloud::Channel::V1::CreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateCustomerRepricingConfigRequest "Google::Cloud::Channel::V1::CreateCustomerRepricingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::CreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateCustomerRepricingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_customer_repricing_config(parent: nil, customer_repricing_config: nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Pass arguments to `create_customer_repricing_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the customer that will receive this repricing config. Parent uses the format: accounts/{account_id}/customers/{customer_id} 
  * **customer_repricing_config** ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig), ::Hash) — Required. The CustomerRepricingConfig object to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::CreateCustomerRepricingConfigRequest.new
    
    # Call the create_customer_repricing_config method.
    result = client.create_customer_repricing_config request
    
    # The returned object is of type Google::Cloud::Channel::V1::CustomerRepricingConfig.
    p result

### #create_entitlement
    
    
    def create_entitlement(request, options = nil) -> ::Gapic::Operation
    def create_entitlement(parent: nil, entitlement: nil, request_id: nil) -> ::Gapic::Operation

Creates an entitlement for a customer.

Possible error codes:

  * PERMISSION_DENIED: 
    * The customer doesn't belong to the reseller.
    * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: 
    * Required request parameters are missing or invalid.
    * There is already a customer entitlement for a SKU from the same product family.
  * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting.
  * NOT_FOUND: The customer or offer resource was not found.
  * ALREADY_EXISTS: 
    * The SKU was already purchased for the customer.
    * The customer's primary email already exists. Retry after changing the customer's primary contact email.
  * CONDITION_NOT_MET or FAILED_PRECONDITION: 
    * The domain required for purchasing a SKU has not been verified.
    * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive.
    * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: 
      * Domain names must start with goog-test.
      * Domain names must include the reseller domain.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def create_entitlement(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_entitlement` via a request object, either of type [Google::Cloud::Channel::V1::CreateEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateEntitlementRequest "Google::Cloud::Channel::V1::CreateEntitlementRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::CreateEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateEntitlementRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_entitlement(parent: nil, entitlement: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_entitlement` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the reseller's customer account in which to create the entitlement. Parent uses the format: accounts/{account_id}/customers/{customer_id} 
  * **entitlement** ([::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement), ::Hash) — Required. The entitlement to create. 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::CreateEntitlementRequest.new
    
    # Call the create_entitlement method.
    result = client.create_entitlement request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_channel_partner_repricing_config
    
    
    def delete_channel_partner_repricing_config(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_channel_partner_repricing_config(name: nil) -> ::Google::Protobuf::Empty

Deletes the given [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") permanently. You can only delete configs if their [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)") is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * FAILED_PRECONDITION: The [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") is active or in the past.
  * NOT_FOUND: No [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") found for the name in the request.



**Overloads**
    
    
    def delete_channel_partner_repricing_config(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_channel_partner_repricing_config` via a request object, either of type [DeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteChannelPartnerRepricingConfigRequest "Google::Cloud::Channel::V1::DeleteChannelPartnerRepricingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::DeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteChannelPartnerRepricingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_channel_partner_repricing_config(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_channel_partner_repricing_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the channel partner repricing config rule to delete. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::DeleteChannelPartnerRepricingConfigRequest.new
    
    # Call the delete_channel_partner_repricing_config method.
    result = client.delete_channel_partner_repricing_config request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_customer
    
    
    def delete_customer(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_customer(name: nil) -> ::Google::Protobuf::Empty

Deletes the given [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") permanently.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * FAILED_PRECONDITION: The customer has existing entitlements.
  * NOT_FOUND: No [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") resource found for the name in the request.



**Overloads**
    
    
    def delete_customer(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_customer` via a request object, either of type [DeleteCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteCustomerRequest "Google::Cloud::Channel::V1::DeleteCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::DeleteCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_customer(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the customer to delete. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::DeleteCustomerRequest.new
    
    # Call the delete_customer method.
    result = client.delete_customer request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_customer_repricing_config
    
    
    def delete_customer_repricing_config(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_customer_repricing_config(name: nil) -> ::Google::Protobuf::Empty

Deletes the given [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") permanently. You can only delete configs if their [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)") is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * FAILED_PRECONDITION: The [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") is active or in the past.
  * NOT_FOUND: No [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") found for the name in the request.



**Overloads**
    
    
    def delete_customer_repricing_config(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_customer_repricing_config` via a request object, either of type [DeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteCustomerRepricingConfigRequest "Google::Cloud::Channel::V1::DeleteCustomerRepricingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::DeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteCustomerRepricingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_customer_repricing_config(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_customer_repricing_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the customer repricing config rule to delete. Format: accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::DeleteCustomerRepricingConfigRequest.new
    
    # Call the delete_customer_repricing_config method.
    result = client.delete_customer_repricing_config request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_channel_partner_link
    
    
    def get_channel_partner_link(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink
    def get_channel_partner_link(name: nil, view: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Returns the requested [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)") resource. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: ChannelPartnerLink resource not found because of an invalid channel partner link name.



Return value: The [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)") resource.

**Overloads**
    
    
    def get_channel_partner_link(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Pass arguments to `get_channel_partner_link` via a request object, either of type [GetChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetChannelPartnerLinkRequest "Google::Cloud::Channel::V1::GetChannelPartnerLinkRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::GetChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetChannelPartnerLinkRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_channel_partner_link(name: nil, view: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Pass arguments to `get_channel_partner_link` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the channel partner link to retrieve. Name uses the format: accounts/{account_id}/channelPartnerLinks/{id} where {id} is the Cloud Identity ID of the partner. 
  * **view** ([::Google::Cloud::Channel::V1::ChannelPartnerLinkView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLinkView)) — Optional. The level of granularity the ChannelPartnerLink will display. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::GetChannelPartnerLinkRequest.new
    
    # Call the get_channel_partner_link method.
    result = client.get_channel_partner_link request
    
    # The returned object is of type Google::Cloud::Channel::V1::ChannelPartnerLink.
    p result

### #get_channel_partner_repricing_config
    
    
    def get_channel_partner_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig
    def get_channel_partner_repricing_config(name: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Gets information about how a Distributor modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * NOT_FOUND: The [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") was not found.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") resource, otherwise returns an error.

**Overloads**
    
    
    def get_channel_partner_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Pass arguments to `get_channel_partner_repricing_config` via a request object, either of type [GetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetChannelPartnerRepricingConfigRequest "Google::Cloud::Channel::V1::GetChannelPartnerRepricingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::GetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetChannelPartnerRepricingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_channel_partner_repricing_config(name: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Pass arguments to `get_channel_partner_repricing_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the ChannelPartnerRepricingConfig Format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}/channelPartnerRepricingConfigs/{id}. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::GetChannelPartnerRepricingConfigRequest.new
    
    # Call the get_channel_partner_repricing_config method.
    result = client.get_channel_partner_repricing_config request
    
    # The returned object is of type Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig.
    p result

### #get_customer
    
    
    def get_customer(request, options = nil) -> ::Google::Cloud::Channel::V1::Customer
    def get_customer(name: nil) -> ::Google::Cloud::Channel::V1::Customer

Returns the requested [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") resource.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer resource doesn't exist. Usually the result of an invalid name parameter.



Return value: The [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") resource.

**Overloads**
    
    
    def get_customer(request, options = nil) -> ::Google::Cloud::Channel::V1::Customer

Pass arguments to `get_customer` via a request object, either of type [GetCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetCustomerRequest "Google::Cloud::Channel::V1::GetCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::GetCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_customer(name: nil) -> ::Google::Cloud::Channel::V1::Customer

Pass arguments to `get_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the customer to retrieve. Name uses the format: accounts/{account_id}/customers/{customer_id} 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::GetCustomerRequest.new
    
    # Call the get_customer method.
    result = client.get_customer request
    
    # The returned object is of type Google::Cloud::Channel::V1::Customer.
    p result

### #get_customer_repricing_config
    
    
    def get_customer_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig
    def get_customer_repricing_config(name: nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Gets information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * NOT_FOUND: The [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") was not found.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") resource, otherwise returns an error.

**Overloads**
    
    
    def get_customer_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Pass arguments to `get_customer_repricing_config` via a request object, either of type [GetCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetCustomerRepricingConfigRequest "Google::Cloud::Channel::V1::GetCustomerRepricingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::GetCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetCustomerRepricingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_customer_repricing_config(name: nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Pass arguments to `get_customer_repricing_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the CustomerRepricingConfig. Format: accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::GetCustomerRepricingConfigRequest.new
    
    # Call the get_customer_repricing_config method.
    result = client.get_customer_repricing_config request
    
    # The returned object is of type Google::Cloud::Channel::V1::CustomerRepricingConfig.
    p result

### #get_entitlement
    
    
    def get_entitlement(request, options = nil) -> ::Google::Cloud::Channel::V1::Entitlement
    def get_entitlement(name: nil) -> ::Google::Cloud::Channel::V1::Entitlement

Returns the requested [Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement "Google::Cloud::Channel::V1::Entitlement \(class\)") resource.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer entitlement was not found.



Return value: The requested [Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement "Google::Cloud::Channel::V1::Entitlement \(class\)") resource.

**Overloads**
    
    
    def get_entitlement(request, options = nil) -> ::Google::Cloud::Channel::V1::Entitlement

Pass arguments to `get_entitlement` via a request object, either of type [GetEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetEntitlementRequest "Google::Cloud::Channel::V1::GetEntitlementRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::GetEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetEntitlementRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_entitlement(name: nil) -> ::Google::Cloud::Channel::V1::Entitlement

Pass arguments to `get_entitlement` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the entitlement to retrieve. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::GetEntitlementRequest.new
    
    # Call the get_entitlement method.
    result = client.get_entitlement request
    
    # The returned object is of type Google::Cloud::Channel::V1::Entitlement.
    p result

### #import_customer
    
    
    def import_customer(request, options = nil) -> ::Google::Cloud::Channel::V1::Customer
    def import_customer(domain: nil, cloud_identity_id: nil, primary_admin_email: nil, parent: nil, auth_token: nil, overwrite_if_exists: nil, channel_partner_id: nil, customer: nil) -> ::Google::Cloud::Channel::V1::Customer

Imports a [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") from the Cloud Identity associated with the provided Cloud Identity ID or domain before a TransferEntitlements call. If a linked Customer already exists and overwrite_if_exists is true, it will update that Customer's data.

Possible error codes:

  * PERMISSION_DENIED: 
    * The reseller account making the request is different from the reseller account in the API request.
    * You are not authorized to import the customer. See <https://support.google.com/channelservices/answer/9759265>
  * NOT_FOUND: Cloud Identity doesn't exist or was deleted.
  * INVALID_ARGUMENT: Required parameters are missing, or the auth_token is expired or invalid.
  * ALREADY_EXISTS: A customer already exists and has conflicting critical fields. Requires an overwrite.



Return value: The [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)").

**Overloads**
    
    
    def import_customer(request, options = nil) -> ::Google::Cloud::Channel::V1::Customer

Pass arguments to `import_customer` via a request object, either of type [ImportCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ImportCustomerRequest "Google::Cloud::Channel::V1::ImportCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ImportCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ImportCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def import_customer(domain: nil, cloud_identity_id: nil, primary_admin_email: nil, parent: nil, auth_token: nil, overwrite_if_exists: nil, channel_partner_id: nil, customer: nil) -> ::Google::Cloud::Channel::V1::Customer

Pass arguments to `import_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **domain** (::String) — Required. Customer domain.

Note: The following parameters are mutually exclusive: `domain`, `cloud_identity_id`, `primary_admin_email`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **cloud_identity_id** (::String) — Required. Customer's Cloud Identity ID

Note: The following parameters are mutually exclusive: `cloud_identity_id`, `domain`, `primary_admin_email`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **primary_admin_email** (::String) — Required. Customer's primary admin email.

Note: The following parameters are mutually exclusive: `primary_admin_email`, `domain`, `cloud_identity_id`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **parent** (::String) — Required. The resource name of the reseller's account. Parent takes the format: accounts/{account_id} or accounts/{account_id}/channelPartnerLinks/{channel_partner_id} 
  * **auth_token** (::String) — Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See https://support.google.com/a/answer/7643790 for more details. 
  * **overwrite_if_exists** (::Boolean) — Required. Choose to overwrite an existing customer if found. This must be set to true if there is an existing customer with a conflicting region code or domain. 
  * **channel_partner_id** (::String) — Optional. Cloud Identity ID of a channel partner who will be the direct reseller for the customer's order. This field is required for 2-tier transfer scenarios and can be provided via the request Parent binding as well. 
  * **customer** (::String) — Optional. Specifies the customer that will receive imported Cloud Identity information. Format: accounts/{account_id}/customers/{customer_id} 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ImportCustomerRequest.new
    
    # Call the import_customer method.
    result = client.import_customer request
    
    # The returned object is of type Google::Cloud::Channel::V1::Customer.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CloudChannelService client object.

**Yields**

  * (config) — Configure the CloudChannelService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Channel::V1::CloudChannelService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_channel_partner_links
    
    
    def list_channel_partner_links(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::ChannelPartnerLink>
    def list_channel_partner_links(parent: nil, page_size: nil, page_token: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::ChannelPartnerLink>

List [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)")s belonging to a distributor. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



Return value: The list of the distributor account's [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)") resources.

**Overloads**
    
    
    def list_channel_partner_links(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::ChannelPartnerLink>

Pass arguments to `list_channel_partner_links` via a request object, either of type [ListChannelPartnerLinksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerLinksRequest "Google::Cloud::Channel::V1::ListChannelPartnerLinksRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListChannelPartnerLinksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerLinksRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_channel_partner_links(parent: nil, page_size: nil, page_token: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::ChannelPartnerLink>

Pass arguments to `list_channel_partner_links` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the reseller account for listing channel partner links. Parent uses the format: accounts/{account_id} 
  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, server will pick a default size (25). The maximum value is 200; the server will coerce values above 200. 
  * **page_token** (::String) — Optional. A token for a page of results other than the first page. Obtained using [ListChannelPartnerLinksResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerLinksResponse#Google__Cloud__Channel__V1__ListChannelPartnerLinksResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListChannelPartnerLinksResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListChannelPartnerLinks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_channel_partner_links_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_channel_partner_links \(method\)") call. 
  * **view** ([::Google::Cloud::Channel::V1::ChannelPartnerLinkView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLinkView)) — Optional. The level of granularity the ChannelPartnerLink will display. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListChannelPartnerLinksRequest.new
    
    # Call the list_channel_partner_links method.
    result = client.list_channel_partner_links request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::ChannelPartnerLink.
      p item
    end

### #list_channel_partner_repricing_configs
    
    
    def list_channel_partner_repricing_configs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig>
    def list_channel_partner_repricing_configs(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig>

Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * NOT_FOUND: The [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") resources. The data for each resource is displayed in the ascending order of:

  * Channel Partner ID
  * [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)")
  * [ChannelPartnerRepricingConfig.update_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig#Google__Cloud__Channel__V1__ChannelPartnerRepricingConfig_update_time_instance_ "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig#update_time \(method\)")



If unsuccessful, returns an error.

**Overloads**
    
    
    def list_channel_partner_repricing_configs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig>

Pass arguments to `list_channel_partner_repricing_configs` via a request object, either of type [ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerRepricingConfigsRequest "Google::Cloud::Channel::V1::ListChannelPartnerRepricingConfigsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerRepricingConfigsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_channel_partner_repricing_configs(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig>

Pass arguments to `list_channel_partner_repricing_configs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the account's [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)"). Parent uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}. Supports accounts/{account_id}/channelPartnerLinks/- to retrieve configs for all channel partners. 
  * **page_size** (::Integer) — Optional. The maximum number of repricing configs to return. The service may return fewer than this value. If unspecified, returns a maximum of 50 rules. The maximum value is 100; values above 100 will be coerced to 100. 
  * **page_token** (::String) — Optional. A token identifying a page of results beyond the first page. Obtained through [ListChannelPartnerRepricingConfigsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerRepricingConfigsResponse#Google__Cloud__Channel__V1__ListChannelPartnerRepricingConfigsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListChannelPartnerRepricingConfigsResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListChannelPartnerRepricingConfigs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_channel_partner_repricing_configs_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_channel_partner_repricing_configs \(method\)") call. 
  * **filter** (::String) — Optional. A filter for [CloudChannelService.ListChannelPartnerRepricingConfigs] results (channel_partner_link only). You can use this filter when you support a BatchGet-like query. To use the filter, you must set `parent=accounts/{account_id}/channelPartnerLinks/-`.

Example: `channel_partner_link = accounts/account_id/channelPartnerLinks/c1` OR `channel_partner_link = accounts/account_id/channelPartnerLinks/c2`. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListChannelPartnerRepricingConfigsRequest.new
    
    # Call the list_channel_partner_repricing_configs method.
    result = client.list_channel_partner_repricing_configs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig.
      p item
    end

### #list_customer_repricing_configs
    
    
    def list_customer_repricing_configs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::CustomerRepricingConfig>
    def list_customer_repricing_configs(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::CustomerRepricingConfig>

Lists information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * NOT_FOUND: The [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") resources. The data for each resource is displayed in the ascending order of:

  * Customer ID
  * [RepricingConfig.EntitlementGranularity.entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig-EntitlementGranularity#Google__Cloud__Channel__V1__RepricingConfig__EntitlementGranularity_entitlement_instance_ "Google::Cloud::Channel::V1::RepricingConfig::EntitlementGranularity#entitlement \(method\)")
  * [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)")
  * [CustomerRepricingConfig.update_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig#Google__Cloud__Channel__V1__CustomerRepricingConfig_update_time_instance_ "Google::Cloud::Channel::V1::CustomerRepricingConfig#update_time \(method\)")



If unsuccessful, returns an error.

**Overloads**
    
    
    def list_customer_repricing_configs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::CustomerRepricingConfig>

Pass arguments to `list_customer_repricing_configs` via a request object, either of type [ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomerRepricingConfigsRequest "Google::Cloud::Channel::V1::ListCustomerRepricingConfigsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomerRepricingConfigsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_customer_repricing_configs(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::CustomerRepricingConfig>

Pass arguments to `list_customer_repricing_configs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the customer. Parent uses the format: accounts/{account_id}/customers/{customer_id}. Supports accounts/{account_id}/customers/- to retrieve configs for all customers. 
  * **page_size** (::Integer) — Optional. The maximum number of repricing configs to return. The service may return fewer than this value. If unspecified, returns a maximum of 50 rules. The maximum value is 100; values above 100 will be coerced to 100. 
  * **page_token** (::String) — Optional. A token identifying a page of results beyond the first page. Obtained through [ListCustomerRepricingConfigsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomerRepricingConfigsResponse#Google__Cloud__Channel__V1__ListCustomerRepricingConfigsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListCustomerRepricingConfigsResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListCustomerRepricingConfigs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_customer_repricing_configs_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_customer_repricing_configs \(method\)") call. 
  * **filter** (::String) — Optional. A filter for [CloudChannelService.ListCustomerRepricingConfigs] results (customer only). You can use this filter when you support a BatchGet-like query. To use the filter, you must set `parent=accounts/{account_id}/customers/-`.

Example: customer = accounts/account_id/customers/c1 OR customer = accounts/account_id/customers/c2. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListCustomerRepricingConfigsRequest.new
    
    # Call the list_customer_repricing_configs method.
    result = client.list_customer_repricing_configs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::CustomerRepricingConfig.
      p item
    end

### #list_customers
    
    
    def list_customers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Customer>
    def list_customers(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Customer>

List [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)")s.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



Return value: List of {::Google::Cloud::Channel::V1::Customer Customer}s, or an empty list if there are no customers.

**Overloads**
    
    
    def list_customers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Customer>

Pass arguments to `list_customers` via a request object, either of type [ListCustomersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomersRequest "Google::Cloud::Channel::V1::ListCustomersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListCustomersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_customers(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Customer>

Pass arguments to `list_customers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the reseller account to list customers from. Parent uses the format: accounts/{account_id}. 
  * **page_size** (::Integer) — Optional. The maximum number of customers to return. The service may return fewer than this value. If unspecified, returns at most 10 customers. The maximum value is 50. 
  * **page_token** (::String) — Optional. A token identifying a page of results other than the first page. Obtained through [ListCustomersResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomersResponse#Google__Cloud__Channel__V1__ListCustomersResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListCustomersResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListCustomers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_customers_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_customers \(method\)") call. 
  * **filter** (::String) — Optional. Filters applied to the [CloudChannelService.ListCustomers] results. See https://cloud.google.com/channel/docs/concepts/google-cloud/filter-customers for more information. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListCustomersRequest.new
    
    # Call the list_customers method.
    result = client.list_customers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::Customer.
      p item
    end

### #list_entitlement_changes
    
    
    def list_entitlement_changes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::EntitlementChange>
    def list_entitlement_changes(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::EntitlementChange>

List entitlement history.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different.
  * INVALID_ARGUMENT: Missing or invalid required fields in the request.
  * NOT_FOUND: The parent resource doesn't exist. Usually the result of an invalid name parameter.
  * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support.



Return value: List of {::Google::Cloud::Channel::V1::EntitlementChange EntitlementChange}s.

**Overloads**
    
    
    def list_entitlement_changes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::EntitlementChange>

Pass arguments to `list_entitlement_changes` via a request object, either of type [ListEntitlementChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementChangesRequest "Google::Cloud::Channel::V1::ListEntitlementChangesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListEntitlementChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementChangesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_entitlement_changes(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::EntitlementChange>

Pass arguments to `list_entitlement_changes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The resource name of the entitlement for which to list entitlement changes. The `-` wildcard may be used to match entitlements across a customer. Formats:

    * accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
    * accounts/{account_id}/customers/{customer_id}/entitlements/-
  * **page_size** (::Integer) — Optional. The maximum number of entitlement changes to return. The service may return fewer than this value. If unspecified, returns at most 10 entitlement changes. The maximum value is 50; the server will coerce values above 50. 
  * **page_token** (::String) — Optional. A page token, received from a previous [CloudChannelService.ListEntitlementChanges](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_entitlement_changes_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_entitlement_changes \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [CloudChannelService.ListEntitlementChanges](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_entitlement_changes_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_entitlement_changes \(method\)") must match the call that provided the page token. 

  * **filter** (::String) — Optional. Filters applied to the list results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::EntitlementChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::EntitlementChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListEntitlementChangesRequest.new
    
    # Call the list_entitlement_changes method.
    result = client.list_entitlement_changes request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::EntitlementChange.
      p item
    end

### #list_entitlements
    
    
    def list_entitlements(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Entitlement>
    def list_entitlements(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Entitlement>

Lists [Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement "Google::Cloud::Channel::V1::Entitlement \(class\)")s belonging to a customer.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



Return value: A list of the customer's {::Google::Cloud::Channel::V1::Entitlement Entitlement}s.

**Overloads**
    
    
    def list_entitlements(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Entitlement>

Pass arguments to `list_entitlements` via a request object, either of type [ListEntitlementsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsRequest "Google::Cloud::Channel::V1::ListEntitlementsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListEntitlementsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_entitlements(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Entitlement>

Pass arguments to `list_entitlements` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the reseller's customer account to list entitlements for. Parent uses the format: accounts/{account_id}/customers/{customer_id} 
  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, return at most 50 entitlements. The maximum value is 100; the server will coerce values above 100. 
  * **page_token** (::String) — Optional. A token for a page of results other than the first page. Obtained using [ListEntitlementsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsResponse#Google__Cloud__Channel__V1__ListEntitlementsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListEntitlementsResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListEntitlements](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_entitlements_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_entitlements \(method\)") call. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListEntitlementsRequest.new
    
    # Call the list_entitlements method.
    result = client.list_entitlements request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::Entitlement.
      p item
    end

### #list_offers
    
    
    def list_offers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Offer>
    def list_offers(parent: nil, page_size: nil, page_token: nil, filter: nil, language_code: nil, show_future_offers: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Offer>

Lists the Offers the reseller can sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Overloads**
    
    
    def list_offers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Offer>

Pass arguments to `list_offers` via a request object, either of type [ListOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListOffersRequest "Google::Cloud::Channel::V1::ListOffersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListOffersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_offers(parent: nil, page_size: nil, page_token: nil, filter: nil, language_code: nil, show_future_offers: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Offer>

Pass arguments to `list_offers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the reseller account from which to list Offers. Parent uses the format: accounts/{account_id}. 
  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 500 Offers. The maximum value is 1000; the server will coerce values above 1000. 
  * **page_token** (::String) — Optional. A token for a page of results other than the first page. 
  * **filter** (::String) — Optional. The expression to filter results by name (name of the Offer), sku.name (name of the SKU), or sku.product.name (name of the Product). Example 1: sku.product.name=products/p1 AND sku.name!=products/p1/skus/s1 Example 2: name=accounts/a1/offers/o1 
  * **language_code** (::String) — Optional. The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". 
  * **show_future_offers** (::Boolean) — Optional. A boolean flag that determines if a response returns future offers 30 days from now. If the show_future_offers is true, the response will only contain offers that are scheduled to be available 30 days from now. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Offer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Offer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListOffersRequest.new
    
    # Call the list_offers method.
    result = client.list_offers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::Offer.
      p item
    end

### #list_products
    
    
    def list_products(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Product>
    def list_products(account: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Product>

Lists the Products the reseller is authorized to sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Overloads**
    
    
    def list_products(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Product>

Pass arguments to `list_products` via a request object, either of type [ListProductsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListProductsRequest "Google::Cloud::Channel::V1::ListProductsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListProductsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListProductsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_products(account: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Product>

Pass arguments to `list_products` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **account** (::String) — Required. The resource name of the reseller account. Format: accounts/{account_id}. 
  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 Products. The maximum value is 1000; the server will coerce values above 1000. 
  * **page_token** (::String) — Optional. A token for a page of results other than the first page. 
  * **language_code** (::String) — Optional. The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Product](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Product)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Product](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Product)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListProductsRequest.new
    
    # Call the list_products method.
    result = client.list_products request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::Product.
      p item
    end

### #list_purchasable_offers
    
    
    def list_purchasable_offers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::PurchasableOffer>
    def list_purchasable_offers(create_entitlement_purchase: nil, change_offer_purchase: nil, customer: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::PurchasableOffer>

Lists the following:

  * Offers that you can purchase for a customer.
  * Offers that you can change for an entitlement.



Possible error codes:

  * PERMISSION_DENIED: 
    * The customer doesn't belong to the reseller
    * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Overloads**
    
    
    def list_purchasable_offers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::PurchasableOffer>

Pass arguments to `list_purchasable_offers` via a request object, either of type [ListPurchasableOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableOffersRequest "Google::Cloud::Channel::V1::ListPurchasableOffersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListPurchasableOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableOffersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_purchasable_offers(create_entitlement_purchase: nil, change_offer_purchase: nil, customer: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::PurchasableOffer>

Pass arguments to `list_purchasable_offers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **create_entitlement_purchase** ([::Google::Cloud::Channel::V1::ListPurchasableOffersRequest::CreateEntitlementPurchase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableOffersRequest-CreateEntitlementPurchase), ::Hash) — List Offers for CreateEntitlement purchase.

Note: The following parameters are mutually exclusive: `create_entitlement_purchase`, `change_offer_purchase`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **change_offer_purchase** ([::Google::Cloud::Channel::V1::ListPurchasableOffersRequest::ChangeOfferPurchase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableOffersRequest-ChangeOfferPurchase), ::Hash) — List Offers for ChangeOffer purchase.

Note: The following parameters are mutually exclusive: `change_offer_purchase`, `create_entitlement_purchase`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **customer** (::String) — Required. The resource name of the customer to list Offers for. Format: accounts/{account_id}/customers/{customer_id}. 
  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 Offers. The maximum value is 1000; the server will coerce values above 1000. 
  * **page_token** (::String) — Optional. A token for a page of results other than the first page. 
  * **language_code** (::String) — Optional. The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::PurchasableOffer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PurchasableOffer)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::PurchasableOffer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PurchasableOffer)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListPurchasableOffersRequest.new
    
    # Call the list_purchasable_offers method.
    result = client.list_purchasable_offers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::PurchasableOffer.
      p item
    end

### #list_purchasable_skus
    
    
    def list_purchasable_skus(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::PurchasableSku>
    def list_purchasable_skus(create_entitlement_purchase: nil, change_offer_purchase: nil, customer: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::PurchasableSku>

Lists the following:

  * SKUs that you can purchase for a customer
  * SKUs that you can upgrade or downgrade for an entitlement.



Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Overloads**
    
    
    def list_purchasable_skus(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::PurchasableSku>

Pass arguments to `list_purchasable_skus` via a request object, either of type [ListPurchasableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableSkusRequest "Google::Cloud::Channel::V1::ListPurchasableSkusRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListPurchasableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableSkusRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_purchasable_skus(create_entitlement_purchase: nil, change_offer_purchase: nil, customer: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::PurchasableSku>

Pass arguments to `list_purchasable_skus` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **create_entitlement_purchase** ([::Google::Cloud::Channel::V1::ListPurchasableSkusRequest::CreateEntitlementPurchase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableSkusRequest-CreateEntitlementPurchase), ::Hash) — List SKUs for CreateEntitlement purchase.

Note: The following parameters are mutually exclusive: `create_entitlement_purchase`, `change_offer_purchase`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **change_offer_purchase** ([::Google::Cloud::Channel::V1::ListPurchasableSkusRequest::ChangeOfferPurchase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableSkusRequest-ChangeOfferPurchase), ::Hash) — List SKUs for ChangeOffer purchase with a new SKU.

Note: The following parameters are mutually exclusive: `change_offer_purchase`, `create_entitlement_purchase`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **customer** (::String) — Required. The resource name of the customer to list SKUs for. Format: accounts/{account_id}/customers/{customer_id}. 
  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000. 
  * **page_token** (::String) — Optional. A token for a page of results other than the first page. 
  * **language_code** (::String) — Optional. The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::PurchasableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PurchasableSku)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::PurchasableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-PurchasableSku)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListPurchasableSkusRequest.new
    
    # Call the list_purchasable_skus method.
    result = client.list_purchasable_skus request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::PurchasableSku.
      p item
    end

### #list_sku_group_billable_skus
    
    
    def list_sku_group_billable_skus(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::BillableSku>
    def list_sku_group_billable_skus(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::BillableSku>

Lists the Billable SKUs in a given SKU group.

Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn't exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support.

Return Value: If successful, the [BillableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-BillableSku "Google::Cloud::Channel::V1::BillableSku \(class\)") resources. The data for each resource is displayed in the ascending order of:

  * [BillableSku.service_display_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-BillableSku#Google__Cloud__Channel__V1__BillableSku_service_display_name_instance_ "Google::Cloud::Channel::V1::BillableSku#service_display_name \(method\)")
  * [BillableSku.sku_display_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-BillableSku#Google__Cloud__Channel__V1__BillableSku_sku_display_name_instance_ "Google::Cloud::Channel::V1::BillableSku#sku_display_name \(method\)")



If unsuccessful, returns an error.

**Overloads**
    
    
    def list_sku_group_billable_skus(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::BillableSku>

Pass arguments to `list_sku_group_billable_skus` via a request object, either of type [ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupBillableSkusRequest "Google::Cloud::Channel::V1::ListSkuGroupBillableSkusRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupBillableSkusRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_sku_group_billable_skus(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::BillableSku>

Pass arguments to `list_sku_group_billable_skus` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource name of the SKU group. Format: accounts/{account}/skuGroups/{sku_group}. 
  * **page_size** (::Integer) — Optional. The maximum number of SKUs to return. The service may return fewer than this value. If unspecified, returns a maximum of 100000 SKUs. The maximum value is 100000; values above 100000 will be coerced to 100000. 
  * **page_token** (::String) — Optional. A token identifying a page of results beyond the first page. Obtained through [ListSkuGroupBillableSkusResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupBillableSkusResponse#Google__Cloud__Channel__V1__ListSkuGroupBillableSkusResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListSkuGroupBillableSkusResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListSkuGroupBillableSkus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_sku_group_billable_skus_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_sku_group_billable_skus \(method\)") call. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::BillableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-BillableSku)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::BillableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-BillableSku)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListSkuGroupBillableSkusRequest.new
    
    # Call the list_sku_group_billable_skus method.
    result = client.list_sku_group_billable_skus request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::BillableSku.
      p item
    end

### #list_sku_groups
    
    
    def list_sku_groups(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::SkuGroup>
    def list_sku_groups(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::SkuGroup>

Lists the Rebilling supported SKU groups the account is authorized to sell. Reference: <https://cloud.google.com/skus/sku-groups>

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different, or the account doesn't exist.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the [SkuGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-SkuGroup "Google::Cloud::Channel::V1::SkuGroup \(class\)") resources. The data for each resource is displayed in the alphabetical order of SKU group display name. The data for each resource is displayed in the ascending order of [SkuGroup.display_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-SkuGroup#Google__Cloud__Channel__V1__SkuGroup_display_name_instance_ "Google::Cloud::Channel::V1::SkuGroup#display_name \(method\)")

If unsuccessful, returns an error.

**Overloads**
    
    
    def list_sku_groups(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::SkuGroup>

Pass arguments to `list_sku_groups` via a request object, either of type [ListSkuGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupsRequest "Google::Cloud::Channel::V1::ListSkuGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListSkuGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_sku_groups(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::SkuGroup>

Pass arguments to `list_sku_groups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the account from which to list SKU groups. Parent uses the format: accounts/{account}. 
  * **page_size** (::Integer) — Optional. The maximum number of SKU groups to return. The service may return fewer than this value. If unspecified, returns a maximum of 1000 SKU groups. The maximum value is 1000; values above 1000 will be coerced to 1000\. 
  * **page_token** (::String) — Optional. A token identifying a page of results beyond the first page. Obtained through [ListSkuGroupsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupsResponse#Google__Cloud__Channel__V1__ListSkuGroupsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListSkuGroupsResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListSkuGroups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_sku_groups_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_sku_groups \(method\)") call. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::SkuGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-SkuGroup)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::SkuGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-SkuGroup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListSkuGroupsRequest.new
    
    # Call the list_sku_groups method.
    result = client.list_sku_groups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::SkuGroup.
      p item
    end

### #list_skus
    
    
    def list_skus(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Sku>
    def list_skus(parent: nil, account: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Sku>

Lists the SKUs for a product the reseller is authorized to sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Overloads**
    
    
    def list_skus(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Sku>

Pass arguments to `list_skus` via a request object, either of type [ListSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkusRequest "Google::Cloud::Channel::V1::ListSkusRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkusRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_skus(parent: nil, account: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::Sku>

Pass arguments to `list_skus` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Product to list SKUs for. Parent uses the format: products/{product_id}. Supports products/- to retrieve SKUs for all products. 
  * **account** (::String) — Required. Resource name of the reseller. Format: accounts/{account_id}. 
  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000. 
  * **page_token** (::String) — Optional. A token for a page of results other than the first page. Optional. 
  * **language_code** (::String) — Optional. The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Sku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Sku)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::Sku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Sku)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListSkusRequest.new
    
    # Call the list_skus method.
    result = client.list_skus request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::Sku.
      p item
    end

### #list_subscribers
    
    
    def list_subscribers(request, options = nil) -> ::Google::Cloud::Channel::V1::ListSubscribersResponse
    def list_subscribers(account: nil, page_size: nil, page_token: nil, integrator: nil) -> ::Google::Cloud::Channel::V1::ListSubscribersResponse

Lists service accounts with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The topic resource doesn't exist.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: A list of service email addresses.

**Overloads**
    
    
    def list_subscribers(request, options = nil) -> ::Google::Cloud::Channel::V1::ListSubscribersResponse

Pass arguments to `list_subscribers` via a request object, either of type [ListSubscribersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSubscribersRequest "Google::Cloud::Channel::V1::ListSubscribersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListSubscribersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSubscribersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_subscribers(account: nil, page_size: nil, page_token: nil, integrator: nil) -> ::Google::Cloud::Channel::V1::ListSubscribersResponse

Pass arguments to `list_subscribers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **account** (::String) — Optional. Resource name of the account. Required if integrator is not provided. Otherwise, leave this field empty/unset. 
  * **page_size** (::Integer) — Optional. The maximum number of service accounts to return. The service may return fewer than this value. If unspecified, returns at most 100 service accounts. The maximum value is 1000; the server will coerce values above 1000\. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListSubscribers` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListSubscribers` must match the call that provided the page token. 

  * **integrator** (::String) — Optional. Resource name of the integrator. Required if account is not provided. Otherwise, leave this field empty/unset. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::ListSubscribersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSubscribersResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListSubscribersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSubscribersResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListSubscribersRequest.new
    
    # Call the list_subscribers method.
    result = client.list_subscribers request
    
    # The returned object is of type Google::Cloud::Channel::V1::ListSubscribersResponse.
    p result

### #list_transferable_offers
    
    
    def list_transferable_offers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::TransferableOffer>
    def list_transferable_offers(cloud_identity_id: nil, customer_name: nil, parent: nil, page_size: nil, page_token: nil, sku: nil, language_code: nil, billing_account: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::TransferableOffer>

List [TransferableOffer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferableOffer "Google::Cloud::Channel::V1::TransferableOffer \(class\)")s of a customer based on Cloud Identity ID or Customer Name in the request.

Use this method when a reseller gets the entitlement information of an unowned customer. The reseller should provide the customer's Cloud Identity ID or Customer Name.

Possible error codes:

  * PERMISSION_DENIED: 
    * The customer doesn't belong to the reseller and has no auth token.
    * The customer provided incorrect reseller information when generating auth token.
    * The reseller account making the request is different from the reseller account in the query.
    * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



Return value: List of [TransferableOffer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferableOffer "Google::Cloud::Channel::V1::TransferableOffer \(class\)") for the given customer and SKU.

**Overloads**
    
    
    def list_transferable_offers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::TransferableOffer>

Pass arguments to `list_transferable_offers` via a request object, either of type [ListTransferableOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableOffersRequest "Google::Cloud::Channel::V1::ListTransferableOffersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListTransferableOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableOffersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_transferable_offers(cloud_identity_id: nil, customer_name: nil, parent: nil, page_size: nil, page_token: nil, sku: nil, language_code: nil, billing_account: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::TransferableOffer>

Pass arguments to `list_transferable_offers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **cloud_identity_id** (::String) — Customer's Cloud Identity ID

Note: The following parameters are mutually exclusive: `cloud_identity_id`, `customer_name`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **customer_name** (::String) — A reseller should create a customer and use the resource name of that customer here.

Note: The following parameters are mutually exclusive: `customer_name`, `cloud_identity_id`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **parent** (::String) — Required. The resource name of the reseller's account. 
  * **page_size** (::Integer) — Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 offers. The maximum value is 1000; the server will coerce values above 1000. 
  * **page_token** (::String) — A token for a page of results other than the first page. Obtained using [ListTransferableOffersResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableOffersResponse#Google__Cloud__Channel__V1__ListTransferableOffersResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListTransferableOffersResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListTransferableOffers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_transferable_offers_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_transferable_offers \(method\)") call. 
  * **sku** (::String) — Required. The SKU to look up Offers for. 
  * **language_code** (::String) — Optional. The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". 
  * **billing_account** (::String) — Optional. The Billing Account to look up Offers for. Format: accounts/{account_id}/billingAccounts/{billing_account_id}.

This field is only relevant for multi-currency accounts. It should be left empty for single currency accounts. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::TransferableOffer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferableOffer)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::TransferableOffer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferableOffer)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListTransferableOffersRequest.new
    
    # Call the list_transferable_offers method.
    result = client.list_transferable_offers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::TransferableOffer.
      p item
    end

### #list_transferable_skus
    
    
    def list_transferable_skus(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::TransferableSku>
    def list_transferable_skus(cloud_identity_id: nil, customer_name: nil, parent: nil, page_size: nil, page_token: nil, auth_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::TransferableSku>

List [TransferableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferableSku "Google::Cloud::Channel::V1::TransferableSku \(class\)")s of a customer based on the Cloud Identity ID or Customer Name in the request.

Use this method to list the entitlements information of an unowned customer. You should provide the customer's Cloud Identity ID or Customer Name.

Possible error codes:

  * PERMISSION_DENIED: 
    * The customer doesn't belong to the reseller and has no auth token.
    * The supplied auth token is invalid.
    * The reseller account making the request is different from the reseller account in the query.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



Return value: A list of the customer's [TransferableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferableSku "Google::Cloud::Channel::V1::TransferableSku \(class\)").

**Overloads**
    
    
    def list_transferable_skus(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::TransferableSku>

Pass arguments to `list_transferable_skus` via a request object, either of type [ListTransferableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableSkusRequest "Google::Cloud::Channel::V1::ListTransferableSkusRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListTransferableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableSkusRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_transferable_skus(cloud_identity_id: nil, customer_name: nil, parent: nil, page_size: nil, page_token: nil, auth_token: nil, language_code: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Channel::V1::TransferableSku>

Pass arguments to `list_transferable_skus` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **cloud_identity_id** (::String) — Customer's Cloud Identity ID

Note: The following parameters are mutually exclusive: `cloud_identity_id`, `customer_name`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **customer_name** (::String) — A reseller is required to create a customer and use the resource name of the created customer here. Customer_name uses the format: accounts/{account_id}/customers/{customer_id}

Note: The following parameters are mutually exclusive: `customer_name`, `cloud_identity_id`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **parent** (::String) — Required. The reseller account's resource name. Parent uses the format: accounts/{account_id} 
  * **page_size** (::Integer) — The requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000. Optional. 
  * **page_token** (::String) — A token for a page of results other than the first page. Obtained using [ListTransferableSkusResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableSkusResponse#Google__Cloud__Channel__V1__ListTransferableSkusResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListTransferableSkusResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListTransferableSkus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_transferable_skus_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_transferable_skus \(method\)") call. Optional. 
  * **auth_token** (::String) — Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See https://support.google.com/a/answer/7643790 for more details. 
  * **language_code** (::String) — The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::TransferableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferableSku)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Channel::V1::TransferableSku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferableSku)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListTransferableSkusRequest.new
    
    # Call the list_transferable_skus method.
    result = client.list_transferable_skus request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::TransferableSku.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #lookup_offer
    
    
    def lookup_offer(request, options = nil) -> ::Google::Cloud::Channel::V1::Offer
    def lookup_offer(entitlement: nil) -> ::Google::Cloud::Channel::V1::Offer

Returns the requested [Offer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer "Google::Cloud::Channel::V1::Offer \(class\)") resource.

Possible error codes:

  * PERMISSION_DENIED: The entitlement doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement or offer was not found.



Return value: The [Offer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer "Google::Cloud::Channel::V1::Offer \(class\)") resource.

**Overloads**
    
    
    def lookup_offer(request, options = nil) -> ::Google::Cloud::Channel::V1::Offer

Pass arguments to `lookup_offer` via a request object, either of type [LookupOfferRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-LookupOfferRequest "Google::Cloud::Channel::V1::LookupOfferRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::LookupOfferRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-LookupOfferRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def lookup_offer(entitlement: nil) -> ::Google::Cloud::Channel::V1::Offer

Pass arguments to `lookup_offer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **entitlement** (::String) — Required. The resource name of the entitlement to retrieve the Offer. Entitlement uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::Offer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Offer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::LookupOfferRequest.new
    
    # Call the lookup_offer method.
    result = client.lookup_offer request
    
    # The returned object is of type Google::Cloud::Channel::V1::Offer.
    p result

### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Channel::V1::CloudChannelService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Channel::V1::CloudChannelService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Operations)) 



### #provision_cloud_identity
    
    
    def provision_cloud_identity(request, options = nil) -> ::Gapic::Operation
    def provision_cloud_identity(customer: nil, cloud_identity_info: nil, user: nil, validate_only: nil) -> ::Gapic::Operation

Creates a Cloud Identity for the given customer using the customer's information, or the information provided here.

Possible error codes:

  * PERMISSION_DENIED: 
    * The customer doesn't belong to the reseller.
    * You are not authorized to provision cloud identity id. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer was not found.
  * ALREADY_EXISTS: The customer's primary email already exists. Retry after changing the customer's primary contact email.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def provision_cloud_identity(request, options = nil) -> ::Gapic::Operation

Pass arguments to `provision_cloud_identity` via a request object, either of type [ProvisionCloudIdentityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ProvisionCloudIdentityRequest "Google::Cloud::Channel::V1::ProvisionCloudIdentityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ProvisionCloudIdentityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ProvisionCloudIdentityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def provision_cloud_identity(customer: nil, cloud_identity_info: nil, user: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `provision_cloud_identity` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **customer** (::String) — Required. Resource name of the customer. Format: accounts/{account_id}/customers/{customer_id} 
  * **cloud_identity_info** ([::Google::Cloud::Channel::V1::CloudIdentityInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo), ::Hash) — CloudIdentity-specific customer information. 
  * **user** ([::Google::Cloud::Channel::V1::AdminUser](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-AdminUser), ::Hash) — Admin user information. 
  * **validate_only** (::Boolean) — Validate the request and preview the review, but do not post it. 



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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ProvisionCloudIdentityRequest.new
    
    # Call the provision_cloud_identity method.
    result = client.provision_cloud_identity request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #query_eligible_billing_accounts
    
    
    def query_eligible_billing_accounts(request, options = nil) -> ::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse
    def query_eligible_billing_accounts(customer: nil, skus: nil) -> ::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse

Lists the billing accounts that are eligible to purchase particular SKUs for a given customer.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



Return value: Based on the provided list of SKUs, returns a list of SKU groups that must be purchased using the same billing account and the billing accounts eligible to purchase each SKU group.

**Overloads**
    
    
    def query_eligible_billing_accounts(request, options = nil) -> ::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse

Pass arguments to `query_eligible_billing_accounts` via a request object, either of type [QueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-QueryEligibleBillingAccountsRequest "Google::Cloud::Channel::V1::QueryEligibleBillingAccountsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-QueryEligibleBillingAccountsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def query_eligible_billing_accounts(customer: nil, skus: nil) -> ::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse

Pass arguments to `query_eligible_billing_accounts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **customer** (::String) — Required. The resource name of the customer to list eligible billing accounts for. Format: accounts/{account_id}/customers/{customer_id}. 
  * **skus** (::Array<::String>) — Required. List of SKUs to list eligible billing accounts for. At least one SKU is required. Format: products/{product_id}/skus/{sku_id}. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-QueryEligibleBillingAccountsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-QueryEligibleBillingAccountsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::QueryEligibleBillingAccountsRequest.new
    
    # Call the query_eligible_billing_accounts method.
    result = client.query_eligible_billing_accounts request
    
    # The returned object is of type Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse.
    p result

### #register_subscriber
    
    
    def register_subscriber(request, options = nil) -> ::Google::Cloud::Channel::V1::RegisterSubscriberResponse
    def register_subscriber(account: nil, service_account: nil, integrator: nil) -> ::Google::Cloud::Channel::V1::RegisterSubscriberResponse

Registers a service account with subscriber privileges on the Pub/Sub topic for this Channel Services account or integrator. After you create a subscriber, you get the events through [SubscriberEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-SubscriberEvent "Google::Cloud::Channel::V1::SubscriberEvent \(class\)")

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The topic name with the registered service email address.

**Overloads**
    
    
    def register_subscriber(request, options = nil) -> ::Google::Cloud::Channel::V1::RegisterSubscriberResponse

Pass arguments to `register_subscriber` via a request object, either of type [RegisterSubscriberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RegisterSubscriberRequest "Google::Cloud::Channel::V1::RegisterSubscriberRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::RegisterSubscriberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RegisterSubscriberRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def register_subscriber(account: nil, service_account: nil, integrator: nil) -> ::Google::Cloud::Channel::V1::RegisterSubscriberResponse

Pass arguments to `register_subscriber` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **account** (::String) — Optional. Resource name of the account. Required if integrator is not provided. Otherwise, leave this field empty/unset. 
  * **service_account** (::String) — Required. Service account that provides subscriber access to the registered topic. 
  * **integrator** (::String) — Optional. Resource name of the integrator. Required if account is not provided. Otherwise, leave this field empty/unset. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::RegisterSubscriberResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RegisterSubscriberResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::RegisterSubscriberResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RegisterSubscriberResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::RegisterSubscriberRequest.new
    
    # Call the register_subscriber method.
    result = client.register_subscriber request
    
    # The returned object is of type Google::Cloud::Channel::V1::RegisterSubscriberResponse.
    p result

### #start_paid_service
    
    
    def start_paid_service(request, options = nil) -> ::Gapic::Operation
    def start_paid_service(name: nil, request_id: nil) -> ::Gapic::Operation

Starts paid service for a trial entitlement.

Starts paid service for a trial entitlement immediately. This method is only applicable if a plan is set up for a trial entitlement but has some trial days remaining.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for entitlement on trial plans.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def start_paid_service(request, options = nil) -> ::Gapic::Operation

Pass arguments to `start_paid_service` via a request object, either of type [StartPaidServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-StartPaidServiceRequest "Google::Cloud::Channel::V1::StartPaidServiceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::StartPaidServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-StartPaidServiceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def start_paid_service(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `start_paid_service` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the entitlement to start a paid service for. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::StartPaidServiceRequest.new
    
    # Call the start_paid_service method.
    result = client.start_paid_service request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #suspend_entitlement
    
    
    def suspend_entitlement(request, options = nil) -> ::Gapic::Operation
    def suspend_entitlement(name: nil, request_id: nil) -> ::Gapic::Operation

Suspends a previously fulfilled entitlement.

An entitlement suspension is a long-running operation.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * NOT_ACTIVE: Entitlement is not active.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def suspend_entitlement(request, options = nil) -> ::Gapic::Operation

Pass arguments to `suspend_entitlement` via a request object, either of type [SuspendEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-SuspendEntitlementRequest "Google::Cloud::Channel::V1::SuspendEntitlementRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::SuspendEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-SuspendEntitlementRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def suspend_entitlement(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `suspend_entitlement` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the entitlement to suspend. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::SuspendEntitlementRequest.new
    
    # Call the suspend_entitlement method.
    result = client.suspend_entitlement request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #transfer_entitlements
    
    
    def transfer_entitlements(request, options = nil) -> ::Gapic::Operation
    def transfer_entitlements(parent: nil, entitlements: nil, auth_token: nil, request_id: nil) -> ::Gapic::Operation

Transfers customer entitlements to new reseller.

Possible error codes:

  * PERMISSION_DENIED: 
    * The customer doesn't belong to the reseller.
    * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer or offer resource was not found.
  * ALREADY_EXISTS: The SKU was already transferred for the customer.
  * CONDITION_NOT_MET or FAILED_PRECONDITION: 
    * The SKU requires domain verification to transfer, but the domain is not verified.
    * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic).
    * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: 
      * Domain names must start with goog-test.
      * Domain names must include the reseller domain.
    * Specify all transferring entitlements.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def transfer_entitlements(request, options = nil) -> ::Gapic::Operation

Pass arguments to `transfer_entitlements` via a request object, either of type [TransferEntitlementsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferEntitlementsRequest "Google::Cloud::Channel::V1::TransferEntitlementsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::TransferEntitlementsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferEntitlementsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def transfer_entitlements(parent: nil, entitlements: nil, auth_token: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `transfer_entitlements` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the reseller's customer account that will receive transferred entitlements. Parent uses the format: accounts/{account_id}/customers/{customer_id} 
  * **entitlements** (::Array<[::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement), ::Hash>) — Required. The new entitlements to create or transfer. 
  * **auth_token** (::String) — The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See https://support.google.com/a/answer/7643790 for more details. 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::TransferEntitlementsRequest.new
    
    # Call the transfer_entitlements method.
    result = client.transfer_entitlements request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #transfer_entitlements_to_google
    
    
    def transfer_entitlements_to_google(request, options = nil) -> ::Gapic::Operation
    def transfer_entitlements_to_google(parent: nil, entitlements: nil, request_id: nil) -> ::Gapic::Operation

Transfers customer entitlements from their current reseller to Google.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer or offer resource was not found.
  * ALREADY_EXISTS: The SKU was already transferred for the customer.
  * CONDITION_NOT_MET or FAILED_PRECONDITION: 
    * The SKU requires domain verification to transfer, but the domain is not verified.
    * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic).
    * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: 
      * Domain names must start with goog-test.
      * Domain names must include the reseller domain.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

**Overloads**
    
    
    def transfer_entitlements_to_google(request, options = nil) -> ::Gapic::Operation

Pass arguments to `transfer_entitlements_to_google` via a request object, either of type [TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferEntitlementsToGoogleRequest "Google::Cloud::Channel::V1::TransferEntitlementsToGoogleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferEntitlementsToGoogleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def transfer_entitlements_to_google(parent: nil, entitlements: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `transfer_entitlements_to_google` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the reseller's customer account where the entitlements transfer from. Parent uses the format: accounts/{account_id}/customers/{customer_id} 
  * **entitlements** (::Array<[::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement), ::Hash>) — Required. The entitlements to transfer to Google. 
  * **request_id** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::TransferEntitlementsToGoogleRequest.new
    
    # Call the transfer_entitlements_to_google method.
    result = client.transfer_entitlements_to_google request
    
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



### #unregister_subscriber
    
    
    def unregister_subscriber(request, options = nil) -> ::Google::Cloud::Channel::V1::UnregisterSubscriberResponse
    def unregister_subscriber(account: nil, service_account: nil, integrator: nil) -> ::Google::Cloud::Channel::V1::UnregisterSubscriberResponse

Unregisters a service account with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator. If there are no service accounts left with subscriber privileges, this deletes the topic. You can call ListSubscribers to check for these accounts.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The topic resource doesn't exist.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The topic name that unregistered the service email address. Returns a success response if the service email address wasn't registered with the topic.

**Overloads**
    
    
    def unregister_subscriber(request, options = nil) -> ::Google::Cloud::Channel::V1::UnregisterSubscriberResponse

Pass arguments to `unregister_subscriber` via a request object, either of type [UnregisterSubscriberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UnregisterSubscriberRequest "Google::Cloud::Channel::V1::UnregisterSubscriberRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::UnregisterSubscriberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UnregisterSubscriberRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def unregister_subscriber(account: nil, service_account: nil, integrator: nil) -> ::Google::Cloud::Channel::V1::UnregisterSubscriberResponse

Pass arguments to `unregister_subscriber` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **account** (::String) — Optional. Resource name of the account. Required if integrator is not provided. Otherwise, leave this field empty/unset. 
  * **service_account** (::String) — Required. Service account to unregister from subscriber access to the topic. 
  * **integrator** (::String) — Optional. Resource name of the integrator. Required if account is not provided. Otherwise, leave this field empty/unset. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::UnregisterSubscriberResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UnregisterSubscriberResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::UnregisterSubscriberResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UnregisterSubscriberResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::UnregisterSubscriberRequest.new
    
    # Call the unregister_subscriber method.
    result = client.unregister_subscriber request
    
    # The returned object is of type Google::Cloud::Channel::V1::UnregisterSubscriberResponse.
    p result

### #update_channel_partner_link
    
    
    def update_channel_partner_link(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink
    def update_channel_partner_link(name: nil, channel_partner_link: nil, update_mask: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Updates a channel partner link. Distributors call this method to change a link's status. For example, to suspend a partner link. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: 
    * Required request parameters are missing or invalid.
    * Link state cannot change from invited to active or suspended.
    * Cannot send reseller_cloud_identity_id, invite_url, or name in update mask.
  * NOT_FOUND: ChannelPartnerLink resource not found.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The updated [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)") resource.

**Overloads**
    
    
    def update_channel_partner_link(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Pass arguments to `update_channel_partner_link` via a request object, either of type [UpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateChannelPartnerLinkRequest "Google::Cloud::Channel::V1::UpdateChannelPartnerLinkRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::UpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateChannelPartnerLinkRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_channel_partner_link(name: nil, channel_partner_link: nil, update_mask: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Pass arguments to `update_channel_partner_link` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the channel partner link to cancel. Name uses the format: accounts/{account_id}/channelPartnerLinks/{id} where {id} is the Cloud Identity ID of the partner. 
  * **channel_partner_link** ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink), ::Hash) — Required. The channel partner link to update. Only channel_partner_link.link_state is allowed for updates. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The update mask that applies to the resource. The only allowable value for an update mask is channel_partner_link.link_state. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::UpdateChannelPartnerLinkRequest.new
    
    # Call the update_channel_partner_link method.
    result = client.update_channel_partner_link request
    
    # The returned object is of type Google::Cloud::Channel::V1::ChannelPartnerLink.
    p result

### #update_channel_partner_repricing_config
    
    
    def update_channel_partner_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig
    def update_channel_partner_repricing_config(channel_partner_repricing_config: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Updates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. This method overwrites the existing CustomerRepricingConfig.

You can only update configs if the [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)") is a future month. To make changes to configs for the current month, use [CreateChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_create_channel_partner_repricing_config_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#create_channel_partner_repricing_config \(method\)"), taking note of its restrictions. You cannot update the [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)").

When updating a config in the future:

  * This config must already exist.



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months.
  * NOT_FOUND: The [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the updated [ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig "Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig \(class\)") resource, otherwise returns an error.

**Overloads**
    
    
    def update_channel_partner_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Pass arguments to `update_channel_partner_repricing_config` via a request object, either of type [UpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateChannelPartnerRepricingConfigRequest "Google::Cloud::Channel::V1::UpdateChannelPartnerRepricingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::UpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateChannelPartnerRepricingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_channel_partner_repricing_config(channel_partner_repricing_config: nil) -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Pass arguments to `update_channel_partner_repricing_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **channel_partner_repricing_config** ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig), ::Hash) — Required. The ChannelPartnerRepricingConfig object to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::UpdateChannelPartnerRepricingConfigRequest.new
    
    # Call the update_channel_partner_repricing_config method.
    result = client.update_channel_partner_repricing_config request
    
    # The returned object is of type Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig.
    p result

### #update_customer
    
    
    def update_customer(request, options = nil) -> ::Google::Cloud::Channel::V1::Customer
    def update_customer(customer: nil, update_mask: nil) -> ::Google::Cloud::Channel::V1::Customer

Updates an existing [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") resource for the reseller or distributor.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: No [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") resource found for the name in the request.



Return value: The updated [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)") resource.

**Overloads**
    
    
    def update_customer(request, options = nil) -> ::Google::Cloud::Channel::V1::Customer

Pass arguments to `update_customer` via a request object, either of type [UpdateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateCustomerRequest "Google::Cloud::Channel::V1::UpdateCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::UpdateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_customer(customer: nil, update_mask: nil) -> ::Google::Cloud::Channel::V1::Customer

Pass arguments to `update_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **customer** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer), ::Hash) — Required. New contents of the customer. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-FieldMask), ::Hash) — The update mask that applies to the resource. Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::UpdateCustomerRequest.new
    
    # Call the update_customer method.
    result = client.update_customer request
    
    # The returned object is of type Google::Cloud::Channel::V1::Customer.
    p result

### #update_customer_repricing_config
    
    
    def update_customer_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig
    def update_customer_repricing_config(customer_repricing_config: nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Updates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. This method overwrites the existing CustomerRepricingConfig.

You can only update configs if the [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)") is a future month. To make changes to configs for the current month, use [CreateCustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_create_customer_repricing_config_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#create_customer_repricing_config \(method\)"), taking note of its restrictions. You cannot update the [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)").

When updating a config in the future:

  * This config must already exist.



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months.
  * NOT_FOUND: The [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support.



Return Value: If successful, the updated [CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig "Google::Cloud::Channel::V1::CustomerRepricingConfig \(class\)") resource, otherwise returns an error.

**Overloads**
    
    
    def update_customer_repricing_config(request, options = nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Pass arguments to `update_customer_repricing_config` via a request object, either of type [UpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateCustomerRepricingConfigRequest "Google::Cloud::Channel::V1::UpdateCustomerRepricingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::UpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateCustomerRepricingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_customer_repricing_config(customer_repricing_config: nil) -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Pass arguments to `update_customer_repricing_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **customer_repricing_config** ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig), ::Hash) — Required. The CustomerRepricingConfig object to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::UpdateCustomerRepricingConfigRequest.new
    
    # Call the update_customer_repricing_config method.
    result = client.update_customer_repricing_config request
    
    # The returned object is of type Google::Cloud::Channel::V1::CustomerRepricingConfig.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
