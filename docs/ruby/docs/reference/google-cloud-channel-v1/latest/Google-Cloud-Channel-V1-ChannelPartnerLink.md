---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChannelPartnerLink (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:08.202099+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChannelPartnerLink (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChannelPartnerLink (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::ChannelPartnerLink.

Entity representing a link between distributors and their indirect resellers in an n-tier resale channel.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #channel_partner_cloud_identity_info
    
    
    def channel_partner_cloud_identity_info() -> ::Google::Cloud::Channel::V1::CloudIdentityInfo

**Returns**

  * ([::Google::Cloud::Channel::V1::CloudIdentityInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo)) — Output only. Cloud Identity info of the channel partner (IR). 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp of when the channel partner link is created. 



### #invite_link_uri
    
    
    def invite_link_uri() -> ::String

**Returns**

  * (::String) — Output only. URI of the web page where partner accepts the link invitation. 



### #link_state
    
    
    def link_state() -> ::Google::Cloud::Channel::V1::ChannelPartnerLinkState

**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerLinkState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLinkState)) — Required. State of the channel partner link. 



### #link_state=
    
    
    def link_state=(value) -> ::Google::Cloud::Channel::V1::ChannelPartnerLinkState

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::ChannelPartnerLinkState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLinkState)) — Required. State of the channel partner link. 



**Returns**

  * ([::Google::Cloud::Channel::V1::ChannelPartnerLinkState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLinkState)) — Required. State of the channel partner link. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Resource name for the channel partner link, in the format accounts/{account_id}/channelPartnerLinks/{id}. 



### #public_id
    
    
    def public_id() -> ::String

**Returns**

  * (::String) — Output only. Public identifier that a customer must use to generate a transfer token to move to this distributor-reseller combination. 



### #reseller_cloud_identity_id
    
    
    def reseller_cloud_identity_id() -> ::String

**Returns**

  * (::String) — Required. Cloud Identity ID of the linked reseller. 



### #reseller_cloud_identity_id=
    
    
    def reseller_cloud_identity_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Cloud Identity ID of the linked reseller. 



**Returns**

  * (::String) — Required. Cloud Identity ID of the linked reseller. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp of when the channel partner link is updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
