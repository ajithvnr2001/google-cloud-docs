---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExerciseOrBuilder
title: Interface ExerciseOrBuilder (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:53.536624+00:00
---

# Interface ExerciseOrBuilder (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExerciseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExerciseOrBuilder (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public interface ExerciseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActiveDuration()
    
    
    public abstract Duration getActiveDuration()

Optional. Duration excluding pauses.

`.google.protobuf.Duration active_duration = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The activeDuration.  
  
### getActiveDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getActiveDurationOrBuilder()

Optional. Duration excluding pauses.

`.google.protobuf.Duration active_duration = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Represents the timestamp of the creation of the exercise.

`.google.protobuf.Timestamp create_time = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Represents the timestamp of the creation of the exercise.

`.google.protobuf.Timestamp create_time = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. The localized, human-readable name of the exercise. For all exercise types other than `OTHER`, the system ignores client input and overrides this field with a generated name based on `exercise_type` (e.g., "Walking" for `WALKING`). If `exercise_type` is `OTHER`, this field can contain the user's custom, free-form display name.

`string display_name = 12 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. The localized, human-readable name of the exercise. For all exercise types other than `OTHER`, the system ignores client input and overrides this field with a generated name based on `exercise_type` (e.g., "Walking" for `WALKING`). If `exercise_type` is `OTHER`, this field can contain the user's custom, free-form display name.

`string display_name = 12 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getExerciseEvents(int index)
    
    
    public abstract Exercise.ExerciseEvent getExerciseEvents(int index)

Optional. Exercise events that happen during an exercise, such as pause & restarts.

` repeated .google.devicesandservices.health.v4.Exercise.ExerciseEvent exercise_events = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exercise.ExerciseEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.ExerciseEvent)` |   
  
### getExerciseEventsCount()
    
    
    public abstract int getExerciseEventsCount()

Optional. Exercise events that happen during an exercise, such as pause & restarts.

` repeated .google.devicesandservices.health.v4.Exercise.ExerciseEvent exercise_events = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExerciseEventsList()
    
    
    public abstract List<Exercise.ExerciseEvent> getExerciseEventsList()

Optional. Exercise events that happen during an exercise, such as pause & restarts.

` repeated .google.devicesandservices.health.v4.Exercise.ExerciseEvent exercise_events = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ExerciseEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.ExerciseEvent)>` |   
  
### getExerciseEventsOrBuilder(int index)
    
    
    public abstract Exercise.ExerciseEventOrBuilder getExerciseEventsOrBuilder(int index)

Optional. Exercise events that happen during an exercise, such as pause & restarts.

` repeated .google.devicesandservices.health.v4.Exercise.ExerciseEvent exercise_events = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exercise.ExerciseEventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.ExerciseEventOrBuilder)` |   
  
### getExerciseEventsOrBuilderList()
    
    
    public abstract List<? extends Exercise.ExerciseEventOrBuilder> getExerciseEventsOrBuilderList()

Optional. Exercise events that happen during an exercise, such as pause & restarts.

` repeated .google.devicesandservices.health.v4.Exercise.ExerciseEvent exercise_events = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.devicesandservices.health.v4.Exercise.ExerciseEventOrBuilder>` |   
  
### getExerciseMetadata()
    
    
    public abstract Exercise.ExerciseMetadata getExerciseMetadata()

Optional. Additional exercise metadata.

` .google.devicesandservices.health.v4.Exercise.ExerciseMetadata exercise_metadata = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Exercise.ExerciseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.ExerciseMetadata)` | The exerciseMetadata.  
  
### getExerciseMetadataOrBuilder()
    
    
    public abstract Exercise.ExerciseMetadataOrBuilder getExerciseMetadataOrBuilder()

Optional. Additional exercise metadata.

` .google.devicesandservices.health.v4.Exercise.ExerciseMetadata exercise_metadata = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Exercise.ExerciseMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.ExerciseMetadataOrBuilder)` |   
  
### getExerciseType()
    
    
    public abstract Exercise.ExerciseType getExerciseType()

Required. The type of activity performed during an exercise.

` .google.devicesandservices.health.v4.Exercise.ExerciseType exercise_type = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Exercise.ExerciseType](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.ExerciseType)` | The exerciseType.  
  
### getExerciseTypeValue()
    
    
    public abstract int getExerciseTypeValue()

Required. The type of activity performed during an exercise.

` .google.devicesandservices.health.v4.Exercise.ExerciseType exercise_type = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for exerciseType.  
  
### getInterval()
    
    
    public abstract SessionTimeInterval getInterval()

Required. Observed exercise interval

` .google.devicesandservices.health.v4.SessionTimeInterval interval = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SessionTimeInterval](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SessionTimeInterval)` | The interval.  
  
### getIntervalOrBuilder()
    
    
    public abstract SessionTimeIntervalOrBuilder getIntervalOrBuilder()

Required. Observed exercise interval

` .google.devicesandservices.health.v4.SessionTimeInterval interval = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SessionTimeIntervalOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SessionTimeIntervalOrBuilder)` |   
  
### getMetricsSummary()
    
    
    public abstract MetricsSummary getMetricsSummary()

Required. Summary metrics for this exercise ( )

` .google.devicesandservices.health.v4.MetricsSummary metrics_summary = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MetricsSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.MetricsSummary)` | The metricsSummary.  
  
### getMetricsSummaryOrBuilder()
    
    
    public abstract MetricsSummaryOrBuilder getMetricsSummaryOrBuilder()

