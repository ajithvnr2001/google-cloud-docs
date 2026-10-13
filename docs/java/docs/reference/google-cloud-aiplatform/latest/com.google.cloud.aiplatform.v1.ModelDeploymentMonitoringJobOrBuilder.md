---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobOrBuilder
title: Interface ModelDeploymentMonitoringJobOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:34.931278+00:00
---

# Interface ModelDeploymentMonitoringJobOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ModelDeploymentMonitoringJobOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface ModelDeploymentMonitoringJobOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 11;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnalysisInstanceSchemaUri()
    
    
    public abstract String getAnalysisInstanceSchemaUri()

YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze.

If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format(data type) as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string.

`string analysis_instance_schema_uri = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The analysisInstanceSchemaUri.  
  
### getAnalysisInstanceSchemaUriBytes()
    
    
    public abstract ByteString getAnalysisInstanceSchemaUriBytes()

YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze.

If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format(data type) as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string.

`string analysis_instance_schema_uri = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for analysisInstanceSchemaUri.  
  
### getBigqueryTables(int index)
    
    
    public abstract ModelDeploymentMonitoringBigQueryTable getBigqueryTables(int index)

Output only. The created bigquery tables for the job under customer project. Customer could do their own query & analysis. There could be 4 log tables in maximum:

  1. Training data logging predict request/response
  2. Serving data logging predict request/response



` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTable bigquery_tables = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringBigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTable)` |   
  
### getBigqueryTablesCount()
    
    
    public abstract int getBigqueryTablesCount()

Output only. The created bigquery tables for the job under customer project. Customer could do their own query & analysis. There could be 4 log tables in maximum:

  1. Training data logging predict request/response
  2. Serving data logging predict request/response



` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTable bigquery_tables = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBigqueryTablesList()
    
    
    public abstract List<ModelDeploymentMonitoringBigQueryTable> getBigqueryTablesList()

Output only. The created bigquery tables for the job under customer project. Customer could do their own query & analysis. There could be 4 log tables in maximum:

  1. Training data logging predict request/response
  2. Serving data logging predict request/response



` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTable bigquery_tables = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ModelDeploymentMonitoringBigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTable)>` |   
  
### getBigqueryTablesOrBuilder(int index)
    
    
    public abstract ModelDeploymentMonitoringBigQueryTableOrBuilder getBigqueryTablesOrBuilder(int index)

Output only. The created bigquery tables for the job under customer project. Customer could do their own query & analysis. There could be 4 log tables in maximum:

  1. Training data logging predict request/response
  2. Serving data logging predict request/response



` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTable bigquery_tables = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringBigQueryTableOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTableOrBuilder)` |   
  
### getBigqueryTablesOrBuilderList()
    
    
    public abstract List<? extends ModelDeploymentMonitoringBigQueryTableOrBuilder> getBigqueryTablesOrBuilderList()

Output only. The created bigquery tables for the job under customer project. Customer could do their own query & analysis. There could be 4 log tables in maximum:

  1. Training data logging predict request/response
  2. Serving data logging predict request/response



` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTable bigquery_tables = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringBigQueryTableOrBuilder>` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Timestamp when this ModelDeploymentMonitoringJob was created.

`.google.protobuf.Timestamp create_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Timestamp when this ModelDeploymentMonitoringJob was created.

`.google.protobuf.Timestamp create_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnableMonitoringPipelineLogs()
    
    
    public abstract boolean getEnableMonitoringPipelineLogs()

If true, the scheduled monitoring pipeline logs are sent to Google Cloud Logging, including pipeline status and anomalies detected. Please note the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging#pricing).

`bool enable_monitoring_pipeline_logs = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableMonitoringPipelineLogs.  
  
### getEncryptionSpec()
    
    
    public abstract EncryptionSpec getEncryptionSpec()

Customer-managed encryption key spec for a ModelDeploymentMonitoringJob. If set, this ModelDeploymentMonitoringJob and all sub-resources of this ModelDeploymentMonitoringJob will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 21;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec)` | The encryptionSpec.  
  
### getEncryptionSpecOrBuilder()
    
    
    public abstract EncryptionSpecOrBuilder getEncryptionSpecOrBuilder()

Customer-managed encryption key spec for a ModelDeploymentMonitoringJob. If set, this ModelDeploymentMonitoringJob and all sub-resources of this ModelDeploymentMonitoringJob will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 21;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpecOrBuilder)` |   
  
### getEndpoint()
    
    
    public abstract String getEndpoint()

Required. Endpoint resource name. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

