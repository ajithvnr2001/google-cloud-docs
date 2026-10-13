---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationSubtaskOrBuilder
title: Interface MigrationSubtaskOrBuilder (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:30.125016+00:00
---

# Interface MigrationSubtaskOrBuilder (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationSubtaskOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MigrationSubtaskOrBuilder (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public interface MigrationSubtaskOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time when the subtask was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time when the subtask was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLastUpdateTime()
    
    
    public abstract Timestamp getLastUpdateTime()

Output only. Time when the subtask was last updated.

` .google.protobuf.Timestamp last_update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastUpdateTime.  
  
### getLastUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastUpdateTimeOrBuilder()

Output only. Time when the subtask was last updated.

` .google.protobuf.Timestamp last_update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getMetrics(int index)
    
    
    public abstract TimeSeries getMetrics(int index)

Output only. The metrics for the subtask.

` repeated .google.cloud.bigquery.migration.v2.TimeSeries metrics = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TimeSeries)` |   
  
### getMetricsCount()
    
    
    public abstract int getMetricsCount()

Output only. The metrics for the subtask.

` repeated .google.cloud.bigquery.migration.v2.TimeSeries metrics = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetricsList()
    
    
    public abstract List<TimeSeries> getMetricsList()

Output only. The metrics for the subtask.

` repeated .google.cloud.bigquery.migration.v2.TimeSeries metrics = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TimeSeries)>` |   
  
### getMetricsOrBuilder(int index)
    
    
    public abstract TimeSeriesOrBuilder getMetricsOrBuilder(int index)

Output only. The metrics for the subtask.

` repeated .google.cloud.bigquery.migration.v2.TimeSeries metrics = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.TimeSeriesOrBuilder)` |   
  
### getMetricsOrBuilderList()
    
    
    public abstract List<? extends TimeSeriesOrBuilder> getMetricsOrBuilderList()

Output only. The metrics for the subtask.

` repeated .google.cloud.bigquery.migration.v2.TimeSeries metrics = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.migration.v2.TimeSeriesOrBuilder>` |   
  
### getName()
    
    
    public abstract String getName()

Output only. Immutable. The resource name for the migration subtask. The ID is server-generated.

Example: `projects/123/locations/us/workflows/345/subtasks/678`

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Immutable. The resource name for the migration subtask. The ID is server-generated.

Example: `projects/123/locations/us/workflows/345/subtasks/678`

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getProcessingError()
    
    
    public abstract ErrorInfo getProcessingError()

Output only. An explanation that may be populated when the task is in FAILED state.

`.google.rpc.ErrorInfo processing_error = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.ErrorInfo` | The processingError.  
  
### getProcessingErrorOrBuilder()
    
    
    public abstract ErrorInfoOrBuilder getProcessingErrorOrBuilder()

Output only. An explanation that may be populated when the task is in FAILED state.

`.google.rpc.ErrorInfo processing_error = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.ErrorInfoOrBuilder` |   
  
### getResourceErrorCount()
    
    
    public abstract int getResourceErrorCount()

Output only. The number or resources with errors. Note: This is not the total number of errors as each resource can have more than one error. This is used to indicate truncation by having a `resource_error_count` that is higher than the size of `resource_error_details`.

`int32 resource_error_count = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The resourceErrorCount.  
  
### getResourceErrorDetails(int index)
    
    
    public abstract ResourceErrorDetail getResourceErrorDetails(int index)

Output only. Provides details to errors and issues encountered while processing the subtask. Presence of error details does not mean that the subtask failed.

` repeated .google.cloud.bigquery.migration.v2.ResourceErrorDetail resource_error_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResourceErrorDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.ResourceErrorDetail)` |   
  
### getResourceErrorDetailsCount()
    
    
    public abstract int getResourceErrorDetailsCount()

Output only. Provides details to errors and issues encountered while processing the subtask. Presence of error details does not mean that the subtask failed.

` repeated .google.cloud.bigquery.migration.v2.ResourceErrorDetail resource_error_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourceErrorDetailsList()
    
    
    public abstract List<ResourceErrorDetail> getResourceErrorDetailsList()

Output only. Provides details to errors and issues encountered while processing the subtask. Presence of error details does not mean that the subtask failed.

` repeated .google.cloud.bigquery.migration.v2.ResourceErrorDetail resource_error_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResourceErrorDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.ResourceErrorDetail)>` |   
  
### getResourceErrorDetailsOrBuilder(int index)
    
    
    public abstract ResourceErrorDetailOrBuilder getResourceErrorDetailsOrBuilder(int index)

Output only. Provides details to errors and issues encountered while processing the subtask. Presence of error details does not mean that the subtask failed.

` repeated .google.cloud.bigquery.migration.v2.ResourceErrorDetail resource_error_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResourceErrorDetailOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.ResourceErrorDetailOrBuilder)` |   
  
### getResourceErrorDetailsOrBuilderList()
    
    
    public abstract List<? extends ResourceErrorDetailOrBuilder> getResourceErrorDetailsOrBuilderList()

Output only. Provides details to errors and issues encountered while processing the subtask. Presence of error details does not mean that the subtask failed.

` repeated .google.cloud.bigquery.migration.v2.ResourceErrorDetail resource_error_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.migration.v2.ResourceErrorDetailOrBuilder>` |   
  
### getState()
    
    
    public abstract MigrationSubtask.State getState()

Output only. The current state of the subtask.

` .google.cloud.bigquery.migration.v2.MigrationSubtask.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigrationSubtask.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2.MigrationSubtask.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state of the subtask.

` .google.cloud.bigquery.migration.v2.MigrationSubtask.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getTaskId()
    
    
    public abstract String getTaskId()

The unique ID of the task to which this subtask belongs.

`string task_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The taskId.  
  
### getTaskIdBytes()
    
    
    public abstract ByteString getTaskIdBytes()

The unique ID of the task to which this subtask belongs.

`string task_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for taskId.  
  
### getType()
    
    
    public abstract String getType()

The type of the Subtask. The migration service does not check whether this is a known type. It is up to the task creator (i.e. orchestrator or worker) to ensure it only creates subtasks for which there are compatible workers polling for Subtasks.

`string type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The type.  
  
### getTypeBytes()
    
    
    public abstract ByteString getTypeBytes()

The type of the Subtask. The migration service does not check whether this is a known type. It is up to the task creator (i.e. orchestrator or worker) to ensure it only creates subtasks for which there are compatible workers polling for Subtasks.

`string type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for type.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time when the subtask was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasLastUpdateTime()
    
    
    public abstract boolean hasLastUpdateTime()

Output only. Time when the subtask was last updated.

` .google.protobuf.Timestamp last_update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastUpdateTime field is set.  
  
### hasProcessingError()
    
    
    public abstract boolean hasProcessingError()

Output only. An explanation that may be populated when the task is in FAILED state.

`.google.rpc.ErrorInfo processing_error = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the processingError field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
