---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService/
title: Cloud Channel V1 API - Module Google::Cloud::Channel::V1::CloudChannelService (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:11.160800+00:00
---

# Cloud Channel V1 API - Module Google::Cloud::Channel::V1::CloudChannelService (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Module Google::Cloud::Channel::V1::CloudChannelService (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API module Google::Cloud::Channel::V1::CloudChannelService.

CloudChannelService lets Google cloud resellers and distributors manage their customers, channel partners, entitlements, and reports.

Using this service:

  1. Resellers and distributors can manage a customer entity.
  2. Distributors can register an authorized reseller in their channel and provide them with delegated admin access.
  3. Resellers and distributors can manage customer entitlements.



CloudChannelService exposes the following resources:

  * [Customer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer "Google::Cloud::Channel::V1::Customer \(class\)")s: An entity-usually an enterprise-managed by a reseller or distributor.

  * [Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Entitlement "Google::Cloud::Channel::V1::Entitlement \(class\)")s: An entity that provides a customer with the means to use a service. Entitlements are created or updated as a result of a successful fulfillment.

  * [ChannelPartnerLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChannelPartnerLink "Google::Cloud::Channel::V1::ChannelPartnerLink \(class\)")s: An entity that identifies links between distributors and their indirect resellers in a channel.




To load this service and instantiate a REST client:
    
    
    require "google/cloud/channel/v1/cloud_channel_service/rest"
    client = ::Google::Cloud::Channel::V1::CloudChannelService::Rest::Client.new
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
