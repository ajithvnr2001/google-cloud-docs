---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport
title: Google Cloud Dataproc Metastore V1alpha Client - Class MetadataImport (1.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:29.766389+00:00
---

# Google Cloud Dataproc Metastore V1alpha Client - Class MetadataImport (1.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc Metastore V1alpha Client - Class MetadataImport (1.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.4  1.1.1  1.0.4  0.11.5  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.1  0.4.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataproc Metastore V1alpha Client class MetadataImport.

A metastore resource that imports metadata.

Generated from protobuf message `google.cloud.metastore.v1alpha.MetadataImport`

## Namespace

Google \ Cloud \ Metastore \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ database_dump` |  `[MetadataImport\DatabaseDump](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport.DatabaseDump)`   
Immutable. A database dump from a pre-existing metastore's database.  
`↳ name` |  `string`   
Immutable. The relative resource name of the metadata import, of the form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}`.  
`↳ description` |  `string`   
The description of the metadata import.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the metadata import was started.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the metadata import was last updated.  
`↳ end_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the metadata import finished.  
`↳ state` |  `int`   
Output only. The current state of the metadata import.  
  
### getDatabaseDump

Immutable. A database dump from a pre-existing metastore's database.

**Returns**  
---  
**Type** | **Description**  
`[MetadataImport\DatabaseDump](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport.DatabaseDump)|null` |   
  
### hasDatabaseDump

### setDatabaseDump

Immutable. A database dump from a pre-existing metastore's database.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MetadataImport\DatabaseDump](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport.DatabaseDump)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Immutable. The relative resource name of the metadata import, of the form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Immutable. The relative resource name of the metadata import, of the form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

The description of the metadata import.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

The description of the metadata import.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time when the metadata import was started.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The time when the metadata import was started.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The time when the metadata import was last updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. The time when the metadata import was last updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndTime

Output only. The time when the metadata import finished.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasEndTime

### clearEndTime

### setEndTime

Output only. The time when the metadata import finished.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the metadata import.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport.State).  
  
### setState

Output only. The current state of the metadata import.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetadata

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
