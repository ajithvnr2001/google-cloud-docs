---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table
title: Cloud Bigtable V2 Client - Class Table (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:54.807982+00:00
---

# Cloud Bigtable V2 Client - Class Table (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class Table (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class Table.

A collection of user data indexed by row, column, and timestamp.

Each table is served using the resources of its parent cluster.

Generated from protobuf message `google.bigtable.admin.v2.Table`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`  
`↳ cluster_states` |  `array|Google\Protobuf\Internal\MapField`   
Output only. Map from cluster ID to per-cluster table state. If it could not be determined whether or not the table has data in a particular cluster (for example, if its zone is unavailable), then there will be an entry for the cluster with UNKNOWN `replication_status`. Views: `REPLICATION_VIEW`, `ENCRYPTION_VIEW`, `FULL`  
`↳ column_families` |  `array|Google\Protobuf\Internal\MapField`   
The column families configured for this table, mapped by column family ID. Views: `SCHEMA_VIEW`, `STATS_VIEW`, `FULL`  
`↳ granularity` |  `int`   
Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.  
`↳ restore_info` |  `[RestoreInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreInfo)`   
Output only. If this table was restored from another data source (e.g. a backup), this field will be populated with information about the restore.  
`↳ change_stream_config` |  `[ChangeStreamConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ChangeStreamConfig)`   
If specified, enable the change stream on this table. Otherwise, the change stream is disabled and the change stream is not retained.  
`↳ deletion_protection` |  `bool`   
Set to true to make the table protected against data loss. i.e. deleting the following resources through Admin APIs are prohibited: * * The table. * * The column families in the table. * * The instance containing the table. Note one can still delete the data stored in the table through Data APIs.  
`↳ automated_backup_policy` |  `[Table\AutomatedBackupPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.AutomatedBackupPolicy)`   
If specified, automated backups are enabled for this table. Otherwise, automated backups are disabled.  
`↳ effective_automated_backup_policy` |  `[Table\AutomatedBackupPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.AutomatedBackupPolicy)`   
Output only. The effective automated backup policy applied to the table. This represents the policy actually in effect, which may be a system-default policy if the user has not explicitly configured one. Views: `SCHEMA_VIEW`, `FULL`.  
`↳ tiered_storage_config` |  `[TieredStorageConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.TieredStorageConfig)`   
Rules to specify what data is stored in each storage tier. Different tiers store data differently, providing different trade-offs between cost and performance. Different parts of a table can be stored separately on different tiers. If a config is specified, tiered storage is enabled for this table. Otherwise, tiered storage is disabled. Only SSD instances can configure tiered storage.  
`↳ row_key_schema` |  `[Type\Struct](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Struct)`   
The row key schema for this table. The schema is used to decode the raw row key bytes into a structured format. The order of field declarations in this schema is important, as it reflects how the raw row key bytes are structured. Currently, this only affects how the key is read via a GoogleSQL query from the ExecuteQuery API. For a SQL query, the _key column is still read as raw bytes. But queries can reference the key fields by name, which will be decoded from _key using provided type and encoding. Queries that reference key fields will fail if they encounter an invalid row key. For example, if _key = "some_id#2024-04-30#\x00\x13\x00\xf3" with the following schema: { fields { field_name: "id" type { string { encoding: utf8_bytes } } } } fields { field_name: "date" type { string { encoding: utf8_bytes } } } } fields { field_name: "product_code" type { int64 { encoding: big_endian_bytes } } } } encoding { delimited_bytes { delimiter: "#" } } } The decoded key parts would be: id = "some_id", date = "2024-04-30", product_code = 1245427 The query "SELECT _key, product_code FROM table" will return two columns: /------------------------------------------------------\ | _key | product_code | | --------------------------------------|--------------| | "some_id#2024-04-30#\x00\x13\x00\xf3" | 1245427 | ------------------------------------------------------/ The schema has the following invariants: (1) The decoded field values are order-preserved. For read, the field values will be decoded in sorted mode from the raw bytes. (2) Every field in the schema must specify a non-empty name. (3) Every field must specify a type with an associated encoding. The type is limited to scalar types only: Array, Map, Aggregate, and Struct are not allowed. (4) The field names must not collide with existing column family names and reserved keywords "_key" and "_timestamp". The following update operations are allowed for row_key_schema: - Update from an empty schema to a new schema. - Remove the existing schema. This operation requires setting the `ignore_warnings` flag to `true`, since it might be a backward incompatible change. Without the flag, the update request will fail with an INVALID_ARGUMENT error. Any other row key schema update operation (e.g. update existing schema columns names or types) is currently unsupported.  
  
### getName

The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`.

Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`.

Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getClusterStates

Output only. Map from cluster ID to per-cluster table state.

If it could not be determined whether or not the table has data in a particular cluster (for example, if its zone is unavailable), then there will be an entry for the cluster with UNKNOWN `replication_status`. Views: `REPLICATION_VIEW`, `ENCRYPTION_VIEW`, `FULL`

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setClusterStates

Output only. Map from cluster ID to per-cluster table state.

If it could not be determined whether or not the table has data in a particular cluster (for example, if its zone is unavailable), then there will be an entry for the cluster with UNKNOWN `replication_status`. Views: `REPLICATION_VIEW`, `ENCRYPTION_VIEW`, `FULL`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getColumnFamilies

The column families configured for this table, mapped by column family ID.

Views: `SCHEMA_VIEW`, `STATS_VIEW`, `FULL`

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setColumnFamilies

The column families configured for this table, mapped by column family ID.

Views: `SCHEMA_VIEW`, `STATS_VIEW`, `FULL`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGranularity

Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [TimestampGranularity](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.TimestampGranularity).  
  
### setGranularity

Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [TimestampGranularity](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.TimestampGranularity).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRestoreInfo

Output only. If this table was restored from another data source (e.g. a backup), this field will be populated with information about the restore.

**Returns**  
---  
**Type** | **Description**  
`[RestoreInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreInfo)|null` |   
  
### hasRestoreInfo

### clearRestoreInfo

### setRestoreInfo

Output only. If this table was restored from another data source (e.g. a backup), this field will be populated with information about the restore.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[RestoreInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreInfo)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getChangeStreamConfig

If specified, enable the change stream on this table.

Otherwise, the change stream is disabled and the change stream is not retained.

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ChangeStreamConfig)|null` |   
  
### hasChangeStreamConfig

### clearChangeStreamConfig

### setChangeStreamConfig

If specified, enable the change stream on this table.

Otherwise, the change stream is disabled and the change stream is not retained.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ChangeStreamConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ChangeStreamConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDeletionProtection

Set to true to make the table protected against data loss. i.e. deleting the following resources through Admin APIs are prohibited:

  * The table.

  * The column families in the table.

  * The instance containing the table. Note one can still delete the data stored in the table through Data APIs.



**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDeletionProtection

Set to true to make the table protected against data loss. i.e. deleting the following resources through Admin APIs are prohibited:

  * The table.

  * The column families in the table.

  * The instance containing the table. Note one can still delete the data stored in the table through Data APIs.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAutomatedBackupPolicy

If specified, automated backups are enabled for this table.

Otherwise, automated backups are disabled.

**Returns**  
---  
**Type** | **Description**  
`[Table\AutomatedBackupPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.AutomatedBackupPolicy)|null` |   
  
### hasAutomatedBackupPolicy

### setAutomatedBackupPolicy

If specified, automated backups are enabled for this table.

Otherwise, automated backups are disabled.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Table\AutomatedBackupPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.AutomatedBackupPolicy)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEffectiveAutomatedBackupPolicy

