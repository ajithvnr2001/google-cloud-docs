---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-SupportEventSubscriptionService-Rest-Client-Configuration-Rpcs/
title: Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::SupportEventSubscriptionService::Rest::Client::Configuration::Rpcs (v0.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:43.919879+00:00
---

# Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::SupportEventSubscriptionService::Rest::Client::Configuration::Rpcs (v0.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-SupportEventSubscriptionService-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::SupportEventSubscriptionService::Rest::Client::Configuration::Rpcs (v0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud Support V2BETA API class Google::Cloud::Support::V2beta::SupportEventSubscriptionService::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the SupportEventSubscriptionService API.

Includes fields providing the configuration for each RPC in this service. Each configuration object is of type `Gapic::Config::Method` and includes the following configuration fields:

  * `timeout` (_type:_ `Numeric`) - The call timeout in seconds
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional headers
  * `retry_policy (_type:_`Hash`) - The retry policy. The policy fields include the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



## Inherits

  * Object 



## Methods 

### #create_support_event_subscription
    
    
    def create_support_event_subscription() -> ::Gapic::Config::Method

RPC-specific configuration for `create_support_event_subscription`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_support_event_subscription
    
    
    def delete_support_event_subscription() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_support_event_subscription`

**Returns**

  * (::Gapic::Config::Method) 



### #expunge_support_event_subscription
    
    
    def expunge_support_event_subscription() -> ::Gapic::Config::Method

RPC-specific configuration for `expunge_support_event_subscription`

**Returns**

  * (::Gapic::Config::Method) 



### #get_support_event_subscription
    
    
    def get_support_event_subscription() -> ::Gapic::Config::Method

RPC-specific configuration for `get_support_event_subscription`

**Returns**

  * (::Gapic::Config::Method) 



### #list_support_event_subscriptions
    
    
    def list_support_event_subscriptions() -> ::Gapic::Config::Method

RPC-specific configuration for `list_support_event_subscriptions`

**Returns**

  * (::Gapic::Config::Method) 



### #undelete_support_event_subscription
    
    
    def undelete_support_event_subscription() -> ::Gapic::Config::Method

RPC-specific configuration for `undelete_support_event_subscription`

**Returns**

  * (::Gapic::Config::Method) 



### #update_support_event_subscription
    
    
    def update_support_event_subscription() -> ::Gapic::Config::Method

RPC-specific configuration for `update_support_event_subscription`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
