---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-OmnichannelIntegrationConfig/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:59.050243+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-OmnichannelIntegrationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig.

OmnichannelIntegrationConfig contains all App integration configs.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #channel_configs
    
    
    def channel_configs() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::ChannelConfig}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::ChannelConfig}) — Optional. Various of configuration for handling App events. 



### #channel_configs=
    
    
    def channel_configs=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::ChannelConfig}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::ChannelConfig}) — Optional. Various of configuration for handling App events. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::ChannelConfig}) — Optional. Various of configuration for handling App events. 



### #routing_configs
    
    
    def routing_configs() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::RoutingConfig}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::RoutingConfig}) — Optional. The key of routing_configs is a key of `app_configs`, value is a `RoutingConfig`, which contains subscriber's key. 



### #routing_configs=
    
    
    def routing_configs=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::RoutingConfig}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::RoutingConfig}) — Optional. The key of routing_configs is a key of `app_configs`, value is a `RoutingConfig`, which contains subscriber's key. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::RoutingConfig}) — Optional. The key of routing_configs is a key of `app_configs`, value is a `RoutingConfig`, which contains subscriber's key. 



### #subscriber_configs
    
    
    def subscriber_configs() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::SubscriberConfig}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::SubscriberConfig}) — Optional. Various of subscribers configs. 



### #subscriber_configs=
    
    
    def subscriber_configs=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::SubscriberConfig}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::SubscriberConfig}) — Optional. Various of subscribers configs. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Ces::V1beta::OmnichannelIntegrationConfig::SubscriberConfig}) — Optional. Various of subscribers configs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
