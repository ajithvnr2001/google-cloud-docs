---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:08.576675+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerRepricingConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::ChannelPartnerRepricingConfig.

Configuration for how a distributor will rebill a channel partner (also known as a distributor-authorized reseller).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Resource name of the ChannelPartnerRepricingConfig. Format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}/channelPartnerRepricingConfigs/{id}. 



### #repricing_config
    
    
    def repricing_config() -> ::Google::Cloud::Channel::V1::RepricingConfig

**Returns**

  * ([::Google::Cloud::Channel::V1::RepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig)) — Required. The configuration for bill modifications made by a reseller before sending it to ChannelPartner. 



### #repricing_config=
    
    
    def repricing_config=(value) -> ::Google::Cloud::Channel::V1::RepricingConfig

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::RepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig)) — Required. The configuration for bill modifications made by a reseller before sending it to ChannelPartner. 



**Returns**

  * ([::Google::Cloud::Channel::V1::RepricingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig)) — Required. The configuration for bill modifications made by a reseller before sending it to ChannelPartner. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp of an update to the repricing rule. If `update_time` is after [RepricingConfig.effective_invoice_month](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RepricingConfig#Google__Cloud__Channel__V1__RepricingConfig_effective_invoice_month_instance_ "Google::Cloud::Channel::V1::RepricingConfig#effective_invoice_month \(method\)") then it indicates this was set mid-month. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
