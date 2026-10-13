---
url: https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.WeeklyMaintenanceWindow
title: Google Cloud Memorystore V1beta Client - Class WeeklyMaintenanceWindow (0.13.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:41.685400+00:00
---

# Google Cloud Memorystore V1beta Client - Class WeeklyMaintenanceWindow (0.13.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.WeeklyMaintenanceWindow

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Memorystore V1beta Client - Class WeeklyMaintenanceWindow (0.13.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.3 (latest)  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Memorystore V1beta Client class WeeklyMaintenanceWindow.

Time window specified for weekly operations.

Generated from protobuf message `google.cloud.memorystore.v1beta.WeeklyMaintenanceWindow`

## Namespace

Google \ Cloud \ Memorystore \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ day` |  `int`   
Optional. Allows to define schedule that runs specified day of the week.  
`↳ start_time` |  `[Google\Type\TimeOfDay](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.TimeOfDay.html)`   
Optional. Start time of the window in UTC.  
  
### getDay

Optional. Allows to define schedule that runs specified day of the week.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [DayOfWeek](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.DayOfWeek.html).  
  
### setDay

Optional. Allows to define schedule that runs specified day of the week.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [DayOfWeek](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.DayOfWeek.html).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartTime

Optional. Start time of the window in UTC.

**Returns**  
---  
**Type** | **Description**  
`[Google\Type\TimeOfDay](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.TimeOfDay.html)|null` |   
  
### hasStartTime

### clearStartTime

### setStartTime

Optional. Start time of the window in UTC.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Type\TimeOfDay](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.TimeOfDay.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
