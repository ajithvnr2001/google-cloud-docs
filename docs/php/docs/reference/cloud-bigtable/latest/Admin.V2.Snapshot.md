---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Snapshot
title: Cloud Bigtable V2 Client - Class Snapshot (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:53.940803+00:00
---

# Cloud Bigtable V2 Client - Class Snapshot (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Snapshot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class Snapshot (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class Snapshot.

A snapshot of a table at a particular time. A snapshot can be used as a checkpoint for data restoration or a data source for a new table.

Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

Generated from protobuf message `google.bigtable.admin.v2.Snapshot`

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
The unique name of the snapshot. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}`.  
`↳ source_table` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)`   
Output only. The source table at the time the snapshot was taken.  
`↳ data_size_bytes` |  `int|string`   
Output only. The size of the data in the source table at the time the snapshot was taken. In some cases, this value may be computed asynchronously via a background process and a placeholder of 0 will be used in the meantime.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the snapshot is created.  
`↳ delete_time` |  `Google\Protobuf\Timestamp`   
The time when the snapshot will be deleted. The maximum amount of time a snapshot can stay active is 365 days. If 'ttl' is not specified, the default maximum of 365 days will be used.  
`↳ state` |  `int`   
Output only. The current state of the snapshot.  
`↳ description` |  `string`   
Description of the snapshot.  
  
### getName

The unique name of the snapshot.

Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The unique name of the snapshot.

Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSourceTable

Output only. The source table at the time the snapshot was taken.

**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)|null` |   
  
### hasSourceTable

### clearSourceTable

### setSourceTable

Output only. The source table at the time the snapshot was taken.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataSizeBytes

Output only. The size of the data in the source table at the time the snapshot was taken. In some cases, this value may be computed asynchronously via a background process and a placeholder of 0 will be used in the meantime.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setDataSizeBytes

Output only. The size of the data in the source table at the time the snapshot was taken. In some cases, this value may be computed asynchronously via a background process and a placeholder of 0 will be used in the meantime.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time when the snapshot is created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The time when the snapshot is created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDeleteTime

The time when the snapshot will be deleted. The maximum amount of time a snapshot can stay active is 365 days. If 'ttl' is not specified, the default maximum of 365 days will be used.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasDeleteTime

### clearDeleteTime

### setDeleteTime

The time when the snapshot will be deleted. The maximum amount of time a snapshot can stay active is 365 days. If 'ttl' is not specified, the default maximum of 365 days will be used.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the snapshot.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Snapshot.State).  
  
### setState

Output only. The current state of the snapshot.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Snapshot.State).   
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
