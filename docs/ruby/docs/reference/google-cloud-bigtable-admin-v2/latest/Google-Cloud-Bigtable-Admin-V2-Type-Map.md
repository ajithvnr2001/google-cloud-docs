---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-Map/
title: Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Type::Map (v1.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:06.862385+00:00
---

# Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Type::Map (v1.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-Map/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Type::Map (v1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.3  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.1 

Reference documentation and code samples for the Cloud Bigtable Admin V2 API class Google::Cloud::Bigtable::Admin::V2::Type::Map.

A mapping of keys to values of a given type. Values of type `Map` are stored in a `Value.array_value` where each entry is another `Value.array_value` with two elements (the key and the value, in that order). Normally encoded Map values won't have repeated keys, however, clients are expected to handle the case in which they do. If the same key appears multiple times, the _last_ value takes precedence.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #key_type
    
    
    def key_type() -> ::Google::Cloud::Bigtable::Admin::V2::Type

**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type)) — The type of a map key. Only `Bytes`, `String`, and `Int64` are allowed as key types. 



### #key_type=
    
    
    def key_type=(value) -> ::Google::Cloud::Bigtable::Admin::V2::Type

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::Admin::V2::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type)) — The type of a map key. Only `Bytes`, `String`, and `Int64` are allowed as key types. 



**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type)) — The type of a map key. Only `Bytes`, `String`, and `Int64` are allowed as key types. 



### #value_type
    
    
    def value_type() -> ::Google::Cloud::Bigtable::Admin::V2::Type

**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type)) — The type of the values in a map. 



### #value_type=
    
    
    def value_type=(value) -> ::Google::Cloud::Bigtable::Admin::V2::Type

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::Admin::V2::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type)) — The type of the values in a map. 



**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type)) — The type of the values in a map. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
