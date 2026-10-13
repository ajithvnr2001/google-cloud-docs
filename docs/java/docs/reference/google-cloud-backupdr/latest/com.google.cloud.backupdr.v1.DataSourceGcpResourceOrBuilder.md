---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSourceGcpResourceOrBuilder
title: Interface DataSourceGcpResourceOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:47.513420+00:00
---

# Interface DataSourceGcpResourceOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSourceGcpResourceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataSourceGcpResourceOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DataSourceGcpResourceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAlloyDbClusterDatasourceProperties()
    
    
    public abstract AlloyDBClusterDataSourceProperties getAlloyDbClusterDatasourceProperties()

Output only. AlloyDBClusterDataSourceProperties has a subset of AlloyDB cluster properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.AlloyDBClusterDataSourceProperties alloy_db_cluster_datasource_properties = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBClusterDataSourceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.AlloyDBClusterDataSourceProperties)` | The alloyDbClusterDatasourceProperties.  
  
### getAlloyDbClusterDatasourcePropertiesOrBuilder()
    
    
    public abstract AlloyDBClusterDataSourcePropertiesOrBuilder getAlloyDbClusterDatasourcePropertiesOrBuilder()

Output only. AlloyDBClusterDataSourceProperties has a subset of AlloyDB cluster properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.AlloyDBClusterDataSourceProperties alloy_db_cluster_datasource_properties = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBClusterDataSourcePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.AlloyDBClusterDataSourcePropertiesOrBuilder)` |   
  
### getCloudSqlInstanceDatasourceProperties()
    
    
    public abstract CloudSqlInstanceDataSourceProperties getCloudSqlInstanceDatasourceProperties()

Output only. CloudSqlInstanceDataSourceProperties has a subset of Cloud SQL Instance properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.CloudSqlInstanceDataSourceProperties cloud_sql_instance_datasource_properties = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudSqlInstanceDataSourceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CloudSqlInstanceDataSourceProperties)` | The cloudSqlInstanceDatasourceProperties.  
  
### getCloudSqlInstanceDatasourcePropertiesOrBuilder()
    
    
    public abstract CloudSqlInstanceDataSourcePropertiesOrBuilder getCloudSqlInstanceDatasourcePropertiesOrBuilder()

Output only. CloudSqlInstanceDataSourceProperties has a subset of Cloud SQL Instance properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.CloudSqlInstanceDataSourceProperties cloud_sql_instance_datasource_properties = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudSqlInstanceDataSourcePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CloudSqlInstanceDataSourcePropertiesOrBuilder)` |   
  
### getComputeInstanceDatasourceProperties()
    
    
    public abstract ComputeInstanceDataSourceProperties getComputeInstanceDatasourceProperties()

ComputeInstanceDataSourceProperties has a subset of Compute Instance properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.ComputeInstanceDataSourceProperties compute_instance_datasource_properties = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceDataSourceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceDataSourceProperties)` | The computeInstanceDatasourceProperties.  
  
### getComputeInstanceDatasourcePropertiesOrBuilder()
    
    
    public abstract ComputeInstanceDataSourcePropertiesOrBuilder getComputeInstanceDatasourcePropertiesOrBuilder()

ComputeInstanceDataSourceProperties has a subset of Compute Instance properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.ComputeInstanceDataSourceProperties compute_instance_datasource_properties = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceDataSourcePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceDataSourcePropertiesOrBuilder)` |   
  
### getDiskDatasourceProperties()
    
    
    public abstract DiskDataSourceProperties getDiskDatasourceProperties()

DiskDataSourceProperties has a subset of Disk properties that are useful at the Datasource level.

`.google.cloud.backupdr.v1.DiskDataSourceProperties disk_datasource_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DiskDataSourceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskDataSourceProperties)` | The diskDatasourceProperties.  
  
### getDiskDatasourcePropertiesOrBuilder()
    
    
    public abstract DiskDataSourcePropertiesOrBuilder getDiskDatasourcePropertiesOrBuilder()

DiskDataSourceProperties has a subset of Disk properties that are useful at the Datasource level.

`.google.cloud.backupdr.v1.DiskDataSourceProperties disk_datasource_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DiskDataSourcePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskDataSourcePropertiesOrBuilder)` |   
  
### getGcpResourcePropertiesCase()
    
    
    public abstract DataSourceGcpResource.GcpResourcePropertiesCase getGcpResourcePropertiesCase()

**Returns**  
---  
**Type** | **Description**  
`[DataSourceGcpResource.GcpResourcePropertiesCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSourceGcpResource.GcpResourcePropertiesCase)` |   
  
### getGcpResourcename()
    
    
    public abstract String getGcpResourcename()

Output only. Full resource pathname URL of the source Google Cloud resource.

`string gcp_resourcename = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcpResourcename.  
  
### getGcpResourcenameBytes()
    
    
    public abstract ByteString getGcpResourcenameBytes()

Output only. Full resource pathname URL of the source Google Cloud resource.

`string gcp_resourcename = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcpResourcename.  
  
### getLocation()
    
    
    public abstract String getLocation()

Location of the resource: <region>/<zone>/"global"/"unspecified".

`string location = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The location.  
  
### getLocationBytes()
    
    
    public abstract ByteString getLocationBytes()

Location of the resource: <region>/<zone>/"global"/"unspecified".

`string location = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for location.  
  
### getType()
    
    
    public abstract String getType()

The type of the Google Cloud resource. Use the Unified Resource Type, eg. compute.googleapis.com/Instance.

`string type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The type.  
  
### getTypeBytes()
    
    
    public abstract ByteString getTypeBytes()

The type of the Google Cloud resource. Use the Unified Resource Type, eg. compute.googleapis.com/Instance.

`string type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for type.  
  
### hasAlloyDbClusterDatasourceProperties()
    
    
    public abstract boolean hasAlloyDbClusterDatasourceProperties()

Output only. AlloyDBClusterDataSourceProperties has a subset of AlloyDB cluster properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.AlloyDBClusterDataSourceProperties alloy_db_cluster_datasource_properties = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the alloyDbClusterDatasourceProperties field is set.  
  
### hasCloudSqlInstanceDatasourceProperties()
    
    
    public abstract boolean hasCloudSqlInstanceDatasourceProperties()

Output only. CloudSqlInstanceDataSourceProperties has a subset of Cloud SQL Instance properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.CloudSqlInstanceDataSourceProperties cloud_sql_instance_datasource_properties = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudSqlInstanceDatasourceProperties field is set.  
  
### hasComputeInstanceDatasourceProperties()
    
    
    public abstract boolean hasComputeInstanceDatasourceProperties()

ComputeInstanceDataSourceProperties has a subset of Compute Instance properties that are useful at the Datasource level.

` .google.cloud.backupdr.v1.ComputeInstanceDataSourceProperties compute_instance_datasource_properties = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeInstanceDatasourceProperties field is set.  
  
### hasDiskDatasourceProperties()
    
    
    public abstract boolean hasDiskDatasourceProperties()

DiskDataSourceProperties has a subset of Disk properties that are useful at the Datasource level.

`.google.cloud.backupdr.v1.DiskDataSourceProperties disk_datasource_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diskDatasourceProperties field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
