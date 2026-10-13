---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-DbHome/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::DbHome (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:38.370228+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::DbHome (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-DbHome/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::DbHome (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::DbHome.

Details of the Database Home resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #database
    
    
    def database() -> ::Google::Cloud::OracleDatabase::V1::Database

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-Database)) — Required. The Database resource. 



### #database=
    
    
    def database=(value) -> ::Google::Cloud::OracleDatabase::V1::Database

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-Database)) — Required. The Database resource. 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-Database)) — Required. The Database resource. 



### #db_version
    
    
    def db_version() -> ::String

**Returns**

  * (::String) — Required. A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. 



### #db_version=
    
    
    def db_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. 



**Returns**

  * (::String) — Required. A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Optional. The display name for the Database Home. The name does not have to be unique within your project. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The display name for the Database Home. The name does not have to be unique within your project. 



**Returns**

  * (::String) — Optional. The display name for the Database Home. The name does not have to be unique within your project. 



### #is_unified_auditing_enabled
    
    
    def is_unified_auditing_enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether unified auditing is enabled for the Database Home. 



### #is_unified_auditing_enabled=
    
    
    def is_unified_auditing_enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether unified auditing is enabled for the Database Home. 



**Returns**

  * (::Boolean) — Optional. Whether unified auditing is enabled for the Database Home. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
