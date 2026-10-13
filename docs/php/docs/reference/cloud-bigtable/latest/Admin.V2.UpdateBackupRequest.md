---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateBackupRequest
title: Cloud Bigtable V2 Client - Class UpdateBackupRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:02.877114+00:00
---

# Cloud Bigtable V2 Client - Class UpdateBackupRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateBackupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class UpdateBackupRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class UpdateBackupRequest.

The request for [UpdateBackup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__updateBackup__).

Generated from protobuf message `google.bigtable.admin.v2.UpdateBackupRequest`

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
`↳ backup` |  `[Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)`   
Required. The backup to update. `backup.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored. Update is only supported for the following fields: * * `backup.expire_time`.  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
Required. A mask specifying which fields (e.g. `expire_time`) in the Backup resource should be updated. This mask is relative to the Backup resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally by clients that do not know about them.  
  
### getBackup

Required. The backup to update. `backup.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored.

Update is only supported for the following fields:

  * `backup.expire_time`.



**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)|null` |   
  
### hasBackup

### clearBackup

### setBackup

Required. The backup to update. `backup.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored.

Update is only supported for the following fields:

  * `backup.expire_time`.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

Required. A mask specifying which fields (e.g. `expire_time`) in the Backup resource should be updated. This mask is relative to the Backup resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally by clients that do not know about them.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Required. A mask specifying which fields (e.g. `expire_time`) in the Backup resource should be updated. This mask is relative to the Backup resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally by clients that do not know about them.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\FieldMask`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`backup` |  `[Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)`   
Required. The backup to update. `backup.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored. Update is only supported for the following fields:

  *     * `backup.expire_time`.

  
`updateMask` |  `Google\Protobuf\FieldMask`   
Required. A mask specifying which fields (e.g. `expire_time`) in the Backup resource should be updated. This mask is relative to the Backup resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally by clients that do not know about them.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateBackupRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
