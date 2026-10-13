---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration-Rpcs/
title: Cloud Trace V2 API - Class Google::Cloud::Trace::V2::TraceService::Client::Configuration::Rpcs (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:37.556027+00:00
---

# Cloud Trace V2 API - Class Google::Cloud::Trace::V2::TraceService::Client::Configuration::Rpcs (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Trace V2 API - Class Google::Cloud::Trace::V2::TraceService::Client::Configuration::Rpcs (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.1  0.5.0  0.4.1  0.3.5 

Reference documentation and code samples for the Cloud Trace V2 API class Google::Cloud::Trace::V2::TraceService::Client::Configuration::Rpcs.

Configuration RPC class for the TraceService API.

Includes fields providing the configuration for each RPC in this service. Each configuration object is of type `Gapic::Config::Method` and includes the following configuration fields:

  * `timeout` (_type:_ `Numeric`) - The call timeout in seconds
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional gRPC headers
  * `retry_policy (_type:_`Hash`) - The retry policy. The policy fields include the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



## Inherits

  * Object 



## Methods 

### #batch_write_spans
    
    
    def batch_write_spans() -> ::Gapic::Config::Method

RPC-specific configuration for `batch_write_spans`

**Returns**

  * (::Gapic::Config::Method) 



### #create_span
    
    
    def create_span() -> ::Gapic::Config::Method

RPC-specific configuration for `create_span`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
