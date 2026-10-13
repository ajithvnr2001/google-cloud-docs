---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-TransferParameters/
title: Cloud Domains V1 API - Class Google::Cloud::Domains::V1::TransferParameters (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:06.985406+00:00
---

# Cloud Domains V1 API - Class Google::Cloud::Domains::V1::TransferParameters (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-TransferParameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Domains V1 API - Class Google::Cloud::Domains::V1::TransferParameters (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Domains V1 API class Google::Cloud::Domains::V1::TransferParameters.

Parameters required to transfer a domain from another registrar.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #current_registrar
    
    
    def current_registrar() -> ::String

**Returns**

  * (::String) — The registrar that currently manages the domain. 



### #current_registrar=
    
    
    def current_registrar=(value) -> ::String

**Parameter**

  * **value** (::String) — The registrar that currently manages the domain. 



**Returns**

  * (::String) — The registrar that currently manages the domain. 



### #domain_name
    
    
    def domain_name() -> ::String

**Returns**

  * (::String) — The domain name. Unicode domain names are expressed in Punycode format. 



### #domain_name=
    
    
    def domain_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The domain name. Unicode domain names are expressed in Punycode format. 



**Returns**

  * (::String) — The domain name. Unicode domain names are expressed in Punycode format. 



### #name_servers
    
    
    def name_servers() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The name servers that currently store the configuration of the domain. 



### #name_servers=
    
    
    def name_servers=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The name servers that currently store the configuration of the domain. 



**Returns**

  * (::Array<::String>) — The name servers that currently store the configuration of the domain. 



### #supported_privacy
    
    
    def supported_privacy() -> ::Array<::Google::Cloud::Domains::V1::ContactPrivacy>

**Returns**

  * (::Array<[::Google::Cloud::Domains::V1::ContactPrivacy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ContactPrivacy)>) — Contact privacy options that the domain supports. 



### #supported_privacy=
    
    
    def supported_privacy=(value) -> ::Array<::Google::Cloud::Domains::V1::ContactPrivacy>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Domains::V1::ContactPrivacy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ContactPrivacy)>) — Contact privacy options that the domain supports. 



**Returns**

  * (::Array<[::Google::Cloud::Domains::V1::ContactPrivacy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-ContactPrivacy)>) — Contact privacy options that the domain supports. 



### #transfer_lock_state
    
    
    def transfer_lock_state() -> ::Google::Cloud::Domains::V1::TransferLockState

**Returns**

  * ([::Google::Cloud::Domains::V1::TransferLockState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-TransferLockState)) — Indicates whether the domain is protected by a transfer lock. For a transfer to succeed, this must show `UNLOCKED`. To unlock a domain, go to its current registrar. 



### #transfer_lock_state=
    
    
    def transfer_lock_state=(value) -> ::Google::Cloud::Domains::V1::TransferLockState

**Parameter**

  * **value** ([::Google::Cloud::Domains::V1::TransferLockState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-TransferLockState)) — Indicates whether the domain is protected by a transfer lock. For a transfer to succeed, this must show `UNLOCKED`. To unlock a domain, go to its current registrar. 



**Returns**

  * ([::Google::Cloud::Domains::V1::TransferLockState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-TransferLockState)) — Indicates whether the domain is protected by a transfer lock. For a transfer to succeed, this must show `UNLOCKED`. To unlock a domain, go to its current registrar. 



### #yearly_price
    
    
    def yearly_price() -> ::Google::Type::Money

**Returns**

  * ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Type-Money)) — Price to transfer or renew the domain for one year. 



### #yearly_price=
    
    
    def yearly_price=(value) -> ::Google::Type::Money

**Parameter**

  * **value** ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Type-Money)) — Price to transfer or renew the domain for one year. 



**Returns**

  * ([::Google::Type::Money](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Type-Money)) — Price to transfer or renew the domain for one year. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
