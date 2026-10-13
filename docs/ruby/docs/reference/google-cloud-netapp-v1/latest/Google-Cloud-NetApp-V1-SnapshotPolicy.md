---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-SnapshotPolicy/
title: NetApp V1 API - Class Google::Cloud::NetApp::V1::SnapshotPolicy (v2.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:40.964391+00:00
---

# NetApp V1 API - Class Google::Cloud::NetApp::V1::SnapshotPolicy (v2.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-SnapshotPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  NetApp V1 API - Class Google::Cloud::NetApp::V1::SnapshotPolicy (v2.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.2 (latest)  2.12.1  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.6.0  0.5.2  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the NetApp V1 API class Google::Cloud::NetApp::V1::SnapshotPolicy.

Snapshot Policy for a volume.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #daily_schedule
    
    
    def daily_schedule() -> ::Google::Cloud::NetApp::V1::DailySchedule

**Returns**

  * ([::Google::Cloud::NetApp::V1::DailySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DailySchedule)) — Daily schedule policy. 



### #daily_schedule=
    
    
    def daily_schedule=(value) -> ::Google::Cloud::NetApp::V1::DailySchedule

**Parameter**

  * **value** ([::Google::Cloud::NetApp::V1::DailySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DailySchedule)) — Daily schedule policy. 



**Returns**

  * ([::Google::Cloud::NetApp::V1::DailySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DailySchedule)) — Daily schedule policy. 



### #enabled
    
    
    def enabled() -> ::Boolean

**Returns**

  * (::Boolean) — If enabled, make snapshots automatically according to the schedules. Default is false. 



### #enabled=
    
    
    def enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If enabled, make snapshots automatically according to the schedules. Default is false. 



**Returns**

  * (::Boolean) — If enabled, make snapshots automatically according to the schedules. Default is false. 



### #hourly_schedule
    
    
    def hourly_schedule() -> ::Google::Cloud::NetApp::V1::HourlySchedule

**Returns**

  * ([::Google::Cloud::NetApp::V1::HourlySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-HourlySchedule)) — Hourly schedule policy. 



### #hourly_schedule=
    
    
    def hourly_schedule=(value) -> ::Google::Cloud::NetApp::V1::HourlySchedule

**Parameter**

  * **value** ([::Google::Cloud::NetApp::V1::HourlySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-HourlySchedule)) — Hourly schedule policy. 



**Returns**

  * ([::Google::Cloud::NetApp::V1::HourlySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-HourlySchedule)) — Hourly schedule policy. 



### #monthly_schedule
    
    
    def monthly_schedule() -> ::Google::Cloud::NetApp::V1::MonthlySchedule

**Returns**

  * ([::Google::Cloud::NetApp::V1::MonthlySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-MonthlySchedule)) — Monthly schedule policy. 



### #monthly_schedule=
    
    
    def monthly_schedule=(value) -> ::Google::Cloud::NetApp::V1::MonthlySchedule

**Parameter**

  * **value** ([::Google::Cloud::NetApp::V1::MonthlySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-MonthlySchedule)) — Monthly schedule policy. 



**Returns**

  * ([::Google::Cloud::NetApp::V1::MonthlySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-MonthlySchedule)) — Monthly schedule policy. 



### #weekly_schedule
    
    
    def weekly_schedule() -> ::Google::Cloud::NetApp::V1::WeeklySchedule

**Returns**

  * ([::Google::Cloud::NetApp::V1::WeeklySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-WeeklySchedule)) — Weekly schedule policy. 



### #weekly_schedule=
    
    
    def weekly_schedule=(value) -> ::Google::Cloud::NetApp::V1::WeeklySchedule

**Parameter**

  * **value** ([::Google::Cloud::NetApp::V1::WeeklySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-WeeklySchedule)) — Weekly schedule policy. 



**Returns**

  * ([::Google::Cloud::NetApp::V1::WeeklySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-WeeklySchedule)) — Weekly schedule policy. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
