---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityCustomerAccount/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudIdentityCustomerAccount (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:16.310069+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudIdentityCustomerAccount (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityCustomerAccount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudIdentityCustomerAccount (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::CloudIdentityCustomerAccount.

Entity representing a Cloud Identity account that may be associated with a Channel Services API partner.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #channel_partner_cloud_identity_id
    
    
    def channel_partner_cloud_identity_id() -> ::String

**Returns**

  * (::String) — If existing = true, and is 2-tier customer, the channel partner of the customer. 



### #channel_partner_cloud_identity_id=
    
    
    def channel_partner_cloud_identity_id=(value) -> ::String

**Parameter**

  * **value** (::String) — If existing = true, and is 2-tier customer, the channel partner of the customer. 



**Returns**

  * (::String) — If existing = true, and is 2-tier customer, the channel partner of the customer. 



### #customer_cloud_identity_id
    
    
    def customer_cloud_identity_id() -> ::String

**Returns**

  * (::String) — If existing = true, the Cloud Identity ID of the customer. 



### #customer_cloud_identity_id=
    
    
    def customer_cloud_identity_id=(value) -> ::String

**Parameter**

  * **value** (::String) — If existing = true, the Cloud Identity ID of the customer. 



**Returns**

  * (::String) — If existing = true, the Cloud Identity ID of the customer. 



### #customer_name
    
    
    def customer_name() -> ::String

**Returns**

  * (::String) — If owned = true, the name of the customer that owns the Cloud Identity account. Customer_name uses the format: accounts/{account_id}/customers/{customer_id} 



### #customer_name=
    
    
    def customer_name=(value) -> ::String

**Parameter**

  * **value** (::String) — If owned = true, the name of the customer that owns the Cloud Identity account. Customer_name uses the format: accounts/{account_id}/customers/{customer_id} 



**Returns**

  * (::String) — If owned = true, the name of the customer that owns the Cloud Identity account. Customer_name uses the format: accounts/{account_id}/customers/{customer_id} 



### #customer_type
    
    
    def customer_type() -> ::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType

**Returns**

  * ([::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo-CustomerType)) — If existing = true, the type of the customer. 



### #customer_type=
    
    
    def customer_type=(value) -> ::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo-CustomerType)) — If existing = true, the type of the customer. 



**Returns**

  * ([::Google::Cloud::Channel::V1::CloudIdentityInfo::CustomerType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo-CustomerType)) — If existing = true, the type of the customer. 



### #existing
    
    
    def existing() -> ::Boolean

**Returns**

  * (::Boolean) — Returns true if a Cloud Identity account exists for a specific domain. 



### #existing=
    
    
    def existing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Returns true if a Cloud Identity account exists for a specific domain. 



**Returns**

  * (::Boolean) — Returns true if a Cloud Identity account exists for a specific domain. 



### #owned
    
    
    def owned() -> ::Boolean

**Returns**

  * (::Boolean) — Returns true if the Cloud Identity account is associated with a customer of the Channel Services partner (with active subscriptions or purchase consents). 



### #owned=
    
    
    def owned=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Returns true if the Cloud Identity account is associated with a customer of the Channel Services partner (with active subscriptions or purchase consents). 



**Returns**

  * (::Boolean) — Returns true if the Cloud Identity account is associated with a customer of the Channel Services partner (with active subscriptions or purchase consents). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
