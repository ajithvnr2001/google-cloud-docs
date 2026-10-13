---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/Shared.Types/TimeOfDay/
title: TimeOfDay \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:12.669899+00:00
---

# TimeOfDay  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/Shared.Types/TimeOfDay/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)
  * [ Reference ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/apis)



Send feedback 

#  TimeOfDay Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `google.type.Date` and `google.protobuf.Timestamp`.

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of hour of day. Must be from 0 to 59.  
`seconds` |  `integer` Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