Required. Summary metrics for this exercise ( )

` .google.devicesandservices.health.v4.MetricsSummary metrics_summary = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MetricsSummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.MetricsSummaryOrBuilder)` |   
  
### getNotes()
    
    
    public abstract String getNotes()

Optional. Standard free-form notes captured at manual logging.

`string notes = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The notes.  
  
### getNotesBytes()
    
    
    public abstract ByteString getNotesBytes()

Optional. Standard free-form notes captured at manual logging.

`string notes = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for notes.  
  
### getSplitSummaries(int index)
    
    
    public abstract Exercise.SplitSummary getSplitSummaries(int index)

Optional. Laps or splits recorded within an exercise. Laps could be split based on distance or other criteria (duration, etc.) Laps should not be overlapping with each other.

` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary split_summaries = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exercise.SplitSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.SplitSummary)` |   
  
### getSplitSummariesCount()
    
    
    public abstract int getSplitSummariesCount()

Optional. Laps or splits recorded within an exercise. Laps could be split based on distance or other criteria (duration, etc.) Laps should not be overlapping with each other.

` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary split_summaries = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSplitSummariesList()
    
    
    public abstract List<Exercise.SplitSummary> getSplitSummariesList()

Optional. Laps or splits recorded within an exercise. Laps could be split based on distance or other criteria (duration, etc.) Laps should not be overlapping with each other.

` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary split_summaries = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SplitSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.SplitSummary)>` |   
  
### getSplitSummariesOrBuilder(int index)
    
    
    public abstract Exercise.SplitSummaryOrBuilder getSplitSummariesOrBuilder(int index)

Optional. Laps or splits recorded within an exercise. Laps could be split based on distance or other criteria (duration, etc.) Laps should not be overlapping with each other.

` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary split_summaries = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exercise.SplitSummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.SplitSummaryOrBuilder)` |   
  
### getSplitSummariesOrBuilderList()
    
    
    public abstract List<? extends Exercise.SplitSummaryOrBuilder> getSplitSummariesOrBuilderList()

Optional. Laps or splits recorded within an exercise. Laps could be split based on distance or other criteria (duration, etc.) Laps should not be overlapping with each other.

` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary split_summaries = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.devicesandservices.health.v4.Exercise.SplitSummaryOrBuilder>` |   
  
### getSplits(int index)
    
    
    public abstract Exercise.SplitSummary getSplits(int index)

Optional. The default split is 1 km or 1 mile.

  * if the movement distance is less than the default, then there are no splits
  * if the movement distance is greater than or equal to the default, then we have splits



` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary splits = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exercise.SplitSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.SplitSummary)` |   
  
### getSplitsCount()
    
    
    public abstract int getSplitsCount()

Optional. The default split is 1 km or 1 mile.

  * if the movement distance is less than the default, then there are no splits
  * if the movement distance is greater than or equal to the default, then we have splits



` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary splits = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSplitsList()
    
    
    public abstract List<Exercise.SplitSummary> getSplitsList()

Optional. The default split is 1 km or 1 mile.

  * if the movement distance is less than the default, then there are no splits
  * if the movement distance is greater than or equal to the default, then we have splits



` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary splits = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SplitSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.SplitSummary)>` |   
  
### getSplitsOrBuilder(int index)
    
    
    public abstract Exercise.SplitSummaryOrBuilder getSplitsOrBuilder(int index)

Optional. The default split is 1 km or 1 mile.

  * if the movement distance is less than the default, then there are no splits
  * if the movement distance is greater than or equal to the default, then we have splits



` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary splits = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exercise.SplitSummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Exercise.SplitSummaryOrBuilder)` |   
  
### getSplitsOrBuilderList()
    
    
    public abstract List<? extends Exercise.SplitSummaryOrBuilder> getSplitsOrBuilderList()

Optional. The default split is 1 km or 1 mile.

  * if the movement distance is less than the default, then there are no splits
  * if the movement distance is greater than or equal to the default, then we have splits



` repeated .google.devicesandservices.health.v4.Exercise.SplitSummary splits = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.devicesandservices.health.v4.Exercise.SplitSummaryOrBuilder>` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. This is the timestamp of the last update to the exercise.

`.google.protobuf.Timestamp update_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. This is the timestamp of the last update to the exercise.

`.google.protobuf.Timestamp update_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasActiveDuration()
    
    
    public abstract boolean hasActiveDuration()

Optional. Duration excluding pauses.

`.google.protobuf.Duration active_duration = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activeDuration field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Represents the timestamp of the creation of the exercise.

`.google.protobuf.Timestamp create_time = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasExerciseMetadata()
    
    
    public abstract boolean hasExerciseMetadata()

Optional. Additional exercise metadata.

` .google.devicesandservices.health.v4.Exercise.ExerciseMetadata exercise_metadata = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the exerciseMetadata field is set.  
  
### hasInterval()
    
    
    public abstract boolean hasInterval()

Required. Observed exercise interval

` .google.devicesandservices.health.v4.SessionTimeInterval interval = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the interval field is set.  
  
### hasMetricsSummary()
    
    
    public abstract boolean hasMetricsSummary()

Required. Summary metrics for this exercise ( )

` .google.devicesandservices.health.v4.MetricsSummary metrics_summary = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metricsSummary field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. This is the timestamp of the last update to the exercise.

`.google.protobuf.Timestamp update_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
