---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CustomTuningModelOrBuilder
title: Interface CustomTuningModelOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:07.660574+00:00
---

# Interface CustomTuningModelOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CustomTuningModelOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CustomTuningModelOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CustomTuningModelOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsMetrics(String key)
    
    
    public abstract boolean containsMetrics(String key)

The metrics of the trained model.

`map<string, double> metrics = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCreateTime() (deprecated)
    
    
    public abstract Timestamp getCreateTime()

**Deprecated.** _google.cloud.discoveryengine.v1.CustomTuningModel.create_time is deprecated. See google/cloud/discoveryengine/v1/custom_tuning_model.proto;l=89_

Deprecated: Timestamp the Model was created at.

`.google.protobuf.Timestamp create_time = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder() (deprecated)
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Deprecated: Timestamp the Model was created at.

`.google.protobuf.Timestamp create_time = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

The display name of the model.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

The display name of the model.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getErrorMessage()
    
    
    public abstract String getErrorMessage()

Currently this is only populated if the model state is `INPUT_VALIDATION_FAILED`.

`string error_message = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The errorMessage.  
  
### getErrorMessageBytes()
    
    
    public abstract ByteString getErrorMessageBytes()

Currently this is only populated if the model state is `INPUT_VALIDATION_FAILED`.

`string error_message = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for errorMessage.  
  
### getMetrics() (deprecated)
    
    
    public abstract Map<String,Double> getMetrics()

Use [#getMetricsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CustomTuningModelOrBuilder#com_google_cloud_discoveryengine_v1_CustomTuningModelOrBuilder_getMetricsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)>` |   
  
### getMetricsCount()
    
    
    public abstract int getMetricsCount()

The metrics of the trained model.

`map<string, double> metrics = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetricsMap()
    
    
    public abstract Map<String,Double> getMetricsMap()

The metrics of the trained model.

`map<string, double> metrics = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)>` |   
  
### getMetricsOrDefault(String key, double defaultValue)
    
    
    public abstract double getMetricsOrDefault(String key, double defaultValue)

The metrics of the trained model.

`map<string, double> metrics = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetricsOrThrow(String key)
    
    
    public abstract double getMetricsOrThrow(String key)

The metrics of the trained model.

`map<string, double> metrics = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getModelState()
    
    
    public abstract CustomTuningModel.ModelState getModelState()

The state that the model is in (e.g.`TRAINING` or `TRAINING_FAILED`).

`.google.cloud.discoveryengine.v1.CustomTuningModel.ModelState model_state = 4;`

**Returns**  
---  
**Type** | **Description**  
`[CustomTuningModel.ModelState](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CustomTuningModel.ModelState)` | The modelState.  
  
### getModelStateValue()
    
    
    public abstract int getModelStateValue()

The state that the model is in (e.g.`TRAINING` or `TRAINING_FAILED`).

`.google.cloud.discoveryengine.v1.CustomTuningModel.ModelState model_state = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for modelState.  
  
### getModelVersion()
    
    
    public abstract long getModelVersion()

The version of the model.

`int64 model_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The modelVersion.  
  
### getName()
    
    
    public abstract String getName()

Required. The fully qualified resource name of the model.

Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/customTuningModels/{custom_tuning_model}`.

Model must be an alpha-numerical string with limit of 40 characters.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The fully qualified resource name of the model.

Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/customTuningModels/{custom_tuning_model}`.

Model must be an alpha-numerical string with limit of 40 characters.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getTrainingStartTime()
    
    
    public abstract Timestamp getTrainingStartTime()

Timestamp the model training was initiated.

`.google.protobuf.Timestamp training_start_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The trainingStartTime.  
  
### getTrainingStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getTrainingStartTimeOrBuilder()

Timestamp the model training was initiated.

`.google.protobuf.Timestamp training_start_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime() (deprecated)
    
    
    public abstract boolean hasCreateTime()

**Deprecated.** _google.cloud.discoveryengine.v1.CustomTuningModel.create_time is deprecated. See google/cloud/discoveryengine/v1/custom_tuning_model.proto;l=89_

Deprecated: Timestamp the Model was created at.

`.google.protobuf.Timestamp create_time = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasTrainingStartTime()
    
    
    public abstract boolean hasTrainingStartTime()

Timestamp the model training was initiated.

`.google.protobuf.Timestamp training_start_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trainingStartTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
