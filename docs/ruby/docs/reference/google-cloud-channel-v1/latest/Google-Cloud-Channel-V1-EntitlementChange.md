---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::EntitlementChange (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:20.737395+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::EntitlementChange (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::EntitlementChange (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::EntitlementChange.

Change event entry for Entitlement order history

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #activation_reason
    
    
    def activation_reason() -> ::Google::Cloud::Channel::V1::EntitlementChange::ActivationReason

**Returns**

  * ([::Google::Cloud::Channel::V1::EntitlementChange::ActivationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-ActivationReason)) — The Entitlement's activation reason

Note: The following fields are mutually exclusive: `activation_reason`, `suspension_reason`, `cancellation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #activation_reason=
    
    
    def activation_reason=(value) -> ::Google::Cloud::Channel::V1::EntitlementChange::ActivationReason

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::EntitlementChange::ActivationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-ActivationReason)) — The Entitlement's activation reason

Note: The following fields are mutually exclusive: `activation_reason`, `suspension_reason`, `cancellation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Channel::V1::EntitlementChange::ActivationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-ActivationReason)) — The Entitlement's activation reason

Note: The following fields are mutually exclusive: `activation_reason`, `suspension_reason`, `cancellation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cancellation_reason
    
    
    def cancellation_reason() -> ::Google::Cloud::Channel::V1::EntitlementChange::CancellationReason

**Returns**

  * ([::Google::Cloud::Channel::V1::EntitlementChange::CancellationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-CancellationReason)) — Cancellation reason for the Entitlement.

Note: The following fields are mutually exclusive: `cancellation_reason`, `suspension_reason`, `activation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cancellation_reason=
    
    
    def cancellation_reason=(value) -> ::Google::Cloud::Channel::V1::EntitlementChange::CancellationReason

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::EntitlementChange::CancellationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-CancellationReason)) — Cancellation reason for the Entitlement.

Note: The following fields are mutually exclusive: `cancellation_reason`, `suspension_reason`, `activation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Channel::V1::EntitlementChange::CancellationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-CancellationReason)) — Cancellation reason for the Entitlement.

Note: The following fields are mutually exclusive: `cancellation_reason`, `suspension_reason`, `activation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #change_type
    
    
    def change_type() -> ::Google::Cloud::Channel::V1::EntitlementChange::ChangeType

**Returns**

  * ([::Google::Cloud::Channel::V1::EntitlementChange::ChangeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-ChangeType)) — The change action type. 



### #change_type=
    
    
    def change_type=(value) -> ::Google::Cloud::Channel::V1::EntitlementChange::ChangeType

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::EntitlementChange::ChangeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-ChangeType)) — The change action type. 



**Returns**

  * ([::Google::Cloud::Channel::V1::EntitlementChange::ChangeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-ChangeType)) — The change action type. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — The submitted time of the change. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — The submitted time of the change. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — The submitted time of the change. 



### #entitlement
    
    
    def entitlement() -> ::String

**Returns**

  * (::String) — Required. Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 



### #entitlement=
    
    
    def entitlement=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 



**Returns**

  * (::String) — Required. Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 



### #offer
    
    
    def offer() -> ::String

**Returns**

  * (::String) — Required. Resource name of the Offer at the time of change. Takes the form: accounts/{account_id}/offers/{offer_id}. 



### #offer=
    
    
    def offer=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Resource name of the Offer at the time of change. Takes the form: accounts/{account_id}/offers/{offer_id}. 



**Returns**

  * (::String) — Required. Resource name of the Offer at the time of change. Takes the form: accounts/{account_id}/offers/{offer_id}. 



### #operator
    
    
    def operator() -> ::String

**Returns**

  * (::String) — Human-readable identifier that shows what operator made a change. When the operator_type is RESELLER, this is the user's email address. For all other operator types, this is empty. 



### #operator=
    
    
    def operator=(value) -> ::String

**Parameter**

  * **value** (::String) — Human-readable identifier that shows what operator made a change. When the operator_type is RESELLER, this is the user's email address. For all other operator types, this is empty. 