Output only. The effective automated backup policy applied to the table.

This represents the policy actually in effect, which may be a system-default policy if the user has not explicitly configured one. Views: `SCHEMA_VIEW`, `FULL`.

**Returns**  
---  
**Type** | **Description**  
`[Table\AutomatedBackupPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.AutomatedBackupPolicy)|null` |   
  
### hasEffectiveAutomatedBackupPolicy

### clearEffectiveAutomatedBackupPolicy

### setEffectiveAutomatedBackupPolicy

Output only. The effective automated backup policy applied to the table.

This represents the policy actually in effect, which may be a system-default policy if the user has not explicitly configured one. Views: `SCHEMA_VIEW`, `FULL`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Table\AutomatedBackupPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.AutomatedBackupPolicy)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTieredStorageConfig

Rules to specify what data is stored in each storage tier.

Different tiers store data differently, providing different trade-offs between cost and performance. Different parts of a table can be stored separately on different tiers. If a config is specified, tiered storage is enabled for this table. Otherwise, tiered storage is disabled. Only SSD instances can configure tiered storage.

**Returns**  
---  
**Type** | **Description**  
`[TieredStorageConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.TieredStorageConfig)|null` |   
  
### hasTieredStorageConfig

### clearTieredStorageConfig

### setTieredStorageConfig

