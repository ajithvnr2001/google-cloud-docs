---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ImportCustomerRequest/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ImportCustomerRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:22.563331+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ImportCustomerRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ImportCustomerRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ImportCustomerRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::ImportCustomerRequest.

Request message for [CloudChannelService.ImportCustomer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_import_customer_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#import_customer \(method\)")

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auth_token
    
    
    def auth_token() -> ::String

**Returns**

  * (::String) — Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See https://support.google.com/a/answer/7643790 for more details. 



### #auth_token=
    
    
    def auth_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See https://support.google.com/a/answer/7643790 for more details. 



**Returns**

  * (::String) — Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See https://support.google.com/a/answer/7643790 for more details. 



### #channel_partner_id
    
    
    def channel_partner_id() -> ::String

**Returns**

  * (::String) — Optional. Cloud Identity ID of a channel partner who will be the direct reseller for the customer's order. This field is required for 2-tier transfer scenarios and can be provided via the request Parent binding as well. 



### #channel_partner_id=
    
    
    def channel_partner_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Cloud Identity ID of a channel partner who will be the direct reseller for the customer's order. This field is required for 2-tier transfer scenarios and can be provided via the request Parent binding as well. 



**Returns**

  * (::String) — Optional. Cloud Identity ID of a channel partner who will be the direct reseller for the customer's order. This field is required for 2-tier transfer scenarios and can be provided via the request Parent binding as well. 



### #cloud_identity_id
    
    
    def cloud_identity_id() -> ::String

**Returns**

  * (::String) — Required. Customer's Cloud Identity ID

Note: The following fields are mutually exclusive: `cloud_identity_id`, `domain`, `primary_admin_email`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloud_identity_id=
    
    
    def cloud_identity_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Customer's Cloud Identity ID

Note: The following fields are mutually exclusive: `cloud_identity_id`, `domain`, `primary_admin_email`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Required. Customer's Cloud Identity ID

Note: The following fields are mutually exclusive: `cloud_identity_id`, `domain`, `primary_admin_email`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #customer
    
    
    def customer() -> ::String

**Returns**

  * (::String) — Optional. Specifies the customer that will receive imported Cloud Identity information. Format: accounts/{account_id}/customers/{customer_id} 



### #customer=
    
    
    def customer=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specifies the customer that will receive imported Cloud Identity information. Format: accounts/{account_id}/customers/{customer_id} 



**Returns**

  * (::String) — Optional. Specifies the customer that will receive imported Cloud Identity information. Format: accounts/{account_id}/customers/{customer_id} 



### #domain
    
    
    def domain() -> ::String

**Returns**

  * (::String) — Required. Customer domain.

Note: The following fields are mutually exclusive: `domain`, `cloud_identity_id`, `primary_admin_email`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #domain=
    
    
    def domain=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Customer domain.

Note: The following fields are mutually exclusive: `domain`, `cloud_identity_id`, `primary_admin_email`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Required. Customer domain.

Note: The following fields are mutually exclusive: `domain`, `cloud_identity_id`, `primary_admin_email`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #overwrite_if_exists
    
    
    def overwrite_if_exists() -> ::Boolean

**Returns**

  * (::Boolean) — Required. Choose to overwrite an existing customer if found. This must be set to true if there is an existing customer with a conflicting region code or domain. 



### #overwrite_if_exists=
    
    
    def overwrite_if_exists=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Required. Choose to overwrite an existing customer if found. This must be set to true if there is an existing customer with a conflicting region code or domain. 



**Returns**

  * (::Boolean) — Required. Choose to overwrite an existing customer if found. This must be set to true if there is an existing customer with a conflicting region code or domain. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the reseller's account. Parent takes the format: accounts/{account_id} or accounts/{account_id}/channelPartnerLinks/{channel_partner_id} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the reseller's account. Parent takes the format: accounts/{account_id} or accounts/{account_id}/channelPartnerLinks/{channel_partner_id} 



**Returns**

  * (::String) — Required. The resource name of the reseller's account. Parent takes the format: accounts/{account_id} or accounts/{account_id}/channelPartnerLinks/{channel_partner_id} 



### #primary_admin_email
    
    
    def primary_admin_email() -> ::String

**Returns**

  * (::String) — Required. Customer's primary admin email.

Note: The following fields are mutually exclusive: `primary_admin_email`, `domain`, `cloud_identity_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #primary_admin_email=
    
    
    def primary_admin_email=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Customer's primary admin email.

Note: The following fields are mutually exclusive: `primary_admin_email`, `domain`, `cloud_identity_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Required. Customer's primary admin email.

Note: The following fields are mutually exclusive: `primary_admin_email`, `domain`, `cloud_identity_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