**Returns**

  * (::String) — Human-readable identifier that shows what operator made a change. When the operator_type is RESELLER, this is the user's email address. For all other operator types, this is empty. 



### #operator_type
    
    
    def operator_type() -> ::Google::Cloud::Channel::V1::EntitlementChange::OperatorType

**Returns**

  * ([::Google::Cloud::Channel::V1::EntitlementChange::OperatorType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-OperatorType)) — Operator type responsible for the change. 



### #operator_type=
    
    
    def operator_type=(value) -> ::Google::Cloud::Channel::V1::EntitlementChange::OperatorType

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::EntitlementChange::OperatorType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-OperatorType)) — Operator type responsible for the change. 



**Returns**

  * ([::Google::Cloud::Channel::V1::EntitlementChange::OperatorType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementChange-OperatorType)) — Operator type responsible for the change. 



### #other_change_reason
    
    
    def other_change_reason() -> ::String

**Returns**

  * (::String) — e.g. purchase_number change reason, entered by CRS.

Note: The following fields are mutually exclusive: `other_change_reason`, `suspension_reason`, `cancellation_reason`, `activation_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #other_change_reason=
    
    
    def other_change_reason=(value) -> ::String

**Parameter**

  * **value** (::String) — e.g. purchase_number change reason, entered by CRS.

Note: The following fields are mutually exclusive: `other_change_reason`, `suspension_reason`, `cancellation_reason`, `activation_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — e.g. purchase_number change reason, entered by CRS.

Note: The following fields are mutually exclusive: `other_change_reason`, `suspension_reason`, `cancellation_reason`, `activation_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #parameters
    
    
    def parameters() -> ::Array<::Google::Cloud::Channel::V1::Parameter>

**Returns**

  * (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — Extended parameters, such as: purchase_order_number, gcp_details; internal_correlation_id, long_running_operation_id, order_id; etc. 



### #parameters=
    
    
    def parameters=(value) -> ::Array<::Google::Cloud::Channel::V1::Parameter>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — Extended parameters, such as: purchase_order_number, gcp_details; internal_correlation_id, long_running_operation_id, order_id; etc. 



**Returns**

  * (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — Extended parameters, such as: purchase_order_number, gcp_details; internal_correlation_id, long_running_operation_id, order_id; etc. 



### #provisioned_service
    
    
    def provisioned_service() -> ::Google::Cloud::Channel::V1::ProvisionedService

**Returns**

  * ([::Google::Cloud::Channel::V1::ProvisionedService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ProvisionedService)) — Service provisioned for an Entitlement. 



### #provisioned_service=
    
    
    def provisioned_service=(value) -> ::Google::Cloud::Channel::V1::ProvisionedService

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::ProvisionedService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ProvisionedService)) — Service provisioned for an Entitlement. 



**Returns**

  * ([::Google::Cloud::Channel::V1::ProvisionedService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ProvisionedService)) — Service provisioned for an Entitlement. 



### #suspension_reason
    
    
    def suspension_reason() -> ::Google::Cloud::Channel::V1::Entitlement::SuspensionReason

**Returns**

  * ([::Google::Cloud::Channel::V1::Entitlement::SuspensionReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement-SuspensionReason)) — Suspension reason for the Entitlement.

Note: The following fields are mutually exclusive: `suspension_reason`, `cancellation_reason`, `activation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #suspension_reason=
    
    
    def suspension_reason=(value) -> ::Google::Cloud::Channel::V1::Entitlement::SuspensionReason

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::Entitlement::SuspensionReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement-SuspensionReason)) — Suspension reason for the Entitlement.

Note: The following fields are mutually exclusive: `suspension_reason`, `cancellation_reason`, `activation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Channel::V1::Entitlement::SuspensionReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement-SuspensionReason)) — Suspension reason for the Entitlement.

Note: The following fields are mutually exclusive: `suspension_reason`, `cancellation_reason`, `activation_reason`, `other_change_reason`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