Rules to specify what data is stored in each storage tier.

Different tiers store data differently, providing different trade-offs between cost and performance. Different parts of a table can be stored separately on different tiers. If a config is specified, tiered storage is enabled for this table. Otherwise, tiered storage is disabled. Only SSD instances can configure tiered storage.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[TieredStorageConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.TieredStorageConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRowKeySchema

The row key schema for this table. The schema is used to decode the raw row key bytes into a structured format. The order of field declarations in this schema is important, as it reflects how the raw row key bytes are structured. Currently, this only affects how the key is read via a GoogleSQL query from the ExecuteQuery API.

For a SQL query, the _key column is still read as raw bytes. But queries can reference the key fields by name, which will be decoded from _key using provided type and encoding. Queries that reference key fields will fail if they encounter an invalid row key. For example, if _key = "some_id#2024-04-30#\x00\x13\x00\xf3" with the following schema: { fields { field_name: "id" type { string { encoding: utf8_bytes } } } } fields { field_name: "date" type { string { encoding: utf8_bytes } } } } fields { field_name: "product_code" type { int64 { encoding: big_endian_bytes } } } } encoding { delimited_bytes { delimiter: "#" } } } The decoded key parts would be: id = "some_id", date = "2024-04-30", product_code = 1245427 The query "SELECT _key, product_code FROM table" will return two columns: /------------------------------------------------------\

_key | product_code  
---|---  
"some_id#2024-04-30#\x00\x13\x00\xf3" | 1245427  
  
\------------------------------------------------------/ The schema has the following invariants: (1) The decoded field values are order-preserved. For read, the field values will be decoded in sorted mode from the raw bytes. (2) Every field in the schema must specify a non-empty name. (3) Every field must specify a type with an associated encoding. The type is limited to scalar types only: Array, Map, Aggregate, and Struct are not allowed. (4) The field names must not collide with existing column family names and reserved keywords "_key" and "_timestamp". The following update operations are allowed for row_key_schema:

  * Update from an empty schema to a new schema.
  * Remove the existing schema. This operation requires setting the `ignore_warnings` flag to `true`, since it might be a backward incompatible change. Without the flag, the update request will fail with an INVALID_ARGUMENT error. Any other row key schema update operation (e.g. update existing schema columns names or types) is currently unsupported.



**Returns**  
---  
**Type** | **Description**  
`[Type\Struct](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Struct)|null` |   
  
### hasRowKeySchema

### clearRowKeySchema

### setRowKeySchema

The row key schema for this table. The schema is used to decode the raw row key bytes into a structured format. The order of field declarations in this schema is important, as it reflects how the raw row key bytes are structured. Currently, this only affects how the key is read via a GoogleSQL query from the ExecuteQuery API.

For a SQL query, the _key column is still read as raw bytes. But queries can reference the key fields by name, which will be decoded from _key using provided type and encoding. Queries that reference key fields will fail if they encounter an invalid row key. For example, if _key = "some_id#2024-04-30#\x00\x13\x00\xf3" with the following schema: { fields { field_name: "id" type { string { encoding: utf8_bytes } } } } fields { field_name: "date" type { string { encoding: utf8_bytes } } } } fields { field_name: "product_code" type { int64 { encoding: big_endian_bytes } } } } encoding { delimited_bytes { delimiter: "#" } } } The decoded key parts would be: id = "some_id", date = "2024-04-30", product_code = 1245427 The query "SELECT _key, product_code FROM table" will return two columns: /------------------------------------------------------\

_key | product_code  
---|---  
"some_id#2024-04-30#\x00\x13\x00\xf3" | 1245427  
  
\------------------------------------------------------/ The schema has the following invariants: (1) The decoded field values are order-preserved. For read, the field values will be decoded in sorted mode from the raw bytes. (2) Every field in the schema must specify a non-empty name. (3) Every field must specify a type with an associated encoding. The type is limited to scalar types only: Array, Map, Aggregate, and Struct are not allowed. (4) The field names must not collide with existing column family names and reserved keywords "_key" and "_timestamp". The following update operations are allowed for row_key_schema:

  * Update from an empty schema to a new schema.
  * Remove the existing schema. This operation requires setting the `ignore_warnings` flag to `true`, since it might be a backward incompatible change. Without the flag, the update request will fail with an INVALID_ARGUMENT error. Any other row key schema update operation (e.g. update existing schema columns names or types) is currently unsupported.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Struct](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Struct)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAutomatedBackupConfig

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
