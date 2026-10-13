---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule/
title: ResourceMaintenanceSchedule \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:29.134458+00:00
---

# ResourceMaintenanceSchedule  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  ResourceMaintenanceSchedule Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DayOfWeek
  * Phase



Maintenance window for the database resource. It specifies preferred time and day of the week and phase in some cases, when the maintenance can start.

JSON representation  
---  
      
    
    {
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TimeOfDay))
      },
      "day": enum ([DayOfWeek](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule#DayOfWeek)),
      "phase": enum ([Phase](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule#Phase))
    }  
  
Fields  
---  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TimeOfDay)`)` Optional. Preferred time to start the maintenance operation on the specified day.  
`day` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule#DayOfWeek)`)` Optional. Preferred day of the week for maintenance, e.g. MONDAY, TUESDAY, etc.  
`phase` |  `enum (`[Phase](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule#Phase)`)` Optional. Phase of the maintenance window. This is to capture order of maintenance. For example, for Cloud SQL resources, this can be used to capture if the maintenance window is in Week1, Week2, Week5, etc. Non production resources are usually part of early phase. For more details, refer to Cloud SQL resources - <https://cloud.google.com/sql/docs/mysql/maintenance>  
  
## DayOfWeek

Represents a day of the week.

Enums  
---  
`DAY_OF_WEEK_UNSPECIFIED` | The day of the week is unspecified.  
`MONDAY` | Monday  
`TUESDAY` | Tuesday  
`WEDNESDAY` | Wednesday  
`THURSDAY` | Thursday  
`FRIDAY` | Friday  
`SATURDAY` | Saturday  
`SUNDAY` | Sunday  
  
## Phase

Phase/Week of the maintenance window. This is to capture order of maintenance. For example, for Cloud SQL resources - <https://cloud.google.com/sql/docs/mysql/maintenance>. This enum can be extended to support DB Center specific phases for recommendation plan generation.

Enums  
---  
`PHASE_UNSPECIFIED` | Phase is unspecified.  
`PHASE_WEEK1` | Week 1.  
`PHASE_WEEK2` | Week 2.  
`PHASE_WEEK5` | Week 5.  
`PHASE_ANY` | Any phase.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
