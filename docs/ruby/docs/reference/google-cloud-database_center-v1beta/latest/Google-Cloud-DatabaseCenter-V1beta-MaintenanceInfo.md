---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-MaintenanceInfo/
title: Database Center V1BETA API - Class Google::Cloud::DatabaseCenter::V1beta::MaintenanceInfo (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:53.645761+00:00
---

# Database Center V1BETA API - Class Google::Cloud::DatabaseCenter::V1beta::MaintenanceInfo (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-MaintenanceInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Database Center V1BETA API - Class Google::Cloud::DatabaseCenter::V1beta::MaintenanceInfo (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Database Center V1BETA API class Google::Cloud::DatabaseCenter::V1beta::MaintenanceInfo.

MaintenanceInfo to capture the maintenance details of database resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #current_version_release_date
    
    
    def current_version_release_date() -> ::Google::Type::Date

**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Type-Date)) — Output only. The date when the maintenance version was released. 



### #deny_maintenance_schedules
    
    
    def deny_maintenance_schedules() -> ::Array<::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceDenySchedule>

**Returns**

  * (::Array<[::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-ResourceMaintenanceDenySchedule)>) — Optional. List of Deny maintenance period for the database resource. 



### #deny_maintenance_schedules=
    
    
    def deny_maintenance_schedules=(value) -> ::Array<::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceDenySchedule>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-ResourceMaintenanceDenySchedule)>) — Optional. List of Deny maintenance period for the database resource. 



**Returns**

  * (::Array<[::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-ResourceMaintenanceDenySchedule)>) — Optional. List of Deny maintenance period for the database resource. 



### #maintenance_schedule
    
    
    def maintenance_schedule() -> ::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceSchedule

**Returns**

  * ([::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-ResourceMaintenanceSchedule)) — Optional. Maintenance window for the database resource. 



### #maintenance_schedule=
    
    
    def maintenance_schedule=(value) -> ::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceSchedule

**Parameter**

  * **value** ([::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-ResourceMaintenanceSchedule)) — Optional. Maintenance window for the database resource. 



**Returns**

  * ([::Google::Cloud::DatabaseCenter::V1beta::ResourceMaintenanceSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-ResourceMaintenanceSchedule)) — Optional. Maintenance window for the database resource. 



### #maintenance_version
    
    
    def maintenance_version() -> ::String

**Returns**

  * (::String) — Output only. Current Maintenance version of the database resource. Example: "MYSQL_8_0_41.R20250531.01_15" 



### #possible_failure_reasons
    
    
    def possible_failure_reasons() -> ::Array<::Google::Cloud::DatabaseCenter::V1beta::PossibleFailureReason>

**Returns**

  * (::Array<[::Google::Cloud::DatabaseCenter::V1beta::PossibleFailureReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-PossibleFailureReason)>) — Output only. List of possible reasons why the maintenance is not completed. This is an optional field and is only populated if there are any reasons for failures recorded for the maintenance by DB Center. FAILURE maintenance status may not always have a failure reason. 



### #previous_maintenance_version
    
    
    def previous_maintenance_version() -> ::String

**Returns**

  * (::String) — Output only. Previous maintenance version of the database resource. Example: "MYSQL_8_0_41.R20250531.01_15". This is available once a minor version maintenance is complete on a database resource. 



### #state
    
    
    def state() -> ::Google::Cloud::DatabaseCenter::V1beta::MaintenanceState

**Returns**

  * ([::Google::Cloud::DatabaseCenter::V1beta::MaintenanceState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-MaintenanceState)) — Output only. Resource maintenance state. This is to capture the current state of the maintenance. 



### #upcoming_maintenance
    
    
    def upcoming_maintenance() -> ::Google::Cloud::DatabaseCenter::V1beta::UpcomingMaintenance

**Returns**

  * ([::Google::Cloud::DatabaseCenter::V1beta::UpcomingMaintenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-UpcomingMaintenance)) — Output only. Upcoming maintenance window for the database resource. This is only populated for an engine, if upcoming maintenance is scheduled for the resource. This schedule is generated per engine and engine version, and there is only one upcoming maintenance window at any given time. In case of upcoming maintenance, the maintenance_state will be set to SCHEDULED first, and then IN_PROGRESS when the maintenance window starts. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
