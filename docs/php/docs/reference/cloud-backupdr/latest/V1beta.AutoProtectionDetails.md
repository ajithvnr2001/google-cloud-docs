---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionDetails
title: Google Cloud Backup Dr V1beta Client - Class AutoProtectionDetails (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:25.012834+00:00
---

# Google Cloud Backup Dr V1beta Client - Class AutoProtectionDetails (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class AutoProtectionDetails (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class AutoProtectionDetails.

AutoProtectionDetails contains the protection details of a resource from the current binding's perspective.

Generated from protobuf message `google.cloud.backupdr.v1beta.AutoProtectionDetails`

## Namespace

Google \ Cloud \ BackupDR \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ state` |  `int`   
Output only. Protection state of the resource from the current binding's perspective. Output only.  
`↳ backup_plan_association` |  `string`   
Output only. Resource name of backup plan association linked to the resource, if any. Format: projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}  
`↳ data_source` |  `string`   
Output only. Resource name of the datasource linked to the resource, if any. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{dataSourceId}  
`↳ error` |  `[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)`   
Output only. Error during last sync for protection/unprotection, if any.  
  
### getState

Output only. Protection state of the resource from the current binding's perspective. Output only.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionDetails.State).  
  
### setState

Output only. Protection state of the resource from the current binding's perspective. Output only.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionDetails.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupPlanAssociation

Output only. Resource name of backup plan association linked to the resource, if any. Format: projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBackupPlanAssociation

Output only. Resource name of backup plan association linked to the resource, if any. Format: projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataSource

Output only. Resource name of the datasource linked to the resource, if any. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{dataSourceId}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDataSource

Output only. Resource name of the datasource linked to the resource, if any. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{dataSourceId}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getError

Output only. Error during last sync for protection/unprotection, if any.

**Returns**  
---  
**Type** | **Description**  
`[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)|null` |   
  
### hasError

### clearError

### setError

Output only. Error during last sync for protection/unprotection, if any.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
