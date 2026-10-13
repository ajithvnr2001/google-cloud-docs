---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.EntryOrBuilder
title: Interface EntryOrBuilder (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:08.612869+00:00
---

# Interface EntryOrBuilder (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.EntryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EntryOrBuilder (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public interface EntryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBigqueryDateShardedSpec()
    
    
    public abstract BigQueryDateShardedSpec getBigqueryDateShardedSpec()

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDateShardedSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec)` | The bigqueryDateShardedSpec.  
  
### getBigqueryDateShardedSpecOrBuilder()
    
    
    public abstract BigQueryDateShardedSpecOrBuilder getBigqueryDateShardedSpecOrBuilder()

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDateShardedSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpecOrBuilder)` |   
  
### getBigqueryTableSpec()
    
    
    public abstract BigQueryTableSpec getBigqueryTableSpec()

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryTableSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryTableSpec)` | The bigqueryTableSpec.  
  
### getBigqueryTableSpecOrBuilder()
    
    
    public abstract BigQueryTableSpecOrBuilder getBigqueryTableSpecOrBuilder()

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryTableSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryTableSpecOrBuilder)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Entry description, which can consist of several sentences or paragraphs that describe entry contents. Default value is an empty string.

`string description = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Entry description, which can consist of several sentences or paragraphs that describe entry contents. Default value is an empty string.

`string description = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Display information such as title and description. A short name to identify the entry, for example, "Analytics Data - Jan 2011". Default value is an empty string.

`string display_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Display information such as title and description. A short name to identify the entry, for example, "Analytics Data - Jan 2011". Default value is an empty string.

`string display_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEntryTypeCase()
    
    
    public abstract Entry.EntryTypeCase getEntryTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[Entry.EntryTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.EntryTypeCase)` |   
  
### getGcsFilesetSpec()
    
    
    public abstract GcsFilesetSpec getGcsFilesetSpec()

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[GcsFilesetSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GcsFilesetSpec)` | The gcsFilesetSpec.  
  
### getGcsFilesetSpecOrBuilder()
    
    
    public abstract GcsFilesetSpecOrBuilder getGcsFilesetSpecOrBuilder()

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[GcsFilesetSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GcsFilesetSpecOrBuilder)` |   
  
### getIntegratedSystem()
    
    
    public abstract IntegratedSystem getIntegratedSystem()

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[IntegratedSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.IntegratedSystem)` | The integratedSystem.  
  
### getIntegratedSystemValue()
    
    
    public abstract int getIntegratedSystemValue()

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for integratedSystem.  
  
### getLinkedResource()
    
    
    public abstract String getLinkedResource()

The resource this metadata entry refers to.

For Google Cloud Platform resources, `linked_resource` is the [full name of the resource](https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is:

  * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty string.




`string linked_resource = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The linkedResource.  
  
### getLinkedResourceBytes()
    
    
    public abstract ByteString getLinkedResourceBytes()

The resource this metadata entry refers to.

For Google Cloud Platform resources, `linked_resource` is the [full name of the resource](https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is:

  * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty string.




`string linked_resource = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for linkedResource.  
  
### getName()
    
    
    public abstract String getName()

Output only. Identifier. The Data Catalog resource name of the entry in URL format. Example:

  * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

Note that this Entry and its child resources may not actually be stored in the location in this name.




` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Identifier. The Data Catalog resource name of the entry in URL format. Example:

  * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

Note that this Entry and its child resources may not actually be stored in the location in this name.




` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSchema()
    
    
    public abstract Schema getSchema()

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Schema)` | The schema.  
  
### getSchemaOrBuilder()
    
    
    public abstract SchemaOrBuilder getSchemaOrBuilder()

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SchemaOrBuilder)` |   
  
### getSourceSystemTimestamps()
    
    
    public abstract SystemTimestamps getSourceSystemTimestamps()

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SystemTimestamps](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SystemTimestamps)` | The sourceSystemTimestamps.  
  
### getSourceSystemTimestampsOrBuilder()
    
    
    public abstract SystemTimestampsOrBuilder getSourceSystemTimestampsOrBuilder()

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SystemTimestampsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SystemTimestampsOrBuilder)` |   
  
### getSystemCase()
    
    
    public abstract Entry.SystemCase getSystemCase()

**Returns**  
---  
**Type** | **Description**  
`[Entry.SystemCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.SystemCase)` |   
  
### getType()
    
    
    public abstract EntryType getType()

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.EntryType)` | The type.  
  
### getTypeSpecCase()
    
    
    public abstract Entry.TypeSpecCase getTypeSpecCase()

**Returns**  
---  
**Type** | **Description**  
`[Entry.TypeSpecCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.TypeSpecCase)` |   
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getUsageSignal()
    
    
    public abstract UsageSignal getUsageSignal()

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UsageSignal](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UsageSignal)` | The usageSignal.  
  
### getUsageSignalOrBuilder()
    
    
    public abstract UsageSignalOrBuilder getUsageSignalOrBuilder()

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UsageSignalOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UsageSignalOrBuilder)` |   
  
### getUserSpecifiedSystem()
    
    
    public abstract String getUserSpecifiedSystem()

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userSpecifiedSystem.  
  
### getUserSpecifiedSystemBytes()
    
    
    public abstract ByteString getUserSpecifiedSystemBytes()

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userSpecifiedSystem.  
  
### getUserSpecifiedType()
    
    
    public abstract String getUserSpecifiedType()

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userSpecifiedType.  
  
### getUserSpecifiedTypeBytes()
    
    
    public abstract ByteString getUserSpecifiedTypeBytes()

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userSpecifiedType.  
  
### hasBigqueryDateShardedSpec()
    
    
    public abstract boolean hasBigqueryDateShardedSpec()

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryDateShardedSpec field is set.  
  
### hasBigqueryTableSpec()
    
    
    public abstract boolean hasBigqueryTableSpec()

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryTableSpec field is set.  
  
### hasGcsFilesetSpec()
    
    
    public abstract boolean hasGcsFilesetSpec()

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsFilesetSpec field is set.  
  
### hasIntegratedSystem()
    
    
    public abstract boolean hasIntegratedSystem()

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the integratedSystem field is set.  
  
### hasSchema()
    
    
    public abstract boolean hasSchema()

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the schema field is set.  
  
### hasSourceSystemTimestamps()
    
    
    public abstract boolean hasSourceSystemTimestamps()

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceSystemTimestamps field is set.  
  
### hasType()
    
    
    public abstract boolean hasType()

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the type field is set.  
  
### hasUsageSignal()
    
    
    public abstract boolean hasUsageSignal()

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the usageSignal field is set.  
  
### hasUserSpecifiedSystem()
    
    
    public abstract boolean hasUserSpecifiedSystem()

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userSpecifiedSystem field is set.  
  
### hasUserSpecifiedType()
    
    
    public abstract boolean hasUserSpecifiedType()

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userSpecifiedType field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
