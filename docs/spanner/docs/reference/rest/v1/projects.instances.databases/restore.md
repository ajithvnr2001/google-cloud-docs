---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore/
title: Method: projects.instances.databases.restore \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:06.414752+00:00
---

# Method: projects.instances.databases.restore  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.restore Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * RestoreDatabaseEncryptionConfig
    * JSON representation
  * EncryptionType
  * Try it!



Create a new database by restoring from a completed backup. The new database must be in the same project and in an instance with the same instance configuration as the instance containing the backup. The returned database long-running operation has a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operationId>`, and can be used to track the progress of the operation, and to cancel it. The metadata field type is `[RestoreDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RestoreDatabaseMetadata)`. The response type is `[Database](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database)`, if successful. Cancelling the returned operation will stop the restore and delete the database. There can be only one database being restored into an instance at a time. Once the restore operation completes, a new restore operation can be initiated, without waiting for the optimize operation associated with the first restore to complete.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{parent=projects/*/instances/*}/databases:restore`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the instance in which to create the restored database. This instance must be in the same project and have the same instance configuration as the instance containing the source backup. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.databases.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "databaseId": string,
      "encryptionConfig": {
        object ([RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#RestoreDatabaseEncryptionConfig))
      },
    
      // Union field source can be only one of the following:
      "backup": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`databaseId` |  `string` Required. The id of the database to create and restore to. This database must not already exist. The `databaseId` appended to `parent` forms the full database name of the form `projects/<project>/instances/<instance>/databases/<databaseId>`.  
`encryptionConfig` |  `object (`[RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#RestoreDatabaseEncryptionConfig)`)` Optional. An encryption configuration describing the encryption type and key resources in Cloud KMS used to encrypt/decrypt the database to restore to. If this field is not specified, the restored database will use the same encryption configuration as the backup by default, namely `[encryptionType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#RestoreDatabaseEncryptionConfig.FIELDS.encryption_type)` = `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION`.  
Union field `source`. Required. The source from which to restore. `source` can be only one of the following:  
`backup` |  `string` Name of the backup from which to restore. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `backup`:

  * `spanner.backups.restoreDatabase`

  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## RestoreDatabaseEncryptionConfig

Encryption configuration for the restored database.

JSON representation  
---  
      
    
    {
      "encryptionType": enum ([EncryptionType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#EncryptionType)),
      "kmsKeyName": string,
      "kmsKeyNames": [
        string
      ]
    }  
  
Fields  
---  
`encryptionType` |  `enum (`[EncryptionType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#EncryptionType)`)` Required. The encryption type of the restored database.  
`kmsKeyName` |  `string` Optional. This field is maintained for backwards compatibility. For new callers, we recommend using `kmsKeyNames` to specify the KMS key. Only use `kmsKeyName` if the location of the KMS key matches the database instance's configuration (location) exactly. For example, if the KMS location is in `us-central1` or `nam3`, then the database instance must also be in `us-central1` or `nam3`.The Cloud KMS key that is used to encrypt and decrypt the restored database. Set this field only when `[encryptionType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#RestoreDatabaseEncryptionConfig.FIELDS.encryption_type)` is `CUSTOMER_MANAGED_ENCRYPTION`. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kmsKeyName>`.  
`kmsKeyNames[]` |  `string` Optional. Specifies the KMS configuration for one or more keys used to encrypt the database. Values have the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kmsKeyName>`.The keys referenced by `kmsKeyNames` must fully cover all regions of the database's instance configuration. Some examples:

  * For regional (single-region) instance configurations, specify a regional location KMS key.
  * For multi-region instance configurations of type `GOOGLE_MANAGED`, either specify a multi-region location KMS key or multiple regional location KMS keys that cover all regions in the instance configuration.
  * For an instance configuration of type `USER_MANAGED`, specify only regional location KMS keys to cover each region in the instance configuration. Multi-region location KMS keys aren't supported for `USER_MANAGED` type instance configurations.

  
  
## EncryptionType

Encryption types for the database to be restored.

Enums  
---  
`ENCRYPTION_TYPE_UNSPECIFIED` | Unspecified. Do not use.  
`USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION` | This is the default option when `[encryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#RestoreDatabaseEncryptionConfig)` is not specified.  
`GOOGLE_DEFAULT_ENCRYPTION` | Use Google default encryption.  
`CUSTOMER_MANAGED_ENCRYPTION` | Use customer managed encryption. If specified, `kmsKeyName` must must contain a valid Cloud KMS key.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
