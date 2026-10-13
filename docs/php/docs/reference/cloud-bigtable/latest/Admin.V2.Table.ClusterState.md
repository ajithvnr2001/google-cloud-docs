---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.ClusterState
title: Cloud Bigtable V2 Client - Class ClusterState (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:55.319248+00:00
---

# Cloud Bigtable V2 Client - Class ClusterState (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.ClusterState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class ClusterState (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class ClusterState.

The state of a table's data in a particular cluster.

Generated from protobuf message `google.bigtable.admin.v2.Table.ClusterState`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2 \ Table

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ replication_state` |  `int`   
Output only. The state of replication for the table in this cluster.  
`↳ encryption_info` |  `array<[Google\Cloud\Bigtable\Admin\V2\EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.EncryptionInfo)>`   
Output only. The encryption information for the table in this cluster. If the encryption key protecting this resource is customer managed, then its version can be rotated in Cloud Key Management Service (Cloud KMS). The primary version of the key and its status will be reflected here when changes propagate from Cloud KMS.  
  
### getReplicationState

Output only. The state of replication for the table in this cluster.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ReplicationState](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.ClusterState.ReplicationState).  
  
### setReplicationState

Output only. The state of replication for the table in this cluster.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ReplicationState](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.ClusterState.ReplicationState).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEncryptionInfo

Output only. The encryption information for the table in this cluster.

If the encryption key protecting this resource is customer managed, then its version can be rotated in Cloud Key Management Service (Cloud KMS). The primary version of the key and its status will be reflected here when changes propagate from Cloud KMS.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[Google\Cloud\Bigtable\Admin\V2\EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.EncryptionInfo)>` |   
  
### setEncryptionInfo

Output only. The encryption information for the table in this cluster.

If the encryption key protecting this resource is customer managed, then its version can be rotated in Cloud Key Management Service (Cloud KMS). The primary version of the key and its status will be reflected here when changes propagate from Cloud KMS.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Google\Cloud\Bigtable\Admin\V2\EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.EncryptionInfo)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
