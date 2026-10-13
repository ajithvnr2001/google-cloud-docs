---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceBackupApplianceApplication/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:43.347070+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceBackupApplianceApplication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication.

BackupApplianceApplication describes a Source Resource when it is an application backed up by a BackupAppliance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #appliance_id
    
    
    def appliance_id() -> ::Integer

**Returns**

  * (::Integer) — Appliance Id of the Backup Appliance. 



### #appliance_id=
    
    
    def appliance_id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Appliance Id of the Backup Appliance. 



**Returns**

  * (::Integer) — Appliance Id of the Backup Appliance. 



### #application_id
    
    
    def application_id() -> ::Integer

**Returns**

  * (::Integer) — The appid field of the application within the Backup Appliance. 



### #application_id=
    
    
    def application_id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The appid field of the application within the Backup Appliance. 



**Returns**

  * (::Integer) — The appid field of the application within the Backup Appliance. 



### #application_name
    
    
    def application_name() -> ::String

**Returns**

  * (::String) — The name of the Application as known to the Backup Appliance. 



### #application_name=
    
    
    def application_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the Application as known to the Backup Appliance. 



**Returns**

  * (::String) — The name of the Application as known to the Backup Appliance. 



### #backup_appliance
    
    
    def backup_appliance() -> ::String

**Returns**

  * (::String) — Appliance name. 



### #backup_appliance=
    
    
    def backup_appliance=(value) -> ::String

**Parameter**

  * **value** (::String) — Appliance name. 



**Returns**

  * (::String) — Appliance name. 



### #host_id
    
    
    def host_id() -> ::Integer

**Returns**

  * (::Integer) — Hostid of the application host. 



### #host_id=
    
    
    def host_id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Hostid of the application host. 



**Returns**

  * (::Integer) — Hostid of the application host. 



### #hostname
    
    
    def hostname() -> ::String

**Returns**

  * (::String) — Hostname of the host where the application is running. 



### #hostname=
    
    
    def hostname=(value) -> ::String

**Parameter**

  * **value** (::String) — Hostname of the host where the application is running. 



**Returns**

  * (::String) — Hostname of the host where the application is running. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — The type of the application. e.g. VMBackup 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — The type of the application. e.g. VMBackup 



**Returns**

  * (::String) — The type of the application. e.g. VMBackup 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
