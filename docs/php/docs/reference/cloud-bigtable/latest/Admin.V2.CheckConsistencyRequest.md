---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CheckConsistencyRequest
title: Cloud Bigtable V2 Client - Class CheckConsistencyRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:35.291852+00:00
---

# Cloud Bigtable V2 Client - Class CheckConsistencyRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CheckConsistencyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class CheckConsistencyRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class CheckConsistencyRequest.

Request message for [google.bigtable.admin.v2.BigtableTableAdmin.CheckConsistency](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__checkConsistency__)

Generated from protobuf message `google.bigtable.admin.v2.CheckConsistencyRequest`

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
Required. The unique name of the Table for which to check replication consistency. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.  
`↳ consistency_token` |  `string`   
Required. The token created using GenerateConsistencyToken for the Table.  
`↳ standard_read_remote_writes` |  `[StandardReadRemoteWrites](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.StandardReadRemoteWrites)`   
Checks that reads using an app profile with `StandardIsolation` can see all writes committed before the token was created, even if the read and write target different clusters.  
`↳ data_boost_read_local_writes` |  `[DataBoostReadLocalWrites](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DataBoostReadLocalWrites)`   
Checks that reads using an app profile with `DataBoostIsolationReadOnly` can see all writes committed before the token was created, but only if the read and write target the same cluster.  
  
### getName

Required. The unique name of the Table for which to check replication consistency. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Required. The unique name of the Table for which to check replication consistency. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getConsistencyToken

Required. The token created using GenerateConsistencyToken for the Table.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setConsistencyToken

Required. The token created using GenerateConsistencyToken for the Table.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStandardReadRemoteWrites

Checks that reads using an app profile with `StandardIsolation` can see all writes committed before the token was created, even if the read and write target different clusters.

**Returns**  
---  
**Type** | **Description**  
`[StandardReadRemoteWrites](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.StandardReadRemoteWrites)|null` |   
  
### hasStandardReadRemoteWrites

### setStandardReadRemoteWrites

Checks that reads using an app profile with `StandardIsolation` can see all writes committed before the token was created, even if the read and write target different clusters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[StandardReadRemoteWrites](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.StandardReadRemoteWrites)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataBoostReadLocalWrites

Checks that reads using an app profile with `DataBoostIsolationReadOnly` can see all writes committed before the token was created, but only if the read and write target the same cluster.

**Returns**  
---  
**Type** | **Description**  
`[DataBoostReadLocalWrites](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DataBoostReadLocalWrites)|null` |   
  
### hasDataBoostReadLocalWrites

### setDataBoostReadLocalWrites

Checks that reads using an app profile with `DataBoostIsolationReadOnly` can see all writes committed before the token was created, but only if the read and write target the same cluster.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DataBoostReadLocalWrites](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DataBoostReadLocalWrites)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMode

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`name` |  `string`   
Required. The unique name of the Table for which to check replication consistency. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`. Please see BigtableTableAdminClient::tableName() for help formatting this field.  
`consistencyToken` |  `string`   
Required. The token created using GenerateConsistencyToken for the Table.  
**Returns**  
---  
**Type** | **Description**  
`[CheckConsistencyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CheckConsistencyRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
