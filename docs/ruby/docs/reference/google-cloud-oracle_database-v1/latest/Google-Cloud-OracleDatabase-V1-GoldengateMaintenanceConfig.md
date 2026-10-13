---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMaintenanceConfig/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateMaintenanceConfig (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:44.815790+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateMaintenanceConfig (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMaintenanceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateMaintenanceConfig (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::GoldengateMaintenanceConfig.

The maintenance configuration of the GoldengateDeployment.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bundle_release_upgrade_period_days
    
    
    def bundle_release_upgrade_period_days() -> ::Integer

**Returns**

  * (::Integer) — Optional. Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases. This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default. 



### #bundle_release_upgrade_period_days=
    
    
    def bundle_release_upgrade_period_days=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases. This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default. 



**Returns**

  * (::Integer) — Optional. Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases. This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default. 



### #interim_release_upgrade_period_days
    
    
    def interim_release_upgrade_period_days() -> ::Integer

**Returns**

  * (::Integer) — Optional. Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period. 



### #interim_release_upgrade_period_days=
    
    
    def interim_release_upgrade_period_days=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period. 



**Returns**

  * (::Integer) — Optional. Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period. 



### #is_interim_release_auto_upgrade_enabled
    
    
    def is_interim_release_auto_upgrade_enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release, you have to specify interim_release_upgrade_period_days too. 



### #is_interim_release_auto_upgrade_enabled=
    
    
    def is_interim_release_auto_upgrade_enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release, you have to specify interim_release_upgrade_period_days too. 



**Returns**

  * (::Boolean) — Optional. By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release, you have to specify interim_release_upgrade_period_days too. 



### #major_release_upgrade_period_days
    
    
    def major_release_upgrade_period_days() -> ::Integer

**Returns**

  * (::Integer) — Optional. Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases. Not passing this field during create will equate to using the service default. 



### #major_release_upgrade_period_days=
    
    
    def major_release_upgrade_period_days=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases. Not passing this field during create will equate to using the service default. 



**Returns**

  * (::Integer) — Optional. Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases. Not passing this field during create will equate to using the service default. 



### #security_patch_upgrade_period_days
    
    
    def security_patch_upgrade_period_days() -> ::Integer

**Returns**

  * (::Integer) — Optional. Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases. Not passing this field during create will equate to using the service default. 



### #security_patch_upgrade_period_days=
    
    
    def security_patch_upgrade_period_days=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases. Not passing this field during create will equate to using the service default. 



**Returns**

  * (::Integer) — Optional. Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases. Not passing this field during create will equate to using the service default. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
