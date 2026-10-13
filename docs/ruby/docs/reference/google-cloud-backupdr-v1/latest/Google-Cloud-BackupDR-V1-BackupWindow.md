---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupWindow/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupWindow (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:39.507906+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupWindow (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupWindow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupWindow (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupWindow.

`BackupWindow` defines a window of the day during which backup jobs will run.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end_hour_of_day
    
    
    def end_hour_of_day() -> ::Integer

**Returns**

  * (::Integer) — Required. The hour of day (1-24) when the window end for e.g. if value of end hour of day is 10 that mean backup window end time is 10:00.

End hour of day should be greater than start hour of day. 0 <= start_hour_of_day < end_hour_of_day <= 24

End hour of day is not include in backup window that mean if end_hour_of_day= 10 jobs should start before 10:00. 




### #end_hour_of_day=
    
    
    def end_hour_of_day=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The hour of day (1-24) when the window end for e.g. if value of end hour of day is 10 that mean backup window end time is 10:00.

End hour of day should be greater than start hour of day. 0 <= start_hour_of_day < end_hour_of_day <= 24

End hour of day is not include in backup window that mean if end_hour_of_day= 10 jobs should start before 10:00. 




**Returns**

  * (::Integer) — Required. The hour of day (1-24) when the window end for e.g. if value of end hour of day is 10 that mean backup window end time is 10:00.

End hour of day should be greater than start hour of day. 0 <= start_hour_of_day < end_hour_of_day <= 24

End hour of day is not include in backup window that mean if end_hour_of_day= 10 jobs should start before 10:00. 




### #start_hour_of_day
    
    
    def start_hour_of_day() -> ::Integer

**Returns**

  * (::Integer) — Required. The hour of day (0-23) when the window starts for e.g. if value of start hour of day is 6 that mean backup window start at 6:00. 



### #start_hour_of_day=
    
    
    def start_hour_of_day=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The hour of day (0-23) when the window starts for e.g. if value of start hour of day is 6 that mean backup window start at 6:00. 



**Returns**

  * (::Integer) — Required. The hour of day (0-23) when the window starts for e.g. if value of start hour of day is 6 that mean backup window start at 6:00. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
