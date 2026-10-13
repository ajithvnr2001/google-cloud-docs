---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ModifyColumnFamiliesRequest.Modification
title: Cloud Bigtable V2 Client - Class Modification (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:39.829709+00:00
---

# Cloud Bigtable V2 Client - Class Modification (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ModifyColumnFamiliesRequest.Modification

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class Modification (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class Modification.

A create, update, or delete of a particular column family.

Generated from protobuf message `google.bigtable.admin.v2.ModifyColumnFamiliesRequest.Modification`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2 \ ModifyColumnFamiliesRequest

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ id` |  `string`   
The ID of the column family to be modified.  
`↳ create` |  `[Google\Cloud\Bigtable\Admin\V2\ColumnFamily](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ColumnFamily)`   
Create a new column family with the specified schema, or fail if one already exists with the given ID.  
`↳ update` |  `[Google\Cloud\Bigtable\Admin\V2\ColumnFamily](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ColumnFamily)`   
Update an existing column family to the specified schema, or fail if no column family exists with the given ID.  
`↳ drop` |  `bool`   
Drop (delete) the column family with the given ID, or fail if no such family exists.  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
Optional. A mask specifying which fields (e.g. `gc_rule`) in the `update` mod should be updated, ignored for other modification types. If unset or empty, we treat it as updating `gc_rule` to be backward compatible.  
  
### getId

The ID of the column family to be modified.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setId

The ID of the column family to be modified.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreate

Create a new column family with the specified schema, or fail if one already exists with the given ID.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\ColumnFamily](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ColumnFamily)|null` |   
  
### hasCreate

### setCreate

Create a new column family with the specified schema, or fail if one already exists with the given ID.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Cloud\Bigtable\Admin\V2\ColumnFamily](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ColumnFamily)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdate

Update an existing column family to the specified schema, or fail if no column family exists with the given ID.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\ColumnFamily](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ColumnFamily)|null` |   
  
### hasUpdate

### setUpdate

Update an existing column family to the specified schema, or fail if no column family exists with the given ID.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Cloud\Bigtable\Admin\V2\ColumnFamily](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ColumnFamily)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDrop

Drop (delete) the column family with the given ID, or fail if no such family exists.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasDrop

### setDrop

Drop (delete) the column family with the given ID, or fail if no such family exists.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

Optional. A mask specifying which fields (e.g. `gc_rule`) in the `update` mod should be updated, ignored for other modification types. If unset or empty, we treat it as updating `gc_rule` to be backward compatible.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Optional. A mask specifying which fields (e.g. `gc_rule`) in the `update` mod should be updated, ignored for other modification types. If unset or empty, we treat it as updating `gc_rule` to be backward compatible.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\FieldMask`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMod

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
