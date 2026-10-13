---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInputOrBuilder
title: Interface ModelMonitoringInputOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:30.084413+00:00
---

# Interface ModelMonitoringInputOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInputOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ModelMonitoringInputOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface ModelMonitoringInputOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBatchPredictionOutput()
    
    
    public abstract ModelMonitoringInput.BatchPredictionOutput getBatchPredictionOutput()

Vertex AI Batch prediction Job.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.BatchPredictionOutput batch_prediction_output = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.BatchPredictionOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.BatchPredictionOutput)` | The batchPredictionOutput.  
  
### getBatchPredictionOutputOrBuilder()
    
    
    public abstract ModelMonitoringInput.BatchPredictionOutputOrBuilder getBatchPredictionOutputOrBuilder()

Vertex AI Batch prediction Job.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.BatchPredictionOutput batch_prediction_output = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.BatchPredictionOutputOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.BatchPredictionOutputOrBuilder)` |   
  
### getColumnizedDataset()
    
    
    public abstract ModelMonitoringInput.ModelMonitoringDataset getColumnizedDataset()

Columnized dataset.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDataset columnized_dataset = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.ModelMonitoringDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDataset)` | The columnizedDataset.  
  
### getColumnizedDatasetOrBuilder()
    
    
    public abstract ModelMonitoringInput.ModelMonitoringDatasetOrBuilder getColumnizedDatasetOrBuilder()

Columnized dataset.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDataset columnized_dataset = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.ModelMonitoringDatasetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDatasetOrBuilder)` |   
  
### getDatasetCase()
    
    
    public abstract ModelMonitoringInput.DatasetCase getDatasetCase()

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.DatasetCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.DatasetCase)` |   
  
### getTimeInterval()
    
    
    public abstract Interval getTimeInterval()

The time interval (pair of start_time and end_time) for which results should be returned.

`.google.type.Interval time_interval = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Interval` | The timeInterval.  
  
### getTimeIntervalOrBuilder()
    
    
    public abstract IntervalOrBuilder getTimeIntervalOrBuilder()

The time interval (pair of start_time and end_time) for which results should be returned.

`.google.type.Interval time_interval = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.IntervalOrBuilder` |   
  
### getTimeOffset()
    
    
    public abstract ModelMonitoringInput.TimeOffset getTimeOffset()

The time offset setting for which results should be returned.

`.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.TimeOffset time_offset = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.TimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.TimeOffset)` | The timeOffset.  
  
### getTimeOffsetOrBuilder()
    
    
    public abstract ModelMonitoringInput.TimeOffsetOrBuilder getTimeOffsetOrBuilder()

The time offset setting for which results should be returned.

`.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.TimeOffset time_offset = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.TimeOffsetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.TimeOffsetOrBuilder)` |   
  
### getTimeSpecCase()
    
    
    public abstract ModelMonitoringInput.TimeSpecCase getTimeSpecCase()

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.TimeSpecCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.TimeSpecCase)` |   
  
### getVertexEndpointLogs()
    
    
    public abstract ModelMonitoringInput.VertexEndpointLogs getVertexEndpointLogs()

Vertex AI Endpoint request & response logging.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.VertexEndpointLogs vertex_endpoint_logs = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.VertexEndpointLogs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.VertexEndpointLogs)` | The vertexEndpointLogs.  
  
### getVertexEndpointLogsOrBuilder()
    
    
    public abstract ModelMonitoringInput.VertexEndpointLogsOrBuilder getVertexEndpointLogsOrBuilder()

Vertex AI Endpoint request & response logging.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.VertexEndpointLogs vertex_endpoint_logs = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringInput.VertexEndpointLogsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.VertexEndpointLogsOrBuilder)` |   
  
### hasBatchPredictionOutput()
    
    
    public abstract boolean hasBatchPredictionOutput()

Vertex AI Batch prediction Job.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.BatchPredictionOutput batch_prediction_output = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the batchPredictionOutput field is set.  
  
### hasColumnizedDataset()
    
    
    public abstract boolean hasColumnizedDataset()

Columnized dataset.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDataset columnized_dataset = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the columnizedDataset field is set.  
  
### hasTimeInterval()
    
    
    public abstract boolean hasTimeInterval()

The time interval (pair of start_time and end_time) for which results should be returned.

`.google.type.Interval time_interval = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeInterval field is set.  
  
### hasTimeOffset()
    
    
    public abstract boolean hasTimeOffset()

The time offset setting for which results should be returned.

`.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.TimeOffset time_offset = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeOffset field is set.  
  
### hasVertexEndpointLogs()
    
    
    public abstract boolean hasVertexEndpointLogs()

Vertex AI Endpoint request & response logging.

` .google.cloud.aiplatform.v1beta1.ModelMonitoringInput.VertexEndpointLogs vertex_endpoint_logs = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vertexEndpointLogs field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
