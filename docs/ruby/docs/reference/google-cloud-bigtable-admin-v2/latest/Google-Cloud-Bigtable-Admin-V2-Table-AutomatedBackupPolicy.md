---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Table-AutomatedBackupPolicy/
title: Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Table::AutomatedBackupPolicy (v1.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:52.019843+00:00
---

# Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Table::AutomatedBackupPolicy (v1.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Table-AutomatedBackupPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Table::AutomatedBackupPolicy (v1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.3  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.1 

Reference documentation and code samples for the Cloud Bigtable Admin V2 API class Google::Cloud::Bigtable::Admin::V2::Table::AutomatedBackupPolicy.

Defines an automated backup policy for a table

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #disabled
    
    
    def disabled() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If `true`, automated backups are explicitly disabled on this table. This allows users to opt out of default enablement. 



### #disabled=
    
    
    def disabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If `true`, automated backups are explicitly disabled on this table. This allows users to opt out of default enablement. 



**Returns**

  * (::Boolean) — Optional. If `true`, automated backups are explicitly disabled on this table. This allows users to opt out of default enablement. 



### #frequency
    
    
    def frequency() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — How frequently automated backups should occur. The only supported value at this time is 24 hours. An undefined frequency is treated as 24 hours. 



### #frequency=
    
    
    def frequency=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — How frequently automated backups should occur. The only supported value at this time is 24 hours. An undefined frequency is treated as 24 hours. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — How frequently automated backups should occur. The only supported value at this time is 24 hours. An undefined frequency is treated as 24 hours. 



### #keep_hot_duration
    
    
    def keep_hot_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — Optional. The amount of time that the automated backups remain hot. If specified, the backups created by this policy are `HOT` backups. If not specified, the backups are `STANDARD` backups.

The value must be at least 24 hours and at most 10 days, and can't exceed the policy's `retention_period`.

Only SSD instances support `HOT` automated backups. 




### #keep_hot_duration=
    
    
    def keep_hot_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — Optional. The amount of time that the automated backups remain hot. If specified, the backups created by this policy are `HOT` backups. If not specified, the backups are `STANDARD` backups.

The value must be at least 24 hours and at most 10 days, and can't exceed the policy's `retention_period`.

Only SSD instances support `HOT` automated backups. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — Optional. The amount of time that the automated backups remain hot. If specified, the backups created by this policy are `HOT` backups. If not specified, the backups are `STANDARD` backups.

The value must be at least 24 hours and at most 10 days, and can't exceed the policy's `retention_period`.

Only SSD instances support `HOT` automated backups. 




### #locations
    
    
    def locations() -> ::Array<::String>

**Returns**

  * ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-Array)<[::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)>) — Optional. A list of Cloud Bigtable zones where automated backups are allowed to be created. If empty, automated backups will be created in all zones of the instance. Locations are in the format `projects/{project}/locations/{zone}`. This field can only set for tables in Enterprise Plus instances. 



### #locations=
    
    
    def locations=(value) -> ::Array<::String>

**Parameter**

  * **value** ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-Array)<[::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)>) — Optional. A list of Cloud Bigtable zones where automated backups are allowed to be created. If empty, automated backups will be created in all zones of the instance. Locations are in the format `projects/{project}/locations/{zone}`. This field can only set for tables in Enterprise Plus instances. 



**Returns**

  * ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-Array)<[::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)>) — Optional. A list of Cloud Bigtable zones where automated backups are allowed to be created. If empty, automated backups will be created in all zones of the instance. Locations are in the format `projects/{project}/locations/{zone}`. This field can only set for tables in Enterprise Plus instances. 



### #retention_period
    
    
    def retention_period() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — Required. How long the automated backups should be retained. Values must be at least 3 days and at most 90 days. 



### #retention_period=
    
    
    def retention_period=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — Required. How long the automated backups should be retained. Values must be at least 3 days and at most 90 days. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Protobuf-Duration)) — Required. How long the automated backups should be retained. Values must be at least 3 days and at most 90 days. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
