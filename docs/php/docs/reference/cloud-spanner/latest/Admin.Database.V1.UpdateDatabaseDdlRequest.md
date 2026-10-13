---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlRequest
title: Cloud Spanner V1 Client - Class UpdateDatabaseDdlRequest (2.11.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:48.865916+00:00
---

# Cloud Spanner V1 Client - Class UpdateDatabaseDdlRequest (2.11.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Spanner V1 Client - Class UpdateDatabaseDdlRequest (2.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

Reference documentation and code samples for the Cloud Spanner V1 Client class UpdateDatabaseDdlRequest.

Enqueues the given DDL statements to be applied, in order but not necessarily all at once, to the database schema at some point (or points) in the future. The server checks that the statements are executable (syntactically valid, name tables that exist, etc.) before enqueueing them, but they may still fail upon later execution (e.g., if a statement from another batch of statements is applied first and it conflicts in some way, or if there is some data-related problem like a `NULL` value in a column to which `NOT NULL` would be added). If a statement fails, all subsequent statements in the batch are automatically cancelled.

Each batch of statements is assigned a name which can be used with the Operations API to monitor progress. See the [operation_id](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlRequest#_Google_Cloud_Spanner_Admin_Database_V1_UpdateDatabaseDdlRequest__getOperationId__) field for more details.

Generated from protobuf message `google.spanner.admin.database.v1.UpdateDatabaseDdlRequest`

## Namespace

Google \ Cloud \ Spanner \ Admin \ Database \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ database` |  `string`   
Required. The database to update.  
`↳ statements` |  `string[]`   
Required. DDL statements to be applied to the database.  
`↳ operation_id` |  `string`   
If empty, the new update request is assigned an automatically-generated operation ID. Otherwise, `operation_id` is used to construct the name of the resulting Operation. Specifying an explicit operation ID simplifies determining whether the statements were executed in the event that the [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) call is replayed, or the return value is otherwise lost: the [database](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlRequest#_Google_Cloud_Spanner_Admin_Database_V1_UpdateDatabaseDdlRequest__getDatabase__) and `operation_id` fields can be combined to form the name of the resulting longrunning.Operation: `<database>/operations/<operation_id>`. `operation_id` should be unique within the database, and must be a valid identifier: `[a-z][a-z0-9_]*`. Note that automatically-generated operation IDs always begin with an underscore. If the named operation already exists, [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) returns `ALREADY_EXISTS`.  
`↳ proto_descriptors` |  `string`   
Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run `$protoc --proto_path=/app_path --proto_path=/lib_path \ --include_imports \ --descriptor_set_out=descriptors.data \ moon/shot/app.proto` For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).  
`↳ throughput_mode` |  `bool`   
Optional. This field is exposed to be used by the Spanner Migration Tool. For more details, see [SMT](https://github.com/GoogleCloudPlatform/spanner-migration-tool).  
  
### getDatabase

Required. The database to update.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDatabase

Required. The database to update.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStatements

Required. DDL statements to be applied to the database.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setStatements

Required. DDL statements to be applied to the database.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOperationId

If empty, the new update request is assigned an automatically-generated operation ID. Otherwise, `operation_id` is used to construct the name of the resulting Operation.

Specifying an explicit operation ID simplifies determining whether the statements were executed in the event that the [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) call is replayed, or the return value is otherwise lost: the [database](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlRequest#_Google_Cloud_Spanner_Admin_Database_V1_UpdateDatabaseDdlRequest__getDatabase__) and `operation_id` fields can be combined to form the name of the resulting longrunning.Operation: `<database>/operations/<operation_id>`. `operation_id` should be unique within the database, and must be a valid identifier: `[a-z][a-z0-9_]*`. Note that automatically-generated operation IDs always begin with an underscore. If the named operation already exists, [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) returns `ALREADY_EXISTS`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOperationId

If empty, the new update request is assigned an automatically-generated operation ID. Otherwise, `operation_id` is used to construct the name of the resulting Operation.

Specifying an explicit operation ID simplifies determining whether the statements were executed in the event that the [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) call is replayed, or the return value is otherwise lost: the [database](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlRequest#_Google_Cloud_Spanner_Admin_Database_V1_UpdateDatabaseDdlRequest__getDatabase__) and `operation_id` fields can be combined to form the name of the resulting longrunning.Operation: `<database>/operations/<operation_id>`. `operation_id` should be unique within the database, and must be a valid identifier: `[a-z][a-z0-9_]*`. Note that automatically-generated operation IDs always begin with an underscore. If the named operation already exists, [UpdateDatabaseDdl](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__updateDatabaseDdl__) returns `ALREADY_EXISTS`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProtoDescriptors

Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements.

Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run
    
    
    $protoc  --proto_path=/app_path --proto_path=/lib_path \
             --include_imports \
             --descriptor_set_out=descriptors.data \
             moon/shot/app.proto
    

For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setProtoDescriptors

Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements.

Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run
    
    
    $protoc  --proto_path=/app_path --proto_path=/lib_path \
             --include_imports \
             --descriptor_set_out=descriptors.data \
             moon/shot/app.proto
    

For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getThroughputMode

Optional. This field is exposed to be used by the Spanner Migration Tool.

For more details, see [SMT](https://github.com/GoogleCloudPlatform/spanner-migration-tool).

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setThroughputMode

Optional. This field is exposed to be used by the Spanner Migration Tool.

For more details, see [SMT](https://github.com/GoogleCloudPlatform/spanner-migration-tool).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`database` |  `string`   
Required. The database to update. Please see DatabaseAdminClient::databaseName() for help formatting this field.  
`statements` |  `string[]`   
Required. DDL statements to be applied to the database.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateDatabaseDdlRequest](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.UpdateDatabaseDdlRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
