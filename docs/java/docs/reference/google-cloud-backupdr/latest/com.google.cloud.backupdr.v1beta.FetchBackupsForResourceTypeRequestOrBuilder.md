---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupsForResourceTypeRequestOrBuilder
title: Interface FetchBackupsForResourceTypeRequestOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:24.356107+00:00
---

# Interface FetchBackupsForResourceTypeRequestOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupsForResourceTypeRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FetchBackupsForResourceTypeRequestOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface FetchBackupsForResourceTypeRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getFilter()
    
    
    public abstract String getFilter()

Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields:

  * name
  * state
  * backup_type
  * create_time
  * expire_time
  * enforced_retention_end_time
  * gcp_backup_plan_info.backup_plan
  * cloud_sql_instance_backup_properties.instance_tier
  * cloud_sql_instance_backup_properties.database_installed_version



`string filter = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filter.  
  
### getFilterBytes()
    
    
    public abstract ByteString getFilterBytes()

Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields:

  * name
  * state
  * backup_type
  * create_time
  * expire_time
  * enforced_retention_end_time
  * gcp_backup_plan_info.backup_plan
  * cloud_sql_instance_backup_properties.instance_tier
  * cloud_sql_instance_backup_properties.database_installed_version



`string filter = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filter.  
  
### getOrderBy()
    
    
    public abstract String getOrderBy()

Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

  * name



`string order_by = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The orderBy.  
  
### getOrderByBytes()
    
    
    public abstract ByteString getOrderByBytes()

Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

  * name



`string order_by = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for orderBy.  
  
### getPageSize()
    
    
    public abstract int getPageSize()

Optional. The maximum number of Backups to return. The service may return fewer than this value. If unspecified, at most 50 Backups will be returned. The maximum value is 100; values above 100 will be coerced to 100.

`int32 page_size = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

Optional. A page token, received from a previous call of `FetchBackupsForResourceType`. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchBackupsForResourceType` must match the call that provided the page token.

`string page_token = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

Optional. A page token, received from a previous call of `FetchBackupsForResourceType`. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchBackupsForResourceType` must match the call that provided the page token.

`string page_token = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getParent()
    
    
    public abstract String getParent()

Required. Datasources are the parent resource for the backups. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. Datasources are the parent resource for the backups. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getResourceType()
    
    
    public abstract String getResourceType()

Required. The type of the GCP resource. Ex: sqladmin.googleapis.com/Instance

`string resource_type = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceType.  
  
### getResourceTypeBytes()
    
    
    public abstract ByteString getResourceTypeBytes()

Required. The type of the GCP resource. Ex: sqladmin.googleapis.com/Instance

`string resource_type = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceType.  
  
### getView()
    
    
    public abstract BackupView getView()

Optional. This parameter is used to specify the view of the backup. If not specified, the default view is BASIC.

` .google.cloud.backupdr.v1beta.BackupView view = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupView](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupView)` | The view.  
  
### getViewValue()
    
    
    public abstract int getViewValue()

Optional. This parameter is used to specify the view of the backup. If not specified, the default view is BASIC.

` .google.cloud.backupdr.v1beta.BackupView view = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for view.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
