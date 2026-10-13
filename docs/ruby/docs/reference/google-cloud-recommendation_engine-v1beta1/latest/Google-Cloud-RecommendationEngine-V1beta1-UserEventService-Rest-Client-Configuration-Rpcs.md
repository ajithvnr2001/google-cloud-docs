---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recommendation_engine-v1beta1/latest/Google-Cloud-RecommendationEngine-V1beta1-UserEventService-Rest-Client-Configuration-Rpcs/
title: Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::UserEventService::Rest::Client::Configuration::Rpcs (v0.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:13.660599+00:00
---

# Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::UserEventService::Rest::Client::Configuration::Rpcs (v0.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recommendation_engine-v1beta1/latest/Google-Cloud-RecommendationEngine-V1beta1-UserEventService-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::UserEventService::Rest::Client::Configuration::Rpcs (v0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.17.1  0.16.0  0.15.1  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.2  0.8.2  0.7.0  0.6.1  0.5.0  0.4.1  0.3.7 

Reference documentation and code samples for the Recommendations AI V1beta1 API class Google::Cloud::RecommendationEngine::V1beta1::UserEventService::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the UserEventService API.

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

### #collect_user_event
    
    
    def collect_user_event() -> ::Gapic::Config::Method

RPC-specific configuration for `collect_user_event`

**Returns**

  * (::Gapic::Config::Method) 



### #import_user_events
    
    
    def import_user_events() -> ::Gapic::Config::Method

RPC-specific configuration for `import_user_events`

**Returns**

  * (::Gapic::Config::Method) 



### #list_user_events
    
    
    def list_user_events() -> ::Gapic::Config::Method

RPC-specific configuration for `list_user_events`

**Returns**

  * (::Gapic::Config::Method) 



### #purge_user_events
    
    
    def purge_user_events() -> ::Gapic::Config::Method

RPC-specific configuration for `purge_user_events`

**Returns**

  * (::Gapic::Config::Method) 



### #write_user_event
    
    
    def write_user_event() -> ::Gapic::Config::Method

RPC-specific configuration for `write_user_event`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
