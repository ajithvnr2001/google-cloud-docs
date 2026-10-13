---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsRequest
title: Cloud Spanner V1 Client - Class ListBackupOperationsRequest (2.11.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:22.278099+00:00
---

# Cloud Spanner V1 Client - Class ListBackupOperationsRequest (2.11.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Spanner V1 Client - Class ListBackupOperationsRequest (2.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

Reference documentation and code samples for the Cloud Spanner V1 Client class ListBackupOperationsRequest.

The request for [ListBackupOperations](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.Client.DatabaseAdminClient#_Google_Cloud_Spanner_Admin_Database_V1_Client_DatabaseAdminClient__listBackupOperations__).

Generated from protobuf message `google.spanner.admin.database.v1.ListBackupOperationsRequest`

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
`↳ parent` |  `string`   
Required. The instance of the backup operations. Values are of the form `projects/<project>/instances/<instance>`.  
`↳ filter` |  `string`   
An expression that filters the list of returned backup operations. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive. The following fields in the operation are eligible for filtering: * * `name` \- The name of the long-running operation * * `done` \- False if the operation is in progress, else true. * * `metadata.\@type` \- the type of metadata. For example, the type string for [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata) is `type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata`. * * `metadata.<field_name>` \- any field in metadata.value. `metadata.\@type` must be specified first if filtering on metadata fields. * * `error` \- Error associated with the long-running operation. * * `response.\@type` \- the type of response. * * `response.<field_name>` \- any field in response.value. You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly. Here are a few examples: * * `done:true` \- The operation is complete. * * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `metadata.database:prod` \- Returns operations where: * * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata). * * The source database name of backup contains the string "prod". * * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.name:howl) AND` \ `(metadata.progress.start_time < \"2018-03-28T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where: * * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata). * * The backup name contains the string "howl". * * The operation started before 2018-03-28T14:50:00Z. * * The operation resulted in an error. * * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test) AND` \ `(metadata.progress.start_time < \"2022-01-18T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where: * * The operation's metadata type is [CopyBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CopyBackupMetadata). * * The source backup name contains the string "test". * * The operation started before 2022-01-18T14:50:00Z. * * The operation resulted in an error. * * `((metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.database:test_db)) OR` \ `((metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test_bkp)) AND` \ `(error:*)` \- Returns operations where: * * The operation's metadata matches either of criteria: * * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata) AND the source database name of the backup contains the string "test_db" * * The operation's metadata type is [CopyBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CopyBackupMetadata) AND the source backup name contains the string "test_bkp" * * The operation resulted in an error.  
`↳ page_size` |  `int`   
Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`↳ page_token` |  `string`   
If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsResponse#_Google_Cloud_Spanner_Admin_Database_V1_ListBackupOperationsResponse__getNextPageToken__) from a previous [ListBackupOperationsResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsResponse) to the same `parent` and with the same `filter`.  
  
### getParent

Required. The instance of the backup operations. Values are of the form `projects/<project>/instances/<instance>`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The instance of the backup operations. Values are of the form `projects/<project>/instances/<instance>`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

An expression that filters the list of returned backup operations.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive. The following fields in the operation are eligible for filtering:

  * `name` \- The name of the long-running operation
  * `done` \- False if the operation is in progress, else true.
  * `metadata.\@type` \- the type of metadata. For example, the type string for [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata) is `type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata`.
  * `metadata.<field_name>` \- any field in metadata.value. `metadata.\@type` must be specified first if filtering on metadata fields.
  * `error` \- Error associated with the long-running operation.
  * `response.\@type` \- the type of response.
  * `response.<field_name>` \- any field in response.value. You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly. Here are a few examples:
  * `done:true` \- The operation is complete.
  * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `metadata.database:prod` \- Returns operations where:
    * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata).
    * The source database name of backup contains the string "prod".
  * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.name:howl) AND` \ `(metadata.progress.start_time < \"2018-03-28T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where:
    * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata).
    * The backup name contains the string "howl".
    * The operation started before 2018-03-28T14:50:00Z.
    * The operation resulted in an error.
  * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test) AND` \ `(metadata.progress.start_time < \"2022-01-18T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where:
    * The operation's metadata type is [CopyBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CopyBackupMetadata).
    * The source backup name contains the string "test".
    * The operation started before 2022-01-18T14:50:00Z.
    * The operation resulted in an error.
  * `((metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.database:test_db)) OR` \ `((metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test_bkp)) AND` \ `(error:*)` \- Returns operations where:
    * The operation's metadata matches either of criteria:
      * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata) AND the source database name of the backup contains the string "test_db"
      * The operation's metadata type is [CopyBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CopyBackupMetadata) AND the source backup name contains the string "test_bkp"
    * The operation resulted in an error.



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

An expression that filters the list of returned backup operations.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive. The following fields in the operation are eligible for filtering:

  * `name` \- The name of the long-running operation
  * `done` \- False if the operation is in progress, else true.
  * `metadata.\@type` \- the type of metadata. For example, the type string for [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata) is `type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata`.
  * `metadata.<field_name>` \- any field in metadata.value. `metadata.\@type` must be specified first if filtering on metadata fields.
  * `error` \- Error associated with the long-running operation.
  * `response.\@type` \- the type of response.
  * `response.<field_name>` \- any field in response.value. You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly. Here are a few examples:
  * `done:true` \- The operation is complete.
  * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `metadata.database:prod` \- Returns operations where:
    * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata).
    * The source database name of backup contains the string "prod".
  * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.name:howl) AND` \ `(metadata.progress.start_time < \"2018-03-28T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where:
    * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata).
    * The backup name contains the string "howl".
    * The operation started before 2018-03-28T14:50:00Z.
    * The operation resulted in an error.
  * `(metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test) AND` \ `(metadata.progress.start_time < \"2022-01-18T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where:
    * The operation's metadata type is [CopyBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CopyBackupMetadata).
    * The source backup name contains the string "test".
    * The operation started before 2022-01-18T14:50:00Z.
    * The operation resulted in an error.
  * `((metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.database:test_db)) OR` \ `((metadata.\@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test_bkp)) AND` \ `(error:*)` \- Returns operations where:
    * The operation's metadata matches either of criteria:
      * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CreateBackupMetadata) AND the source database name of the backup contains the string "test_db"
      * The operation's metadata type is [CopyBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.CopyBackupMetadata) AND the source backup name contains the string "test_bkp"
    * The operation resulted in an error.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsResponse#_Google_Cloud_Spanner_Admin_Database_V1_ListBackupOperationsResponse__getNextPageToken__) from a previous [ListBackupOperationsResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsResponse) to the same `parent` and with the same `filter`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsResponse#_Google_Cloud_Spanner_Admin_Database_V1_ListBackupOperationsResponse__getNextPageToken__) from a previous [ListBackupOperationsResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsResponse) to the same `parent` and with the same `filter`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The instance of the backup operations. Values are of the form `projects/<project>/instances/<instance>`. Please see DatabaseAdminClient::instanceName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupOperationsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Database.V1.ListBackupOperationsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
