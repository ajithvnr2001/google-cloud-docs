---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Paths/
title: Cloud Channel V1 API - Module Google::Cloud::Channel::V1::CloudChannelService::Paths (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:13.217673+00:00
---

# Cloud Channel V1 API - Module Google::Cloud::Channel::V1::CloudChannelService::Paths (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Module Google::Cloud::Channel::V1::CloudChannelService::Paths (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API module Google::Cloud::Channel::V1::CloudChannelService::Paths.

Path helper methods for the CloudChannelService API.

## Extended By

  * [Google::Cloud::Channel::V1::CloudChannelService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Paths)



## Included In

  * [Google::Cloud::Channel::V1::CloudChannelService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client)
  * [Google::Cloud::Channel::V1::CloudChannelService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Paths)
  * [Google::Cloud::Channel::V1::CloudChannelService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Rest-Client)



## Methods 

### #account_path
    
    
    def account_path(account:) -> ::String

Create a fully-qualified Account resource string.

The resource will be in the following format:

`accounts/{account}`

**Parameter**

  * **account** (String) 



**Returns**

  * (::String) 



### #channel_partner_link_path
    
    
    def channel_partner_link_path(account:, channel_partner_link:) -> ::String

Create a fully-qualified ChannelPartnerLink resource string.

The resource will be in the following format:

`accounts/{account}/channelPartnerLinks/{channel_partner_link}`

**Parameters**

  * **account** (String) 
  * **channel_partner_link** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #channel_partner_repricing_config_path
    
    
    def channel_partner_repricing_config_path(account:, channel_partner:, channel_partner_repricing_config:) -> ::String

Create a fully-qualified ChannelPartnerRepricingConfig resource string.

The resource will be in the following format:

`accounts/{account}/channelPartnerLinks/{channel_partner}/channelPartnerRepricingConfigs/{channel_partner_repricing_config}`

**Parameters**

  * **account** (String) 
  * **channel_partner** (String) 
  * **channel_partner_repricing_config** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #customer_path
    
    
    def customer_path(account:, customer:) -> ::String

Create a fully-qualified Customer resource string.

The resource will be in the following format:

`accounts/{account}/customers/{customer}`

**Parameters**

  * **account** (String) 
  * **customer** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #customer_repricing_config_path
    
    
    def customer_repricing_config_path(account:, customer:, customer_repricing_config:) -> ::String

Create a fully-qualified CustomerRepricingConfig resource string.

The resource will be in the following format:

`accounts/{account}/customers/{customer}/customerRepricingConfigs/{customer_repricing_config}`

**Parameters**

  * **account** (String) 
  * **customer** (String) 
  * **customer_repricing_config** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #entitlement_path
    
    
    def entitlement_path(account:, customer:, entitlement:) -> ::String

Create a fully-qualified Entitlement resource string.

The resource will be in the following format:

`accounts/{account}/customers/{customer}/entitlements/{entitlement}`

**Parameters**

  * **account** (String) 
  * **customer** (String) 
  * **entitlement** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #offer_path
    
    
    def offer_path(account:, offer:) -> ::String

Create a fully-qualified Offer resource string.

The resource will be in the following format:

`accounts/{account}/offers/{offer}`

**Parameters**

  * **account** (String) 
  * **offer** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #product_path
    
    
    def product_path(product:) -> ::String

Create a fully-qualified Product resource string.

The resource will be in the following format:

`products/{product}`

**Parameter**

  * **product** (String) 



**Returns**

  * (::String) 



### #sku_group_path
    
    
    def sku_group_path(account:, sku_group:) -> ::String

Create a fully-qualified SkuGroup resource string.

The resource will be in the following format:

`accounts/{account}/skuGroups/{sku_group}`

**Parameters**

  * **account** (String) 
  * **sku_group** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
