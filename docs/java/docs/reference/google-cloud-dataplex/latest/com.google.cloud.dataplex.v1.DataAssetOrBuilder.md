---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAssetOrBuilder
title: Interface DataAssetOrBuilder (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:45.886527+00:00
---

# Interface DataAssetOrBuilder (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAssetOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataAssetOrBuilder (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 
    
    
    public interface DataAssetOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsAccessGroupConfigs(String key)
    
    
    public abstract boolean containsAccessGroupConfigs(String key)

Optional. Access groups configurations for this data asset.

The key is `DataProduct.AccessGroup.id` and the value is `AccessGroupConfig`.

Example: `<code><code> { "analyst": { "iamRoles": ["roles/bigquery.dataViewer"] } } </code></code>`

Currently, at most one IAM role is allowed per access group. For providing multiple predefined IAM roles, wrap them in a custom IAM role as per <https://cloud.google.com/iam/docs/creating-custom-roles>.

` map<string, .google.cloud.dataplex.v1.DataAsset.AccessGroupConfig> access_group_configs = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. User-defined labels for the data asset.

Example: `<code><code> { "environment": "production", "billing": "marketing-department" } </code></code>`

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccessGroupConfigs() (deprecated)
    
    
    public abstract Map<String,DataAsset.AccessGroupConfig> getAccessGroupConfigs()

Use [#getAccessGroupConfigsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAssetOrBuilder#com_google_cloud_dataplex_v1_DataAssetOrBuilder_getAccessGroupConfigsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AccessGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.AccessGroupConfig)>` |   
  
### getAccessGroupConfigsCount()
    
    
    public abstract int getAccessGroupConfigsCount()

Optional. Access groups configurations for this data asset.

The key is `DataProduct.AccessGroup.id` and the value is `AccessGroupConfig`.

Example: `<code><code> { "analyst": { "iamRoles": ["roles/bigquery.dataViewer"] } } </code></code>`

Currently, at most one IAM role is allowed per access group. For providing multiple predefined IAM roles, wrap them in a custom IAM role as per <https://cloud.google.com/iam/docs/creating-custom-roles>.

` map<string, .google.cloud.dataplex.v1.DataAsset.AccessGroupConfig> access_group_configs = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccessGroupConfigsMap()
    
    
    public abstract Map<String,DataAsset.AccessGroupConfig> getAccessGroupConfigsMap()

Optional. Access groups configurations for this data asset.

The key is `DataProduct.AccessGroup.id` and the value is `AccessGroupConfig`.

Example: `<code><code> { "analyst": { "iamRoles": ["roles/bigquery.dataViewer"] } } </code></code>`

Currently, at most one IAM role is allowed per access group. For providing multiple predefined IAM roles, wrap them in a custom IAM role as per <https://cloud.google.com/iam/docs/creating-custom-roles>.

` map<string, .google.cloud.dataplex.v1.DataAsset.AccessGroupConfig> access_group_configs = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AccessGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.AccessGroupConfig)>` |   
  
### getAccessGroupConfigsOrDefault(String key, DataAsset.AccessGroupConfig defaultValue)
    
    
    public abstract DataAsset.AccessGroupConfig getAccessGroupConfigsOrDefault(String key, DataAsset.AccessGroupConfig defaultValue)

Optional. Access groups configurations for this data asset.

The key is `DataProduct.AccessGroup.id` and the value is `AccessGroupConfig`.

Example: `<code><code> { "analyst": { "iamRoles": ["roles/bigquery.dataViewer"] } } </code></code>`

Currently, at most one IAM role is allowed per access group. For providing multiple predefined IAM roles, wrap them in a custom IAM role as per <https://cloud.google.com/iam/docs/creating-custom-roles>.

` map<string, .google.cloud.dataplex.v1.DataAsset.AccessGroupConfig> access_group_configs = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[DataAsset.AccessGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.AccessGroupConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataAsset.AccessGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.AccessGroupConfig)` |   
  
### getAccessGroupConfigsOrThrow(String key)
    
    
    public abstract DataAsset.AccessGroupConfig getAccessGroupConfigsOrThrow(String key)

Optional. Access groups configurations for this data asset.

The key is `DataProduct.AccessGroup.id` and the value is `AccessGroupConfig`.

Example: `<code><code> { "analyst": { "iamRoles": ["roles/bigquery.dataViewer"] } } </code></code>`

Currently, at most one IAM role is allowed per access group. For providing multiple predefined IAM roles, wrap them in a custom IAM role as per <https://cloud.google.com/iam/docs/creating-custom-roles>.

` map<string, .google.cloud.dataplex.v1.DataAsset.AccessGroupConfig> access_group_configs = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataAsset.AccessGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.AccessGroupConfig)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time at which the data asset was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time at which the data asset was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getEtag()
    
    
    public abstract String getEtag()

Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.

`string etag = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.

`string etag = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAssetOrBuilder#com_google_cloud_dataplex_v1_DataAssetOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. User-defined labels for the data asset.

Example: `<code><code> { "environment": "production", "billing": "marketing-department" } </code></code>`

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. User-defined labels for the data asset.

Example: `<code><code> { "environment": "production", "billing": "marketing-department" } </code></code>`

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. User-defined labels for the data asset.

Example: `<code><code> { "environment": "production", "billing": "marketing-department" } </code></code>`

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. User-defined labels for the data asset.

Example: `<code><code> { "environment": "production", "billing": "marketing-department" } </code></code>`

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. Resource name of the data asset. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Resource name of the data asset. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getResource()
    
    
    public abstract String getResource()

Required. Immutable. Full resource name of the cloud resource represented by the data asset. This must follow <https://cloud.google.com/iam/docs/full-resource-names>. Example: `//bigquery.googleapis.com/projects/my_project_123/datasets/dataset_456/tables/table_789` Only BigQuery tables and datasets are currently supported. Data asset creator must have getIamPolicy and setIamPolicy permissions on the resource. Data asset creator must also have resource specific get permission, for instance, bigquery.tables.get for BigQuery tables.

` string resource = 7 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resource.  
  
### getResourceBytes()
    
    
    public abstract ByteString getResourceBytes()

Required. Immutable. Full resource name of the cloud resource represented by the data asset. This must follow <https://cloud.google.com/iam/docs/full-resource-names>. Example: `//bigquery.googleapis.com/projects/my_project_123/datasets/dataset_456/tables/table_789` Only BigQuery tables and datasets are currently supported. Data asset creator must have getIamPolicy and setIamPolicy permissions on the resource. Data asset creator must also have resource specific get permission, for instance, bigquery.tables.get for BigQuery tables.

` string resource = 7 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resource.  
  
### getUid()
    
    
    public abstract String getUid()

Output only. System generated globally unique ID for the data asset. This ID will be different if the data asset is deleted and re-created with the same name.

` string uid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. System generated globally unique ID for the data asset. This ID will be different if the data asset is deleted and re-created with the same name.

` string uid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The time at which the data asset was last updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time at which the data asset was last updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time at which the data asset was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The time at which the data asset was last updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
