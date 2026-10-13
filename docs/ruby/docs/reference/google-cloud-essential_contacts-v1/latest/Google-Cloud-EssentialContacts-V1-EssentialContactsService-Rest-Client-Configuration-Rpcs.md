---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-essential_contacts-v1/latest/Google-Cloud-EssentialContacts-V1-EssentialContactsService-Rest-Client-Configuration-Rpcs/
title: Essential Contacts V1 API - Class Google::Cloud::EssentialContacts::V1::EssentialContactsService::Rest::Client::Configuration::Rpcs (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:08.058784+00:00
---

# Essential Contacts V1 API - Class Google::Cloud::EssentialContacts::V1::EssentialContactsService::Rest::Client::Configuration::Rpcs (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-essential_contacts-v1/latest/Google-Cloud-EssentialContacts-V1-EssentialContactsService-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Essential Contacts V1 API - Class Google::Cloud::EssentialContacts::V1::EssentialContactsService::Rest::Client::Configuration::Rpcs (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.7.0  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Essential Contacts V1 API class Google::Cloud::EssentialContacts::V1::EssentialContactsService::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the EssentialContactsService API.

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

### #compute_contacts
    
    
    def compute_contacts() -> ::Gapic::Config::Method

RPC-specific configuration for `compute_contacts`

**Returns**

  * (::Gapic::Config::Method) 



### #create_contact
    
    
    def create_contact() -> ::Gapic::Config::Method

RPC-specific configuration for `create_contact`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_contact
    
    
    def delete_contact() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_contact`

**Returns**

  * (::Gapic::Config::Method) 



### #get_contact
    
    
    def get_contact() -> ::Gapic::Config::Method

RPC-specific configuration for `get_contact`

**Returns**

  * (::Gapic::Config::Method) 



### #list_contacts
    
    
    def list_contacts() -> ::Gapic::Config::Method

RPC-specific configuration for `list_contacts`

**Returns**

  * (::Gapic::Config::Method) 



### #send_test_message
    
    
    def send_test_message() -> ::Gapic::Config::Method

RPC-specific configuration for `send_test_message`

**Returns**

  * (::Gapic::Config::Method) 



### #update_contact
    
    
    def update_contact() -> ::Gapic::Config::Method

RPC-specific configuration for `update_contact`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
