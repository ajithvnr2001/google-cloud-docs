---
url: https://docs.cloud.google.com/python/docs/reference/composer/latest/google.cloud.orchestration.airflow.service_v1beta1.types.MaintenanceWindow
title: Class MaintenanceWindow (1.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:50.397678+00:00
---

# Class MaintenanceWindow (1.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/composer/latest/google.cloud.orchestration.airflow.service_v1beta1.types.MaintenanceWindow

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MaintenanceWindow (1.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.23.0 (latest)  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.5  1.16.1  1.15.1  1.14.0  1.13.1  1.12.2  1.11.1  1.10.0  1.9.1  1.8.0  1.7.1  1.6.1  1.5.0  1.4.4  1.3.2  1.2.1  1.1.0  1.0.0  0.1.3 
    
    
    MaintenanceWindow(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The configuration settings for Cloud Composer maintenance window. The following example:

::
    
    
      {
        "startTime":"2019-08-01T01:00:00Z"
        "endTime":"2019-08-01T07:00:00Z"
        "recurrence":"FREQ=WEEKLY;BYDAY=TU,WE"
      }
    

would define a maintenance window between 01 and 07 hours UTC during each Tuesday and Wednesday.

## Attributes  
  
---  
**Name** | **Description**  
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. Start time of the first recurrence of the maintenance window.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. Maintenance window end time. It is used only to calculate the duration of the maintenance window. The value for end_time must be in the future, relative to `start_time`.   
`recurrence` |  `str`   
Required. Maintenance window recurrence. Format is a subset of `RFC-5545 `__ `RRULE`. The only allowed values for `FREQ` field are `FREQ=DAILY` and `FREQ=WEEKLY;BYDAY=...` Example values: `FREQ=WEEKLY;BYDAY=TU,WE`, `FREQ=DAILY`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
