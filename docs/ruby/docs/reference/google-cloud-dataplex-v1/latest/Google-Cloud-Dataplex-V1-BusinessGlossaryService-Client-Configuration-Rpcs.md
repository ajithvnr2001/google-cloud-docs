---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Client-Configuration-Rpcs/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client::Configuration::Rpcs (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:56.777027+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client::Configuration::Rpcs (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-BusinessGlossaryService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client::Configuration::Rpcs (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client::Configuration::Rpcs.

Configuration RPC class for the BusinessGlossaryService API.

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

### #create_glossary
    
    
    def create_glossary() -> ::Gapic::Config::Method

RPC-specific configuration for `create_glossary`

**Returns**

  * (::Gapic::Config::Method) 



### #create_glossary_category
    
    
    def create_glossary_category() -> ::Gapic::Config::Method

RPC-specific configuration for `create_glossary_category`

**Returns**

  * (::Gapic::Config::Method) 



### #create_glossary_term
    
    
    def create_glossary_term() -> ::Gapic::Config::Method

RPC-specific configuration for `create_glossary_term`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_glossary
    
    
    def delete_glossary() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_glossary`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_glossary_category
    
    
    def delete_glossary_category() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_glossary_category`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_glossary_term
    
    
    def delete_glossary_term() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_glossary_term`

**Returns**

  * (::Gapic::Config::Method) 



### #get_glossary
    
    
    def get_glossary() -> ::Gapic::Config::Method

RPC-specific configuration for `get_glossary`

**Returns**

  * (::Gapic::Config::Method) 



### #get_glossary_category
    
    
    def get_glossary_category() -> ::Gapic::Config::Method

RPC-specific configuration for `get_glossary_category`

**Returns**

  * (::Gapic::Config::Method) 



### #get_glossary_term
    
    
    def get_glossary_term() -> ::Gapic::Config::Method

RPC-specific configuration for `get_glossary_term`

**Returns**

  * (::Gapic::Config::Method) 



### #list_glossaries
    
    
    def list_glossaries() -> ::Gapic::Config::Method

RPC-specific configuration for `list_glossaries`

**Returns**

  * (::Gapic::Config::Method) 



### #list_glossary_categories
    
    
    def list_glossary_categories() -> ::Gapic::Config::Method

RPC-specific configuration for `list_glossary_categories`

**Returns**

  * (::Gapic::Config::Method) 



### #list_glossary_terms
    
    
    def list_glossary_terms() -> ::Gapic::Config::Method

RPC-specific configuration for `list_glossary_terms`

**Returns**

  * (::Gapic::Config::Method) 



### #update_glossary
    
    
    def update_glossary() -> ::Gapic::Config::Method

RPC-specific configuration for `update_glossary`

**Returns**

  * (::Gapic::Config::Method) 



### #update_glossary_category
    
    
    def update_glossary_category() -> ::Gapic::Config::Method

RPC-specific configuration for `update_glossary_category`

**Returns**

  * (::Gapic::Config::Method) 



### #update_glossary_term
    
    
    def update_glossary_term() -> ::Gapic::Config::Method

RPC-specific configuration for `update_glossary_term`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
