---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Instance-ClientConnectionConfig/
title: AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::Instance::ClientConnectionConfig (v0.25.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:52.573253+00:00
---

# AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::Instance::ClientConnectionConfig (v0.25.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Instance-ClientConnectionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::Instance::ClientConnectionConfig (v0.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.25.0 (latest)  0.24.1  0.23.1  0.22.0  0.21.0  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1BETA API class Google::Cloud::AlloyDB::V1beta::Instance::ClientConnectionConfig.

Client connection configuration

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #require_connectors
    
    
    def require_connectors() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Configuration to enforce connectors only (ex: AuthProxy) connections to the database. 



### #require_connectors=
    
    
    def require_connectors=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Configuration to enforce connectors only (ex: AuthProxy) connections to the database. 



**Returns**

  * (::Boolean) — Optional. Configuration to enforce connectors only (ex: AuthProxy) connections to the database. 



### #ssl_config
    
    
    def ssl_config() -> ::Google::Cloud::AlloyDB::V1beta::SslConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SslConfig)) — Optional. SSL configuration option for this instance. 



### #ssl_config=
    
    
    def ssl_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::SslConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SslConfig)) — Optional. SSL configuration option for this instance. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SslConfig)) — Optional. SSL configuration option for this instance. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
