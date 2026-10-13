---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.UpcomingMaintenanceOrBuilder
title: Interface UpcomingMaintenanceOrBuilder (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:09.854268+00:00
---

# Interface UpcomingMaintenanceOrBuilder (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.UpcomingMaintenanceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpcomingMaintenanceOrBuilder (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface UpcomingMaintenanceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEndTime()
    
    
    public abstract Timestamp getEndTime()

Output only. End time of the upcoming maintenance. This is only populated for an engine, if end time is public for the engine.

`.google.protobuf.Timestamp end_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEndTimeOrBuilder()

Output only. End time of the upcoming maintenance. This is only populated for an engine, if end time is public for the engine.

`.google.protobuf.Timestamp end_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

Output only. Start time of the upcoming maintenance. Start time is always populated when an upcoming maintenance is scheduled.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

Output only. Start time of the upcoming maintenance. Start time is always populated when an upcoming maintenance is scheduled.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasEndTime()
    
    
    public abstract boolean hasEndTime()

Output only. End time of the upcoming maintenance. This is only populated for an engine, if end time is public for the engine.

`.google.protobuf.Timestamp end_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

Output only. Start time of the upcoming maintenance. Start time is always populated when an upcoming maintenance is scheduled.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
