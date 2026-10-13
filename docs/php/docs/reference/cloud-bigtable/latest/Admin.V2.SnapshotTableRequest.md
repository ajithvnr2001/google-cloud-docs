---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SnapshotTableRequest
title: Cloud Bigtable V2 Client - Class SnapshotTableRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:54.103246+00:00
---

# Cloud Bigtable V2 Client - Class SnapshotTableRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SnapshotTableRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class SnapshotTableRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class SnapshotTableRequest.

Request message for [google.bigtable.admin.v2.BigtableTableAdmin.SnapshotTable](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__snapshotTable__) Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

Generated from protobuf message `google.bigtable.admin.v2.SnapshotTableRequest`

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
Required. The unique name of the table to have the snapshot taken. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.  
`↳ cluster` |  `string`   
Required. The name of the cluster where the snapshot will be created in. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.  
`↳ snapshot_id` |  `string`   
Required. The ID by which the new snapshot should be referred to within the parent cluster, e.g., `mysnapshot` of the form: `[_a-zA-Z0-9][-_.a-zA-Z0-9]*` rather than `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/mysnapshot`.  
`↳ ttl` |  `Google\Protobuf\Duration`   
The amount of time that the new snapshot can stay active after it is created. Once 'ttl' expires, the snapshot will get deleted. The maximum amount of time a snapshot can stay active is 7 days. If 'ttl' is not specified, the default value of 24 hours will be used.  
`↳ description` |  `string`   
Description of the snapshot.  
  
### getName

Required. The unique name of the table to have the snapshot taken.

Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Required. The unique name of the table to have the snapshot taken.

Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCluster

Required. The name of the cluster where the snapshot will be created in.

Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCluster

Required. The name of the cluster where the snapshot will be created in.

Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSnapshotId

Required. The ID by which the new snapshot should be referred to within the parent cluster, e.g., `mysnapshot` of the form: `[_a-zA-Z0-9][-_.a-zA-Z0-9]*` rather than `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/mysnapshot`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSnapshotId

Required. The ID by which the new snapshot should be referred to within the parent cluster, e.g., `mysnapshot` of the form: `[_a-zA-Z0-9][-_.a-zA-Z0-9]*` rather than `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/mysnapshot`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTtl

The amount of time that the new snapshot can stay active after it is created. Once 'ttl' expires, the snapshot will get deleted. The maximum amount of time a snapshot can stay active is 7 days. If 'ttl' is not specified, the default value of 24 hours will be used.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasTtl

### clearTtl

### setTtl

The amount of time that the new snapshot can stay active after it is created. Once 'ttl' expires, the snapshot will get deleted. The maximum amount of time a snapshot can stay active is 7 days. If 'ttl' is not specified, the default value of 24 hours will be used.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Description of the snapshot.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Description of the snapshot.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`name` |  `string`   
Required. The unique name of the table to have the snapshot taken. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`. Please see BigtableTableAdminClient::tableName() for help formatting this field.  
`cluster` |  `string`   
Required. The name of the cluster where the snapshot will be created in. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`. Please see BigtableTableAdminClient::clusterName() for help formatting this field.  
`snapshotId` |  `string`   
Required. The ID by which the new snapshot should be referred to within the parent cluster, e.g., `mysnapshot` of the form: `[_a-zA-Z0-9][-_.a-zA-Z0-9]*` rather than `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/mysnapshot`.  
`description` |  `string`   
Description of the snapshot.  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SnapshotTableRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
