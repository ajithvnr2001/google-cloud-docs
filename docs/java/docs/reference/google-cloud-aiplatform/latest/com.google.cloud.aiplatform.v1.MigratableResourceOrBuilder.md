---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResourceOrBuilder
title: Interface MigratableResourceOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:29.407858+00:00
---

# Interface MigratableResourceOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResourceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MigratableResourceOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface MigratableResourceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAutomlDataset()
    
    
    public abstract MigratableResource.AutomlDataset getAutomlDataset()

Output only. Represents one Dataset in automl.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.AutomlDataset automl_dataset = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.AutomlDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.AutomlDataset)` | The automlDataset.  
  
### getAutomlDatasetOrBuilder()
    
    
    public abstract MigratableResource.AutomlDatasetOrBuilder getAutomlDatasetOrBuilder()

Output only. Represents one Dataset in automl.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.AutomlDataset automl_dataset = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.AutomlDatasetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.AutomlDatasetOrBuilder)` |   
  
### getAutomlModel()
    
    
    public abstract MigratableResource.AutomlModel getAutomlModel()

Output only. Represents one Model in automl.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.AutomlModel automl_model = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.AutomlModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.AutomlModel)` | The automlModel.  
  
### getAutomlModelOrBuilder()
    
    
    public abstract MigratableResource.AutomlModelOrBuilder getAutomlModelOrBuilder()

Output only. Represents one Model in automl.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.AutomlModel automl_model = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.AutomlModelOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.AutomlModelOrBuilder)` |   
  
### getDataLabelingDataset()
    
    
    public abstract MigratableResource.DataLabelingDataset getDataLabelingDataset()

Output only. Represents one Dataset in datalabeling.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.DataLabelingDataset data_labeling_dataset = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.DataLabelingDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.DataLabelingDataset)` | The dataLabelingDataset.  
  
### getDataLabelingDatasetOrBuilder()
    
    
    public abstract MigratableResource.DataLabelingDatasetOrBuilder getDataLabelingDatasetOrBuilder()

Output only. Represents one Dataset in datalabeling.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.DataLabelingDataset data_labeling_dataset = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.DataLabelingDatasetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.DataLabelingDatasetOrBuilder)` |   
  
### getLastMigrateTime()
    
    
    public abstract Timestamp getLastMigrateTime()

Output only. Timestamp when the last migration attempt on this MigratableResource started. Will not be set if there's no migration attempt on this MigratableResource.

` .google.protobuf.Timestamp last_migrate_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastMigrateTime.  
  
### getLastMigrateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastMigrateTimeOrBuilder()

Output only. Timestamp when the last migration attempt on this MigratableResource started. Will not be set if there's no migration attempt on this MigratableResource.

` .google.protobuf.Timestamp last_migrate_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLastUpdateTime()
    
    
    public abstract Timestamp getLastUpdateTime()

Output only. Timestamp when this MigratableResource was last updated.

` .google.protobuf.Timestamp last_update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastUpdateTime.  
  
### getLastUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastUpdateTimeOrBuilder()

Output only. Timestamp when this MigratableResource was last updated.

` .google.protobuf.Timestamp last_update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getMlEngineModelVersion()
    
    
    public abstract MigratableResource.MlEngineModelVersion getMlEngineModelVersion()

Output only. Represents one Version in ml.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.MlEngineModelVersion ml_engine_model_version = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.MlEngineModelVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.MlEngineModelVersion)` | The mlEngineModelVersion.  
  
### getMlEngineModelVersionOrBuilder()
    
    
    public abstract MigratableResource.MlEngineModelVersionOrBuilder getMlEngineModelVersionOrBuilder()

Output only. Represents one Version in ml.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.MlEngineModelVersion ml_engine_model_version = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.MlEngineModelVersionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.MlEngineModelVersionOrBuilder)` |   
  
### getResourceCase()
    
    
    public abstract MigratableResource.ResourceCase getResourceCase()

**Returns**  
---  
**Type** | **Description**  
`[MigratableResource.ResourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MigratableResource.ResourceCase)` |   
  
### hasAutomlDataset()
    
    
    public abstract boolean hasAutomlDataset()

Output only. Represents one Dataset in automl.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.AutomlDataset automl_dataset = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the automlDataset field is set.  
  
### hasAutomlModel()
    
    
    public abstract boolean hasAutomlModel()

Output only. Represents one Model in automl.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.AutomlModel automl_model = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the automlModel field is set.  
  
### hasDataLabelingDataset()
    
    
    public abstract boolean hasDataLabelingDataset()

Output only. Represents one Dataset in datalabeling.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.DataLabelingDataset data_labeling_dataset = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataLabelingDataset field is set.  
  
### hasLastMigrateTime()
    
    
    public abstract boolean hasLastMigrateTime()

Output only. Timestamp when the last migration attempt on this MigratableResource started. Will not be set if there's no migration attempt on this MigratableResource.

` .google.protobuf.Timestamp last_migrate_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastMigrateTime field is set.  
  
### hasLastUpdateTime()
    
    
    public abstract boolean hasLastUpdateTime()

Output only. Timestamp when this MigratableResource was last updated.

` .google.protobuf.Timestamp last_update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastUpdateTime field is set.  
  
### hasMlEngineModelVersion()
    
    
    public abstract boolean hasMlEngineModelVersion()

Output only. Represents one Version in ml.googleapis.com.

` .google.cloud.aiplatform.v1.MigratableResource.MlEngineModelVersion ml_engine_model_version = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mlEngineModelVersion field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
