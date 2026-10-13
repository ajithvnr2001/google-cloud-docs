---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleConfig/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ScheduleConfig (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:54.684051+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ScheduleConfig (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ScheduleConfig (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::ScheduleConfig.

Timing and frequency parameters for recurring audit runs.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Optional. Date that the schedule stops. If not specified, the schedule runs indefinitely. 



### #end_time=
    
    
    def end_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Optional. Date that the schedule stops. If not specified, the schedule runs indefinitely. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Optional. Date that the schedule stops. If not specified, the schedule runs indefinitely. 



### #frequency
    
    
    def frequency() -> ::Google::Cloud::AuditManager::V1::ScheduleConfig::Frequency

**Returns**

  * ([::Google::Cloud::AuditManager::V1::ScheduleConfig::Frequency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleConfig-Frequency)) — Required. Frequency of audit runs. 



### #frequency=
    
    
    def frequency=(value) -> ::Google::Cloud::AuditManager::V1::ScheduleConfig::Frequency

**Parameter**

  * **value** ([::Google::Cloud::AuditManager::V1::ScheduleConfig::Frequency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleConfig-Frequency)) — Required. Frequency of audit runs. 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ScheduleConfig::Frequency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleConfig-Frequency)) — Required. Frequency of audit runs. 



### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Date and time when the first audit run is triggered. Subsequent runs are based on this time and the chosen frequency. 



### #start_time=
    
    
    def start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Date and time when the first audit run is triggered. Subsequent runs are based on this time and the chosen frequency. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Date and time when the first audit run is triggered. Subsequent runs are based on this time and the chosen frequency. 



### #time_zone
    
    
    def time_zone() -> ::String

**Returns**

  * (::String) — Optional. Time zone for the audit schedule in IANA format (for example, `America/New_York`). The time zone is used to interpret the `start_time` and the `end_time`, and to calculate subsequent run dates. If not specified, the time zone default is UTC. 



### #time_zone=
    
    
    def time_zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Time zone for the audit schedule in IANA format (for example, `America/New_York`). The time zone is used to interpret the `start_time` and the `end_time`, and to calculate subsequent run dates. If not specified, the time zone default is UTC. 



**Returns**

  * (::String) — Optional. Time zone for the audit schedule in IANA format (for example, `America/New_York`). The time zone is used to interpret the `start_time` and the `end_time`, and to calculate subsequent run dates. If not specified, the time zone default is UTC. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
