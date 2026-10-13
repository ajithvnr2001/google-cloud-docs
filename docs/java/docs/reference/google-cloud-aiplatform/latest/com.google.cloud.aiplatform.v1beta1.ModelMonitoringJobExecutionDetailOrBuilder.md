---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetailOrBuilder
title: Interface ModelMonitoringJobExecutionDetailOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:46.193521+00:00
---

# Interface ModelMonitoringJobExecutionDetailOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetailOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ModelMonitoringJobExecutionDetailOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface ModelMonitoringJobExecutionDetailOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsObjectiveStatus(String key)
    
    
    public abstract boolean containsObjectiveStatus(String key)

Status of data processing for each monitoring objective. Key is the objective.

`map<string, .google.rpc.Status> objective_status = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBaselineDatasets(int index)
    
    
    public abstract ModelMonitoringJobExecutionDetail.ProcessedDataset getBaselineDatasets(int index)

Processed baseline datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset baseline_datasets = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringJobExecutionDetail.ProcessedDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset)` |   
  
### getBaselineDatasetsCount()
    
    
    public abstract int getBaselineDatasetsCount()

Processed baseline datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset baseline_datasets = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBaselineDatasetsList()
    
    
    public abstract List<ModelMonitoringJobExecutionDetail.ProcessedDataset> getBaselineDatasetsList()

Processed baseline datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset baseline_datasets = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProcessedDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset)>` |   
  
### getBaselineDatasetsOrBuilder(int index)
    
    
    public abstract ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder getBaselineDatasetsOrBuilder(int index)

Processed baseline datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset baseline_datasets = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder)` |   
  
### getBaselineDatasetsOrBuilderList()
    
    
    public abstract List<? extends ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder> getBaselineDatasetsOrBuilderList()

Processed baseline datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset baseline_datasets = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder>` |   
  
### getError()
    
    
    public abstract Status getError()

Additional job error status.

`.google.rpc.Status error = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

Additional job error status.

`.google.rpc.Status error = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getObjectiveStatus() (deprecated)
    
    
    public abstract Map<String,Status> getObjectiveStatus()

Use [#getObjectiveStatusMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetailOrBuilder#com_google_cloud_aiplatform_v1beta1_ModelMonitoringJobExecutionDetailOrBuilder_getObjectiveStatusMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),com.google.rpc.Status>` |   
  
### getObjectiveStatusCount()
    
    
    public abstract int getObjectiveStatusCount()

Status of data processing for each monitoring objective. Key is the objective.

`map<string, .google.rpc.Status> objective_status = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getObjectiveStatusMap()
    
    
    public abstract Map<String,Status> getObjectiveStatusMap()

Status of data processing for each monitoring objective. Key is the objective.

`map<string, .google.rpc.Status> objective_status = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),com.google.rpc.Status>` |   
  
### getObjectiveStatusOrDefault(String key, Status defaultValue)
    
    
    public abstract Status getObjectiveStatusOrDefault(String key, Status defaultValue)

Status of data processing for each monitoring objective. Key is the objective.

`map<string, .google.rpc.Status> objective_status = 3;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `com.google.rpc.Status`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` |   
  
### getObjectiveStatusOrThrow(String key)
    
    
    public abstract Status getObjectiveStatusOrThrow(String key)

Status of data processing for each monitoring objective. Key is the objective.

`map<string, .google.rpc.Status> objective_status = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` |   
  
### getTargetDatasets(int index)
    
    
    public abstract ModelMonitoringJobExecutionDetail.ProcessedDataset getTargetDatasets(int index)

Processed target datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset target_datasets = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringJobExecutionDetail.ProcessedDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset)` |   
  
### getTargetDatasetsCount()
    
    
    public abstract int getTargetDatasetsCount()

Processed target datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset target_datasets = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTargetDatasetsList()
    
    
    public abstract List<ModelMonitoringJobExecutionDetail.ProcessedDataset> getTargetDatasetsList()

Processed target datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset target_datasets = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProcessedDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset)>` |   
  
### getTargetDatasetsOrBuilder(int index)
    
    
    public abstract ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder getTargetDatasetsOrBuilder(int index)

Processed target datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset target_datasets = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder)` |   
  
### getTargetDatasetsOrBuilderList()
    
    
    public abstract List<? extends ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder> getTargetDatasetsOrBuilderList()

Processed target datasets.

` repeated .google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset target_datasets = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDatasetOrBuilder>` |   
  
### hasError()
    
    
    public abstract boolean hasError()

Additional job error status.

`.google.rpc.Status error = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
