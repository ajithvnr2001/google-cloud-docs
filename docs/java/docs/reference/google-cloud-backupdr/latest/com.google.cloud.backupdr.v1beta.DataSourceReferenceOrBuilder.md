---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSourceReferenceOrBuilder
title: Interface DataSourceReferenceOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:28.089203+00:00
---

# Interface DataSourceReferenceOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSourceReferenceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataSourceReferenceOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DataSourceReferenceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when the DataSourceReference was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when the DataSourceReference was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDataSource()
    
    
    public abstract String getDataSource()

Output only. The resource name of the DataSource. Format: projects/{project}/locations/{location}/backupVaults/{backupVault}/dataSources/{dataSource}

` string data_source = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataSource.  
  
### getDataSourceBackupConfigInfo()
    
    
    public abstract DataSourceBackupConfigInfo getDataSourceBackupConfigInfo()

Output only. Information of backup configuration on the DataSource.

` .google.cloud.backupdr.v1beta.DataSourceBackupConfigInfo data_source_backup_config_info = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataSourceBackupConfigInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSourceBackupConfigInfo)` | The dataSourceBackupConfigInfo.  
  
### getDataSourceBackupConfigInfoOrBuilder()
    
    
    public abstract DataSourceBackupConfigInfoOrBuilder getDataSourceBackupConfigInfoOrBuilder()

Output only. Information of backup configuration on the DataSource.

` .google.cloud.backupdr.v1beta.DataSourceBackupConfigInfo data_source_backup_config_info = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataSourceBackupConfigInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSourceBackupConfigInfoOrBuilder)` |   
  
### getDataSourceBackupConfigState()
    
    
    public abstract BackupConfigState getDataSourceBackupConfigState()

Output only. The backup configuration state of the DataSource.

` .google.cloud.backupdr.v1beta.BackupConfigState data_source_backup_config_state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigState](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupConfigState)` | The dataSourceBackupConfigState.  
  
### getDataSourceBackupConfigStateValue()
    
    
    public abstract int getDataSourceBackupConfigStateValue()

Output only. The backup configuration state of the DataSource.

` .google.cloud.backupdr.v1beta.BackupConfigState data_source_backup_config_state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for dataSourceBackupConfigState.  
  
### getDataSourceBackupCount()
    
    
    public abstract long getDataSourceBackupCount()

Output only. Number of backups in the DataSource.

`int64 data_source_backup_count = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The dataSourceBackupCount.  
  
### getDataSourceBytes()
    
    
    public abstract ByteString getDataSourceBytes()

Output only. The resource name of the DataSource. Format: projects/{project}/locations/{location}/backupVaults/{backupVault}/dataSources/{dataSource}

` string data_source = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataSource.  
  
### getDataSourceGcpResourceInfo()
    
    
    public abstract DataSourceGcpResourceInfo getDataSourceGcpResourceInfo()

Output only. The Google Cloud resource that the DataSource is associated with.

` .google.cloud.backupdr.v1beta.DataSourceGcpResourceInfo data_source_gcp_resource_info = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataSourceGcpResourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSourceGcpResourceInfo)` | The dataSourceGcpResourceInfo.  
  
### getDataSourceGcpResourceInfoOrBuilder()
    
    
    public abstract DataSourceGcpResourceInfoOrBuilder getDataSourceGcpResourceInfoOrBuilder()

Output only. The Google Cloud resource that the DataSource is associated with.

` .google.cloud.backupdr.v1beta.DataSourceGcpResourceInfo data_source_gcp_resource_info = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataSourceGcpResourceInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSourceGcpResourceInfoOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the DataSourceReference. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the DataSourceReference. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getTotalStoredBytes()
    
    
    public abstract long getTotalStoredBytes()

Output only. Total size of the storage used by all backup resources for the referenced datasource.

`optional int64 total_stored_bytes = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalStoredBytes.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when the DataSourceReference was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDataSourceBackupConfigInfo()
    
    
    public abstract boolean hasDataSourceBackupConfigInfo()

Output only. Information of backup configuration on the DataSource.

` .google.cloud.backupdr.v1beta.DataSourceBackupConfigInfo data_source_backup_config_info = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataSourceBackupConfigInfo field is set.  
  
### hasDataSourceGcpResourceInfo()
    
    
    public abstract boolean hasDataSourceGcpResourceInfo()

Output only. The Google Cloud resource that the DataSource is associated with.

` .google.cloud.backupdr.v1beta.DataSourceGcpResourceInfo data_source_gcp_resource_info = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataSourceGcpResourceInfo field is set.  
  
### hasTotalStoredBytes()
    
    
    public abstract boolean hasTotalStoredBytes()

Output only. Total size of the storage used by all backup resources for the referenced datasource.

`optional int64 total_stored_bytes = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the totalStoredBytes field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