` string endpoint = 3 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endpoint.  
  
### getEndpointBytes()
    
    
    public abstract ByteString getEndpointBytes()

Required. Endpoint resource name. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

` string endpoint = 3 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endpoint.  
  
### getError()
    
    
    public abstract Status getError()

Output only. Only populated when the job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.

`.google.rpc.Status error = 23 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

Output only. Only populated when the job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.

`.google.rpc.Status error = 23 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobOrBuilder#com_google_cloud_aiplatform_v1_ModelDeploymentMonitoringJobOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 11;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 11;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLatestMonitoringPipelineMetadata()
    
    
    public abstract ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadata getLatestMonitoringPipelineMetadata()

Output only. Latest triggered monitoring pipeline metadata.

` .google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadata latest_monitoring_pipeline_metadata = 25 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadata)` | The latestMonitoringPipelineMetadata.  
  
### getLatestMonitoringPipelineMetadataOrBuilder()
    
    
    public abstract ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadataOrBuilder getLatestMonitoringPipelineMetadataOrBuilder()

Output only. Latest triggered monitoring pipeline metadata.

` .google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadata latest_monitoring_pipeline_metadata = 25 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadataOrBuilder)` |   
  
### getLogTtl()
    
    
    public abstract Duration getLogTtl()

The TTL of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl = 1 day.

`.google.protobuf.Duration log_ttl = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The logTtl.  
  
### getLogTtlOrBuilder()
    
    
    public abstract DurationOrBuilder getLogTtlOrBuilder()

The TTL of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl = 1 day.

`.google.protobuf.Duration log_ttl = 17;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getLoggingSamplingStrategy()
    
    
    public abstract SamplingStrategy getLoggingSamplingStrategy()

Required. Sample Strategy for logging.

` .google.cloud.aiplatform.v1.SamplingStrategy logging_sampling_strategy = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SamplingStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SamplingStrategy)` | The loggingSamplingStrategy.  
  
### getLoggingSamplingStrategyOrBuilder()
    
    
    public abstract SamplingStrategyOrBuilder getLoggingSamplingStrategyOrBuilder()

Required. Sample Strategy for logging.

` .google.cloud.aiplatform.v1.SamplingStrategy logging_sampling_strategy = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SamplingStrategyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SamplingStrategyOrBuilder)` |   
  
### getModelDeploymentMonitoringObjectiveConfigs(int index)
    
    
    public abstract ModelDeploymentMonitoringObjectiveConfig getModelDeploymentMonitoringObjectiveConfigs(int index)

Required. The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately.

` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfig model_deployment_monitoring_objective_configs = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringObjectiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfig)` |   
  
### getModelDeploymentMonitoringObjectiveConfigsCount()
    
    
    public abstract int getModelDeploymentMonitoringObjectiveConfigsCount()

Required. The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately.

` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfig model_deployment_monitoring_objective_configs = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getModelDeploymentMonitoringObjectiveConfigsList()
    
    
    public abstract List<ModelDeploymentMonitoringObjectiveConfig> getModelDeploymentMonitoringObjectiveConfigsList()

Required. The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately.

` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfig model_deployment_monitoring_objective_configs = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ModelDeploymentMonitoringObjectiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfig)>` |   
  
### getModelDeploymentMonitoringObjectiveConfigsOrBuilder(int index)
    
    
    public abstract ModelDeploymentMonitoringObjectiveConfigOrBuilder getModelDeploymentMonitoringObjectiveConfigsOrBuilder(int index)

Required. The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately.

` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfig model_deployment_monitoring_objective_configs = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringObjectiveConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfigOrBuilder)` |   
  
### getModelDeploymentMonitoringObjectiveConfigsOrBuilderList()
    
    
    public abstract List<? extends ModelDeploymentMonitoringObjectiveConfigOrBuilder> getModelDeploymentMonitoringObjectiveConfigsOrBuilderList()

Required. The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately.

` repeated .google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfig model_deployment_monitoring_objective_configs = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveConfigOrBuilder>` |   
  
### getModelDeploymentMonitoringScheduleConfig()
    
    
    public abstract ModelDeploymentMonitoringScheduleConfig getModelDeploymentMonitoringScheduleConfig()

Required. Schedule config for running the monitoring job.

` .google.cloud.aiplatform.v1.ModelDeploymentMonitoringScheduleConfig model_deployment_monitoring_schedule_config = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringScheduleConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringScheduleConfig)` | The modelDeploymentMonitoringScheduleConfig.  
  
### getModelDeploymentMonitoringScheduleConfigOrBuilder()
    
    
    public abstract ModelDeploymentMonitoringScheduleConfigOrBuilder getModelDeploymentMonitoringScheduleConfigOrBuilder()

Required. Schedule config for running the monitoring job.

` .google.cloud.aiplatform.v1.ModelDeploymentMonitoringScheduleConfig model_deployment_monitoring_schedule_config = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringScheduleConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringScheduleConfigOrBuilder)` |   
  
### getModelMonitoringAlertConfig()
    
    
    public abstract ModelMonitoringAlertConfig getModelMonitoringAlertConfig()

Alert config for model monitoring.

` .google.cloud.aiplatform.v1.ModelMonitoringAlertConfig model_monitoring_alert_config = 15; `

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringAlertConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelMonitoringAlertConfig)` | The modelMonitoringAlertConfig.  
  
