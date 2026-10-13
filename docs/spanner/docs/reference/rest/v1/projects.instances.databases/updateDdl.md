---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/updateDdl/
title: Method: projects.instances.databases.updateDdl \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:07.424312+00:00
---

# Method: projects.instances.databases.updateDdl  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/updateDdl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.updateDdl Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc. The returned long-running operation will have a name of the format `<database_name>/operations/<operationId>` and can be used to track execution of the schema changes. The metadata field type is `[UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateDatabaseDdlMetadata)`. The operation has no response.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`PATCH https://spanner.googleapis.com/v1/{database=projects/*/instances/*/databases/*}/ddl`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`database` |  `string` Required. The database to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.databases.updateDdl`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "statements": [
        string
      ],
      "operationId": string,
      "protoDescriptors": string
    }  
  
Fields  
---  
`statements[]` |  `string` Required. DDL statements to be applied to the database.  
`operationId` |  `string` If empty, the new update request is assigned an automatically-generated operation ID. Otherwise, `operationId` is used to construct the name of the resulting Operation.Specifying an explicit operation ID simplifies determining whether the statements were executed in the event that the `[databases.updateDdl](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/updateDdl#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)` call is replayed, or the return value is otherwise lost: the `[database](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/updateDdl#body.PATH_PARAMETERS.database)` and `operationId` fields can be combined to form the `name` of the resulting longrunning.Operation: `<database>/operations/<operationId>`.`operationId` should be unique within the database, and must be a valid identifier: `[a-z][a-z0-9_]*`. Note that automatically-generated operation IDs always begin with an underscore. If the named operation already exists, `[databases.updateDdl](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/updateDdl#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)` returns `ALREADY_EXISTS`.  
`protoDescriptors` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run
    
    
    $protoc  --proto_path=/app_path --proto_path=/lib_path \
             --include_imports \
             --descriptor_set_out=descriptors.data \
             moon/shot/app.proto
    

For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).A base64-encoded string.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
