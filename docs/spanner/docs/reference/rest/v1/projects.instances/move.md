---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/move/
title: Method: projects.instances.move \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:02.810163+00:00
---

# Method: projects.instances.move  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.move Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * DatabaseMoveConfig
    * JSON representation
  * EncryptionConfig
    * JSON representation
  * Try it!



Moves an instance to the target instance configuration. You can use the returned long-running operation to track the progress of moving the instance.

`instances.move` returns `FAILED_PRECONDITION` if the instance meets any of the following criteria:

  * Is undergoing a move to a different instance configuration
  * Has backups
  * Has an ongoing update
  * Contains any CMEK-enabled databases
  * Is a free trial instance



While the operation is pending:

  * All other attempts to modify the instance, including changes to its compute capacity, are rejected.
  * The following database and backup admin operations are rejected:


    
    
    * `DatabaseAdmin.CreateDatabase`
    * `DatabaseAdmin.UpdateDatabaseDdl` (disabled if defaultLeader is
       specified in the request.)
    * `DatabaseAdmin.RestoreDatabase`
    * `DatabaseAdmin.CreateBackup`
    * `DatabaseAdmin.CopyBackup`
    

  * Both the source and target instance configurations are subject to hourly compute and storage charges.
  * The instance might experience higher read-write latencies and a higher transaction abort rate. However, moving an instance doesn't cause any downtime.



The returned long-running operation has a name of the format `<instance_name>/operations/<operationId>` and can be used to track the move instance operation. The metadata field type is `[MoveInstanceMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MoveInstanceMetadata)`. The response field type is `[Instance](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance)`, if successful. Cancelling the operation sets its metadata's `[cancelTime](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MoveInstanceMetadata#FIELDS.cancel_time)`. Cancellation is not immediate because it involves moving any data previously moved to the target instance configuration back to the original instance configuration. You can use this operation to track the progress of the cancellation. Upon successful completion of the cancellation, the operation terminates with `CANCELLED` status.

If not cancelled, upon completion of the returned operation:

  * The instance successfully moves to the target instance configuration.
  * You are billed for compute and storage in target instance configuration.



Authorization requires the `spanner.instances.update` permission on the resource `[instance](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance)`.

For more details, see [Move an instance](https://cloud.google.com/spanner/docs/move-instance).

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{name=projects/*/instances/*}:move`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The instance to move. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.instances.update`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "targetConfig": string,
      "targetDatabaseMoveConfigs": [
        {
          object ([DatabaseMoveConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/move#DatabaseMoveConfig))
        }
      ]
    }  
  
Fields  
---  
`targetConfig` |  `string` Required. The target instance configuration where to move the instance. Values are of the form `projects/<project>/instanceConfigs/<config>`.  
`targetDatabaseMoveConfigs[]` |  `object (`[DatabaseMoveConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/move#DatabaseMoveConfig)`)` Optional. The configuration for each database in the target instance configuration.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## DatabaseMoveConfig

The configuration for each database in the target instance configuration.

JSON representation  
---  
      
    
    {
      "databaseId": string,
      "encryptionConfig": {
        object ([EncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/move#EncryptionConfig))
      }
    }  
  
Fields  
---  
`databaseId` |  `string` Required. The unique identifier of the database resource in the Instance. For example, if the database uri is `projects/foo/instances/bar/databases/baz`, then the id to supply here is baz.  
`encryptionConfig` |  `object (`[EncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/move#EncryptionConfig)`)` Optional. Encryption configuration to be used for the database in the target configuration. The encryption configuration must be specified for every database which currently uses CMEK encryption. If a database currently uses Google-managed encryption and a target encryption configuration is not specified, then the database defaults to Google-managed encryption.If a database currently uses Google-managed encryption and a target CMEK encryption is specified, the request is rejected.If a database currently uses CMEK encryption, then a target encryption configuration must be specified. You can't move a CMEK database to a Google-managed encryption database using the instances.move API.  
  
## EncryptionConfig

Encryption configuration for a Cloud Spanner database.

JSON representation  
---  
      
    
    {
      "kmsKeyName": string,
      "kmsKeyNames": [
        string
      ]
    }  
  
Fields  
---  
`kmsKeyName` |  `string` Optional. This field is maintained for backwards compatibility. For new callers, we recommend using `kmsKeyNames` to specify the KMS key. Only use `kmsKeyName` if the location of the KMS key matches the database instance's configuration (location) exactly. For example, if the KMS location is in `us-central1` or `nam3`, then the database instance must also be in `us-central1` or `nam3`.The Cloud KMS key that is used to encrypt and decrypt the restored database. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kmsKeyName>`.  
`kmsKeyNames[]` |  `string` Optional. Specifies the KMS configuration for one or more keys used to encrypt the database. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kmsKeyName>`.The keys referenced by `kmsKeyNames` must fully cover all regions of the database's instance configuration. Some examples:

  * For regional (single-region) instance configurations, specify a regional location KMS key.
  * For multi-region instance configurations of type `GOOGLE_MANAGED`, either specify a multi-region location KMS key or multiple regional location KMS keys that cover all regions in the instance configuration.
  * For an instance configuration of type `USER_MANAGED`, specify only regional location KMS keys to cover each region in the instance configuration. Multi-region location KMS keys aren't supported for `USER_MANAGED` type instance configurations.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
