---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle/
title: Lifecycle \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:44.627897+00:00
---

# Lifecycle  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * State
  * Date
    * JSON representation



Catalog resource lifecycle: maturity state plus key lifecycle dates.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle#State)),
      "removalDate": {
        object ([Date](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle#Date))
      }
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle#State)`)` Output only. Specifies the current maturity state of the resource.  
`removalDate` |  `object (`[Date](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle#Date)`)` Output only. Specifies the date the resource is scheduled to be removed from the catalog. Only set when `state == DEPRECATED`.  
  
## State

Maturity state of a resource in the catalog.

New values may be added in the future.

Enums  
---  
`STATE_UNSPECIFIED` | State not specified.  
`PREVIEW` | Early access. This resource may have reduced stability and availability.  
`ACTIVE` | Generally available.  
`DEPRECATED` | Still usable, but scheduled for removal.  
  
## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * `google.type.TimeOfDay`
  * `google.type.DateTime`
  * `[google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
