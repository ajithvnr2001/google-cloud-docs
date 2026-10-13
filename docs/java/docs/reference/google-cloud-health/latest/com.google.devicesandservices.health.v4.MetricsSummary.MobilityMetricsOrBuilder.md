---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.MetricsSummary.MobilityMetricsOrBuilder
title: Interface MetricsSummary.MobilityMetricsOrBuilder (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:32.967412+00:00
---

# Interface MetricsSummary.MobilityMetricsOrBuilder (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.MetricsSummary.MobilityMetricsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MetricsSummary.MobilityMetricsOrBuilder (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public static interface MetricsSummary.MobilityMetricsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAvgCadenceStepsPerMinute()
    
    
    public abstract double getAvgCadenceStepsPerMinute()

Optional. Cadence is a measure of the frequency of your foot strikes. Steps / min in real time during workout.

` optional double avg_cadence_steps_per_minute = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The avgCadenceStepsPerMinute.  
  
### getAvgGroundContactTimeDuration()
    
    
    public abstract Duration getAvgGroundContactTimeDuration()

Optional. The ground contact time for a particular stride is the amount of time for which the foot was in contact with the ground on that stride

` .google.protobuf.Duration avg_ground_contact_time_duration = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The avgGroundContactTimeDuration.  
  
### getAvgGroundContactTimeDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getAvgGroundContactTimeDurationOrBuilder()

Optional. The ground contact time for a particular stride is the amount of time for which the foot was in contact with the ground on that stride

` .google.protobuf.Duration avg_ground_contact_time_duration = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getAvgStrideLengthMillimeters()
    
    
    public abstract long getAvgStrideLengthMillimeters()

Optional. Stride length is a measure of the distance covered by a single stride

` optional int64 avg_stride_length_millimeters = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The avgStrideLengthMillimeters.  
  
### getAvgVerticalOscillationMillimeters()
    
    
    public abstract long getAvgVerticalOscillationMillimeters()

Optional. Distance off the ground your center of mass moves with each stride while running

` optional int64 avg_vertical_oscillation_millimeters = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The avgVerticalOscillationMillimeters.  
  
### getAvgVerticalRatio()
    
    
    public abstract double getAvgVerticalRatio()

Optional. Vertical oscillation/stride length between [5.0, 11.0].

`optional double avg_vertical_ratio = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The avgVerticalRatio.  
  
### hasAvgCadenceStepsPerMinute()
    
    
    public abstract boolean hasAvgCadenceStepsPerMinute()

Optional. Cadence is a measure of the frequency of your foot strikes. Steps / min in real time during workout.

` optional double avg_cadence_steps_per_minute = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avgCadenceStepsPerMinute field is set.  
  
### hasAvgGroundContactTimeDuration()
    
    
    public abstract boolean hasAvgGroundContactTimeDuration()

Optional. The ground contact time for a particular stride is the amount of time for which the foot was in contact with the ground on that stride

` .google.protobuf.Duration avg_ground_contact_time_duration = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avgGroundContactTimeDuration field is set.  
  
### hasAvgStrideLengthMillimeters()
    
    
    public abstract boolean hasAvgStrideLengthMillimeters()

Optional. Stride length is a measure of the distance covered by a single stride

` optional int64 avg_stride_length_millimeters = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avgStrideLengthMillimeters field is set.  
  
### hasAvgVerticalOscillationMillimeters()
    
    
    public abstract boolean hasAvgVerticalOscillationMillimeters()

Optional. Distance off the ground your center of mass moves with each stride while running

` optional int64 avg_vertical_oscillation_millimeters = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avgVerticalOscillationMillimeters field is set.  
  
### hasAvgVerticalRatio()
    
    
    public abstract boolean hasAvgVerticalRatio()

Optional. Vertical oscillation/stride length between [5.0, 11.0].

`optional double avg_vertical_ratio = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avgVerticalRatio field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