### getModelMonitoringAlertConfigOrBuilder()
    
    
    public abstract ModelMonitoringAlertConfigOrBuilder getModelMonitoringAlertConfigOrBuilder()

Alert config for model monitoring.

` .google.cloud.aiplatform.v1.ModelMonitoringAlertConfig model_monitoring_alert_config = 15; `

**Returns**  
---  
**Type** | **Description**  
`[ModelMonitoringAlertConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelMonitoringAlertConfigOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Output only. Resource name of a ModelDeploymentMonitoringJob.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Resource name of a ModelDeploymentMonitoringJob.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNextScheduleTime()
    
    
    public abstract Timestamp getNextScheduleTime()

Output only. Timestamp when this monitoring pipeline will be scheduled to run for the next round.

` .google.protobuf.Timestamp next_schedule_time = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The nextScheduleTime.  
  
### getNextScheduleTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getNextScheduleTimeOrBuilder()

Output only. Timestamp when this monitoring pipeline will be scheduled to run for the next round.

` .google.protobuf.Timestamp next_schedule_time = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getPredictInstanceSchemaUri()
    
    
    public abstract String getPredictInstanceSchemaUri()

YAML schema file uri describing the format of a single instance, which are given to format this Endpoint's prediction (and explanation). If not set, we will generate predict schema from collected predict requests.

`string predict_instance_schema_uri = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The predictInstanceSchemaUri.  
  
### getPredictInstanceSchemaUriBytes()
    
    
    public abstract ByteString getPredictInstanceSchemaUriBytes()

YAML schema file uri describing the format of a single instance, which are given to format this Endpoint's prediction (and explanation). If not set, we will generate predict schema from collected predict requests.

`string predict_instance_schema_uri = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for predictInstanceSchemaUri.  
  
### getSamplePredictInstance()
    
    
    public abstract Value getSamplePredictInstance()

Sample Predict instance, same format as PredictRequest.instances, this can be set as a replacement of ModelDeploymentMonitoringJob.predict_instance_schema_uri. If not set, we will generate predict schema from collected predict requests.

`.google.protobuf.Value sample_predict_instance = 19;`

**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` | The samplePredictInstance.  
  
### getSamplePredictInstanceOrBuilder()
    
    
    public abstract ValueOrBuilder getSamplePredictInstanceOrBuilder()

Sample Predict instance, same format as PredictRequest.instances, this can be set as a replacement of ModelDeploymentMonitoringJob.predict_instance_schema_uri. If not set, we will generate predict schema from collected predict requests.

`.google.protobuf.Value sample_predict_instance = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### getSatisfiesPzi()
    
    
    public abstract boolean getSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 27 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public abstract boolean getSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 26 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getScheduleState()
    
    
    public abstract ModelDeploymentMonitoringJob.MonitoringScheduleState getScheduleState()

Output only. Schedule state when the monitoring job is in Running state.

` .google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob.MonitoringScheduleState schedule_state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob.MonitoringScheduleState](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob.MonitoringScheduleState)` | The scheduleState.  
  
### getScheduleStateValue()
    
    
    public abstract int getScheduleStateValue()

Output only. Schedule state when the monitoring job is in Running state.

` .google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob.MonitoringScheduleState schedule_state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for scheduleState.  
  
### getState()
    
    
    public abstract JobState getState()

Output only. The detailed state of the monitoring job. When the job is still creating, the state will be 'PENDING'. Once the job is successfully created, the state will be 'RUNNING'. Pause the job, the state will be 'PAUSED'. Resume the job, the state will return to 'RUNNING'.

