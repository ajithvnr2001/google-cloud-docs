---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ScheduleOptionsV2OrBuilder
title: Interface ScheduleOptionsV2OrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:28.878773+00:00
---

# Interface ScheduleOptionsV2OrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ScheduleOptionsV2OrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ScheduleOptionsV2OrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.17  2.2.6  2.1.23  2.0.27 
    
    
    public interface ScheduleOptionsV2OrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEventDrivenSchedule()
    
    
    public abstract EventDrivenSchedule getEventDrivenSchedule()

Event driven transfer schedule options. If set, the transfer will be scheduled upon events arrial.

`.google.cloud.bigquery.datatransfer.v1.EventDrivenSchedule event_driven_schedule = 3; `

**Returns**  
---  
**Type** | **Description**  
`[EventDrivenSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.EventDrivenSchedule)` | The eventDrivenSchedule.  
  
### getEventDrivenScheduleOrBuilder()
    
    
    public abstract EventDrivenScheduleOrBuilder getEventDrivenScheduleOrBuilder()

Event driven transfer schedule options. If set, the transfer will be scheduled upon events arrial.

`.google.cloud.bigquery.datatransfer.v1.EventDrivenSchedule event_driven_schedule = 3; `

**Returns**  
---  
**Type** | **Description**  
`[EventDrivenScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.EventDrivenScheduleOrBuilder)` |   
  
### getManualSchedule()
    
    
    public abstract ManualSchedule getManualSchedule()

Manual transfer schedule. If set, the transfer run will not be auto-scheduled by the system, unless the client invokes StartManualTransferRuns. This is equivalent to disable_auto_scheduling = true.

`.google.cloud.bigquery.datatransfer.v1.ManualSchedule manual_schedule = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ManualSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ManualSchedule)` | The manualSchedule.  
  
### getManualScheduleOrBuilder()
    
    
    public abstract ManualScheduleOrBuilder getManualScheduleOrBuilder()

Manual transfer schedule. If set, the transfer run will not be auto-scheduled by the system, unless the client invokes StartManualTransferRuns. This is equivalent to disable_auto_scheduling = true.

`.google.cloud.bigquery.datatransfer.v1.ManualSchedule manual_schedule = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ManualScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ManualScheduleOrBuilder)` |   
  
### getScheduleCase()
    
    
    public abstract ScheduleOptionsV2.ScheduleCase getScheduleCase()

**Returns**  
---  
**Type** | **Description**  
`[ScheduleOptionsV2.ScheduleCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ScheduleOptionsV2.ScheduleCase)` |   
  
### getTimeBasedSchedule()
    
    
    public abstract TimeBasedSchedule getTimeBasedSchedule()

Time based transfer schedule options. This is the default schedule option.

`.google.cloud.bigquery.datatransfer.v1.TimeBasedSchedule time_based_schedule = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TimeBasedSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TimeBasedSchedule)` | The timeBasedSchedule.  
  
### getTimeBasedScheduleOrBuilder()
    
    
    public abstract TimeBasedScheduleOrBuilder getTimeBasedScheduleOrBuilder()

Time based transfer schedule options. This is the default schedule option.

`.google.cloud.bigquery.datatransfer.v1.TimeBasedSchedule time_based_schedule = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TimeBasedScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.TimeBasedScheduleOrBuilder)` |   
  
### hasEventDrivenSchedule()
    
    
    public abstract boolean hasEventDrivenSchedule()

Event driven transfer schedule options. If set, the transfer will be scheduled upon events arrial.

`.google.cloud.bigquery.datatransfer.v1.EventDrivenSchedule event_driven_schedule = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the eventDrivenSchedule field is set.  
  
### hasManualSchedule()
    
    
    public abstract boolean hasManualSchedule()

Manual transfer schedule. If set, the transfer run will not be auto-scheduled by the system, unless the client invokes StartManualTransferRuns. This is equivalent to disable_auto_scheduling = true.

`.google.cloud.bigquery.datatransfer.v1.ManualSchedule manual_schedule = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the manualSchedule field is set.  
  
### hasTimeBasedSchedule()
    
    
    public abstract boolean hasTimeBasedSchedule()

Time based transfer schedule options. This is the default schedule option.

`.google.cloud.bigquery.datatransfer.v1.TimeBasedSchedule time_based_schedule = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeBasedSchedule field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
