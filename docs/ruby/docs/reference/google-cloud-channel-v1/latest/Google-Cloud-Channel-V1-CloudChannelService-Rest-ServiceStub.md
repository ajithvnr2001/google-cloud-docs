---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Rest-ServiceStub/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Rest::ServiceStub (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:16.169893+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Rest::ServiceStub (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelService::Rest::ServiceStub (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::CloudChannelService::Rest::ServiceStub.

REST service stub for the CloudChannelService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #activate_entitlement
    
    
    def activate_entitlement(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the activate_entitlement REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ActivateEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ActivateEntitlementRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #cancel_entitlement
    
    
    def cancel_entitlement(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the cancel_entitlement REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::CancelEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CancelEntitlementRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #change_offer
    
    
    def change_offer(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the change_offer REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ChangeOfferRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeOfferRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #change_parameters
    
    
    def change_parameters(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the change_parameters REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ChangeParametersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeParametersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #change_renewal_settings
    
    
    def change_renewal_settings(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the change_renewal_settings REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ChangeRenewalSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeRenewalSettingsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #check_cloud_identity_accounts_exist
    
    
    def check_cloud_identity_accounts_exist(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse

Baseline implementation for the check_cloud_identity_accounts_exist REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_channel_partner_link
    
    
    def create_channel_partner_link(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Baseline implementation for the create_channel_partner_link REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::CreateChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateChannelPartnerLinkRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_channel_partner_repricing_config
    
    
    def create_channel_partner_repricing_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Baseline implementation for the create_channel_partner_repricing_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::CreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateChannelPartnerRepricingConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_customer
    
    
    def create_customer(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::Customer

Baseline implementation for the create_customer REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::CreateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateCustomerRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_customer_repricing_config
    
    
    def create_customer_repricing_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Baseline implementation for the create_customer_repricing_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::CreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateCustomerRepricingConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_entitlement
    
    
    def create_entitlement(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_entitlement REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::CreateEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CreateEntitlementRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_channel_partner_repricing_config
    
    
    def delete_channel_partner_repricing_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_channel_partner_repricing_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::DeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteChannelPartnerRepricingConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_customer
    
    
    def delete_customer(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_customer REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::DeleteCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteCustomerRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_customer_repricing_config
    
    
    def delete_customer_repricing_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_customer_repricing_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::DeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DeleteCustomerRepricingConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_channel_partner_link
    
    
    def get_channel_partner_link(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Baseline implementation for the get_channel_partner_link REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::GetChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetChannelPartnerLinkRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_channel_partner_repricing_config
    
    
    def get_channel_partner_repricing_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Baseline implementation for the get_channel_partner_repricing_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::GetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetChannelPartnerRepricingConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_customer
    
    
    def get_customer(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::Customer

Baseline implementation for the get_customer REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::GetCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetCustomerRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_customer_repricing_config
    
    
    def get_customer_repricing_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Baseline implementation for the get_customer_repricing_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::GetCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetCustomerRepricingConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_entitlement
    
    
    def get_entitlement(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::Entitlement

Baseline implementation for the get_entitlement REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::GetEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-GetEntitlementRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #import_customer
    
    
    def import_customer(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::Customer

Baseline implementation for the import_customer REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ImportCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ImportCustomerRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_channel_partner_links
    
    
    def list_channel_partner_links(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListChannelPartnerLinksResponse

Baseline implementation for the list_channel_partner_links REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListChannelPartnerLinksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerLinksRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListChannelPartnerLinksResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerLinksResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListChannelPartnerLinksResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerLinksResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_channel_partner_repricing_configs
    
    
    def list_channel_partner_repricing_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListChannelPartnerRepricingConfigsResponse

Baseline implementation for the list_channel_partner_repricing_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerRepricingConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListChannelPartnerRepricingConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerRepricingConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListChannelPartnerRepricingConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListChannelPartnerRepricingConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_customer_repricing_configs
    
    
    def list_customer_repricing_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListCustomerRepricingConfigsResponse

Baseline implementation for the list_customer_repricing_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomerRepricingConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListCustomerRepricingConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomerRepricingConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListCustomerRepricingConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomerRepricingConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_customers
    
    
    def list_customers(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListCustomersResponse

Baseline implementation for the list_customers REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListCustomersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListCustomersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListCustomersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListCustomersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_entitlement_changes
    
    
    def list_entitlement_changes(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListEntitlementChangesResponse

Baseline implementation for the list_entitlement_changes REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListEntitlementChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementChangesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListEntitlementChangesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementChangesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListEntitlementChangesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementChangesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_entitlements
    
    
    def list_entitlements(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListEntitlementsResponse

Baseline implementation for the list_entitlements REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListEntitlementsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListEntitlementsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListEntitlementsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_offers
    
    
    def list_offers(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListOffersResponse

Baseline implementation for the list_offers REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListOffersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListOffersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListOffersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListOffersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListOffersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_products
    
    
    def list_products(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListProductsResponse

Baseline implementation for the list_products REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListProductsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListProductsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListProductsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListProductsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListProductsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListProductsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_purchasable_offers
    
    
    def list_purchasable_offers(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListPurchasableOffersResponse

Baseline implementation for the list_purchasable_offers REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListPurchasableOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableOffersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListPurchasableOffersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableOffersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListPurchasableOffersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableOffersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_purchasable_skus
    
    
    def list_purchasable_skus(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListPurchasableSkusResponse

Baseline implementation for the list_purchasable_skus REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListPurchasableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableSkusRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListPurchasableSkusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableSkusResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListPurchasableSkusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListPurchasableSkusResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_sku_group_billable_skus
    
    
    def list_sku_group_billable_skus(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListSkuGroupBillableSkusResponse

Baseline implementation for the list_sku_group_billable_skus REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupBillableSkusRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListSkuGroupBillableSkusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupBillableSkusResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListSkuGroupBillableSkusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupBillableSkusResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_sku_groups
    
    
    def list_sku_groups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListSkuGroupsResponse

Baseline implementation for the list_sku_groups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListSkuGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListSkuGroupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListSkuGroupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkuGroupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_skus
    
    
    def list_skus(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListSkusResponse

Baseline implementation for the list_skus REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkusRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListSkusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkusResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListSkusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSkusResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_subscribers
    
    
    def list_subscribers(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListSubscribersResponse

Baseline implementation for the list_subscribers REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListSubscribersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSubscribersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListSubscribersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSubscribersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListSubscribersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListSubscribersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_transferable_offers
    
    
    def list_transferable_offers(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListTransferableOffersResponse

Baseline implementation for the list_transferable_offers REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListTransferableOffersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableOffersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListTransferableOffersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableOffersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListTransferableOffersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableOffersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_transferable_skus
    
    
    def list_transferable_skus(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ListTransferableSkusResponse

Baseline implementation for the list_transferable_skus REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ListTransferableSkusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableSkusRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ListTransferableSkusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableSkusResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ListTransferableSkusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListTransferableSkusResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #lookup_offer
    
    
    def lookup_offer(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::Offer

Baseline implementation for the lookup_offer REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::LookupOfferRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-LookupOfferRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::Offer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Offer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #provision_cloud_identity
    
    
    def provision_cloud_identity(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the provision_cloud_identity REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::ProvisionCloudIdentityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ProvisionCloudIdentityRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #query_eligible_billing_accounts
    
    
    def query_eligible_billing_accounts(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse

Baseline implementation for the query_eligible_billing_accounts REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-QueryEligibleBillingAccountsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-QueryEligibleBillingAccountsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-QueryEligibleBillingAccountsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #register_subscriber
    
    
    def register_subscriber(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::RegisterSubscriberResponse

Baseline implementation for the register_subscriber REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::RegisterSubscriberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RegisterSubscriberRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::RegisterSubscriberResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RegisterSubscriberResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::RegisterSubscriberResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RegisterSubscriberResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #start_paid_service
    
    
    def start_paid_service(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the start_paid_service REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::StartPaidServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-StartPaidServiceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #suspend_entitlement
    
    
    def suspend_entitlement(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the suspend_entitlement REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::SuspendEntitlementRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-SuspendEntitlementRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #transfer_entitlements
    
    
    def transfer_entitlements(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the transfer_entitlements REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::TransferEntitlementsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferEntitlementsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #transfer_entitlements_to_google
    
    
    def transfer_entitlements_to_google(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the transfer_entitlements_to_google REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TransferEntitlementsToGoogleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #unregister_subscriber
    
    
    def unregister_subscriber(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::UnregisterSubscriberResponse

Baseline implementation for the unregister_subscriber REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::UnregisterSubscriberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UnregisterSubscriberRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::UnregisterSubscriberResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UnregisterSubscriberResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::UnregisterSubscriberResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UnregisterSubscriberResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_channel_partner_link
    
    
    def update_channel_partner_link(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ChannelPartnerLink

Baseline implementation for the update_channel_partner_link REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::UpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateChannelPartnerLinkRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_channel_partner_repricing_config
    
    
    def update_channel_partner_repricing_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig

Baseline implementation for the update_channel_partner_repricing_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::UpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateChannelPartnerRepricingConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_customer
    
    
    def update_customer(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::Customer

Baseline implementation for the update_customer REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::UpdateCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateCustomerRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_customer_repricing_config
    
    
    def update_customer_repricing_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Channel::V1::CustomerRepricingConfig

Baseline implementation for the update_customer_repricing_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Channel::V1::UpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-UpdateCustomerRepricingConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Channel::V1::CustomerRepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CustomerRepricingConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
