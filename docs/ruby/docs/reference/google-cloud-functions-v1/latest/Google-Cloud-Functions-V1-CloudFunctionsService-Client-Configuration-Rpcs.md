---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v1/latest/Google-Cloud-Functions-V1-CloudFunctionsService-Client-Configuration-Rpcs/
title: Cloud Functions V1 API - Class Google::Cloud::Functions::V1::CloudFunctionsService::Client::Configuration::Rpcs (v2.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:29.887739+00:00
---

# Cloud Functions V1 API - Class Google::Cloud::Functions::V1::CloudFunctionsService::Client::Configuration::Rpcs (v2.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v1/latest/Google-Cloud-Functions-V1-CloudFunctionsService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Functions V1 API - Class Google::Cloud::Functions::V1::CloudFunctionsService::Client::Configuration::Rpcs (v2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.1  2.4.0  2.3.1  2.2.0  2.1.0  2.0.2  1.3.0  1.2.0  1.1.1  1.0.0  0.15.0  0.14.1  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.1 

Reference documentation and code samples for the Cloud Functions V1 API class Google::Cloud::Functions::V1::CloudFunctionsService::Client::Configuration::Rpcs.

Configuration RPC class for the CloudFunctionsService API.

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

### #call_function
    
    
    def call_function() -> ::Gapic::Config::Method

RPC-specific configuration for `call_function`

**Returns**

  * (::Gapic::Config::Method) 



### #create_function
    
    
    def create_function() -> ::Gapic::Config::Method

RPC-specific configuration for `create_function`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_function
    
    
    def delete_function() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_function`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_download_url
    
    
    def generate_download_url() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_download_url`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_upload_url
    
    
    def generate_upload_url() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_upload_url`

**Returns**

  * (::Gapic::Config::Method) 



### #get_function
    
    
    def get_function() -> ::Gapic::Config::Method

RPC-specific configuration for `get_function`

**Returns**

  * (::Gapic::Config::Method) 



### #get_iam_policy
    
    
    def get_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #list_functions
    
    
    def list_functions() -> ::Gapic::Config::Method

RPC-specific configuration for `list_functions`

**Returns**

  * (::Gapic::Config::Method) 



### #set_iam_policy
    
    
    def set_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `set_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #test_iam_permissions
    
    
    def test_iam_permissions() -> ::Gapic::Config::Method

RPC-specific configuration for `test_iam_permissions`

**Returns**

  * (::Gapic::Config::Method) 



### #update_function
    
    
    def update_function() -> ::Gapic::Config::Method

RPC-specific configuration for `update_function`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
