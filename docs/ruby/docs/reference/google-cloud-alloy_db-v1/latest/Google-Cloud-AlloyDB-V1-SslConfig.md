---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SslConfig/
title: AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::SslConfig (v1.10.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:55.307090+00:00
---

# AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::SslConfig (v1.10.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SslConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::SslConfig (v1.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.2 (latest)  1.10.1  1.9.0  1.7.0  1.6.2  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.12.0  0.11.0  0.10.0  0.9.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1 API class Google::Cloud::AlloyDB::V1::SslConfig.

SSL configuration.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ca_source
    
    
    def ca_source() -> ::Google::Cloud::AlloyDB::V1::SslConfig::CaSource

**Returns**

  * ([::Google::Cloud::AlloyDB::V1::SslConfig::CaSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SslConfig-CaSource)) — Optional. Certificate Authority (CA) source. Only CA_SOURCE_MANAGED is supported currently, and is the default value. 



### #ca_source=
    
    
    def ca_source=(value) -> ::Google::Cloud::AlloyDB::V1::SslConfig::CaSource

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1::SslConfig::CaSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SslConfig-CaSource)) — Optional. Certificate Authority (CA) source. Only CA_SOURCE_MANAGED is supported currently, and is the default value. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::SslConfig::CaSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SslConfig-CaSource)) — Optional. Certificate Authority (CA) source. Only CA_SOURCE_MANAGED is supported currently, and is the default value. 



### #ssl_mode
    
    
    def ssl_mode() -> ::Google::Cloud::AlloyDB::V1::SslConfig::SslMode

**Returns**

  * ([::Google::Cloud::AlloyDB::V1::SslConfig::SslMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SslConfig-SslMode)) — Optional. SSL mode. Specifies client-server SSL/TLS connection behavior. 



### #ssl_mode=
    
    
    def ssl_mode=(value) -> ::Google::Cloud::AlloyDB::V1::SslConfig::SslMode

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1::SslConfig::SslMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SslConfig-SslMode)) — Optional. SSL mode. Specifies client-server SSL/TLS connection behavior. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::SslConfig::SslMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SslConfig-SslMode)) — Optional. SSL mode. Specifies client-server SSL/TLS connection behavior. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
