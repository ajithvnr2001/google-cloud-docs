---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesVerifyExternalSyncSettingsResponse/
title: Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsResponse (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:16.602616+00:00
---

# Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsResponse (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesVerifyExternalSyncSettingsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsResponse (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API class Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsResponse.

Instance verify external sync settings response.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #errors
    
    
    def errors() -> ::Array<::Google::Cloud::Sql::V1::SqlExternalSyncSettingError>

**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::SqlExternalSyncSettingError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlExternalSyncSettingError)>) — List of migration violations. 



### #errors=
    
    
    def errors=(value) -> ::Array<::Google::Cloud::Sql::V1::SqlExternalSyncSettingError>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Sql::V1::SqlExternalSyncSettingError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlExternalSyncSettingError)>) — List of migration violations. 



**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::SqlExternalSyncSettingError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlExternalSyncSettingError)>) — List of migration violations. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — This is always `sql#migrationSettingErrorList`. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — This is always `sql#migrationSettingErrorList`. 



**Returns**

  * (::String) — This is always `sql#migrationSettingErrorList`. 



### #warnings
    
    
    def warnings() -> ::Array<::Google::Cloud::Sql::V1::SqlExternalSyncSettingError>

**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::SqlExternalSyncSettingError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlExternalSyncSettingError)>) — List of migration warnings. 



### #warnings=
    
    
    def warnings=(value) -> ::Array<::Google::Cloud::Sql::V1::SqlExternalSyncSettingError>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Sql::V1::SqlExternalSyncSettingError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlExternalSyncSettingError)>) — List of migration warnings. 



**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::SqlExternalSyncSettingError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlExternalSyncSettingError)>) — List of migration warnings. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
