---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/create/
title: Method: projects.instances.databases.create \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:05.079503+00:00
---

# Method: projects.instances.databases.create  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Creates a new Spanner database and starts to prepare it for serving. The returned long-running operation will have a name of the format `<database_name>/operations/<operationId>` and can be used to track preparation of the database. The metadata field type is `[CreateDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateDatabaseMetadata)`. The response field type is `[Database](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database)`, if successful.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{parent=projects/*/instances/*}/databases`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the instance that will serve the new database. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.databases.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "createStatement": string,
      "extraStatements": [
        string
      ],
      "encryptionConfig": {
        object ([EncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#EncryptionConfig))
      },
      "databaseDialect": enum ([DatabaseDialect](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DatabaseDialect)),
      "protoDescriptors": string
    }  
  
Fields  
---  
`createStatement` |  `string` Required. A `CREATE DATABASE` statement, which specifies the ID of the new database. The database ID must conform to the regular expression `[a-z][a-z0-9_\-]*[a-z0-9]` and be between 2 and 30 characters in length. If the database ID is a reserved word or if it contains a hyphen, the database ID must be enclosed in backticks (```).  
`extraStatements[]` |  `string` Optional. A list of DDL statements to run inside the newly created database. Statements can create tables, indexes, etc. These statements execute atomically with the creation of the database: if there is an error in any statement, the database is not created.  
`encryptionConfig` |  `object (`[EncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#EncryptionConfig)`)` Optional. The encryption configuration for the database. If this field is not specified, Cloud Spanner will encrypt/decrypt all data at rest using Google default encryption.  
`databaseDialect` |  `enum (`[DatabaseDialect](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DatabaseDialect)`)` Optional. The dialect of the Cloud Spanner Database.  
`protoDescriptors` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Proto descriptors used by `CREATE/ALTER PROTO BUNDLE` statements in 'extraStatements'. Contains a protobuf-serialized [`google.protobuf.FileDescriptorSet`](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto) descriptor set. To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run
    
    
    $protoc  --proto_path=/app_path --proto_path=/lib_path \
             --include_imports \
             --descriptor_set_out=descriptors.data \
             moon/shot/app.proto
    

For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).A base64-encoded string.  
  
### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
