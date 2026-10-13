---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Entitlement (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:20.602102+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Entitlement (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Entitlement (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::Entitlement.

An entitlement is a representation of a customer's ability to use a service.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #association_info
    
    
    def association_info() -> ::Google::Cloud::Channel::V1::AssociationInfo

**Returns**

  * ([::Google::Cloud::Channel::V1::AssociationInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-AssociationInfo)) — Association information to other entitlements. 



### #association_info=
    
    
    def association_info=(value) -> ::Google::Cloud::Channel::V1::AssociationInfo

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::AssociationInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-AssociationInfo)) — Association information to other entitlements. 



**Returns**

  * ([::Google::Cloud::Channel::V1::AssociationInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-AssociationInfo)) — Association information to other entitlements. 



### #billing_account
    
    
    def billing_account() -> ::String

**Returns**

  * (::String) — Optional. The billing account resource name that is used to pay for this entitlement. 



### #billing_account=
    
    
    def billing_account=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The billing account resource name that is used to pay for this entitlement. 



**Returns**

  * (::String) — Optional. The billing account resource name that is used to pay for this entitlement. 



### #commitment_settings
    
    
    def commitment_settings() -> ::Google::Cloud::Channel::V1::CommitmentSettings

**Returns**

  * ([::Google::Cloud::Channel::V1::CommitmentSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CommitmentSettings)) — Commitment settings for a commitment-based Offer. Required for commitment based offers. 



### #commitment_settings=
    
    
    def commitment_settings=(value) -> ::Google::Cloud::Channel::V1::CommitmentSettings

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::CommitmentSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CommitmentSettings)) — Commitment settings for a commitment-based Offer. Required for commitment based offers. 



**Returns**

  * ([::Google::Cloud::Channel::V1::CommitmentSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CommitmentSettings)) — Commitment settings for a commitment-based Offer. Required for commitment based offers. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which the entitlement is created. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}. 



### #offer
    
    
    def offer() -> ::String

**Returns**

  * (::String) — Required. The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}. 



### #offer=
    
    
    def offer=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}. 



**Returns**

  * (::String) — Required. The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}. 



### #parameters
    
    
    def parameters() -> ::Array<::Google::Cloud::Channel::V1::Parameter>

**Returns**

  * (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — 

Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the [Offer.parameter_definitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer#Google__Cloud__Channel__V1__Offer_parameter_definitions_instance_ "Google::Cloud::Channel::V1::Offer#parameter_definitions \(method\)").

For Google Workspace, the following Parameters may be accepted as input:

    * max_units: The maximum assignable units for a flexible offer

OR

    * num_units: The total commitment for commitment-based offers

The response may additionally include the following output-only Parameters:

    * assigned_units: The number of licenses assigned to users.

For Google Cloud billing subaccounts, the following Parameter may be accepted as input:

    * display_name: The display name of the billing subaccount.



### #parameters=
    
    
    def parameters=(value) -> ::Array<::Google::Cloud::Channel::V1::Parameter>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — 

Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the [Offer.parameter_definitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer#Google__Cloud__Channel__V1__Offer_parameter_definitions_instance_ "Google::Cloud::Channel::V1::Offer#parameter_definitions \(method\)").

For Google Workspace, the following Parameters may be accepted as input:

    * max_units: The maximum assignable units for a flexible offer

OR

    * num_units: The total commitment for commitment-based offers

The response may additionally include the following output-only Parameters:

    * assigned_units: The number of licenses assigned to users.

For Google Cloud billing subaccounts, the following Parameter may be accepted as input:

    * display_name: The display name of the billing subaccount.



**Returns**

  * (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — 

Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the [Offer.parameter_definitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer#Google__Cloud__Channel__V1__Offer_parameter_definitions_instance_ "Google::Cloud::Channel::V1::Offer#parameter_definitions \(method\)").

For Google Workspace, the following Parameters may be accepted as input:

    * max_units: The maximum assignable units for a flexible offer

OR

    * num_units: The total commitment for commitment-based offers

The response may additionally include the following output-only Parameters:

    * assigned_units: The number of licenses assigned to users.

For Google Cloud billing subaccounts, the following Parameter may be accepted as input:

    * display_name: The display name of the billing subaccount.



### #price_reference_id
    
    
    def price_reference_id() -> ::String

**Returns**

  * (::String) — Optional. Price reference ID for the offer. Only for offers that require additional price information. Used to guarantee that the pricing is consistent between quoting the offer and placing the order. 



### #price_reference_id=
    
    
    def price_reference_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Price reference ID for the offer. Only for offers that require additional price information. Used to guarantee that the pricing is consistent between quoting the offer and placing the order. 



**Returns**

  * (::String) — Optional. Price reference ID for the offer. Only for offers that require additional price information. Used to guarantee that the pricing is consistent between quoting the offer and placing the order. 



### #provisioned_service
    
    
    def provisioned_service() -> ::Google::Cloud::Channel::V1::ProvisionedService

**Returns**

  * ([::Google::Cloud::Channel::V1::ProvisionedService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ProvisionedService)) — Output only. Service provisioning details for the entitlement. 



### #provisioning_state
    
    
    def provisioning_state() -> ::Google::Cloud::Channel::V1::Entitlement::ProvisioningState

**Returns**

  * ([::Google::Cloud::Channel::V1::Entitlement::ProvisioningState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement-ProvisioningState)) — Output only. Current provisioning state of the entitlement. 



### #purchase_order_id
    
    
    def purchase_order_id() -> ::String

**Returns**

  * (::String) — Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements. 



### #purchase_order_id=
    
    
    def purchase_order_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements. 



**Returns**

  * (::String) — Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements. 



### #suspension_reasons
    
    
    def suspension_reasons() -> ::Array<::Google::Cloud::Channel::V1::Entitlement::SuspensionReason>

**Returns**

  * (::Array<[::Google::Cloud::Channel::V1::Entitlement::SuspensionReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement-SuspensionReason)>) — Output only. Enumerable of all current suspension reasons for an entitlement. 



### #trial_settings
    
    
    def trial_settings() -> ::Google::Cloud::Channel::V1::TrialSettings

**Returns**

  * ([::Google::Cloud::Channel::V1::TrialSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-TrialSettings)) — Output only. Settings for trial offers. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which the entitlement is updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