` .google.cloud.aiplatform.v1.JobState state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[JobState](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobState)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The detailed state of the monitoring job. When the job is still creating, the state will be 'PENDING'. Once the job is successfully created, the state will be 'RUNNING'. Pause the job, the state will be 'PAUSED'. Resume the job, the state will return to 'RUNNING'.

` .google.cloud.aiplatform.v1.JobState state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getStatsAnomaliesBaseDirectory()
    
    
    public abstract GcsDestination getStatsAnomaliesBaseDirectory()

Stats anomalies base folder path.

`.google.cloud.aiplatform.v1.GcsDestination stats_anomalies_base_directory = 20;`

**Returns**  
---  
**Type** | **Description**  
`[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination)` | The statsAnomaliesBaseDirectory.  
  
### getStatsAnomaliesBaseDirectoryOrBuilder()
    
    
    public abstract GcsDestinationOrBuilder getStatsAnomaliesBaseDirectoryOrBuilder()

Stats anomalies base folder path.

`.google.cloud.aiplatform.v1.GcsDestination stats_anomalies_base_directory = 20;`

**Returns**  
---  
**Type** | **Description**  
`[GcsDestinationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestinationOrBuilder)` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Timestamp when this ModelDeploymentMonitoringJob was updated most recently.

`.google.protobuf.Timestamp update_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Timestamp when this ModelDeploymentMonitoringJob was updated most recently.

`.google.protobuf.Timestamp update_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Timestamp when this ModelDeploymentMonitoringJob was created.

`.google.protobuf.Timestamp create_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEncryptionSpec()
    
    
    public abstract boolean hasEncryptionSpec()

Customer-managed encryption key spec for a ModelDeploymentMonitoringJob. If set, this ModelDeploymentMonitoringJob and all sub-resources of this ModelDeploymentMonitoringJob will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionSpec field is set.  
  
### hasError()
    
    
    public abstract boolean hasError()

Output only. Only populated when the job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.

`.google.rpc.Status error = 23 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasLatestMonitoringPipelineMetadata()
    
    
    public abstract boolean hasLatestMonitoringPipelineMetadata()

Output only. Latest triggered monitoring pipeline metadata.

` .google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadata latest_monitoring_pipeline_metadata = 25 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the latestMonitoringPipelineMetadata field is set.  
  
### hasLogTtl()
    
    
    public abstract boolean hasLogTtl()

The TTL of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl = 1 day.

`.google.protobuf.Duration log_ttl = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the logTtl field is set.  
  
### hasLoggingSamplingStrategy()
    
    
    public abstract boolean hasLoggingSamplingStrategy()

Required. Sample Strategy for logging.

` .google.cloud.aiplatform.v1.SamplingStrategy logging_sampling_strategy = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the loggingSamplingStrategy field is set.  
  
### hasModelDeploymentMonitoringScheduleConfig()
    
    
    public abstract boolean hasModelDeploymentMonitoringScheduleConfig()

Required. Schedule config for running the monitoring job.

` .google.cloud.aiplatform.v1.ModelDeploymentMonitoringScheduleConfig model_deployment_monitoring_schedule_config = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the modelDeploymentMonitoringScheduleConfig field is set.  
  
### hasModelMonitoringAlertConfig()
    
    
    public abstract boolean hasModelMonitoringAlertConfig()

Alert config for model monitoring.

` .google.cloud.aiplatform.v1.ModelMonitoringAlertConfig model_monitoring_alert_config = 15; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the modelMonitoringAlertConfig field is set.  
  
### hasNextScheduleTime()
    
    
    public abstract boolean hasNextScheduleTime()

Output only. Timestamp when this monitoring pipeline will be scheduled to run for the next round.

` .google.protobuf.Timestamp next_schedule_time = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nextScheduleTime field is set.  
  
### hasSamplePredictInstance()
    
    
    public abstract boolean hasSamplePredictInstance()

Sample Predict instance, same format as PredictRequest.instances, this can be set as a replacement of ModelDeploymentMonitoringJob.predict_instance_schema_uri. If not set, we will generate predict schema from collected predict requests.

`.google.protobuf.Value sample_predict_instance = 19;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the samplePredictInstance field is set.  
  
### hasStatsAnomaliesBaseDirectory()
    
    
    public abstract boolean hasStatsAnomaliesBaseDirectory()

Stats anomalies base folder path.

`.google.cloud.aiplatform.v1.GcsDestination stats_anomalies_base_directory = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the statsAnomaliesBaseDirectory field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Timestamp when this ModelDeploymentMonitoringJob was updated most recently.

`.google.protobuf.Timestamp update_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
